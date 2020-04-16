<template>
<div class="dashboard">
  
    <v-container fluid>
      <navbar/><br>
   <v-layout row wrap justify-space-around>
     <v-flex xs10 md6>
       <v-hover v-slot:default="{ hover }">
       <v-card :elevation="hover ? 12 : 2" class="pa-3" outline  max-width="820" height="500px">
         <pie/>
       </v-card>
       </v-hover>
     </v-flex>
     <v-flex xs10 md6>
       <v-hover v-slot:default="{ hover }">
       <v-card :elevation="hover ? 12 : 2" max-height="500px" style="overflow-y: auto" class="pa-3" outline max-width="820"  height="500px"> 
         <!-- <div width="1000px"><bar/></div> -->
          <div  style=" font-family: Avenir;color:#031273;font-size: 30px;">Summary of complaints </div>
         <carlender/>
       </v-card>
       </v-hover>
     </v-flex>
   </v-layout>
   </v-container>
   
   <!-- <br>
   <v-layout row wrap justify-space-around>
     <v-flex xs10 md5>
       <v-card class="pa-3" outline max-width="800"  height="400px">
         <donut/>
       </v-card>
     </v-flex>
     <v-flex xs10 md5 >
       <v-card max-height="400px" style="overflow-y: auto" class="pa-3" outline max-width="800"  height="400px">
         <carlender/>
       </v-card>
     </v-flex>
   </v-layout> -->
   

 
</div>
 
</template>

<script>
import axios from 'axios'
import pie from '../components/DashViews/PieChart.vue'
import donut from '../components/DashViews/Donut.vue';
import bar from '../components/DashViews/BarChart.vue'
import carlender from '../components/DashViews/Carlender.vue'
import navbar from '../components/DashViews/NavBar'

export default{
    components:{
      pie,
      donut,
      bar,
      carlender,
      navbar
    },
  data(){
    return{
     
      
    }
  },

}

</script>