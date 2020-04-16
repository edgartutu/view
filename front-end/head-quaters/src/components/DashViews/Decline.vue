<template>
  <div >
    <v-dialog
      v-model="dialog"
      width="500"
    >
      <template v-slot:activator="{ on }">
        <v-btn
          color="red"
          dark
          v-on="on"
          
        >
          Decline
        </v-btn>
      </template>

      <v-card>
        <v-card-text>
           <v-container>
              <v-layout row wrap>
                  <v-flex xs12 md12>
                        <v-textarea :rules="nameRules" label="Decline Resolution" v-model="comments" required></v-textarea>
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
            @click="dialog = false; declined()"
            >
            Submit
          </v-btn>
          </router-link>
          
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
<script>
import axios from 'axios'
  //import router from './router'
  export default {
    data () {
      return {
        dialog: false,
        userData: 0,
        comments:"",
        admin_email:"",
        user: localStorage.getItem('user'),
        token: localStorage.getItem('token'),
        nameRules: [
        v => !!v || 'Input is required',
        // v => (v && v.length <= 10) || 'Name must be less than 10 characters',
      ],

      }
    },
    created() {
          this.userData = this.$route.params.userData;
        },
    methods:{
      declined(){
        //console.log(this.userData.refnumber)
        axios.post('http://127.0.0.1:5000/adminpostcomplaints',{
          'status':'Declined','comment':this.comments,'complaints_refn0':this.userData.refnumber, 'admin_email':this.user
          },
          {headers:{'x-access-token':this.token}}
          ) .then(response=>{
                window.location.reload()
            })
      }
    }
  }
</script>