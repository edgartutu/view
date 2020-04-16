<template>
  <div>
    <navbar/>
    <v-container fluid>
  <v-layout row wrap column>       
    <v-flex xs12 md12 >
      <export-excel style="float:left;" :data="items">
            <h6  >Export to Excel</h6>
            <img src="@/assets/img/512.png" style="width:40px;height:40px">
        </export-excel>  
        <!-- <v-flex>
          <router-link to="/reports">
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
            <template slot="items" slot-scope="{ item,index }" >          
              <!-- <tr @click="props.expanded = !props.expanded">   -->
                 <td class="datatable-cell-wrapper"><div>{{index}}</div></td>
                <td class="datatable-cell-wrapper"><div>{{ item.nature_complaint }}</div></td>
                <td class="datatable-cell-wrapper"><div>{{ item.complaints_refn0}}</div></td>
                <td class="datatable-cell-wrapper"><div><v-btn
            :loading="loading5"
            :disabled="loading5"
            color="blue-grey"
            class="ma-2 white--text"
            fab
            small
            @click="loader = 'loading5',downlod(index)"
          >
            <v-icon dark>mdi-cloud-download</v-icon>
          </v-btn></div></td>
                <td class="datatable-cell-wrapper">{{ item.date }}</td>
                <td class="datatable-cell-wrapper">{{ item.date_submit }}</td>
                <td>
                   
          <div class="right">
            <v-chip  small :class="`${item.status}  white--text caption my-2`">
              {{item.status}}
            </v-chip>
          </div>
         </td>
                <td>
                  <router-link   :to="{ name: 'allcompaints',
            params: { userDeta:{ref:item.complaints_refn0,complaint:item.complaint,dresolution:item.district_resolutions,head:item.headdescription,resoln:item.headresolution,dreslon:item.district_description,
            date:item.date,date_resolved:item.date_submit,complainants:item.compalianant_name,agentname:item.agent_name,post:item.agent_staff,compn0:item.agent_phone,location:item.district,
            complaint_detail:item.nature_complaint,description:item.comments,resolving:item.headdescription,Complaint_category:item.Complaint_category} } }" >
				    <v-btn
                
                 class="pink"
                small
              
                
              >
              <div class="mx-2">View</div>
              </v-btn>
				</router-link>
              
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
      headers: [
         { text: 'N/0', value: 'index' },
        { text: 'Complaint Category', value: '' },
        { text: 'Complaint Ref', value: 'complaint_refn0' },

          { text: 'file', value: 'complaint' },
          { text: 'Date Recieved', value: 'district' },
          { text: 'Date Resolved ', value: 'date' },
           { text: 'Status ', value: 'date_submit' },
      
      ],
      items: [],
      token: localStorage.getItem('token')
      
    }
    
    },
    created(){
      axios.get('http://127.0.0.1:5000/alladmincomplaints',{headers:{'x-access-token':this.token}}).then(
        response =>{
          this.items = response.data
        }
      )
    },
    methods:{
        downlod(index){
       axios.post('http://127.0.0.1:5000/files',{'complaints_refn0':this.items[index].complaints_refn0},
        {headers:{'x-access-token': this.token}})
        //.then(
      //response => {

        //this.forceFileDownload(response)
       //console.log(response)
      //}
      //)
      
    },

                 print(index){
        // Get HTML to print from element
       

    // if (index){
     
            const prtHtml = document.getElementById('print').innerHTML;
           var children =  prtHtml.childNodes;
            for(var i = 0; i < children.length; i++)
                someDiv.removeChild(children[i]);
// const prtHtmls = document.getElementById('prints').innerHTML;

// Get all stylesheets HTML
let stylesHtml = '';
for (const node of [...document.querySelectorAll('link[rel="stylesheet"], style')]) {
  stylesHtml += node.outerHTML;
}

// Open the print window
const WinPrint = window.open('', '', 'left=0,top=0,width=800,height=900,toolbar=0,scrollbars=0,status=0');

WinPrint.document.write(`<!DOCTYPE html>
<html>
  <head>
    ${stylesHtml}
  </head>
  <body>
   <div style="width:5px;margin-top:20%;" class="logo-print"></div>
${prtHtml}
  </body>
</html>`);
        // }
// }
        

// setTimeout(function() {
//     WinPrint.print();
// }, 3000)

// WinPrint.document.close();
// WinPrint.focus();
// WinPrint.print();
// WinPrint.close();
      }
    }
  }
</script>
<style >
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
.item.props.Pending{
  border-left: 4px solid green
}
.project.Resolved{
  border-left: 4px solid orange
}
.project.Declined{
  border-left: 4px solid tomato
}
.project.Unresolved{
  border-left: 4px solid purple
}
.v-chip.Pending{
  background: green 
}
.v-chip.Resolved{
  background:  #004080
}
.v-chip.Declined{
  background:  tomato
}
.v-chip.Unresolved{
  background:  purple
}


</style>

