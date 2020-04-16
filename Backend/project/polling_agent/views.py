from project import app, db
from project.models import Admin_District,Complaints,Rejected_Complaint,PolingAgent,Complaints
from flask_restful import Resource, Api
from flask import flash, redirect, render_template, request, url_for,make_response
from flask_login import login_user,login_required, logout_user
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
import random

api = Api(app)

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return make_response('Invalid Token',401,{'www-Authenticate':'Invalid Token"'})
        try:
            data = jwt.decode(token,app.config['SECRET_KEY'])
            current_user = PolingAgent.query.filter_by(agent_email=data['email']).first()
        except:
            return make_response('Invalid Token',401,{'www-Authenticate':'Invalid Token"'})
        return f(current_user,*args,**kwargs)   
    return decorated


class PollingAgentLogin(Resource):
    def post(self):
        data = request.get_json()
        '''checking if authorization information is complete'''
        if not data or not data['username'] or not data['password']:
            return make_response('Could not verify',401,{'www-Authenticate':'Basic realm-"login required!"'})
        polling_agent = PolingAgent.query.filter_by(agent_email=data['username']).first()
        
        if not polling_agent:
            return make_response('Could not verify',401,{'www-Authenticate':'Basic realm-"login required!"'})       

        if check_password_hash(polling_agent.password_hash,data['password']):
            token = jwt.encode({'agent_email':polling_agent.agent_email,'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=120)},app.config['SECRET_KEY'])
            return jsonify({'token':token.decode('UTF-8'),"email":polling_agent.agent_email,'nin':polling_agent.nin})
        return make_response('Could not verify',401,{'www-Authenticate':'Basic realm-"login required!"'})

class PollingAgentRegistration(Resource):
    def post(self):
        data = request.form
        try:
            email = data["email"]
            phone_number = data["phone_number"]
            name = data["name"]
            password_hash = data["password"]
            nin = data["nin"]
            
    ##        image = request.files["file"]
    ##        imagename = secure_filename(file.filename)
    ##        imageExt = imagename.split('.')[1]
    ##        autoname = name+' '+str(phone_number)+'.'+imageExt
    ##        file.save(os.path.join(app.config['PROFILE_FOLDER'],autoname))


            pollingagent = PolingAgent(nin=nin,name=name,agent_email=email,phone_number=phone_number,password_hash=password_hash,agent_image='none')

            db.session.add(pollingagent)
            db.session.commit()

            return {'status':'Success'}
        except Exception:
            return {'error':'account already exists'}

class PostComplaint(Resource):
##    @token_required
    def post(self):

       # while True:
        #    number  = random.randrange(1000000, 9999999)
        # make sure id works
        
        data = request.form
        dt = datetime.datetime.today().year
        agent_email = data['email']
        agent = PolingAgent.query.filter_by(agent_email=data['email']).first() 
        agent_name = agent.name
        agent_phone = agent.phone_number
        agent_idn0 = agent.nin
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
        districtagent_name = ''
        districtagent_email = ''
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
        filename = secure_filename(file.name)
        fileext = filename.splite('.')[1]
        newfilename = str(id_)+'.'+ fileext
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],newfilename))

        complaint = Complaints(agent_email=agent_email,agent_name=agent_name,agent_phone=agent_phone,agent_idn0=agent_idn0,agent_staff=agent_staff,
                                district=district,poling_station=poling_station,complaints_refn0=complaints_refn0,nature_complaint=nature_complaint,
                                date=date,districtagent_name=districtagent_name,districtagent_email=districtagent_email,districtagent_idn0=districtagent_idn0,
                                districtagent_post=districtagent_post,files=newfilename,districtagent_signet=districtagent_signet,status=status,district_resolutions=districtagent_resolutions,
                                classify_complaint=classify_complaint,district_description=district_description,headagent_name=headagent_name,
                                headagent_email=headagent_email,headagent_idn0=headagent_idn0,head_post=head_post,head_signet=head_signet,
                                headresolution=headresolution,headdescription=headdescription,headclassification=headclassification,date_submit=date_submit,comments=comments,complaint=complaint)
        
        db.session.add(complaint)
        db.session.commit()


class GetComplaint(Resource):
##    @token_required
    def post(self):
        data = request.get_json()
        p=Complaints.query.filter_by(agent_idn0=data['agent_idn0'])
        return [x.json()for x in p[-1::-1]]


class PostComplaintshead(Resource):
##    @token_required
    def post(self):

       # while True:
        #    number  = random.randrange(1000000, 9999999)
        # make sure id works
        
        data = request.get_json()
        dt = datetime.datetime.today().year
        agent_email = data['email']
        agent = PolingAgent.query.filter_by(agent_email=data['email']).first() 
        agent_name = agent.name
        agent_phone = agent.phone_number
        agent_idn0 = agent.nin
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
        districtagent_name = ''
        districtagent_email = ''
        districtagent_idn0 = ''
        districtagent_post = ''
        districtagent_signet = ''
        status = 'Unresolved'
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

        complaint = Complaints(agent_email=agent_email,agent_name=agent_name,agent_phone=agent_phone,agent_idn0=agent_idn0,agent_staff=agent_staff,
                                district=district,poling_station=poling_station,complaints_refn0=complaints_refn0,nature_complaint=nature_complaint,
                                date=date,districtagent_name=districtagent_name,districtagent_email=districtagent_email,districtagent_idn0=districtagent_idn0,
                                districtagent_post=districtagent_post,districtagent_signet=districtagent_signet,status=status,district_resolutions=districtagent_resolutions,
                                classify_complaint=classify_complaint,district_description=district_description,headagent_name=headagent_name,
                                headagent_email=headagent_email,headagent_idn0=headagent_idn0,head_post=head_post,head_signet=head_signet,
                                headresolution=headresolution,headdescription=headdescription,headclassification=headclassification,date_submit=date_submit,comments=comments,complaint=complaint)
        
        db.session.add(complaint)
        db.session.commit()


