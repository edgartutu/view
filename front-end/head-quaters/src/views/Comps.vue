<template>
<div class="dashboard">
    <navbar/>
    <v-layout wrap >
         <v-flex xs12 md12>
           <v-container>
                         <v-card  class="white"  >
              <v-container fluid >
                <v-form v-model="valid" ref="form">
              <v-flex xs12 md6>
                 <v-col cols="12">
                  <v-autocomplete
                    v-model="district"
                    :items="itemn"
                    outlined
                    dense
                    label="District Name"
                    single-line
                    :rules="nameRules"
                    :counter="10"
                    required
                    
                  ></v-autocomplete>
                </v-col>
              </v-flex>
                <v-flex xs12 md6>
                  <v-text-field v-model="town"  label="Address(Town,Parish,Village)" :rules="nameRules"
                    :counter="10"
                    required ></v-text-field>
              </v-flex>
              <v-flex xs12 md6>
                <v-text-field v-model="compalianant"  label="Complainants" :rules="nameRules" required ></v-text-field>
              </v-flex>
              <v-flex xs12 md6>
                <v-text-field  v-model="phonen0"  label="Complainant Phone(+256)" required ></v-text-field>
              </v-flex>
              <v-flex xs12 md12>
                  <v-select
                      v-model="select"
                      :items="itemz"
                      label="Position"
                      
                      :rules="nameRules"
                    :counter="10"
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
                  label="Classification of Complaint"
                   :rules="nameRules"
                    :counter="10"
                    required
                    ></v-select>
              </v-flex>
                <v-flex xs12 md12>
                  
                  <v-textarea
                    v-model="inputs"
                    counter
                    label="Complaints"
                    :rules="nameRules"
                    
                    required
                    
                  ></v-textarea>
              </v-flex>
              <v-flex xs12 sm4 text-xs-center>
                <input type="file" name="Upload File"  @change="uploadfile" required :rules="nameRules" />
				
					<!-- <v-btn flat class="teal" @click="sub()">Submit</v-btn> -->
					</v-flex>
              <!-- <router-link to="/projects"> -->
                <v-btn flat class="teal" @click="submit()" >Submit</v-btn>
            <!-- </router-link> -->
              </v-form>
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
            </v-container>
            
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
      snackbar:false,
      color: 'general',
      valid: false,
        district:'',
        town:'',
        phonen0:'',
        compalianant:"",
         errorMessages: 'Fill all required fields ',
        category:'',
        select:'',
        select2:'',
        file: null,
        inputs:'',
                nameRules: [
          (v) => !!v || 'Field is required',
          (v) => v && v.length <= 500 || 'Max 500 characters'
        ],
        rules: [v => v.length <= 500 || 'Max 500 characters'],
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
        'Staff',
        'Others'
      ], itemn:[
        'Buikwe',
'Bukomansimbi',
'Butambala',
'Buvuma',
'Gomba',
'Kalangala',
'Kalungu',
'Kampala',
'Kayunga',
'Kiboga',
'Kyankwanzi',
'Luweero',
'Lwengo',
'Lyantonde',
'Masaka',
'Mityana',
'Mpigi',
'Mubende',
'Mukono',
'Nakaseke',
'Nakasongola',
'Rakai',
'Sembabule',
'Wakiso',
'Amuria',
'Budaka',
'Bududa',
'Bugiri',
'Bukedea',
'Bukwa',
'Bulambuli',
'Busia',
'Butaleja',
'Buyende',
'Iganga',
'Jinja',
'Kaberamaido',
'Kaliro',
'Kamuli',
'Kapchorwa',
'Katakwi',
'Kibuku',
'Kumi',
'Kween',
'Luuka',
'Manafwa',
'Mayuge',
'Mbale',
'Namayingo',
'Namutumba',
'Ngora',
'Pallisa',
'Serere',
'Sironko',
'Soroti',
'Tororo',
'Abim',
'Adjumani',
'Agago',
'Alebtong',
'Amolatar',
'Amudat',
'Amuru',
'Apac',
'Arua',
'Dokolo',
'Gulu',
'Kaabong',
'Kitgum',
'Koboko',
'Kole',
'Kotido',
'Lamwo',
'Lira',
'Maracha',
'Moroto',
'Moyo',
'Nakapiripirit',
'Napak',
'Nebbi',
'Nwoya',
'Otuke',
'Oyam',
'Pader',
'Yumbe',
'Zombo',
'Buhweju',
'Buliisa',
'Bundibugyo',
'Bushenyi',
'Hoima',
'Ibanda',
'Isingiro',
'Kabale',
'Kabarole',
'Kamwenge',
'Kanungu',
'Kasese',
'Kibaale',
'Kiruhura',
'Kiryandongo',
'Kisoro',
'Kyegegwa',
'Kyenjojo',
'Masindi',
'Mbarara',
'Mitooma',
'Ntoroko',
'Ntungamo',
'Rubirizi',
'Rukungiri',
'Sheema',

      ],
       radios: 'radio-1',
      projects:[],
      dialog: false,
      user: localStorage.getItem('user'),
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
                fd.append('filename',this.file["name"])
                fd.append('file', this.file)
                fd.append('email', this.user)
                 fd.append('agent_staff', this.select)
                  fd.append('complain_n0',this.phonen0)
                   fd.append('district', this.district)
                     fd.append('poling_station',this.town)
                       fd.append('nature_complaint', this.select2)
                        fd.append('complaint', this.inputs)
                         fd.append('Complaint_category', this.category)
                          fd.append('compalianant_name', this.compalianant)
                  axios.post('http://127.0.0.1:5000/Postzadmin2Complaint',fd,
                  {headers:{'x-access-token':this.token}}).then(response=>{
                    this.$router.push('/projects')

                    this.$noty.success("Complaint has been captured!")

                    // this.snackbar=true
                   
                // window.location.reload()
                
            })
            .catch(response => {

              if(response.status===401){
                this.$noty.error("Oops, Your session has expired!")

              }


        
        }
        )
            

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
