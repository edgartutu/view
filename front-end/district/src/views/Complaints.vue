<template>
<div class="dashboard">
    <navbar/>
    <!-- <v-form>
      <v-container fluid>
        <v-row>
          <v-layout row wrap >
            <v-flex xs10 md3>
              <v-col cols="12" sm="4">
                <v-text-field
                  :rules="rules"
                  counter="25"
                  label="Level 1 Code"
                  outlined
                ></v-text-field>
            </v-col>
            </v-flex>
              <v-btn class="mx-2" fab dark large color="cyan">
                  Search
               </v-btn>
               <v-spacer></v-spacer>
                <v-flex xs10 md3>
              <v-col cols="12" sm="4">
                <v-text-field
                  :rules="rules"
                  counter="25"
                  label="User Code"
                  outlined
                ></v-text-field>
            </v-col>
            </v-flex>
              <v-btn class="mx-2" fab dark large color="cyan">
                  Search
               </v-btn>
          </v-layout>    
        </v-row>
      </v-container>
    </v-form> -->
   <v-container fluid>
     <v-layout row class="mb-2">
       <v-tooltip top>
         <v-btn small flat style="background-color:#ffbb00;" @click="sortBy('nature_complaint')" slot="activator">
         <v-icon left small >folder</v-icon>
         <span class="caption text-lowercase">By Complaint</span>
        </v-btn>
        <span class="white--text">sort product by Complaint</span>
       </v-tooltip>
       <v-tooltip top>
          <v-btn small flat style="background-color:#ffbb00;" @click="sortBy('status')" slot="activator">
         <v-icon left small >person</v-icon>
          <span class="caption text-lowercase">By status</span>
        </v-btn>
        <span class="white--text">sort by status</span>
       </v-tooltip>

     </v-layout>
     <v-card  class="white"   v-for="(project,index) in projects" :key="project.complaints_refn0">
       <v-layout row wrap :class="`pa-3 project ${project.status}`">
         <v-flex xs12 md4>
           <div class="caption grey--text">Complaint Category</div>
           <div>{{project.nature_complaint}}</div> 
            
         </v-flex>
         <v-flex xs6 sm4 md2>
           <div class="caption grey--text">Ref Number</div>
           <div>{{project.complaints_refn0}}</div>
         </v-flex>
         <v-flex xs6 sm4 md2>
           <div class="caption grey--text">File</div>
           <div> <v-btn
          :loading="loading5"
            :disabled="loading5"
            color="blue-grey"
            class="ma-2 white--text"
            fab
            small
            @click="loader = 'loading5',downlod(index)"
          > <v-icon dark>mdi-cloud-download</v-icon>
          </v-btn> </div>
         </v-flex>
         <v-flex xs6 sm4 md2>
           <div class="caption grey--text">Date</div>
           <div>{{project.date}}</div>
         </v-flex>
         
         <v-flex xs2 sm4 md1>
          <div class="right">
            <v-chip  small :class="`${project.status}  white--text caption my-2`">
              {{project.status}}
            </v-chip>
          </div>
         </v-flex>
         <v-flex xs2 sm4 md1>
           <router-link :event="isDis(project.status)"   :to="{ name: 'Stepperview',
            params: { userData:{partieshead:project.head_post,state:project.status,parties:project.districtagent_post,nameofcomplainant:project.compalianant_name,remaks:project.headresolution,classify:project.classify_complaint,resolving:project.headdescription,dt:project.date_submit,complaint:project.nature_complaint,refnumber:project.complaints_refn0,agentname:project.agent_name,
            date:project.date,phoneno:project.agent_phone,location:project.district,description:project.comments,time:project.date_submit,complainants:project.compalianant_name,Complaint_category:project.Complaint_category,
            complaint_detail:project.complaint,levels:project.classify_complaint,post:project.agent_staff,picto:project.picture,distro:project.district_resolutions,dis:project.district_description} },query:{debug:true} }" >
				    <v-btn
                :color="getColor(project.status)"
                dark
                small
                class="mx-2"
                :disabled='isDisabled(project.status)'
              >
              <div v-if="project.status=='Resolved'" class="mx-2" >View</div>
              <div v-else-if="project.status=='Pending'" class="mx-2" >Resolve</div>
              
                <!-- <div class="mx-2" >{{word}}</div> -->
              
              </v-btn>
				</router-link>
         </v-flex>
       </v-layout>
       <v-divider></v-divider>
     </v-card>
     <!-- <div class="text-center">
    <v-pagination v-model="pagination.page" :length="pages"></v-pagination>
  </div> -->
  </v-container>
</div>
</template>

<script>
import navbar from '../components/DashViews/NavBar'
import axios from 'axios'
export default{
    components:{
      navbar
    },
  data(){
    return{
      
     e1: 0,
     terms: false,
     clickable:'clickable',
    // pagination: {
      
    // },

      projects:[],
      btnDisabled: false,
      dialog: false,
      token: localStorage.getItem('token'),
      district_no: localStorage.getItem('district'),
     
    }
   
  },
   computed: {
    pages () {
      return this.pagination.rowsPerPage ? Math.ceil(this.items.length / this.pagination.rowsPerPage) : 0
    },
    
    //  isresolved(status){
    //   if(status=="Resolved")
    //   return this.word="View"
    //   else if (status=="Pending")
    //   return this.word="Resolve"
    // }
   
  },
  created(){
    axios.post('http://127.0.0.1:5000/getcomplaints',{'district_n0': this.district_no},
            {
              headers:{
              'x-access-token':this.token
            }
            }
    ).then(
      response => {this.projects = response.data})
  },
  // computed:{
  //   update: function(event) {

  //     value = event.target.value;

  //     this.word = value;
  //     // console.log(value)
  //   }


  // },

  methods: {
    sortBy(prop){
      this.projects.sort((a,b) => a[prop] < b[prop] ? -1:1)

    },
    getColor (status) {
        if (status =="Resolved" ) return 'green darken-2'
        else if (status=="Declined") return 'red'
        else if (status=="Unresolved") return '#5e0c1d'
        else return '#004080'
        
      },
       isDisabled(status){
      if(status=="Unresolved")
      return !this.terms
      else return this.terms
    },

     isDis(status){
      if(status=="Unresolved")
      return this.terms
      else return this.clickable ? 'click' : ''
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
       axios.post('https://aaomach.pythonanywhere.com/files2',{'complaints_refn0':this.projects[index].complaints_refn0},
        {headers:{'x-access-token': this.token}})
        //.then(
      //response => {

        //this.forceFileDownload(response)
       //console.log(response)
      //}
      //)
      
    }
     
        
      },
   
   
    

  }
 



</script>
<style lang="stylus" scoped>
.project.Pending{
  border-left: 4px solid green
}
.project.Resolved{
  border-left: 4px solid orange
}
.project.Declined{
  border-left: 4px solid tomato
}
.project.Unresolved{
  border-left: 4px solid purple
}
.v-chip.Pending{
  background: #004080
}
.v-chip.Resolved{
  background:  green
}
.v-chip.Declined{
  background:  tomato
}
.v-chip.Unresolved{
  background:  #5e0c1d
}
</style>
