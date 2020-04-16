from project import app, db
from project.models import Admin_District,Complaints,Rejected_Complaint,Bar
from flask_restful import Resource, Api
from flask import flash, redirect, render_template, request, url_for,make_response
from flask_login import login_user,login_required, logout_user
from project.models import Admin_District,Complaints,Rejected_Complaint,Bar
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
import datetime
from flask_mail import Message
from flask import send_file, send_from_directory, safe_join, abort
import flask_excel as excel
import pyexcel
import random


api = Api(app)

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = None
        #print(request.headers['X-Access_Token'])
        try:
            if request.headers['X-Access_Token'] is not None:
                token = request.headers['X-Access-Token']

            if not token:
                return make_response('Invalid Token',401,{'www-Authenticate':'Invalid Token"'})

            try:
                data = jwt.decode(token,app.config['SECRET_KEY'])
                current_user = Admin_District.query.filter_by(admin_email=data['admin_email']).first()
            except:
                return make_response('Invalid Token',401,{'www-Authenticate':'Invalid Token"'})
            return f(current_user,*args,**kwargs)

        except:
            return make_response('Invalid Token',401,{'www-Authenticate':'Invalid Token"'})

    return decorated

class Register(Resource):

    #@staticmethod
    def post(current_user):
        '''Generating public ID'''
        try:
            publicID = str(uuid.uuid4())
            data = request.get_json()

            admin_Name= data['Name']
            admin_email = data['email']
            tel = data['tel']
            post = data['post']
            district_n0 = data['district']
            password = data['password']
            confirm_password = data['confirm_password']
            if admin_email is None or password is None :
                return {'error':'error'}
            if password==confirm_password :
                user = Admin_District(admin_Name=admin_Name,admin_email=admin_email,district_n0=district_n0,post=post,tel=tel,password_hash=password)
                db.session.add(user)
                db.session.commit()
                return data
            else:
                return {'error':'Could not creat account'}

        except Exception:
            return {'error':'Could not creat account'}


class Login1(Resource):
    def post(self):
        #data = request.authorization
        data = request.get_json()
        if not data or not data['username'] or not data['password']:
            return make_response('Could not verify1',401,{'www-Authenticate':'Basic realm-"login required!"'})
        admin = Admin_District.query.filter_by(admin_email=data['username']).first()
        if not admin:
            return make_response('Could not verify2',401,{'www-Authenticate':'Basic realm-"login required!"'})
        if admin.password_hash == data['password']:
            token = jwt.encode({'admin_email':admin.admin_email,'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60)},app.config['SECRET_KEY'])
            return jsonify({'token':token.decode('UTF-8'),'username':admin.admin_email,'district':admin.district_n0})
        return make_response('Could not verify3',401,{'www-Authenticate':'Basic realm-"login required!"'})

class GetComplaints(Resource):
    @token_required
    def post(self,current_user):
        data=request.get_json()

        try:
            #districtno=Complaints.query.filter_by(district=data['district_n0']).first()
            ##while True:
             #   complaint=Complaints.query.filter_by(status="Pending").first()
             #   return complaint.json()

            districtno = Complaints.query.filter_by(district=data['district_n0']).all()
            return [x.json() for x in districtno[-1::-1]]

        except Exception:
            return {'error':'No data'}

class AllComplaints(Resource):
    @token_required
    def post(self,current_user):
        data = request.get_json()
        try:
            complaints = Complaints.query.filter_by(district=data['district_n0'])
            return [x.json() for x in complaints[-1::-1]]

        except Exception:
            return {'Status':'No Complaints available'}

class PieChart(Resource):
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


class PostComplaints(Resource):
    @token_required
    def post(self,current_user):
        data =request.get_json()
        admin=data['admin_email']
        complaint=Complaints.query.filter_by(complaints_refn0=data['complaints_refn0']).first()
        information=Admin_District.query.filter_by(admin_email=admin).first()
        p=str(datetime.date.today())
        if complaint is not None:
            status = data["status"]
            if status =="Resolved":
                complaint.status=data["status"]
                complaint.districtagent_name= information.admin_Name
                complaint.districtagent_idn0=data['districtagent_idn0']
                complaint.districtagent_post=data['districtagent_post']
                complaint.districtagent_signet= information.publicID
                complaint.district_resolutions=data['district_resolutions']
                complaint.classify_complaint=data['classify_complaint']
                complaint.district_description=data['district_description']
                complaint.date_submit=p
                db.session.commit()

            elif status =="Unresolved":
                complaint.districtagent_name= information.admin_Name
                complaint.districtagent_idn0= information.publicID
                complaint.districtagent_post= information.post
                complaint.districtagent_signet= information.tel
                complaint.status=data['status']
                complaint.comments=data['comment']
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
                agent_post= rejected.agent_staff
                district= rejected.district
                poling_station = rejected.poling_station
                complaints_refn0 = rejected.complaints_refn0
                nature_complaint = rejected.nature_complaint
                complaint= rejected.complaint
                agent_staff=rejected.agent_staff
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

class AllDistrictComplaints(Resource):
    @token_required
    def get(self,current_user):
        data=request.get_json()
        try:
            districts =Complaints.query.filter_by(district=data['district_n0']).first()
            return districts.json()
        except Exception:
            return{'error':'no data available'}

class ApprovedCompalints(Resource):
    @token_required
    def get (self,current_user):
        data=request.get_json()
        complaints=Complaints.query.filter_by(status=data['status']).first()
        return complaints.json()

class Complainantsinfo(Resource):
    @token_required
    def post (self,current_user):
        data=request.get_json()
        try:
            complaints=Complaints.query.filter_by(agent_idn0=data['agent_idn0']).first()
            return complaints.json()
        except Exception:
            return{'error':'no agent data'}

class UpdateDeclinedComplaint(Resource):
    @token_required
    def post(self,current_user):
        data=request.get_json()
        admin=data['admin_email']
        information=Admin_District.query.filter_by(admin_email=admin).first()
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
                agent_staff= rejected.agent_staff
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
                update=Complaints(agent_name=agent_name,agent_email=agent_email,agent_phone=agent_phone,agent_idn0=agent_idn0,agent_staff=agent_staff,district=district,
                                  poling_station=poling_station,
                                  complaints_refn0=complaints_refn0,nature_complaint=nature_complaint,complaint=complaint,date=date,districtagent_name=districtagent_name,
                                  districtagent_email=districtagent_email, districtagent_idn0=districtagent_idn0,districtagent_post=districtagent_post,districtagent_signet=districtagent_signet,status=status,
                                  district_resolutions=district_resolutions,classify_complaint=classify_complaint,district_description=district_description,headagent_name=headagent_name,headagent_email=headagent_email,headagent_idn0=headagent_idn0,head_post=head_post,head_signet=head_signet,headresolution=headresolution,
                                  headdescription=headdescription,headclassification=headclassification,comments=comments,date_submit=date_submit)
                db.session.add(update)
                db.session.delete(rejected)
                db.session.commit()


class AllDeclinedComplaints(Resource):
    @token_required
    def post(self,current_user):
        data=request.get_json()
        try:
            complaints = Rejected_Complaint.query.filter_by(district=data['district_n0'])
            return [x.json() for x in complaints[-1::-1]]

        except Exception:
            return {'Status':'No declined Complaints available'}

class excelexport1(Resource):
    @token_required
    def post(self,current_user):
        query_sets = Rejected_Complaint.query.filter_by(status="Declined")
        autoGenFileName = uuid.uuid4()
        filename1 = str(autoGenFileName)+".xls"
        dictionary1 = [x.json() for x in query_sets]
        try:

            pyexcel.save_as(records=dictionary1, dest_file_name=os.path.join(app.config['EXCEL_FOLDER'],filename1))
            #download(filename1)
            return send_file(os.path.join(app.config['EXCEL_FOLDER'],filename=filename1), as_attachment=True)

        except FileNotFoundError:
            abort(404)

class PostsComplaint(Resource):
    @token_required
    def post(self,current_user):

       # while True:
        #    number  = random.randrange(1000000, 9999999)
        # make sure id works

        data = request.form
        dt = datetime.datetime.today().year
        admin_email = data['email']
        agent = Admin_District.query.filter_by(admin_email=data['email']).first()
        agent_email=data['email']
        agent_name = agent.admin_Name
        agent_phone = data['phone']
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
        Complaint_category=data['Complaint_category']
        districtagent_name = ''
        districtagent_email = data['email']
        districtagent_idn0 = ''
        districtagent_post = ''
        districtagent_signet = ''
        status = 'Pending'
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

class Monthly(Resource):
    @token_required
    def post(self,current_user):

       # while True:
        #    number  = random.randrange(1000000, 9999999)
        # make sure id works

        data = request.get_json()
        month = Complaints.query.filter_by(status="Resolved").first()
        date = month.date
        file_date=int(date.split("-")[1])
        sys_date=datetime.datetime.now().month
        if file_date==sys_date:
            try:
                resolved = Complaints.query.filter_by(district=data['district_n0'],status='Resolved').count()

            except Exception:
                resolved = 0

            try:
                unresolved = Complaints.query.filter_by(district=data['district_n0'],status='Unresolved').count()

            except Exception:
                unresolved = 0
            try:
                for i in range(1,13):
                    months=datetime.date(2008, i, 1).strftime('%B')
                    Resolved=0
                    Unresolved=0
                    p=Bar(month=months,Unresolved=Unresolved,Resolved=Resolved)
                    db.session.add(p)
                    db.session.commit()
            except Exception :
                id_=Bar.query.filter_by(id=sys_date).first()
                id_.Resolved=resolved
                id_.Unresolved=unresolved
                db.session.commit()


        unres=Bar.query.all()
        p=[]
        k=[]
        for x in unres:
            p.append(x.Unresolved)
            k.append(x.Resolved)
        return {'deta':p,'dema':k}

##        return [x.json() for x in unres]

class Pendings(Resource):
    @token_required
    def post(self,current_user):
        data = request.get_json()
        pends = Complaints.query.filter_by(district=data['district_n0'],status='Pending')
        return [x.json() for x in pends]

class AdminDistrict(Resource):
    # @token_required
    def post(self):
        data = request.get_json()
        try:

            pends = Admin_District.query.filter_by(district_n0=data['district_n0'])
            return [x.json() for x in pends]
        except Exception:
            return {'error':'no district person '}

class AccountDistrict(Resource):
    # @token_required
    def post(self):
        data=request.get_json()
        account=Admin_District.query.filter_by(district_n0=data['district_n0']).first()
        if account is not None:
            Admin_District.query.filter(Admin_District.district_n0 == data["district_n0"]).delete()
            db.session.commit()
        else:
            pass


class AmendComplaints(Resource):
    @token_required
    def post(self,current_user):
        data =request.get_json()
        admin=data['admin_email']
        complaint=Complaints.query.filter_by(complaints_refn0=data['complaints_refn0']).first()
        information=Admin_District.query.filter_by(admin_email=admin).first()
        p=str(datetime.date.today())
        if complaint is not None:
            status = data["status"]
            if status =="Resolved":
                complaint.classify_complaint=data["classify_complaint"]
                db.session.commit()
            else:
                pass
        else:
            pass

class files2(Resource):
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


class ComplainUpdatezdistrict(Resource):
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




























































