<template>
<v-card class="rounded-card">

  <v-container
    
    grid-list-xl>
     <h4  v-for="proposal in items" :key="proposal.reg_no2" class="orange--text">{{proposal.reg_no2}}</h4>
    <v-layout justify-right>
     
     
        <v-dialog
      v-model="dialog"
      width="500"
    >
      <template v-slot:activator="{ on }">
        <v-btn
          color="primary"
          dark
          v-on="on"
        >
          Add Project Partner
        </v-btn>
      </template>

      <v-card class="rounded-card">
       

        <v-card-text>
           <v-container>
           <h3 class="red--text" style="font-style:italic">Make sure your partner has registered on the system. Once your patner has confirmed, you will not be able to switch partners</h3>
          </v-container>
         
            <v-text-field class="ma-3" label="Registration number1" placeholder="  reg_no" v-model="reg_no2"></v-text-field>
         
         
          
          
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="submit"
          >
            Submit
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  
 <v-spacer></v-spacer>
    

    <div class="mx-6 hidden-sm-and-down"></div>

   <div class="text-right">
    <v-menu left>
      <template v-slot:activator="{ on: menu }">
        <v-tooltip left>
          <template v-slot:activator="{ on: tooltip }" >
            <v-btn
              color="primary"
              
              v-on="{ ...tooltip, ...menu }"
            >Partner Requests</v-btn>
          </template>
          <span   >
            <v-card >
              <v-card-text  >
                <h6>click button to approve or reject</h6>
                <h6 class="green--text">Student-1</h6>
              <p>{{request.reg_no}}</p>
              <h6 class="green--text">Student-2</h6>
               <p>{{request.reg_no2}}</p>
               <h6 class="green--text">status </h6>
               <p >{{request.status}}</p> 
               
                
              

              </v-card-text>

              
            </v-card>
          </span>
        </v-tooltip>
      </template>
      
        <v-flex>
          <v-btn small class="blue" @click="approve">accept</v-btn>
       
       <v-btn small class="red" @click="reject">reject</v-btn>

        </v-flex>
      
    
    </v-menu>
  </div>
  </v-layout>
 
   

    <v-layout wrap>
     <v-flex
        md12
        lg12
      >
        <material-card 
          color="deep-orange lighten-1"
          title="Submited Projects"
           class="rounded-card"
          popout  
        >
          <user/>
        </material-card>
      </v-flex>
      <v-flex
        md12
        lg12
      >
        <material-card
          title="New Projects"
          color="cyan darken-3"
           class="rounded-card"
          >
          

          <simple/>

        </material-card>
      </v-flex>
    </v-layout>
  </v-container>
  </v-card>
</template>

<script>
import axios from "axios";
import user from './UserProfile.vue'
import table from './UsersTable.vue'
import simple from './SimpleTables.vue'
export default {
  name: 'Dashboard',
  components:{
    user,
    table,
    simple

  },
  data () {
    return {
       dialog: false,
        notifications: false,
        sound: true,
        widgets: false,
        reg_no2:"",
        reg_no:"",
        items:[],
        request:{},
            itemz: [
        { title: 'Click Me1' },
        { title: 'Click Me2' },
        { title: 'Click Me3' },
        { title: 'Click Me4' },
      ],

      
 
     
     
     
     
    }
  },
  created(){
    this.reg_no = localStorage.getItem('user')
    axios.get("http://127.0.0.1:5000/viewpartner",{"reg_no": this.reg_no}).then(response => {
                this.items= response.data })

  },

  mounted(){
    this.reg_no = localStorage.getItem('user')
    axios.post("http://127.0.0.1:5000/viewpartnerequest",{"reg_no": this.reg_no}).then(response =>{
      this.request=response.data
    })

  },

  methods: {
    submit(){
      this.reg_no = localStorage.getItem('user')
      axios.post("http://127.0.0.1:5000/addpartner",{"reg_no": this.reg_no,"reg_no2":this.reg_no2}).then(this.dialog=false)

    },
     approve() {
        this.reg_no = localStorage.getItem('user')
        axios.post("http://127.0.0.1:5000/confirmrequest",{"reg_no": this.reg_no,"response":"accept"}
        ).then(response =>{
          console.log(response);
          window.location.reload()
        })

  },
  reject() {
        this.reg_no = localStorage.getItem('user')
        axios.post("http://127.0.0.1:5000/confirmrequest",{"reg_no": this.reg_no,"response":"reject"}
        ).then(response =>{
          console.log(response);
          window.location.reload()
        })
  },
    
  }
}
</script>

<style>
.rounded-card{
    border-radius:200px;
    border-color: brown;
    
}
</style>

