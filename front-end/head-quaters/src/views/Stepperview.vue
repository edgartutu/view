<template>
<div>
  <navbar/>
  <v-stepper v-model="e1">
    <v-stepper-header class="white" >
      <v-stepper-step class="white--text"  :complete="e1 > 1" step="1">Complaint Details - {{userData.complainants}}</v-stepper-step>
      <v-divider></v-divider>
      
      <v-divider></v-divider>
      <v-stepper-step step="2">Resolve</v-stepper-step>
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
                <p class="left mx-2">{{userData.agentname}}</p>
              </v-flex>
            </v-layout>
            <v-layout>
              <v-flex xs12 md4>
                <div class="left" style="font-weight:bold;">Complainants :</div>
              </v-flex >
              <v-flex xs12 md8>
                <p class="left mx-2">{{userData.complainants}}</p>
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
                  <p  class="left mx-2 ">{{userData.complaint}}</p>
              </v-flex>
            </v-layout>
             <v-layout>
              <v-flex xs12 md4>
                  <div class="left">Complaint category :</div>
              </v-flex>
              <v-flex xs12 md8>
                  <p  class="left mx-2 ">{{userData.Complaint_category}}</p>
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
            <div v-if="userData.description">

                           <v-layout>
              <v-flex xs12 md4>
                  <div class="left">District submission :</div>
              </v-flex>
              <v-flex xs12 md8>
                   <v-dialog
                
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
                    <div class="left blue--text">District submission :</div>
                    {{userData.description}}
                      
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

            </div>
            <div v-else></div>

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
                      
                      style=" background-color: #004080;"
                      dark
                      v-on="on"
                      flat
                      class="white--text right"
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
                      <!-- <router-link to="/projects"> -->
                      <div v-if="complains">
                         <v-btn
                        style=" background-color: #004080;"
                        text
                        @click="Update(index),dialog = false"
                      >
                        Update
                      </v-btn>

                      </div>
                         
                      <!-- </router-link> -->
                      
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              
                </v-container>
               <!-- </v-container> -->
               </v-card>
            </v-flex>
          </v-layout>
          <div id="appz" style=" background-color: #004080;"  >
            <v-layout>
              <v-flex xs6 md6>
              <router-link to="/projects">
                <v-btn class="left " flat style=" background-color: #004080;"  small tile outlined>
                  Back
                </v-btn>
              </router-link>

            </v-flex>
            <v-flex xs6 md6>
              <v-btn
          class="right"
          style=" background-color: #004080;" 
          @click="e1 = 2"
          small
          tile 
          flat
          outlined
        >
          Resolve
        </v-btn>

            </v-flex>

            </v-layout>
            
            
          
         </div>
        </v-container>
         <!-- <decline/> -->
         
       
       
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
          
          >
          <v-container>
              <v-layout row wrap>
                  <!-- <v-flex xs12 md6>
                        <v-text-field :rules="nameRules"  label="Resolver Post" required v-model="post"></v-text-field>
                  </v-flex> -->
                  <!-- <v-flex xs6 md6>
                    <v-col cols="12" sm="6">
                        <v-text-field :rules="nameRules"  label="Persons Involved" required v-model="post"></v-text-field>
                         </v-col>
                  </v-flex> -->
                  <!-- <v-flex xs12 md12>
                        <v-text-field :rules="nameRules"  label="Complaint Clasification" required v-model="classification"></v-text-field>
                  </v-flex> -->
                  <v-flex xs12 md12>
                        <v-textarea :rules="nameRules" label="Complaint Resolution" required v-model="resolution"></v-textarea>
                  </v-flex>
                  <v-flex xs12 md12>
                        <v-textarea :rules="nameRules" label="Decision of Commission" required v-model="details"></v-textarea>
                  </v-flex>
                  <!-- <v-flex xs6 md6>
                         <v-col cols="12" sm="6">
                            <v-text-field label="Signatue" single-line outlined :rules="nameRules" required v-model="signature"></v-text-field>
                        </v-col>
                  </v-flex> -->
                 
              </v-layout >
               </v-container>
               <div v-if="resolution || details">
                        <v-btn
         :disabled="clickable"
          style=" background-color: #004080;"
          @click=" submit()"
        >
          Submit
        </v-btn>

               </div>
          
        <!-- </router-link> -->
       
        
        <!-- <v-btn class="right"
          color="primary"
          @click="e1 = 3; "
          small
          tile 
          outlined
        >
          Continue
        </v-btn> -->
        <div id="appz" style=" background-color: #004080;"  >
            <v-layout>
              <v-flex xs6 md6>
              
                   <v-btn
          class="left"
          style=" background-color: #004080;"
          @click="e1 = 1"
          small
          tile 
          flat
          outlined
        >
          Back
        </v-btn>
            </v-flex>
           

            </v-layout>
            
            
          
         </div>
               </v-card>
            </v-flex>
          </v-layout>
        </v-container>
       
        <!-- <router-link to="/resolved"> -->
        

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
        userData: 0,
        debug: false,
      
        post:"None",
        nin:"None",
        complainings:'',
        complains:'',
        classification:"None",
        resolution:"",
        details:"",
        signature:localStorage.getItem('name'),
        nameRules: [
        v => !!v || 'Input is required',
        // v => (v && v.length <= 10) || 'Name must be less than 10 characters',
      ],
      user: localStorage.getItem('user'),
      token: localStorage.getItem('token')
      
      }
    },
    created() {
            this.userData = this.$route.params.userData;
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
          },{headers:{'x-access-token':this.token}}).then(response=>{
                    this.$router.push('/projects')

                    this.$noty.success("Decision has been registered!")

                    // this.snackbar=true
                   
                // window.location.reload()
                
            })
      },
      print(){
        // Get HTML to print from element
const prtHtml = document.getElementById('print').innerHTML;

// Get all stylesheets HTML
let stylesHtml = '';
for (const node of [...document.querySelectorAll('link[rel="stylesheet"], style')]) {
  stylesHtml += node.outerHTML;
}

// Open the print window
const WinPrint = window.open('', '', 'left=0,top=0,width=800,height=900,toolbar=0,scrollbars=0,status=0');

WinPrint.document.write(`<!DOCTYPE html>
<html>
  <head>
    ${stylesHtml}
  </head>
  <body>
  <img
  src="@/assets/img/com.jpg"
  alt="John"
id="print"  
>
${prtHtml}
  </body>
</html>`);

WinPrint.document.close();
WinPrint.focus();
// WinPrint.print();
// WinPrint.close();
      },

        forceFileDownload(response){
            const url = window.URL.createObjectURL(new Blob([response.data]))
             const link = document.createElement('a')
             link.href = url
             link.setAttribute('download', 'file.pdf') //or any other extension
             document.body.appendChild(link)
            link.click()
    },

    downlod(index){
       axios.post('http://127.0.0.1:5000/files',{'complaints_refn0':this.projects[index].complaints_refn0},
        {headers:{'x-access-token': this.token}}).then(
      response => {
       this.forceFileDownload(response)
      //  console.log(response)
      })
      
    },
    Update(index){
       axios.post('http://127.0.0.1:5000/ComplainUpdates',{'complaints_refn0':this.userData.refnumber,
       'complains':this.complains,'complainings':this.complainings},
        {headers:{'x-access-token': this.token}})
        .then(
      response => {
      //  this.forceFileDownload(response)
      
      this.$router.push('/projects')
      
      this.$noty.success("Complaint Updated!")
      // window.location.reload()
      //  console.log(this.userData.refnumber)
      })
      
    }
    }
  }
</script>
<style>
#appz{
  display: flex;
  flex-direction: column;
  height: 100%;
}
</style>