<template>
<div class="dashboard">
    <navbar/>
    <v-layout wrap >
   
         <v-flex xs12 md12>
           <v-container>
                         <v-card  class="white "  >
              <v-container fluid >
                <v-form v-model="valid" ref="form">
              <!-- <v-flex xs12 md6>
                  <v-text-field v-model="district"   label="District code" required ></v-text-field>
              </v-flex> -->
              <v-flex xs12 md6>
                <v-text-field :rules="nameRules"
                  
                     v-model="compalianant"  label="Complainant Name" required ></v-text-field>
              </v-flex>
               <v-flex xs12 md6>
                <v-text-field  :rules="nameRules"
                    :counter="10" v-model="phone"  label="Complainant Phone(+256)" required ></v-text-field>
              </v-flex>
                <v-flex xs12 md6>
                  <v-text-field :rules="nameRules"
                    :counter="30" v-model="town"  label="Address(Town,Village,Parish)" required ></v-text-field>
              </v-flex>
              <v-flex xs12 md12>
                  <v-select
                      v-model="select"
                      :items="itemz"
                      label="Position"
                      :rules="nameRules"
                    :counter="30"
                      required
                    ></v-select>
              </v-flex>
               <v-flex xs12 md12>
                  <v-select
                  v-model="category"
                  :items="itemc"
                  label="Category of Complaint"
                   :rules="nameRules"
                    
                    required
                    ></v-select>
              </v-flex>
                <v-flex xs12 md12>
                  <v-select
                  v-model="select2"
                  :items="items"
                  label="Classification"
                  :rules="nameRules"
                    :counter="30"
                   required
                    ></v-select>
              </v-flex>
              
                <v-flex xs12 md12>
                  
                  <v-textarea
                    v-model="complaints"
                    counter
                    label="Complaint"
                 
                    :rules="nameRules"
                    
                  ></v-textarea>
              </v-flex>
                 <v-flex xs12 sm4 text-xs-center>
                <input type="file" name="Upload File"  @change="uploadfile" />
              
                <!-- <v-btn flat class="teal" @click="sub()">Submit</v-btn> -->
                </v-flex>
              
                  <!-- <router-link to="/projects"> -->
                      <v-btn flat class="green" @click="submit()" >Submit</v-btn>
                  <!-- </router-link> -->
              </v-form>
            </v-container>
            
             
             <v-snackbar
              v-model="snackbar"
              :color="color"
              :top='true'
            >
              {{ errorMessages }}
              <v-btn
                dark
                flat
                @click="snackbar = false"
              >
                Close
              </v-btn>
            </v-snackbar>
            </v-card>

           </v-container>

         </v-flex>
       </v-layout>
  
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
      phone:'',
        compalianant:'',
         snackbar:false,
        town:'',
        valid: false,
         file: null,
          errorMessages: 'Fill all required fields ',
        category:'',
        select:'',
        select2:'',
        complaints:'',
        // district:'',
        rules: [v => v.length <= 500 || 'Max 500 characters'],
         nameRules: [
          (v) => !!v || 'Field is required',
          (v) => v && v.length <= 500 || 'Max 500 characters'
        ],
      items: [
        'Registration/Update',
        'Display/Register',
        'Nomination',
        'Campaigns',
        'Polling Day',
        'General Complaint'
      ],
        itemc:[
        'Presidential',
        'parliamentary',
        'Local Government 5',
        'Local Government 3',
        'Local Government Municpality',
        'Administrative Units'
      ],
      itemz:[
        'RO',
        'Others'
      ],
       
       radios: 'radio-1',
      projects:[],
      dialog: false,
    
      token: localStorage.getItem('token')
      
     
    }
   
  },
   computed: {
    pages () {
      return this.pagination.rowsPerPage ? Math.ceil(this.items.length / this.pagination.rowsPerPage) : 0
    }
  },
  

  methods: {
   
    getColor (status) {
        if (status =="Resolved" ) return 'orange'
        else if (status=="Declined") return 'red'
        else if (status=="Unresolved") return 'purple'
        else return 'green darken-2'
      },
      submit(){
          if( this.$refs.form.validate()){
          const fd = new FormData();
                fd.append('foo', 'bar')
                fd.append('filename', this.file['name'])
                fd.append('file', this.file)
                fd.append('email', localStorage.getItem('user'))
                 fd.append('agent_staff', this.select)
                  fd.append('phone',this.phone)
                   fd.append('district', localStorage.getItem('district'))
                     fd.append('poling_station',this.town)
                       fd.append('nature_complaint', this.select2)
                        fd.append('complaint', this.complaints)
                         fd.append('Complaint_category', this.category)
                          fd.append('compalianant_name', this.compalianant)
                  axios.post('http://127.0.0.1:5000/postadmin1Complaint',fd,
                  {headers:{'x-access-token':this.token}}).then(response=>{
               this.$router.push('/projects')

                    this.$noty.success("Complaint has been captured!")
                // window.location.reload()
                // this.snackbar=true
            })
        }
        else {
          this.snackbar=true
        }
      },
       uploadfile() {
                this.file = event.target.files[0]
            }

        
      },
   
   
    

  }
 



</script>
<style lang="scoped">
/* .custom-selector{
  font-size: 3em;
  
} */
</style>
