<template>
<div>
  <navbar/>
  <v-stepper v-model="e1">
    <v-stepper-header class="white" >
      <v-stepper-step class="white--text"  :complete="e1 > 1" step="1">Complaint Details - {{userData.complainants}}</v-stepper-step>
      <v-divider></v-divider>
      <v-stepper-step :complete="e1 > 2" step="2">Complaint Resolution</v-stepper-step>
      <v-divider></v-divider>
      <v-stepper-step step="3">View</v-stepper-step>
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
                <div class="left" >Complainant :</div>
              </v-flex>
              <v-flex xs12 md8>
                <p class="left mx-2">{{userData.nameofcomplainant}}</p>
              </v-flex>
            </v-layout>
            <v-layout>
              <v-flex xs12 md4>
                <div class="left" style="font-weight:bold;">Staff :</div>
              </v-flex >
              <v-flex xs12 md8>
                <p class="left mx-2">{{userData.post}}</p>
              </v-flex>
            </v-layout>
            <v-layout>
              <v-flex xs12 md4>
                  <div class="left">Position Held :</div>
              </v-flex >
              <v-flex xs12 md8>
                  <p class="left mx-2">{{userData.post}}</p>
              </v-flex>
            </v-layout>
            <v-layout>
              <v-flex xs12 md4>
                  <div class="left">Complainant Phone Number</div>
              </v-flex>
              <v-flex xs12 md8>
                  <p  class="left mx-2">{{userData.compn0}}</p>
              </v-flex>
            </v-layout>
            <v-layout>
              <v-flex xs12 md4>
                  <div class="left">Location :</div>
              </v-flex>
              <v-flex xs12 md8>
                  <p  class="left mx-2">{{userData.location}}</p>
              </v-flex>
            </v-layout>
             <v-layout>
              <v-flex xs12 md4>
                  <div class="left" style="font-weight:bold;">Reference Number :</div>
              </v-flex>
              <v-flex xs12 md8>
                  <p  class="left mx-2 red--text">{{userData.refnumber}}</p>
              </v-flex>
            </v-layout>
            <v-layout>
              <v-flex xs12 md4>
                  <div class="left">Complaint Clasification :</div>
              </v-flex>
              <v-flex xs12 md8>
                  <p  class="left mx-2 ">{{userData.Complaint_category}}</p>
              </v-flex>
            </v-layout>
             <v-layout>
              <v-flex xs12 md4>
                  <div class="left">Complaint category :</div>
              </v-flex>
              <v-flex xs12 md8>
                  <p  class="left mx-2 ">{{userData.complaint}}</p>
              </v-flex>
            </v-layout>
            <v-layout>
              <v-flex xs12 md4>
                  <div class="left" style="font-weight:bold;">Complaint Details :</div>
              </v-flex>
              <v-flex xs12 md8>
                  <p  class="left mx-2 ">{{userData.complaint_detail}}</p>
              </v-flex>
            </v-layout>
            <v-layout>
              <v-flex xs12 md4>
                  <div class="left">Date Submited :</div>
              </v-flex>
              <v-flex xs12 md8>
                  <p  class="left mx-2 ">{{userData.date}}</p>
              </v-flex>
            </v-layout>
            
            <v-layout>
              <!-- <v-flex xs12 md4>
                  <div class="left">Resolution date :</div>
              </v-flex> -->
              <v-flex xs12 md8>
                  <p  class="left mx-2 ">{{userData.time}}</p>
              </v-flex>
            </v-layout>
            
         
          <!-- <v-container> -->
               <v-dialog
      v-model="dialog"
      width="500"
    >
      <template v-slot:activator="{ on }">
        <v-btn
           style=" background-color: #5e0c1d;"
           :disabled='isDisabled(userData.resolving,userData.distro,userData.state)'
         
          v-on="on"
          flat
          
          class="right red--text"
        >
          Update
        </v-btn>
      </template>

      <v-card>
        <v-card-text>
          <v-flex xs12 md8>
                        <v-text-field :rules="nameRules"  label="Complainants" required v-model="complainings"></v-text-field>
                  </v-flex>
          <v-flex xs12 md12>
                        <v-textarea :rules="nameRules" label="Complaint" required v-model="complains"></v-textarea>
                  </v-flex>
          
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <router-link to="/projects">
              <v-btn
             style=" background-color: #5e0c1d;"
            text
            @click="Update(index),dialog = false"
          >
            Update
          </v-btn>
          </router-link>
          
        </v-card-actions>
      </v-card>
    </v-dialog>
              
                </v-container>

         
               </v-card>
            </v-flex>
          </v-layout>
        </v-container>
        <unresolve/>
         <!-- <decline/> -->
        <v-btn
        class="right"
          style=" background-color: #5e0c1d;"
          @click="e1 = 2"
          small
          tile 
          outlined
        >
          Continue
        </v-btn>
        <router-link to="/projects">
             <v-btn
              class="left"
                 style=" background-color: #5e0c1d;"
              
                small
                tile 
                outlined
              >
          Previous
        </v-btn>

        </router-link>
        
      </v-stepper-content>

      <v-stepper-content step="2">
       
        <v-container>
          <v-layout  >
            <v-flex
              xs12
              md12  
            >
            <v-card
          class="mb-12"
          flat
          >
          <v-container>
              <v-layout row wrap>
                <v-spacer></v-spacer>
                  <v-flex xs4 md4>
                         <!-- <v-dialog
                    v-model="dialog"
                    width="500"
                  >
                    <template v-slot:activator="{ on }">
                      <v-btn
                        color="blue-grey darken-1"
                        dark
                        v-on="on"
                        class="right"
                        :disabled='isDisable(userData.resolving,userData.distro)'
                        
                      >
                        Amend Resolution
                      </v-btn>
                    </template>

                    <v-card>
                      <v-card-text>
                        <v-container>
                            <v-layout row wrap>
                                <v-flex xs12 md12>
                                      <v-textarea :rules="nameRules" label="Description" v-model="classify" required ></v-textarea>
                                </v-flex>
                            </v-layout >
                            </v-container>
                      </v-card-text>
                      <v-divider></v-divider>
                      <v-card-actions>
                        <div class="flex-grow-1"></div>
                        <router-link to="/projects">
                          <v-btn
                          color="primary"
                          text
                         @click="dialog = false;submis()"
                         :disabled='isDisable(userData.resolving,userData.distro)'
                          >
                          Amend
                        </v-btn>
                        </router-link>
                        
                      </v-card-actions>
                    </v-card>
                  </v-dialog> -->
                  </v-flex>
                  <!-- <v-flex xs12 md6>
                        <v-text-field :rules="nameRules"  label="NiN Number" required v-model="nin"></v-text-field>
                  </v-flex> -->
                  <v-flex xs12 md12>
                        <v-text-field :rules="nameRules"  label="Persons Involved" required v-model="post"></v-text-field>
                  </v-flex>
                  <v-flex xs12 md12>
                        <v-textarea :rules="nameRules" label="Complaint Resolution" required v-model="resolution"></v-textarea>
                  </v-flex>
                  <v-flex xs12 md12>
                        <v-textarea :rules="nameRules" label="Decision of Commission" required v-model="details"></v-textarea>
                  </v-flex>
                  <!-- <v-flex xs6 md6>
                         <v-col cols="12" sm="6">
                            <v-text-field label="Signatue(Your name)" single-line outlined :rules="nameRules" required v-model="signature"></v-text-field>
                        </v-col>
                  </v-flex> -->
                 
              </v-layout >
               </v-container>
               </v-card>
            </v-flex>
          </v-layout>
        </v-container>
        <v-btn
          class="left"
          style=" background-color: #5e0c1d;"
          @click="e1 = 1"
          small
          tile 
          outlined
        >
          Back
        </v-btn>
        <router-link to="/projects">
             <v-btn
          :disabled='isDisabled(userData.resolving,userData.distro,userData.state)'
          color="green darken-4"
          @click="e1 = 3;submit()"
          
        >
          Submit
        </v-btn>
        </router-link>
        <v-btn class="right"
           style=" background-color: #5e0c1d;"
          @click="e1 = 3"
          small
          tile 
          outlined
        >
          Continue
        </v-btn>

      </v-stepper-content>
        
      <v-stepper-content step="3">
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
                         
                        <h3 class="font-weight-bold">{{userData.complainants}}</h3>
                        <h4 class="red--text" style="font-weight:bold;">{{userData.refnumber}}</h4>
                         </v-card>
                         <!-- <v-card flat id="log">
                            
                         </v-card> -->
                        
                       <v-card  id="print" class="mb-12"  flat >
                         <div style="width:10px;" class="logo-print"></div>
                        <h4 class="font-weight-bold">Complaint</h4>
                        <p>{{userData.complaint_detail}}</p>
                        <h4 class="font-weight-bold" >Commission Decission </h4>
                        <p>{{userData.remaks}} {{userData.dis}}</p>
                         </v-card>
                         
                         <v-card flat id="date">
                           <div  style="bottom: 0;" class="left " >ReportDate:  {{userData.date}}  </div><br>
                        
                        <div  style="bottom: 0;" class="left">ResolvedDate: {{userData.dt}}</div>

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
          style=" background-color: #5e0c1d;"
          @click="e1 = 2"
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
import unresolve from '../components/DashViews/Unresolved.vue'
  import router from '../router'
  import navbar from '../components/DashViews/NavBar'
  export default {
      name:'Stepperview',
    components:{
      data1,
      navbar,
      unresolve
    },
    data () {
      return {
        terms: false,
        e1: 0,
        post:"",
        dialog: false,
        debug:true,
        nin:"None",
        classification:"None",
        resolution:"",
        details:"",
        complainings:'',
        complains:'',
        signature:"None",
        classify:"",
        userData: 0,
        debug: false,
        nameRules: [
        v => !!v || 'Input is required',
        // v => (v && v.length <= 10) || 'Name must be less than 10 characters',
      ],
      email: localStorage.getItem('user'),
      token: localStorage.getItem('token')
      
      }
    },
    created() {
            this.userData = this.$route.params.userData;
            if(this.$route.query.debug){
              this.debug=this.$route.query.debug;
            }
        },
        computed: {
  
},

    methods:{

       Update(index){
       axios.post('http://127.0.0.1:5000/ComplainUpdatezdistrict',{'complaints_refn0':this.userData.refnumber,
       'complains':this.complains,'complainings':this.complainings},
        {headers:{'x-access-token': this.token}})
        .then(
      response => {
      //  this.forceFileDownload(response)
      this.$noty.success("Complaint has been fowarded!")
      })
      
    },
  
       isDisable(resolving,distro,status){
      if(resolving &&!distro)
      return !this.terms
      else if (!resolving &&!distro)
      return !this.terms
      else if (status=="Unresolved")
      return !this.terms
      else return this.terms
    },
       isDisabled(resolving,distro,status){
      if(resolving || distro)
      return !this.terms
      else if (status=="Unresolved")
      return !this.terms
      else return this.terms
    },
      submit(){
        axios.post('http://127.0.0.1:5000/postcomplaints',{
          'status':'Resolved','complaints_refn0':this.userData.refnumber, 'admin_email':this.email,
          'districtagent_idn0':this.nin,'districtagent_post':this.post,
          'district_resolutions':this.resolution,'classify_complaint':this.classification,
          'district_description':this.details
          },
          {
            headers:{
            'x-access-token':this.token
            }
        }).then(
        response =>{
         this.$noty.success("Complaint has been resolved!")
        }
      )
          // console.log(this.userData.refnumber)
          
      },
       submis(){
        axios.post('http://127.0.0.1:5000/AmendComplaints',{
          'status':'Resolved','complaints_refn0':this.userData.refnumber, 'admin_email':this.email,
          
         'classify_complaint':this.classify,
        
          },
          {
            headers:{
            'x-access-token':this.token
            }
        })
          // console.log(this.userData.refnumber)
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