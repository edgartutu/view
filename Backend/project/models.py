# set up  db in __init__.py under my projects folder

from project import db, login_manager,app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin,current_user,login_user,logout_user
from flask_admin.contrib.sqla import ModelView
from wtforms import form, fields, validators
from flask_admin import Admin
import os
from flask import Flask,url_for,redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
import flask_admin as admins
import flask_login as login
from flask_admin.contrib import sqla
from flask_admin import helpers, expose
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    login = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(64))

    def __init__(self,first_name,last_name,login,email, password):
        self.first_name = first_name
        self.last_name=last_name
        self.login=login
        self.email=email
        self.password = password

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username

class LoginForm(form.Form):
    login = fields.StringField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        # we're comparing the plaintext pw with the the hash from the db
        if not check_password_hash(user.password, self.password.data):
        # to compare plain text passwords use
        # if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(login=self.login.data).first()


class RegistrationForm(form.Form):
    first_name = fields.StringField()
    last_name = fields.StringField()
    login = fields.StringField(validators=[validators.required()])
    email = fields.StringField()
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        if db.session.query(User).filter_by(login=self.login.data).count() > 0:
            raise validators.ValidationError('Duplicate username')


# Initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)


# Create customized model view class
class MyModelView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated


# Create customized index view class that handles login & registration
class MyAdminIndexView(admins.AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))
        link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') + '">Click here to register.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegistrationForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = User(first_name=form.first_name.data,last_name=form.last_name.data,login=form.login.data,email=form.email.data,password=form.password.data)

            form.populate_obj(user)
            # we hash the users password to avoid saving it as plaintext in the db,
            # remove to use plain text:
            user.password = generate_password_hash(form.password.data)

            db.session.add(user)
            db.session.commit()

            login.login_user(user)
            return redirect(url_for('.index'))
        link = '<p>Already have an account? <a href="' + url_for('.login_view') + '">Click here to log in.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))


# Flask views
@app.route('/')
def index():
    return render_template('index.html')


# Initialize flask-login
init_login()

# Create admin
# admin = admin.Admin(app)
admin=Admin(app, 'EC-ADMIN', index_view=MyAdminIndexView(), base_template='my_master.html')
# Add view
# admin.add_view(MyModelView(User, db.session))


class Admin_District(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True,index=True)
    admin_email = db.Column(db.String(64),unique=True)
    admin_Name= db.Column(db.String(100))
    tel = db.Column(db.String(100))
    district_n0 = db.Column(db.String(100))
    post = db.Column(db.String(100))
    publicID = db.Column(db.String(100))
    password_hash = db.Column(db.String(128))


    def __init__(self,admin_email,admin_Name,password_hash,tel,post,district_n0):
        self.admin_email = admin_email
        self.admin_Name=admin_Name
        self.tel=tel
        self.district_n0=district_n0
        self.post=post
        self.password_hash = password_hash

    def check_password(self,password_hash):     
        return check_password_hash(self.password_hash,password_hash)

    def json(self):
        return {'admin_email':self.admin_email,'admin_Name':self.admin_Name,'post':self.post,'tel':self.tel,'district_n0':self.district_n0}

class Admin_Headquaters(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True,index=True)
    admin_email = db.Column(db.String(64),unique=True)
    admin_Name= db.Column(db.String(100))
    publicID = db.Column(db.String(100))
    password = db.Column(db.String(128))


    def __init__(self, admin_email,admin_Name, password):
        self.admin_email = admin_email
        self.admin_Name=admin_Name
        self.password = password

    def json(self):
        return {'admin_email':self.admin_email,'admin_name':self.admin_Name,'password':self.password}

    def check_password(self,password):     
        return check_password_hash(self.password,password)


class PolingAgent(db.Model, UserMixin):
    nin = db.Column(db.String(64), primary_key=True, unique=True, index=True)
    agent_email = db.Column(db.String(64))
    phone_number = db.Column(db.String(200))
    name = db.Column(db.String(200))
    agent_image = db.Column(db.String(200))
    publicID = db.Column(db.String(100))
    password_hash = db.Column(db.String(128))

    def __init__(self,agent_email, password_hash,name,phone_number,agent_image, nin):
        self.agent_email = agent_email
        self.name = name
        self.phone_number=phone_number
        self.nin=nin
        self.agent_image=agent_image
        self.password_hash = generate_password_hash(password_hash)

    def json(self):
        return {'nin':self.nin,'name':self.name,'email':self.agent_email,'password_hash':self.password_hash,'phone':self.phone_number}
        

    def check_password(self,password_hash):
        return check_password_hash(self.password_hash,password_hash)



class Complaints(db.Model, UserMixin):
    
    complaints_refn0 = db.Column(db.String(500) , primary_key=True, unique=True, index=True)
    agent_name = db.Column(db.String(25))
    agent_email=db.Column(db.String(100))
   
    agent_name = db.Column(db.String(25))
    agent_email=db.Column(db.String(100))
    agent_phone=db.Column(db.String(100))
    agent_idn0=db.Column(db.String(100))
    agent_staff=db.Column(db.String(100))
    district=db.Column(db.String(100))
    poling_station = db.Column(db.String(500))
    nature_complaint = db.Column(db.String(500))
    Complaint_category = db.Column(db.String(500))
    complaint=db.Column(db.String(1000))
    date = db.Column(db.String(100))
    compalianant_name=db.Column(db.String(100))
    districtagent_name=db.Column(db.String(100))
    districtagent_email=db.Column(db.String(1000))
    
    districtagent_idn0=db.Column(db.String(1000))
    districtagent_post=db.Column(db.String(1000))
    districtagent_signet=db.Column(db.String(1000))
    status= db.Column(db.String(100))
    district_resolutions = db.Column(db.String(10000))
    classify_complaint= db.Column(db.String(500))
    district_description = db.Column(db.String(10000))
    
    headagent_name=db.Column(db.String(100))
    headagent_email=db.Column(db.String(100))
    headagent_idn0=db.Column(db.String(100))
    head_post=db.Column(db.String(100))
    head_signet=db.Column(db.String(1000))
    headresolution = db.Column(db.String(10000))
    headdescription = db.Column(db.String(10000))
    headclassification= db.Column(db.String(10000))
    date_submit=db.Column(db.String(100))
    comments = db.Column(db.String(500))
    files = db.Column(db.String(100))
    
    
    ## status of the project  

    def __init__(self,agent_name,agent_email,agent_phone,agent_idn0,agent_staff,district,poling_station,compalianant_name,
                 complaints_refn0,nature_complaint,complaint,date,districtagent_name,districtagent_email,Complaint_category,
                 districtagent_idn0,districtagent_post,districtagent_signet,status,district_resolutions,
                 classify_complaint,district_description,headagent_name,headagent_email,files,
                 headagent_idn0,head_post,head_signet,headresolution,headdescription,headclassification,comments,date_submit):
        
        self.agent_name = agent_name
        self.files = files
        self.agent_email = agent_email
        self.agent_phone = agent_phone
        self.agent_idn0 = agent_idn0
        self.agent_staff= agent_staff
        self.district = district
        self.poling_station = poling_station
        self.complaints_refn0 = complaints_refn0
        self.nature_complaint = nature_complaint
        self.complaint = complaint
        self.date = date
        self.compalianant_name=compalianant_name
        self.Complaint_category=Complaint_category
        self.districtagent_name = districtagent_name
        self.districtagent_email = districtagent_email
        self.districtagent_idn0 = districtagent_idn0
        self.districtagent_post = districtagent_post
        self.districtagent_signet = districtagent_signet
        self.status=status
        self.district_resolutions=district_resolutions
        self.classify_complaint = classify_complaint
        self.district_description = district_description
        self.headagent_name = headagent_name
        self.headagent_email = headagent_email
        self.headagent_idn0 = headagent_idn0
        self.head_post=head_post
        self.head_signet=head_signet
        self.headresolution = headresolution
        self.headdescription = headdescription
        self.headclassification=headclassification
        self.date_submit=date_submit
        self.comments=comments





    def json(self):
        return {'agent_name':self.agent_name,'files':self.files,
                'agent_idn0':self.agent_idn0, 'date_submit':self.date_submit,'Complaint_category':self.Complaint_category,
                'district':self.district,'compalianant_name':self.compalianant_name,'headdescription':self.headdescription,'headresolution':self.headresolution,
                'poling_station':self.poling_station, 'complaints_refn0':self.complaints_refn0,'nature_complaint':self.nature_complaint,'complaint':self.complaint,'date':self.date,
                'districtagent_name':self.districtagent_name,'districtagent_email':self.districtagent_email,'districtagent_idn0':self.districtagent_idn0,
                'districtagent_post':self.districtagent_post,'districtagent_signet':self.districtagent_signet,'status':self.status,'district_resolutions': self.district_resolutions,
                'classify_complaint':self.classify_complaint,'district_description':self.district_description,'headagent_name':self.headagent_name,
                'headagent_email':self.headagent_email,'headagent_idn0':self.headagent_idn0,'head_post':self.head_post,'head_signet': self.head_signet,
                'headclassification':self.headclassification,'comments': self.comments,'agent_phone':self.agent_phone,'agent_staff':self.agent_staff,'agent_email':self.agent_email
                }

class Rejected_Complaint(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    agent_name = db.Column(db.String(25))
    agent_email=db.Column(db.String(100))
    agent_phone=db.Column(db.String(100))
    agent_idn0=db.Column(db.String(100))
    agent_post=db.Column(db.String(100))
    agent_staff=db.Column(db.String(100))
    district=db.Column(db.String(100))
    poling_station = db.Column(db.String(500))
    complaints_refn0 = db.Column(db.String(500))
    nature_complaint = db.Column(db.String(500))
    complaint=db.Column(db.String(1000))
    date = db.Column(db.String(100))
    districtagent_name=db.Column(db.String(100))
    status=db.Column(db.String(100))
    comment = db.Column(db.String(500))
    ## status of the project  

    def __init__(self,agent_name, agent_staff,agent_email,agent_phone,agent_idn0,agent_post,district,poling_station,
                 complaints_refn0,nature_complaint,date,districtagent_name,complaint,
                 status,comment):
    
        self.agent_name = agent_name
        self.agent_email = agent_email
        self.agent_phone = agent_phone
        self.agent_idn0 = agent_idn0
        self.agent_post= agent_post
        self.agent_staff= agent_staff
        self.district = district
        self.poling_station = poling_station
        self.complaints_refn0 = complaints_refn0
        self.nature_complaint = nature_complaint
        self.complaint=complaint
        self.date = date
        self.districtagent_name = districtagent_name
        self.status=status
        self.comment=comment
       

    def json(self):
        return {'agent_name':self.agent_name,'agent_email':self.agent_email,'agent_phone':self.agent_phone,
                'agent_idn0':self.agent_idn0, 'agent_post':self.agent_post,
                'district':self.district,
                'poling_station':self.poling_station, 'complaints_refn0':self.complaints_refn0,'nature_complaint':self.nature_complaint,'date':self.date,
                'districtagent_name':self.districtagent_name,'status':self.status,'comment':self.comment,'complaint':self.complaint}


class Bar(db.Model,UserMixin):
    __tablename__='bar'
    id = db.Column(db.Integer())
    month = db.Column(db.String(25),primary_key=True, unique=True, index=True)
    Resolved = db.Column(db.Integer)
    Unresolved = db.Column(db.Integer)
    

    def __init__(self,id,month,Unresolved, Resolved):
        self.id=id
        self.Resolved =Resolved
        self.month = month
        self.Unresolved = Unresolved

    def json(self):
        return{'Unresolved': self.Unresolved,'Resolved':self.Resolved}
        
    

class ExportApproved(db.Model, UserMixin):
    __tablename__ = 'ApprovedExports'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(500))

    def __init__(self,name):
        self.name = name

    def json(self):
        return {"name":self.name}


class ComplaintStore(db.Model, UserMixin):
    
    complaints_refn0 = db.Column(db.String(500) , primary_key=True, unique=True, index=True)
    agent_name = db.Column(db.String(25))
    agent_email=db.Column(db.String(100))
   
    agent_name = db.Column(db.String(25))
    agent_email=db.Column(db.String(100))
    agent_phone=db.Column(db.String(100))
    agent_idn0=db.Column(db.String(100))
    agent_staff=db.Column(db.String(100))
    district=db.Column(db.String(100))
    poling_station = db.Column(db.String(500))
    nature_complaint = db.Column(db.String(500))
    complaint=db.Column(db.String(1000))
    date = db.Column(db.String(100))
    
    districtagent_name=db.Column(db.String(100))
    districtagent_email=db.Column(db.String(1000))
    
    districtagent_idn0=db.Column(db.String(1000))
    districtagent_post=db.Column(db.String(1000))
    districtagent_signet=db.Column(db.String(1000))
    status= db.Column(db.String(100))
    district_resolutions = db.Column(db.String(10000))
    classify_complaint= db.Column(db.String(500))
    district_description = db.Column(db.String(10000))
    complainants=db.Column(db.String(100))
    headagent_name=db.Column(db.String(100))
    headagent_email=db.Column(db.String(100))
    headagent_idn0=db.Column(db.String(100))
    head_post=db.Column(db.String(100))
    head_signet=db.Column(db.String(1000))
    headresolution = db.Column(db.String(10000))
    headdescription = db.Column(db.String(10000))
    headclassification= db.Column(db.String(10000))
    date_submit=db.Column(db.String(100))
    comments = db.Column(db.String(500))
    filez=db.Column(db.String(500))
    
    
    ## status of the project  

    def __init__(self,agent_name,agent_email,agent_phone,agent_idn0,agent_staff,district,poling_station,filez,
                 complaints_refn0,nature_complaint,complaint,date,districtagent_name,districtagent_email,complainants,
                 districtagent_idn0,districtagent_post,districtagent_signet,status,district_resolutions,
                 classify_complaint,district_description,headagent_name,headagent_email,
                 headagent_idn0,head_post,head_signet,headresolution,headdescription,headclassification,comments,date_submit):
        
        self.agent_name = agent_name
        self.agent_email = agent_email
        self.agent_phone = agent_phone
        self.agent_idn0 = agent_idn0
        self.agent_staff= agent_staff
        self.district = district
        self.poling_station = poling_station
        self.complaints_refn0 = complaints_refn0
        self.nature_complaint = nature_complaint
        self.complaint = complaint
        self.complainants=complainants
        self.date = date
        self.districtagent_name = districtagent_name
        self.districtagent_email = districtagent_email
        self.districtagent_idn0 = districtagent_idn0
        self.districtagent_post = districtagent_post
        self.districtagent_signet = districtagent_signet
        self.status=status
        self.district_resolutions=district_resolutions
        self.classify_complaint = classify_complaint
        self.district_description = district_description
        self.headagent_name = headagent_name
        self.headagent_email = headagent_email
        self.headagent_idn0 = headagent_idn0
        self.head_post=head_post
        self.head_signet=head_signet
        self.headresolution = headresolution
        self.headdescription = headdescription
        self.headclassification=headclassification
        self.date_submit=date_submit
        self.comments=comments
        self.filez=filez





    def json(self):
        return {'agent_name':self.agent_name,'agent_email':self.agent_email,'agent_phone':self.agent_phone,
                'agent_idn0':self.agent_idn0, 'agent_staff':self.agent_staff,'compalianant_name':self.complainants,
                'district':self.district,"filez":self.filez,
                'poling_station':self.poling_station, 'complaints_refn0':self.complaints_refn0,'nature_complaint':self.nature_complaint,'complaint':self.complaint,'date':self.date,
                'districtagent_name':self.districtagent_name,'districtagent_email':self.districtagent_email,'districtagent_idn0':self.districtagent_idn0,
                'districtagent_post':self.districtagent_post,'districtagent_signet':self.districtagent_signet,'status':self.status,'district_resolutions': self.district_resolutions,
                'classify_complaint':self.classify_complaint,'district_description':self.district_description,'headagent_name':self.headagent_name,
                'headagent_email':self.headagent_email,'headagent_idn0':self.headagent_idn0,'head_post':self.head_post,'head_signet': self.head_signet,
                'headresolution':self.headresolution,'headdescription':self.headdescription,'headclassification':self.headclassification,'date_submit':self.date_submit,'comments': self.comments
                }


admin.add_view(MyModelView(Admin_District,db.session))
admin.add_view(MyModelView(Admin_Headquaters,db.session))
admin.add_view(MyModelView(Complaints,db.session))
admin.add_view(MyModelView(ComplaintStore,db.session))
admin.add_view(MyModelView(Rejected_Complaint,db.session))
admin.add_view(MyModelView(PolingAgent,db.session))
admin.add_view(MyModelView(User,db.session))

db.create_all()
