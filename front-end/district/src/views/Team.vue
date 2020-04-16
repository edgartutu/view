<template>
  <div>
    <navbar/>
    <!-- <div class="text-center"> -->
     
    <!-- </div>  -->
    <v-container fluid>
  <v-layout row wrap column>       
    <v-flex xs12 md12 >
       <export-excel style="float:left;" :data="items">
            <h6  >Export to Excel</h6>
            <img src="@/assets/img/512.png" style="width:40px;height:40px">
        </export-excel> 
        <!-- <v-flex>
          <router-link to="/report">
              <v-btn style="float:right;" ripple outlined color="indigo">Register Complaint</v-btn>
          </router-link>
        </v-flex> -->
        
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
            <template slot="items" slot-scope="{item}" >          
              <!-- <tr @click="props.expanded = !props.expanded">   -->
                <td class="datatable-cell-wrapper"><div>{{ item.nature_complaint }}</div></td>
                <td class="datatable-cell-wrapper"><div>{{ item.complaints_refn0}}</div></td>
                <!-- <td class="datatable-cell-wrapper">{{ props.item.complaint }}</td> -->
                <td class="datatable-cell-wrapper">{{ item.district }}</td>
                <td class="datatable-cell-wrapper">{{ item.date }}</td>
                <td class="datatable-cell-wrapper">{{ item.date_submit }}</td>
                
                <td>
                <v-dialog
                v-model="dialog"
                width="800"
                >
                  <template v-slot:activator="{ on }">
                    <v-btn
                      small 
                      class="pink"
                      v-on="on"
                    >
                    review
                    </v-btn>
                      </template>
                        <v-card>
                            <v-card-title
                            class="purple"
                          primary-title
                          style="color:white;"
                            >
                            Complaint Details
                          </v-card-title>
                                <!-- <v-btn class="right teal"   @click.native="print(index)">Print</v-btn> -->
                                   <v-card-text  class="px-16">
                                     <v-avatar size="100">
                                      <img
                                          src="../assets/img/ECLOGO.jpg"
                                        style="width:200px;"
                                      >
                                      </v-avatar>
                                      
                                      <h3>The Electoral Commission</h3>
                                      <h3 style="color: #004080;" class="font-weight-bold">Certificate Of Resolution</h3>
                                      <h4 id="print" class="red--text" style="font-weight:bold;">{{item.complaints_refn0}}</h4>
                                      <!-- <h4 class="font-weight-bold">Complaint Ref</h4>
                                      <p>{{props.item.complaints_refn0}}</p> -->
                                      <!-- <h4 class="font-weight-bold">Complaint Category</h4>
                                      <p>{{props.item.nature_complaint}}</p> -->
                                      <h4 class="font-weight-bold">Complainant</h4>
                                      <p>{{item.complaint}}</p>
                                      <!-- <h4 class="font-weight-bold">Location</h4>
                                      <p>{{props.item.district}}</p> -->
                                      <h4 class="font-weight-bold">District Resolution</h4>
                                      <p>{{item.district_resolutions}}</p>
                                       <h4 class="font-weight-bold">HeadQuater Resolution</h4>
                                      <p>{{item.headdescription}}</p>
                                       <h4 class="font-weight-bold">Commission Decission</h4>
                                      <p>{{item.district_description}}</p><p>{{item.headresolution}}</p>
                                       <!-- <h4 class="font-weight-bold">Amendement</h4>
                                      <p>{{props.item.classify_complaint}}</p> -->
                                      <div class="left font-weight-bold">Date Recieved :</div>
                                      <div class="left">{{item.date}}</div><br>
                                        <div class="left font-weight-bold">Date Resolved :</div>
                                      <div class="left">{{item.date_submit}}</div> 
                                      <div class="right">Signature: ...........................................</div>
                                      <br>
                                      <div class="right">Chairperson Electoral Commision</div><br>
                                      
                                  </v-card-text> 
                            
                           
                          </v-card>
                        </v-dialog>
                        </td>
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
        search: '',
        token: localStorage.getItem('token'),
      headers: [
        { text: 'Complaint Category', value: 'nature_complaint' },
        { text: 'Complaint Ref', value: 'complaints_refn0' },
          // { text: 'Complainant', value: 'complaint' },
          { text: 'Location', value: 'district' },
          { text: 'Date Recieved', value: 'date' },
          { text: 'Date Resolved ', value: 'date_submit' },
      
      ],
      items: []
      
    }
    
    
    }, 
    created(){
      axios.post('http://127.0.0.1:5000/allcomplaints',{
        "district_n0":localStorage.getItem('district')},
        {headers:{'x-access-token': this.token}}
        ).then(
        response =>{
          this.items = response.data
        }
      )
    },
     methods:{
       print(index){
        // Get HTML to print from element
        
const prtHtml = document.getElementById('print').innerHTML;

// Get all stylesheets HTML
let stylesHtml = '';
for (const node of [...document.querySelectorAll('link[rel="stylesheet"], style')]) {
  stylesHtml += node.outerHTML;
}

// Open the print window
const WinPrint = window.open('', '_parent', 'left=0,top=0,width=800,height=900,toolbar=0,scrollbars=0,status=0');


WinPrint.document.write(`<!DOCTYPE html>
<html>
  <head>
    ${stylesHtml}
  </head>
  <body>
   <div style="width:5px;" class="logo-print">
   
   </div>
    ${prtHtml}
  </body>
</html>`);
// setTimeout(function() {
//     WinPrint.print();
// }, 1000)

// WinPrint.document.close();
// WinPrint.focus();
// WinPrint.print();
// WinPrint.close();
      }
    }
  }
</script>
<style>
@media all{
   printed-div{
       display:none;
   }
}

@media print{
   printed-div{
       display:block;
   }
   .logo-print{
       width:5px;
       height:5px;
       display: list-item;
       list-style-image: url(../assets/img/ECLOGO.jpg);
       list-style-position: inside;
       opacity: 0.1;
  filter: alpha(opacity=50);
   }
}


</style>
