<template>
<div >
 
   <v-container max-height="400px" style="overflow-y: auto">
   
       <v-layout row wrap >
         <v-flex xs12 md6>
           <div class="caption " style="color: #5e0c1d;">Complaint Category</div>
           
         </v-flex>
         <v-flex xs12 md6>
           <div class="caption right" style=" color: #5e0c1d;">Complaint Status</div>
         </v-flex>
       
       </v-layout>
         <v-card  flat class="white"  v-for="project in projects" :key="project.content">
       <v-layout row wrap :class="`pa-3 project ${project.status}`">
         <v-flex xs12 md6>
         
           <div>{{project.nature_complaint}}</div>  
         </v-flex>
         <v-flex xs12  md6>
          <div class="right">
            <v-chip  small :class="`${project.status} white--text caption my-3`">
              {{project.status}}
            </v-chip>
          </div>
         </v-flex>
       </v-layout>
        
     </v-card>
     
  </v-container>
</div>
 
</template>

<script>
import axios from 'axios'
export default{

  data(){
    return{
      projects:[],
      district: localStorage.getItem('district'),
      token: localStorage.getItem('token')

      
    }
  },
  created(){
    axios.post('http://127.0.0.1:5000/getcomplaints',{'district_n0':this.district},
    {
       headers:{
       'x-access-token':this.token
     }
    }
    
    ).then(response =>{
      this.projects = response.data;
      console.log(this.token)
    }
      
    )
  }
  

}

</script>

<style lang="stylus" scoped>
.project.Pending{
  border-left: 4px solid #004080;
}
.project.Resolved{
  border-left: 4px solid green;
}
.project.Unresolved{
  border-left: 4px solid #5e0c1d;
}
.project.Declined{
  border-left: 4px solid tomato;
}
.v-chip.Pending{
  background: #004080;
}
.v-chip.Resolved{
  background: green;
}
.v-chip.Declined{
  background:  tomato;
}
.v-chip.Unresolved{
    background: #5e0c1d;
}

</style>
