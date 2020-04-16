<template>
  <article>
    <div class="container" :class="{'sign-up-active' : signUp}">
      <div class="overlay-container">
        <div class="overlay">
          <div class="overlay-left">
            <h2>Register!</h2>
            <p>Please login with your personal info</p>
            <button class="invert" id="signIn" @click="signUp = !signUp">Sign In</button>
          </div>
          <div class="overlay-right">
            <h2>Hey Student</h2>
            <p>Please enter your personal details</p>
            <button class="invert" id="signUp" @click="signUp = !signUp">Sign Up</button>
          </div>
        </div>
      </div>
      
      <form class="sign-up" action="/">
          <h2>Create login</h2>
          <div>Use your email for registration</div>
          <input type="text" placeholder="Student1 Name" v-model="student1" />
          <input type="text" placeholder="Student1 Reg n0" v-model="reg_no" />
          <input type="email" placeholder="Email-1" v-model="email" />
          <input type="text" placeholder="Tel1" v-model="tel" />
          <input type="text" placeholder="Course: E for BELE T for BSTE and C for BSCE" v-model="course" />
          <input type="password" placeholder="Password" v-model="password_hash" />
          <input type="password" placeholder="Confirm Password" v-model="confirm" />
          <button @click="register">Sign Up</button>
      </form>
      <form class="sign-in" action="#">
        <h2>Sign In</h2>
        <div>Use your account</div>
        <input type="text" placeholder="Reg n0" 
        ref="username"
        v-model="reg_no"
        :rules="[() => !!username || 'This field is required']"
        required />
        <input  placeholder="Password" 
        ref="password"
                  v-model="password_hash"
                  :rules="[() => !!password || 'This field is required']"
                  :append-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'"
                 :type="showPassword ? 'text' : 'password'"
                  prepend-icon="mdi-lock"
                  label="Password"
                  counter
                  required
                  @keydown.enter="login"
                  @click:append="showPassword = !showPassword" />
        <a href="/reset">Forgot your password?</a>
        <button  @click="login">Sign in</button>
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
      </form>
    </div>
  </article>
</template>

<script>
import axios from 'axios'
import reset from './DashViews/ResetPass.vue'
  export default {
    components:{
      reset

    },

       data: function () {
    return {
      
      signUp: false,
      reg_no:'',
      reg_no2:'',
      student1:'',
      student2:'',
      email:'',
      email2:'',
      tel:'',
      tel2:'',
      password_hash:'',
      username: '',
      confirm: '',
      course: '',
    
      errorMessages: 'Incorrect login info',
      snackbar: false,
      color: 'general',
      showPassword: false
    }

  },
  // Sends action to Vuex that will log you in and redirect to the dash otherwise, error
 methods: {
    login: function () {
      let username = this.reg_no
      let password = this.password_hash
      this.$store.dispatch('login', {username,password})
        .then(() => this.$router.push('/dashboard'))
        .catch(err => {
        console.log(err)
        this.snackbar= true
        }
        )
     },
     register() {
         axios.post('http://127.0.0.1:5000/register', {
             "student1": this.student1,"reg_no":this.reg_no,"email": this.email,
              "tel": this.tel,"password": this.password_hash,"confirm_password": this.confirm,
              'course':this.course
         }).then(response => {console.log(response)})
     }
  },
  metaInfo () {
    return {
      title: 'Super Secret | Login'
    }
  }
    
  }
</script>

<style lang="scss" scoped>
  .container {
    position: relative;
    width: 768px;
    height: 480px;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 15px 30px rgba(0, 0, 0, .2),
                0 10px 10px rgba(0, 0, 0, .2);
    background: linear-gradient(to bottom, #efefef, #ccc);
    .overlay-container {
      position: absolute;
      top: 0;
      left: 50%;
      width: 50%;
      height: 100%;
      overflow: hidden;
      transition: transform .5s ease-in-out;
      z-index: 100;
    }
    .overlay {
      position: relative;
      left: -100%;
      height: 100%;
      width: 200%;
      background: linear-gradient(to bottom right, #7FD625, #009345);
      color: #fff;
      transform: translateX(0);
      transition: transform .5s ease-in-out;
    }
    @mixin overlays($property) {
      position: absolute;
      top: 0;
      display: flex;
      align-items: center;
      justify-content: space-around;
      flex-direction: column;
      padding: 70px 40px;
      width: calc(50% - 80px);
      height: calc(100% - 140px);
      text-align: center;
      transform: translateX($property);
      transition: transform .5s ease-in-out;
    }
    .overlay-left {
      @include overlays(-20%);
    }
    .overlay-right {
      @include overlays(0);
      right: 0;
    }
  }
  h2 {
    margin: 0;
  }
  p {
    margin: 20px 0 30px;
  }
  a {
    color: #222;
    text-decoration: none;
    margin: 15px 0;
    font-size: 1rem;
  }
  button {
    border-radius: 20px;
    border: 1px solid #009345;
    background-color: #009345;
    color: #fff;
    font-size: 1rem;
    font-weight: bold;
    padding: 10px 40px;
    letter-spacing: 1px;
    text-transform: uppercase;
    cursor: pointer;
    transition: transform .1s ease-in;
    &:active {
      transform: scale(.9);
    }
    &:focus {
      outline: none;
    }
  }
  button.invert {
    background-color: transparent;
    border-color: #fff;
  }
  form {
    position: absolute;
    top: 0;
    display: flex;
    align-items: center;
    justify-content: space-around;
    flex-direction: column;
    width: calc(50% );
    height: calc(100% );
    text-align: center;
    background: linear-gradient(to bottom, #efefef, #ccc);
    transition: all .5s ease-in-out;
    div {
      font-size: 1rem;
    }
    input {
      background-color: #eee;
      border: none;
      padding: 8px 15px;
      margin: 6px 0;
      width: calc(100% - 30px);
      border-radius: 15px;
      border-bottom: 1px solid #ddd;
      box-shadow: inset 0 1px 2px rgba(0, 0, 0, .4), 
                        0 -1px 1px #fff, 
                        0 1px 0 #fff;
      overflow: hidden;
      &:focus {
        outline: none;
        background-color: #fff;
      }
    }
  }
  .sign-in {
    left: 0;
    z-index: 1;
  }
  .sign-up {
    left: 0;
    z-index: 1;
    opacity: 0;
  }
  .sign-up-active {
    .sign-in {
      transform: translateX(100%);
    }
    .sign-up {
      transform: translateX(100%);
      opacity: 1;
      z-index: 5;
      animation: show .5s;
    }
    .overlay-container {
      transform: translateX(-100%);
    }
    .overlay {
      transform: translateX(50%);
    }
    .overlay-left {
      transform: translateX(0);
    }
    .overlay-right {
      transform: translateX(20%);
    }
  }
  @keyframes show {
    0% {
      opacity: 0;
      z-index: 1;
    }
    49% {
      opacity: 0;
      z-index: 1;
    }
    50% {
      opacity: 1;
      z-index: 10;
    }
  }
</style>