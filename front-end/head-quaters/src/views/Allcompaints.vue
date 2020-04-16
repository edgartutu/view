<template>
<div>
  <navbar/>
  <v-stepper v-model="e1">
    <v-stepper-header class="white" >
      <v-stepper-step class="white--text"  :complete="e1 > 1" step="1">{{userDeta.complainants}}</v-stepper-step>
      <!-- <v-divider></v-divider>
      <v-stepper-step :complete="e1 > 2" step="2">Complaint Resolution</v-stepper-step> -->
      <v-divider></v-divider>
      <v-stepper-step step="2">View</v-stepper-step>
    </v-stepper-header>
    <v-stepper-items>
      <v-stepper-content  step="1">
        <v-container>
          <v-layout  >
            <v-flex
              xs12
              md12  
            >
            <v-card
          class="mb-12"
          
          >
          
                      <v-container>
            <v-layout>
              <v-flex xs12 md4>
                <div class="left" >Commission Representative :</div>
              </v-flex>
              <v-flex xs12 md8>
                <p class="left mx-2">{{userDeta.agentname}}</p>
              </v-flex>
            </v-layout>
            <v-layout>
              <v-flex xs12 md4>
                <div class="left" style="font-weight:bold;">Complainants :</div>
              </v-flex >
              <v-flex xs12 md8>
                <p class="left mx-2">{{userDeta.complainants}}</p>
              </v-flex>
            </v-layout>
            <v-layout>
              <v-flex xs12 md4>
                  <div class="left">Position Held :</div>
              </v-flex >
              <v-flex xs12 md8>
                  <p class="left mx-2">{{userDeta.post}}</p>
              </v-flex>
            </v-layout>
            <v-layout>
              <v-flex xs12 md4>
                  <div class="left">Complainant Phone Number</div>
              </v-flex>
              <v-flex xs12 md8>
                  <p  class="left mx-2">{{userDeta.compn0}}</p>
              </v-flex>
            </v-layout>
            <v-layout>
              <v-flex xs12 md4>
                  <div class="left">Location :</div>
              </v-flex>
              <v-flex xs12 md8>
                  <p  class="left mx-2">{{userDeta.location}}</p>
              </v-flex>
            </v-layout>
             <v-layout>
              <v-flex xs12 md4>
                  <div class="left" style="font-weight:bold;">Reference Number :</div>
              </v-flex>
              <v-flex xs12 md8>
                  <p  class="left mx-2 red--text">{{userDeta.ref}}</p>
              </v-flex>
            </v-layout>
            <v-layout>
              <v-flex xs12 md4>
                  <div class="left">Complaint Clasification :</div>
              </v-flex>
              <v-flex xs12 md8>
                  <p  class="left mx-2 ">{{userDeta. complaint_detail}}</p>
              </v-flex>
            </v-layout>
             <v-layout>
              <v-flex xs12 md4>
                  <div class="left">Complaint category :</div>
              </v-flex>
              <v-flex xs12 md8>
                  <p  class="left mx-2 ">{{userDeta.Complaint_category}}</p>
              </v-flex>
            </v-layout>
            <v-layout>
              <v-flex xs12 md4>
                  <div class="left" style="font-weight:bold;">Complaint Details :</div>
              </v-flex>
              <v-flex xs12 md8>
                  <p  class="left mx-2 ">{{userDeta.complaint_detail}}</p>
              </v-flex>
            </v-layout>
            <v-layout>
              <v-flex xs12 md4>
                  <div class="left">Date Submited :</div>
              </v-flex>
              <v-flex xs12 md8>
                  <p  class="left mx-2 ">{{userDeta.date}}</p>
              </v-flex>
            </v-layout>
             <v-layout>
              <v-flex xs12 md4>
                  <div class="left">District submission :</div>
              </v-flex>
              <v-flex xs12 md8>
                   <v-dialog
                  v-model="dialog"
                  width="500"
                >
                  <template v-slot:activator="{ on }">
                    <v-btn
                      small
                      style=" background-color: #004080;"
                      dark
                      v-on="on"
                      flat
                      class="white--text left"
                    >
                      View
                    </v-btn>
                  </template>

                  <v-card>
                    <v-card-text>
                   {{userDeta.description}}
                      
                    </v-card-text>

                    <v-divider></v-divider>

                    <v-card-actions>
                      <v-spacer></v-spacer>
                      
                        <!-- <v-btn
                        style=" background-color: #004080;"
                        text
                        @click="dialog = false"
                      >
                        Exit
                      </v-btn> -->
                    
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </v-flex>
            </v-layout>
            <v-layout>
              <v-flex xs12 md4>
                  <div class="left">Resolution date :</div>
              </v-flex>
              <v-flex xs12 md8>
                  <p  class="left mx-2 ">{{userDeta.date_resolved}}</p>
              </v-flex>
            </v-layout>
            
          <v-layout>
              <v-flex xs12 md4>
                  <div class="left" style="font-weight:bold;">Details of Resolution :</div>
              </v-flex>
              <v-flex xs12 md8>
                  <p  class="left mx-2 ">{{userDeta.resolving}}</p>
              </v-flex>
            </v-layout>
          <!-- <v-container> -->
               
                </v-container>

                <div id="appz" style=" background-color: #004080;"  >
            <v-layout>
              <v-flex xs6 md6>
              <router-link to="/resolved">
                <v-btn flat class="left" style=" background-color: #004080;" small tile outlined>
                  Back
                </v-btn>
              </router-link>

            </v-flex>
            <v-flex xs6 md6>
              <v-btn
              flat
              class="right"
               style=" background-color: #004080;"
                @click="e1 = 2"
                small
                tile 
                outlined
              >
                View Certificate
              </v-btn>

            </v-flex>

            </v-layout>
            
            
          
         </div>
          <!-- <v-container> --> 
                  
            
                
               
             <!-- </v-container> -->
               </v-card>
            </v-flex>
          </v-layout>
        </v-container>
         <!-- <decline/> -->
    
      </v-stepper-content>


        
      <v-stepper-content step="2">
        <v-container>
          <v-layout>
            <v-flex xs12 md12>
              
                   
                       <v-avatar  id="pic" width="500" size="100" class="center">
                        
                        <img
                            src="../assets/img/ECLOGO.jpg"
                            alt="John"
                          id="prints"  
                          style="width:200px;"
                        >
                        </v-avatar>
                         <v-card flat id="title">
                           <h3>The Electoral Commission </h3>
                        <h3 style="color: #004080;" class="font-weight-bold">Certificate Of Resolution</h3>
                         
                        <h3 class="font-weight-bold">{{userDeta.complainants}}</h3>
                        <h4 class="red--text" style="font-weight:bold;">{{userDeta.ref}}</h4>
                         </v-card>
                         <!-- <v-card flat id="log">
                            
                         </v-card> -->
                        
                       <v-card  id="print" class="mb-12"  flat >
                         <div style="width:10px;" class="logo-print"></div>
                        <h4 class="font-weight-bold">Complaint</h4>
                        <p>{{userDeta.complaint}}</p>
                        <h4 class="font-weight-bold" >Commission Decission </h4>
                        <p>{{userDeta.dreslon}}</p><p>{{userDeta.resoln}}</p>
                         </v-card>
                         
                         <v-card flat id="date">
                           <div  style="bottom: 0;" class="left " >ReportDate:  {{userDeta.date}}  </div><br>
                        
                        <div  style="bottom: 0;" class="left">ResolvedDate: {{userDeta.date_resolved}}</div>

                         </v-card>
                        
                        <!-- <div  style="bottom: 0;" class="right">Signature: ...........................................</div>
                        <br>
                        <div  style="bottom: 0;" class="right"> Chairperson Electoral Commision</div>
                         -->
                        <!-- <p class="left"> </p> -->
                      
                        
                   
                  
            </v-flex>
          </v-layout>
        </v-container>
         <v-btn
          class="left"
          style=" background-color: #004080;"
          @click="e1 = 1"
          small
          tile 
          outlined
        >
          Previous
        </v-btn>
        <v-btn
        class="right"
          color="teal"
          @click.native="print"
        >
          Print
        </v-btn>
      </v-stepper-content>
    </v-stepper-items>
  </v-stepper>
  </div>
  
</template>
<script>
import axios from 'axios'
import data1 from '@/views/Complaints.vue'
// import decline from '../components/DashViews/Decline.vue'
  import router from '../router'
  import navbar from '../components/DashViews/NavBar'
  export default {
      name:'Stepperview',
    components:{
      data1,
     
      navbar
    },
    data () {
      return {
        e1: 0,
        userDeta: 0,
        debug: false,
        post:"None",
        nin:"None",
        classification:"None",
        resolution:"",
        details:"",
        signature:"",
        nameRules: [
        v => !!v || 'Input is required',
        // v => (v && v.length <= 10) || 'Name must be less than 10 characters',
      ],
      user: localStorage.getItem('user'),
      token: localStorage.getItem('token')
      
      }
    },
    created() {
            this.userDeta = this.$route.params.userDeta;
        },
        computed: {
  isDisabled() {
    if (status =="Resolved" ){
      return false;
    }else{
      return true;
    }
    
  }
},
    methods:{
      submit(){
        axios.post('http://127.0.0.1:5000/adminpostcomplaints',{
          'status':'Resolved','complaints_refn0':this.userData.refnumber, 'admin_email':this.user,
          'nin':this.nin,'districtagent_post':this.post,
          'district_resolutions':this.resolution,'classify_complaint':this.classification,
          'district_description':this.details,
          'head_signature':this.signature
          },{headers:{'x-access-token':this.token}})
      },
      print(){
        // Get HTML to print from element
const prtHtml = document.getElementById('print').innerHTML;
const prtpic = document.getElementById('pic').innerHTML;
const prtdate = document.getElementById('date').innerHTML;
const prttitle = document.getElementById('title').innerHTML;
// const prtlog = document.getElementById('log').innerHTML;
// const prtHtmls = document.getElementById('prints').innerHTML;

// Get all stylesheets HTML
let stylesHtml = '';
for (const node of [...document.querySelectorAll('link[rel="stylesheet"], style')]) {
  stylesHtml += node.outerHTML;
}

// Open the print window
const WinPrint = window.open('', '', 'left=0,top=0,width=800,height=600,toolbar=0,scrollbars=0,status=0');

WinPrint.document.write(`<!DOCTYPE html>
<html>
  <head>
    ${stylesHtml}
  </head>
  <body>
  
 <div  style="margin-top:3%;margin-left:3%;margin-right:3%;bottom:0%;">
<div style="margin-left:35%;" >${prtpic}</div>
<div style="margin-left:30%;" >${prttitle}</div>
 
 ${prtHtml}
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <div  style="margin-bottom: 5%;" > ${prtdate}</div>
      <div  style="margin-bottom: 0%;" class="right">Signature: ...........................................</div>
      <br>
      <div  style="bottom: 0;" class="right"> Chairperson Electoral Commision</div>
  </body>
</html>`);
setTimeout(function() {
    WinPrint.print();
}, 2500)

// WinPrint.document.close();
// WinPrint.focus();
// WinPrint.print();
// WinPrint.close();
      }
    }
  }
</script>
<style>
@media all{
   printed-div{
       display:none;
   }
}

@media print{
   printed-div{
       display:block;
   }
   .logo-print{
     
       width:10px;
       height:10px;
       display: list-item;
       list-style-image: url(../assets/img/ECLOGO.jpg);
       list-style-position: inside;
       opacity: 0.1;
  filter: alpha(opacity=50);
   }
}


</style>