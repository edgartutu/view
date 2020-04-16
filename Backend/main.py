from project import app, db
from flask_restful import Resource, Api
from flask_restful import Api
## change thr names of these files
from project.polling_agent.views import PostComplaintshead,PollingAgentLogin,PollingAgentRegistration,PostComplaint,GetComplaint
from project.admin_district.views import ComplainUpdatezdistrict,AmendComplaints,files2,AccountDistrict,AdminDistrict,Pendings,PostsComplaint,Monthly,Register,PieChart,Complainantsinfo,UpdateDeclinedComplaint,Login1,AllComplaints,excelexport1,GetComplaints,PostComplaints,AllDistrictComplaints,ApprovedCompalints,AllDeclinedComplaints
##from project.admin_headquaters.views import AminPostComplaints,AdminGetComplaints
from project.admin_headquaters.views import  AdminPass,ComplainUpdates,filezresolved,files,Tabledistrict,Account,Accounts,AminStore,AllDeclinedComplaintsadmin,CodeDistrict,PieChartsdistrict,UpdateDeclinedComplaints,Unresolves, Monthlys,LoginHeadquaters,Register2,AllDistrictheadComplaints,PostzComplaint,AminPostComplaints,AdminGetComplaints,AllAdminGetComplaints,AdminPieChart,Alllevelones

api = Api(app)
## Polling agents
api.add_resource(PollingAgentLogin, '/pollingagentlogin')
api.add_resource(PollingAgentRegistration, '/pollingagentregistration')
api.add_resource(PostComplaint, '/postcomplaint')
api.add_resource(GetComplaint, '/GetComplaint')
api.add_resource(PostComplaintshead, '/PostComplaintshead')


## District Admin
api.add_resource(Register, '/register')
api.add_resource(Login1, '/districtadminlogin')
api.add_resource(GetComplaints, '/getcomplaints')
api.add_resource(PostComplaints, '/postcomplaints')
api.add_resource(AllDistrictComplaints, '/alldistrictcomplaints')
api.add_resource(ApprovedCompalints, '/approvedcomplaints')
api.add_resource(Complainantsinfo, '/complainantsinfor')
api.add_resource(UpdateDeclinedComplaint, '/updatedeclinedcomplaint')
api.add_resource(AllComplaints, '/allcomplaints')
api.add_resource(PieChart, '/piechart')
api.add_resource(AllDeclinedComplaints, '/AllDeclinedComplaints')
api.add_resource(excelexport1, '/excelexport1')
api.add_resource(PostsComplaint, '/postadmin1Complaint')
api.add_resource(Monthly, '/Monthly')
api.add_resource(Pendings, '/Pendings')
api.add_resource(AdminDistrict, '/AdminDistrict')
api.add_resource(AccountDistrict, '/AccountDistrict')
api.add_resource(AmendComplaints, '/AmendComplaints')
api.add_resource(files2, '/files2')
api.add_resource(ComplainUpdatezdistrict, '/ComplainUpdatezdistrict')

## Head Admin
api.add_resource(Register2, '/head_register')
api.add_resource(LoginHeadquaters, '/loginheadquaters')
api.add_resource(AdminGetComplaints, '/admingetcomplaints')
api.add_resource(AminPostComplaints, '/adminpostcomplaints')
api.add_resource(AllAdminGetComplaints, '/alladmincomplaints')
api.add_resource(AdminPieChart, '/adminpiechart')
api.add_resource(Alllevelones, '/Alllevelones')
api.add_resource(PostzComplaint, '/Postzadmin2Complaint')
api.add_resource(AllDistrictheadComplaints, '/AllDistrictheadComplaints')
api.add_resource(Unresolves, '/Unresolves')
api.add_resource(UpdateDeclinedComplaints, '/UpdateDeclinedComplaints')
api.add_resource(PieChartsdistrict, '/PieChartsdistrict')
api.add_resource(CodeDistrict, '/CodeDistrict')
api.add_resource(Monthlys, '/Monthlysbar')
api.add_resource(AllDeclinedComplaintsadmin, '/AllDeclinedComplaintsadmin')
api.add_resource(AminStore, '/AminStore')
api.add_resource(Accounts, '/Accounts')
api.add_resource(Account, '/Account')
api.add_resource(Tabledistrict, '/Tabledistrict')
api.add_resource(files, '/files')
api.add_resource(filezresolved, '/filezresolved')
api.add_resource(ComplainUpdates, '/ComplainUpdates')
api.add_resource(AdminPass, '/AdminPass')

##api.add_resource(AllStored,'/AllStored')




if __name__ == '__main__':
    app.run(debug=True)

