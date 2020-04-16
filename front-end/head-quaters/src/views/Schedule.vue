<template>
    <div>
        <navbar/>
        <v-container fluid>
       <v-layout row wrap justify-space-around>
     <!-- <v-flex xs10 md5>
       <v-card class="pa-3" outline  max-width="800" height="400px">
      
          <v-date-picker  class="pa-3" outline  width="200" height="300px" flat dark green color="purple"   v-model="picker"></v-date-picker>
         
       </v-card>
     </v-flex> -->
     <v-flex xs10 md12>
       <v-card max-height="600px" class="pa-2" style="overflow-y: auto"  outline max-width="1300" > 
         <div width="1000px"></div>
          <admin/>
       </v-card>
     </v-flex>
   </v-layout><br>
   <!-- <v-layout row wrap justify-space-around >
     
     <v-flex xs10 md12 >
       <v-card max-height="400px" style="overflow-y: auto" class="pa-3" outline max-width="1300"  height="400px">
         <decline/>
       </v-card>
     </v-flex>
   </v-layout> -->
   </v-container>
    </div>
</template>
<script>
import axios from 'axios'
import navbar from '../components/DashViews/NavBar'
import oclock from '../components/DashViews/Oclock'
import decline from '../components/DashViews/Stores.vue'
import admin from '../components/DashViews/Admins.vue'
import clock from '../components/DashViews/Clock'


export default {
    components:{
        navbar,
        oclock,
        decline,
        admin,
        clock
    },
     data () {
      return {
        picker: new Date().toISOString().substr(0, 10),
      }
    },
}

</script>