from project import app, db
from project.models import Admin_District,Admin_Headquaters,Complaints,Rejected_Complaint,Bar
from flask_restful import Resource, Api
from flask import flash, redirect, render_template, request, url_for,make_response
from flask_login import login_user,login_required, logout_user
from project.models import Admin_District,Complaints,Rejected_Complaint,Bar,ComplaintStore
from project import db, login_manager,mail
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash,check_password_hash
import os
import functools
from flask_login import login_user,login_required,logout_user
import json
import logging
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash,check_password_hash
import jwt
from functools import wraps
from flask import send_file, send_from_directory, safe_join, abort
import datetime
from flask_mail import Message
import random
import datetime

api = Api(app)

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = None
        try:

            if request.headers['X-Access_Token'] is not None:
                token = request.headers['X-Access_Token']
            if not token:
                return make_response('Invalid Token',401,{'www-Authenticate':'Invalid Token"'})
            try:
                data = jwt.decode(token,app.config['SECRET_KEY'])
                current_user = Admin_Headquaters.query.filter_by(admin_email=data['admin_email']).first()
            except:
                return make_response('Invalid Token',401,{'www-Authenticate':'Invalid Token"'})
            return f(current_user,*args,**kwargs)

        except:
            return make_response('Invalid Token',401,{'www-Authenticate':'Invalid Token"'})

    return decorated


class Register2(Resource):

    #@staticmethod
    def post(self):

        data = request.get_json()

        admin_Name= data['Name']
        admin_email = data['email']
        #publicID = str(uuid.uuid4)
        password = data['password']
        confirm_password = data['confirm_password']
        if admin_email is None or password is None :
            return {'error':'error'}
        if password==confirm_password:
            user = Admin_Headquaters(admin_Name=admin_Name,admin_email=admin_email,password=password)
            db.session.add(user)
            db.session.commit()
            return data
        else:
            return {'error':'Could not creat account'}


class AdminPass(Resource):
    def post(self):
        admin_Name= 'Ec'
        admin_email = 'complaints@ec.co.ug'
        #publicID = str(uuid.uuid4)
        password = 'adminEc'
        try:
            user = Admin_Headquaters(admin_Name=admin_Name,admin_email=admin_email,password=password)
            db.session.add(user)
            db.session.commit()
        except Exception:
            return {"error":"reset email already exists"}


class LoginHeadquaters(Resource):
    def post(self):
        #data = request.authorization
        data = request.get_json()
        if not data or not data['username'] or not data['password']:
            return make_response('Could not verify1',401,{'www-Authenticate':'Basic realm-"login required!"'})
        admin = Admin_Headquaters.query.filter_by(admin_email=data['username']).first()
        if not admin:
            return make_response('Could not verify2',401,{'www-Authenticate':'Basic realm-"login required!"'})
        if admin.password == data['password']:
            token = jwt.encode({'admin_email':admin.admin_email,'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=120)},app.config['SECRET_KEY'])
            return jsonify({'token':token.decode('UTF-8'),'username':admin.admin_email,'admin_Name':admin.admin_Name})
        return make_response('Could not verify3',401,{'www-Authenticate':'Basic realm-"login required!"'})

class AdminGetComplaints(Resource):
    @token_required
    def get(self,current_user):
        data=request.get_json()
        complaint=Complaints.query.filter_by(status="Unresolved")
        return [x.json() for x in complaint[-1::-1]]

class AllAdminGetComplaints(Resource):
    @token_required
    def get(self,current_user):
        data=request.get_json()
        complaint=Complaints.query.all()
        return [x.json() for x in complaint[-1::-1]]

class AdminPieChart(Resource):
    @token_required
    def post(self,current_user):
        #data = request.get_json()

        try:
            resolved = Complaints.query.filter_by(status='Resolved').count()

        except Exception:
            resolved = 0

        try:
            unresolved = Complaints.query.filter_by(status='Unresolved').count()

        except Exception:
            unresolved = 0

        try:
            pending = Complaints.query.filter_by(status='Pending').count()

        except Exception:
            pending = 0
        try:
            sum_= resolved+unresolved+pending
            resolv=(resolved*100)/sum_
            unresolv=(unresolved*100)/sum_
            pen=(pending*100)/sum_
            resolve=round(resolv,2)
            unresolve=round(unresolv,2)
            pend=round(pen,2)
        except Exception:
            resolve=0
            unresolve=0
            pend=0


        return {'data':[resolve,unresolve,pend]}

class AminPostComplaints(Resource):
    @token_required
    def post(self,current_user):
        data =request.get_json()
        admin=data['admin_email']
        complaint=Complaints.query.filter_by(complaints_refn0=data['complaints_refn0']).first()
        information=Admin_Headquaters.query.filter_by(admin_email=admin).first()
        p=str(datetime.date.today())
        if complaint is not None:
            status = data["status"]
            if status =="Resolved":
                complaint.status=data["status"]
                complaint.headagent_name= information.admin_Name
                complaint.headagent_idn0=data['nin']
                complaint.head_post=data['districtagent_post']
                complaint.head_signet=data['head_signature']
                complaint.headdescription=data['district_resolutions']
                complaint.headclassification=data['classify_complaint']
                complaint.headresolution=data['district_description']
                complaint.date_submit=p
                db.session.commit()

            elif status =="Unresolved":
                complaint.districtagent_name= information.admin_Name
                complaint.districtagent_idn0=data['districtagent_idn0']
                complaint.districtagent_post=data['districtagent_post']
                complaint.districtagent_signet=data['districtagent_signet']
                complaint.status=data['status']
                complaint.comment=data['comment']
                complaint.date_submit=p
                complaint.headagent_name=''
                complaint.headagent_email=''
                complaint.headagent_idn0=''
                complaint.head_post=''
                complaint.head_signet=''
                complaint.headresolution = ''
                complaint.headdescription = ''
                complaint.headclassification= ''
                db.session.commit()

            elif status =="Declined":
                rejected = Complaints.query.filter_by(complaints_refn0=data['complaints_refn0']).first()

                status='Declined'
                comment = data['comment']
                districtagent_name= information.admin_Name
                agent_name = rejected.agent_name
                agent_email= rejected.agent_email
                agent_phone= rejected.agent_phone
                agent_idn0= rejected.agent_idn0
                agent_staff= rejected.agent_staff
                agent_post= rejected.agent_staff
                district= rejected.district
                poling_station = rejected.poling_station
                complaints_refn0 = rejected.complaints_refn0
                nature_complaint = rejected.nature_complaint
                complaint= rejected.complaint
                date = p


                insert = Rejected_Complaint(agent_name=agent_name,agent_email=agent_email,agent_phone=agent_phone,agent_staff=agent_staff,
                                            agent_idn0=agent_idn0,agent_post=agent_post,district=district,poling_station=poling_station,
                                            complaints_refn0=complaints_refn0,nature_complaint=nature_complaint,complaint=complaint,
                                            date=date,districtagent_name=districtagent_name,status=status,comment=comment)
                db.session.add(insert)
                db.session.delete(rejected)
                db.session.commit()


            else:
                make_response('Could not verify7',401,{'www-Authenticate':'Basic realm-"login required!"'})

        else:
            make_response('Could not verify2',401,{'www-Authenticate':'Basic realm-"login required!"'})

class AllDistrictheadComplaints(Resource):
    @token_required
    def post(self,current_user):
        data=request.get_json()
        districts =Complaints.query.filter_by(district=data['district_name']).first()
        return districts.json()

class ApprovedCompalints(Resource):
    @token_required
    def get (self,current_user):
        data=request.get_json()
        complaints=Complaints.query.filter_by(status=data['status'])
        return complaints.json()

class UnresolvedCompalints(Resource):
    @token_required
    def get (self,current_user):
        data=request.get_json()
        complaints=Complaints.query.filter_by(status=data['status'])
        return complaints.json()

class UpdateDeclinedComplaints(Resource):
    @token_required
    def post(self,current_user):
        data=request.get_json()
        admin=data['admin_email']
        information=Admin_Headquaters.query.filter_by(admin_email=admin).first()
        rejected=Rejected_Complaint.query.filter_by(complaints_refn0=data['complaints_refn0']).first()
        p=str(datetime.date.today())
        if data['complaints_refn0'] is not None:
            status=data['status']
            if data['status'] is not None:
                districtagent_name= information.admin_Name
                agent_name = rejected.agent_name
                agent_email= rejected.agent_email
                agent_phone= rejected.agent_phone
                agent_idn0= rejected.agent_idn0
                agent_post= rejected.agent_post
                district= rejected.district
                poling_station = rejected.poling_station
                complaints_refn0 = rejected.complaints_refn0
                nature_complaint = rejected.nature_complaint
                complaint= rejected.complaint
                comments=rejected.comment
                date = p
                districtagent_idn0=''
                districtagent_post=''
                districtagent_signet=''
                districtagent_email=''
                district_resolutions=''
                classify_complaint=''
                district_description=''
                date_submit=''
                headagent_name=''
                headagent_email=''
                headagent_idn0=''
                head_post=''
                head_signet=''
                headresolution = ''
                headdescription = ''
                headclassification= ''
                update=Complaints(agent_name=agent_name,agent_email=agent_email,agent_phone=agent_phone,agent_idn0=agent_idn0,agent_staff=agent_post,district=district,
                                  poling_station=poling_station,complaint=complaint,
                                  complaints_refn0=complaints_refn0,nature_complaint=nature_complaint,date=date,districtagent_name=districtagent_name,
                                  districtagent_email=districtagent_email, districtagent_idn0=districtagent_idn0,districtagent_post=districtagent_post,districtagent_signet=districtagent_signet,status=status,
                                  district_resolutions=district_resolutions,classify_complaint=classify_complaint,district_description=district_description,headagent_name=headagent_name,headagent_email=headagent_email,headagent_idn0=headagent_idn0,head_post=head_post,head_signet=head_signet,headresolution=headresolution,
                                  headdescription=headdescription,headclassification=headclassification,comments=comments,date_submit=date_submit)
                db.session.add(update)
                db.session.delete(rejected)
                db.session.commit()




class Alllevelones(Resource):
    @token_required
    def get (self,current_user):
        data=request.get_json()
        complaints= Admin_District.query.all()
        return [x.json()for x in complaints]


class PostzComplaint(Resource):
    @token_required
    def post(self,current_user):

       # while True:
        #    number  = random.randrange(1000000, 9999999)
        # make sure id works

        data = request.form
        dt = datetime.datetime.today().year
        admin_email = data['email']
        agent = Admin_Headquaters.query.filter_by(admin_email=data['email']).first()
        agent_email=data['email']
        agent_name = agent.admin_Name
        agent_phone = data['complain_n0']
        agent_idn0 = ''
        agent_staff = data['agent_staff']
        district = data['district']
        poling_station = data['poling_station']


        number = random.randrange(1000000, 9999999)
        id_ = 'EC-'+str(number)+'-'+str(dt)+'-'+district

        no = Complaints.query.filter_by(complaints_refn0=id_).count()
        try:
            while True:
                if no==0:
                    complaints_refn0 = id_
                    break
                else:
                    pass
        except Exception:
            return {'error':'reference already exists'}



        nature_complaint = data['nature_complaint']
        complaint=data['complaint']
        date = str(datetime.datetime.today())
        compalianant_name = data['compalianant_name']
        Complaint_category = data['Complaint_category']
        districtagent_name = ''
        districtagent_email = data['email']
        districtagent_idn0 = ''
        districtagent_post = ''
        districtagent_signet = ''
        status ='Unresolved'
        districtagent_resolutions = ''
        classify_complaint = ''
        district_description = ''
        headagent_name = ''
        headagent_email = ''
        headagent_idn0 = ''
        head_post = ''
        head_signet = ''
        headresolution = ''
        headdescription = ''
        headclassification = ''
        date_submit = ''
        comments=''
        file = request.files['file']
        filename = data['filename']
        fileExt = filename.split('.')[1]
        newfilename = str(id_)+'.'+fileExt
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],newfilename))

        complaint = Complaints(agent_email=agent_email,agent_name=agent_name,agent_phone=agent_phone,agent_idn0=agent_idn0,agent_staff=agent_staff,compalianant_name=compalianant_name,
                                district=district,poling_station=poling_station,complaints_refn0=complaints_refn0,nature_complaint=nature_complaint,Complaint_category=Complaint_category,
                                date=date,districtagent_name=districtagent_name,districtagent_email=districtagent_email,districtagent_idn0=districtagent_idn0,
                                districtagent_post=districtagent_post,districtagent_signet=districtagent_signet,status=status,district_resolutions=districtagent_resolutions,
                                classify_complaint=classify_complaint,files=newfilename,district_description=district_description,headagent_name=headagent_name,
                                headagent_email=headagent_email,headagent_idn0=headagent_idn0,head_post=head_post,head_signet=head_signet,
                                headresolution=headresolution,headdescription=headdescription,headclassification=headclassification,date_submit=date_submit,comments=comments,complaint=complaint)

        db.session.add(complaint)
        db.session.commit()



class Monthlys(Resource):
    @token_required
    def post(self,current_user):

        last_day=str(datetime.datetime.today().month)
        if last_day == "1":
            Bar.query.delete()

        else:
            pass

        data = request.get_json()
        month = Complaints.query.all()

        for x in month:
            date=x.json()['date']
            file_date=int(date.split("-")[1])
            c_date=int(date.split("-")[0])
            now_date=datetime.datetime.now().year
            sys_date=datetime.datetime.now().month
##        print(sys_date)
##        for x in month:
##            date=x.date
##            file_date=int(date.split("-")[1])
##            sys_date=datetime.datetime.now().month
            if file_date==sys_date:
                resolved = Complaints.query.filter_by(status='Resolved')
                count = 0
                for x in resolved:
                    g = x.date
                    fyle=int(g.split("-")[1])
                    file_yr=int(g.split("-")[0])
                    if fyle == sys_date and x.status=='Resolved' and file_yr==now_date:
                        count = count+1

                    else:
                        pass

                unresolved = Complaints.query.filter_by(status='Unresolved')
                count2 = 0
                for x in unresolved:
                    m = x.date
                    fyle2=int(m.split("-")[1])
                    file_yr2=int(m.split("-")[0])
                    if fyle2 == sys_date and x.status=="Unresolved" and file_yr2==now_date :
                        count2 = count2+1

                    else:
                        pass
                try:

                    id_=Bar.query.filter_by(id=sys_date).first()
                    id_.Resolved=count
                    id_.Unresolved=count2
                    db.session.commit()

                except Exception:
                    for i in range(1,13):
                        months=datetime.date(2008, i, 1).strftime('%B')
                        Resolved=0
                        Unresolved=0
                        p=Bar(id=i,month=months,Unresolved=Unresolved,Resolved=Resolved)
                        db.session.add(p)
                        db.session.commit()



            else:
                pass

        unres=Bar.query.all()
        p=[]
        k=[]
        for x in unres:
            p.append(x.Unresolved)
            k.append(x.Resolved)
        return {'deta':p,'dema':k}

        return [x.json() for x in unres]




class Unresolves(Resource):
    @token_required
    def post(self,current_user):
        data = request.get_json()
        unresolve = Complaints.query.filter_by(status='Unresolved')
        return [x.json() for x in unresolve]


class PieChartsdistrict(Resource):
    @token_required
    def post(self,current_user):
        data = request.get_json()

        try:
            resolved = Complaints.query.filter_by(district=data['district_n0'],status='Resolved').count()

        except Exception:
            resolved = 0

        try:
            unresolved = Complaints.query.filter_by(district=data['district_n0'],status='Unresolved').count()

        except Exception:
            unresolved = 0

        try:
            pending = Complaints.query.filter_by(district=data['district_n0'],status='Pending').count()

        except Exception:
            pending = 0

        return {'data':[resolved,unresolved,pending]}



class CodeDistrict(Resource):
    @token_required
    def post(self,current_user):
        data = request.get_json()
        code=Complaints.query.all()
        p=[x.district for x in code]
        k=list(set(p))
        return k

class AllDeclinedComplaintsadmin(Resource):
    @token_required
    def post(self,current_user):
        data=request.get_json()
        try:
            complaints = Rejected_Complaint.query.all()
            return [x.json() for x in complaints[-1::-1]]

        except Exception:
            return {'Status':'No declined Complaints available'}

class AminStore(Resource):
    @token_required
    def post(self,current_user):
        data =request.get_json()
        complaint=Complaints.query.all()
        p=str(datetime.date.today())
        ComplaintStore.query.delete()
        for x in complaint:
            if x.headagent_name:
                districtagent_name= x.districtagent_name
                agent_name = x.agent_name
                agent_email= x.agent_email
                agent_phone= x.agent_phone
                agent_idn0= x.agent_idn0
                agent_post= x.agent_staff
                district= x.district
                poling_station = x.poling_station
                complaints_refn0 = x.complaints_refn0
                nature_complaint = x.nature_complaint
                complaint= x.complaint
                comments=x.comments
                date = x.date
                districtagent_idn0=x.districtagent_idn0
                districtagent_post=x.districtagent_post
                districtagent_signet=x.districtagent_signet
                districtagent_email=x.districtagent_email
                district_resolutions=x.district_resolutions
                classify_complaint=x.Complaint_category
                district_description=x.district_description
                date_submit=x.date_submit
                headagent_name=x.headagent_name
                headagent_email=x.headagent_email
                headagent_idn0=x.headagent_idn0
                head_post=x.head_post
                head_signet=x.head_signet
                headresolution = x.headresolution
                headdescription = x.headdescription
                headclassification= x.headclassification
                status=x.status
                complainants=x.compalianant_name
                filez=x.files

                update=ComplaintStore(agent_name=agent_name,agent_email=agent_email,agent_phone=agent_phone,agent_idn0=agent_idn0,agent_staff=agent_post,district=district,
                                      poling_station=poling_station,complaint=complaint,complainants=complainants,filez=filez,
                                      complaints_refn0=complaints_refn0,nature_complaint=nature_complaint,date=date,districtagent_name=districtagent_name,
                                      districtagent_email=districtagent_email, districtagent_idn0=districtagent_idn0,districtagent_post=districtagent_post,districtagent_signet=districtagent_signet,status=status,
                                      district_resolutions=district_resolutions,classify_complaint=classify_complaint,district_description=district_description,headagent_name=headagent_name,headagent_email=headagent_email,headagent_idn0=headagent_idn0,head_post=head_post,head_signet=head_signet,headresolution=headresolution,
                                      headdescription=headdescription,headclassification=headclassification,comments=comments,date_submit=date_submit)
                db.session.add(update)
                db.session.commit()
                p=ComplaintStore.query.all()
            else:
                pass
        return [x.json()for x in p[-1::-1]]

class Accounts(Resource):
    # @token_required
    def get(self):
        data=request.get_json()

        try:
            accounts=Admin_Headquaters.query.all()
            return [x.json() for x in accounts[-1::-1]]
        except Exception:
            return {'status':'No Accounts available'}



class Account(Resource):
    # @token_required
    def post(self):
        data=request.get_json()
        account=Admin_Headquaters.query.filter_by(admin_email=data['admin_email']).first()
        if account is not None:
            Admin_Headquaters.query.filter(Admin_Headquaters.admin_email == data["admin_email"]).delete()
            db.session.commit()
        else:
            pass


class Tabledistrict(Resource):
    @token_required
    def get(self,current_user):
        data = request.get_json()

        code=Complaints.query.all()
        p=[x.district for x in code]
##        return p
        k=list(set(p))
        lis=[]
        for n in k:
            try:
                resolved = Complaints.query.filter_by(district=n,status='Resolved').count()

            except Exception:
                resolved = 0

            try:
                unresolved = Complaints.query.filter_by(district=n,status='Unresolved').count()

            except Exception:
                unresolved = 0

            try:
                pending = Complaints.query.filter_by(district=n,status='Pending').count()

            except Exception:
                pending = 0
            p={'district':n,'data':[resolved,unresolved,pending],'sum':resolved+unresolved+pending}
            lis.append(p)
        return lis



class files(Resource):
#    @token_required
    def post(current_user):
        data = request.get_json()
        comp = data['complaints_refn0']
        #reg_no = '3'
        file_ = Complaints.query.filter_by(complaints_refn0=comp).first()
        name = file_.json()["files"]
        try:
            return send_file(os.path.join(app.config['UPLOAD_FOLDER'],str(name)))

        except FileNotFoundError:
            abort(404)

class filezresolved(Resource):
#    @token_required
    def post(current_user):
        data = request.get_json()
        comp = data['complaints_refn0']
        #reg_no = '3'
        file_ = ComplaintStore.query.filter_by(complaints_refn0=comp).first()
        name = file_.json()["filez"]
        try:
            return send_file(os.path.join(app.config['UPLOAD_FOLDER'],str(name)))

        except FileNotFoundError:
            abort(404)


class ComplainUpdates(Resource):
#    @token_required
    def post(current_user):
        data = request.get_json()
        comp = data['complaints_refn0']

        edit = Complaints.query.filter_by(complaints_refn0=comp).first()
        try:

            edit.compalianant_name=data["complainings"]
            edit.complaint=data["complains"]
            db.session.commit()


        except Exception:
            print( {"error":"no updates made"})





































