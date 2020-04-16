<template>
<div>
<v-toolbar style=" background-color: #004080;" flat fixed>
          <h3 class="white--text">HEADQUATER</h3>
         <v-spacer></v-spacer>
            <v-avatar>
                <img
                    src="@/assets/img/com.jpg"
                    alt="John"
                >
                </v-avatar>
           <v-toolbar-title style="color:#faee02;" >eCMS</v-toolbar-title>
          
           <!-- <p></p>
           <p></p>
            <v-toolbar-items class="hidden-sm-and-down" >
                <v-layout  row >
                <v-btn  flat small  class=" mx-2 white--text" v-for="link in links" :key="link.text" router :to="link.route">
                    <span>{{link.text}}</span>
                </v-btn>
                </v-layout>
            </v-toolbar-items>
            <v-spacer></v-spacer>
                <p></p>
                 <v-menu class="hidden-md-and-up">
                    <v-toolbar-side-icon slot="activator" class="purple--text"   ></v-toolbar-side-icon>
                    <v-list>
                    <v-list-tile v-for="link in links" :key="link.text" router :to="link.route">
                        <v-list-tile-content>
                        <v-list-tile-title class="purple--text">{{ link.text}}</v-list-tile-title>
                        </v-list-tile-content>
                    </v-list-tile>   
                    </v-list>
                </v-menu>
                <router-link v-ripple  to="/dashboard">
					<v-icon class="mx-2" color="white">mdi-home</v-icon><br>
				</router-link>
                <v-menu bottom left content-class offset-y transition="slide-y-transition">
					<router-link v-ripple slot="activator"  to="/projects">
						<v-badge color="#f73b3b" overlap>
					        <template slot="badge"  >
                               {{projects.length}}
                                </template>
					            <v-icon class="mx-2" color="white">mdi-bell</v-icon>
				        </v-badge>
					</router-link> -->
					<!-- <v-card> -->
						<!-- <v-list dense>
							<v-list-tile v-for="notification in notifications" :key="notification" @click="onClick">
								<v-list-tile-title v-text="notification"/>
							</v-list-tile>
						</v-list> -->
					<!-- </v-card> -->
				<!-- </v-menu>
                     <v-btn flat class="white--text" @click=" logout()">
                    <span style="color:#faee02;">SignOut</span>
                    <v-icon>exit_to_app</v-icon>
                    </v-btn>  -->
        </v-toolbar><br>
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
               <h2 style="margin-left:30%;color:#faee02;" >eCMS</h2>
                <v-spacer></v-spacer>
                <!-- <v-tooltip right>
                  <template v-slot:activator="{ on }"> -->
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
                  <!-- </template>
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
                <router-link to="/login">
                      <v-btn small color="primary" @click="submit()">Register</v-btn>
                </router-link>
              </v-card-actions>
            </v-card>
            </v-flex>
          </v-layout>
           
           
          </v-col>
        </v-row>
        </div>
</template>
<script>
import axios from 'axios'
  export default {
    props: {
      source: String,
    },
    data: () => ({
      drawer: null,
      name:"",
      email:"",
      tel:"",
      password:"",
      confirm:"",
    }),
    methods:{
      submit(){
        axios.post('http://127.0.0.1:5000/head_register',{
          'Name':this.name,'email':this.email,'tel':this.tel,'password':this.password,'confirm_password':this.confirm
          }).then(response=>{
                window.location.reload()
            })
          }

      }
  }
</script>