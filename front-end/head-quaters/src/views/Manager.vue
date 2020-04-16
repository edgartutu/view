<template>
    <div>
        <nav>
       <v-toolbar style=" background-color: #004080;"  fixed>
            <v-avatar size="60">
                <img
                    src="@/assets/img/elec.jpg"
                    alt="John"
                >
                </v-avatar>
           <v-toolbar-title style="color:#faee02;" >eCMS</v-toolbar-title>
           <p></p>
           <p></p>
            <v-toolbar-items class="hidden-sm-and-down" >
                <v-layout  row >
                <!-- <v-btn  flat small  class=" mx-2 white--text" v-for="link in links" :key="link.text" router :to="link.route">
                </v-btn> -->
                
                </v-layout>
            </v-toolbar-items>
            <v-spacer></v-spacer>
                <p></p>
                 <v-menu class="hidden-md-and-up">
                    <v-toolbar-side-icon slot="activator" class="purple--text"   ></v-toolbar-side-icon>
                    <!-- <v-list>
                    <v-list-tile v-for="link in links" :key="link.text" router :to="link.route">
                        <v-list-tile-content>
                        <v-list-tile-title class="purple--text">{{ link.text}}</v-list-tile-title>
                        </v-list-tile-content>
                    </v-list-tile>   
                    </v-list> -->
                    
                </v-menu>
                <!-- <router-link v-ripple  to="/dashboard">
					<v-icon class="mx-2" color="white">mdi-home</v-icon><br>
				</router-link> -->
                <v-menu bottom left content-class offset-y transition="slide-y-transition">
					<router-link v-ripple slot="activator"  to="/projects">
						<!-- <v-badge  overlap color="#f73b3b" >
					        <template slot="badge"  >
                               {{projects.length}}
                                </template>
					            <v-icon class="mx-2" color="white">mdi-bell</v-icon>
				        </v-badge> -->
					</router-link>
					<v-card>
						<!-- <v-list dense>
							<v-list-tile v-for="notification in notifications" :key="notification" @click="onClick">
								<v-list-tile-title v-text="notification"/>
							</v-list-tile>
						</v-list> -->
                        
					</v-card>
				</v-menu>
                     <v-btn flat class="white--text" >
                    <span  style="color:#faee02;" >ADMINSTRATOR</span>
                    
                    <v-icon>exit_to_app</v-icon>
                    
                    </v-btn> 
        </v-toolbar>
    </nav>
        <!-- <v-layout row wrap justify-space-around> -->
     <!-- <v-flex xs10 md5>
       <v-card class="pa-3" outline  max-width="800" height="400px">
      
          <v-date-picker  class="pa-3" outline  width="200" height="300px" flat dark green color="purple"   v-model="picker"></v-date-picker>
         
       </v-card>
     </v-flex> -->
     <!-- <v-flex xs10 md5>
       <v-card class="pa-2"  outline max-width="800"  height="400px"> 
         <div width="1000px"></div>
          <admin/>
       </v-card>
     </v-flex>
   </v-layout><br> -->
   <v-checkbox v-model="terms"  ></v-checkbox>
   <v-layout row wrap justify-space-around >
     
     <v-flex xs10 md10 >
       <v-card max-height="400px" style="overflow-y: auto" class="pa-3" outline max-width="1300"  height="400px">
           <v-layout row wrap column>  
    <v-flex xs12 md12 >
        <!-- <export-excel :data="items">
            <h6 >Export to Excel</h6>
            <img src="@/assets/img/512.png" style="width:40px;height:40px">
        </export-excel>   -->
         <v-text-field
            v-model="search"
            append-icon="search"
            label="Search"
            single-line
            hide-details
          ></v-text-field>
        <v-data-table class="fb-table-elem"
            :headers="headers"
            :items="items"
             :search="search"
            hide-actions
            item-key="name"
            expand >
            <template slot="items" slot-scope="{item,index}" >          
              <!-- <tr @click="props.expanded = !props.expanded">   -->
                <td class="datatable-cell-wrapper"><div>{{ item.admin_email }}</div></td>
                <td class="datatable-cell-wrapper"><div>{{ item.admin_name}}</div></td>
                <td class="datatable-cell-wrapper">{{ item.password }}</td>
                <!-- <td class="datatable-cell-wrapper red--text">{{ item.status }}</td> -->
                <v-btn small :disabled='isDisabled' class="lime darken-1" @click="retrieve(index)">Delete</v-btn>
                
                <!-- </tr> -->
              </template>
            </v-data-table>
      </v-flex>
      </v-layout>
         <!-- <decline/> -->
       </v-card>
     </v-flex>
      <v-flex xs10 md10 >
       <v-card max-height="400px" style="overflow-y: auto" class="pa-3" outline max-width="1300"  height="400px">
                   <v-row
          align="center"
          justify="center"
        >
          <v-col
            cols="6"
            sm="8"
            md="4"
          >
          <v-layout row justify-center>
            <v-flex sm12 md6>
                 <v-card class="elevation-12" >
              <v-toolbar
                color="#004080"
                dark
                flat
              >
                <v-toolbar-title class="white--text">Register </v-toolbar-title>
                <div class="flex-grow-4"></div>
               <h2 style="margin-left:30%;color:#faee02;"  >eCMS</h2>
                <v-spacer></v-spacer>
                <!-- <v-tooltip right>
                  <template v-slot:activator="{ on }">
                      <router-link to="/login">
                            <v-btn
                            icon
                            large
                            href="https://codepen.io/johnjleider/pen/pMvGQO"
                            target="_blank"
                            v-on="on"
                            >
                            Login
                            </v-btn>
                      </router-link>
                  </template>
                  <span class="white--text" >Login Now</span>
                </v-tooltip> -->
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field
                    label="Name"
                    name="login"
                    v-model="name"
                    prepend-icon="person"
                     :rules="[() => !!name || 'This field is required']"
                    type="text"
                  ></v-text-field>

                  <v-text-field
                    label="Email"
                    name="login"
                    v-model="email"
                     :rules="[() => !!email || 'This field is required']"
                    prepend-icon="email"
                    type="text"
                  ></v-text-field>
                  <v-text-field
                    label="Tel"
                    name="login"
                    v-model="tel"
                     :rules="[() => !!tel || 'This field is required']"
                    prepend-icon="email"
                    type="text"
                  ></v-text-field>
                  <v-text-field
                    id="password"
                    label="Password"
                    v-model="password"
                    name="password"
                    prepend-icon="lock"
                     :rules="[() => !!password || 'This field is required']"
                    type="password"
                  ></v-text-field>
                  <v-text-field
                    id="confirm"
                    label="Confirm Password"
                    v-model="confirm"
                    name="password"
                    prepend-icon="lock"
                    :rules="[() => !!confirm || 'This field is required']"
                    type="password"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <div class="flex-grow-1"></div>
                <v-spacer></v-spacer>
                <v-btn :disabled='isDisabled' color="primary" @click="submit()">Register</v-btn>
              </v-card-actions>
            </v-card>
            </v-flex>
          </v-layout>
           
           
          </v-col>
        </v-row>
         <!-- <decline/> -->
       </v-card>
     </v-flex>
   </v-layout>
   
    </div>
</template>
<script>
import axios from 'axios'
export default {

    data(){
        return{
        posts:'',
          search: '',
          status:'',
          admin_email:'',
          drawer: null,
      name:"",
      email:"",
      tel:"",
      password:"",
      confirm:"",
      terms: false,
          
      headers: [
        { text: 'Admin Email', value: 'admin_email' },
        { text: 'Admin Name', value: 'admin_name' },
          { text: 'Admin Password', value: 'password' },
         
      
      ],
      items: [],
      complaints_refn0:'',
      token: localStorage.getItem('token'),
      user: localStorage.getItem('user')
      
    }
        },
         created(){
      axios.get('http://127.0.0.1:5000/Accounts',
        {headers:{'x-access-token': localStorage.getItem('token')}}).then(
        response =>{
          this.items = response.data
       
         
         
            
           
        }
      )
    },
    computed:{
            isDisabled: function(){
    	return !this.terms;
    }
    },
    methods:{
       
         submit(){
        axios.post('http://127.0.0.1:5000/head_register',{
          'Name':this.name,'email':this.email,'tel':this.tel,'password':this.password,'confirm_password':this.confirm
          },
          {headers:{'x-access-token': this.token}}
          ).then(response=>{
                  window.location.reload()
              })
            },
        retrieve(index){
             this.admin_email= this.items[index].admin_email
             axios.post('http://127.0.0.1:5000/Account',{'admin_email':this.admin_email},
            {headers:{'x-access-token': this.token}}
            ).then(
            response =>{
              window.location.reload()
          
            
            
                
              
            }
      )


        }
    }
    }
    

</script>