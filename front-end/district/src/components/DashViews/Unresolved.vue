<template>
  <div >
    <v-dialog
      v-model="dialog"
      width="500"
    >
      <template v-slot:activator="{ on }">
        <v-btn
          color="blue-grey darken-1"
          dark
          v-on="on"
          class="center"
           :disabled='isDisabled(userData.resolving,userData.distro)'
        >
          Foward To HeadQuaters
        </v-btn>
      </template>

      <v-card>
        <v-card-text>
           <v-container>
              <v-layout row wrap>
                  <v-flex xs12 md12>
                        <v-textarea :rules="nameRules" label="Description" v-model="comment" required ></v-textarea>
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
            :disabled='isDisabled(userData.resolving,userData.distro)'
            >
            Foward
          </v-btn>
          </router-link>
          
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
<script>
import axios from 'axios'
  export default {
    data () {
      return {
        dialog: false,
        userData: 0,
        terms:false,
        comment:'',
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
        },
    methods:{
        isDisabled(resolving,distro){
      if(resolving || distro)
      return !this.terms
      else return this.terms
    },
      declined(){
        //console.log(this.userData.refnumber)
        axios.post('http://127.0.0.1:5000/postcomplaints',{
          'status':'Unresolved','comment':this.comment,'complaints_refn0':this.userData.refnumber, 'admin_email':this.email
          },
          {
            headers:{
            'x-access-token':this.token
          }
          }
          ) .then(response=>{
               this.$router.push('/projects')
                this.$noty.success("Complaint has been fowarded!")
                //  window.location.reload()
            })
      }
  }
  }
</script>