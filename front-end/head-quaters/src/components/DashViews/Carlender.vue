<template>
<div >
 
   <v-container max-height="400px" style="overflow-y: auto">
     <v-card  flat class="white" width="400px"   >
       <!-- <v-card v-for="x in project" :key="x.district"> -->
         <v-layout>
           <v-flex xs12 md4>
           <div class="caption" style="color:#031273;">District</div>
            
         </v-flex>

         <v-flex xs12 md2>
           <div class="caption green--text">Resolved overall</div>
             
         </v-flex>
         <v-flex xs12 md2>
           <div class="caption purple--text">Pending at HQ</div>
            
         </v-flex>
         <v-flex xs12 md2>
           <div class="caption blue--text">Pending at District</div>
          
         </v-flex>
           <v-flex xs12 md2>
           <div class="caption orange--text">Total complaints </div>
          
         </v-flex>

         </v-layout>
         <v-card  v-for="folder in projects.folders" :key="folder.district">

        <v-layout row wrap >
         <v-flex xs12 md4>
         
           <div style="color:#031273;">{{folder.district}}</div>  
         </v-flex>

         <v-flex xs12 md2>
           
           <div>{{folder.data[0]}}</div>  
         </v-flex>
         <v-flex xs12 md2>
           
           <div>{{folder.data[1]}}</div>  
         </v-flex>
         <v-flex xs12 md2>
           
           <div>{{folder.data[2]}}</div>  
         </v-flex>
           <v-flex xs12 md2>
           
           <div>{{folder.sum}}</div>  
         </v-flex>
        
       </v-layout>
         </v-card>
          
       <!-- </v-card> -->
       
        
     </v-card> 
    
     
  </v-container>
</div>
 
</template>

<script>
import axios from 'axios'
export default{
  data(){
    return{
      projects:{
        folders:[

        ]
      },
      token: localStorage.getItem('token')

      
    }
  },
  created(){
    axios.get('http://127.0.0.1:5000/Tabledistrict',{headers:{'x-access-token':this.token}}).then(response =>{
      this.projects.folders = response.data
    }
      
    )
  }

  

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
  background: green 
}
.v-chip.Resolved{
  background:  #004080
}
.v-chip.Declined{
  background:  tomato
}
.v-chip.Unresolved{
  background:  purple
}
</style>
