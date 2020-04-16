<template>
  <div>
    <navbar/>
    <v-container fluid>
  <v-layout row wrap column>  
    <v-flex xs12 md12 >
        <export-excel style="float:left;" :data="items">
            <h6 >Export to Excel</h6>
            <img src="@/assets/img/512.png" style="width:40px;height:40px">
        </export-excel>  
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
                <td class="datatable-cell-wrapper"><div>{{ item.nature_complaint }}</div></td>
                <td class="datatable-cell-wrapper"><div>{{ item.complaints_refn0}}</div></td>
                <td class="datatable-cell-wrapper">{{ item.complaint }}</td>
                <td class="datatable-cell-wrapper">{{ item.comment }}</td>
                <td class="datatable-cell-wrapper">{{ item.date }}</td>
                <td class="datatable-cell-wrapper red--text">{{ item.status }}</td>
                <v-btn small class="lime darken-1" @click="retrieve(index)">Retrieve</v-btn>
                
                <!-- </tr> -->
              </template>
            </v-data-table>
      </v-flex>
      </v-layout>
      </v-container>
  </div>
</template>
<script>
import navbar from '../components/DashViews/NavBar'
import axios from 'axios'
  export default {
    components:{
      navbar
    },
    data(){
    
      return {
          posts:'',
          search: '',
          status:'',
          
      headers: [
         { text: 'Complaint Category', value: 'nature_complaint' },
        { text: 'Complaint Ref', value: 'complaints_refn0' },
          { text: 'Complainant', value: 'complaint' },
          { text: 'Comments', value: 'comment' },
          { text: 'Date Recieved', value: 'date' },
          { text: 'Status ', value: 'status' },
      
      ],
      items: [],
      complaints_refn0:'',
      email: localStorage.getItem('user'),
      token: localStorage.getItem('token')
      
    }
    
    
    }, 
    created(){
      axios.post('http://127.0.0.1:5000/AllDeclinedComplaints',{"district_n0":localStorage.getItem('district')},
            {
              headers:{
              'x-access-token':localStorage.getItem('token')
            }
            }).then(
        response =>{
          this.items = response.data
        }
      )
    },
    methods:{
        retrieve(index){
            this.complaints_refn0 = this.items[index].complaints_refn0
             axios.post('http://127.0.0.1:5000/updatedeclinedcomplaint',{'admin_email':this.email,
             'complaints_refn0':this.complaints_refn0,'status':'Pending'},
             {
                headers:{
                'x-access-token':this.token
              }
              }
             )
            .then(response=>{
                window.location.reload()
            })


             
             
        },
         exportdb() {
                axios.post("http://127.0.0.1:5000/excelexport1",
                {
                  headers:{
                  'x-access-token':this.token
                }
                }
                ).then(response => {
                    console.log(response)
                })
            },
    }
  }
</script>
