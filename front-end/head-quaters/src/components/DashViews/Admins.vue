<template>
  <div>
    <!-- <navbar/> -->
  <v-layout row wrap column>       
    <v-flex xs12 md12 >
      <export-excel :data="items">
            <h6  >Export to Excel</h6>
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
                 <td class="datatable-cell-wrapper"><div>{{index}}</div></td>
               <td class="datatable-cell-wrapper"><div>{{ item.admin_Name }}</div></td>
                <td class="datatable-cell-wrapper"><div>{{ item.admin_email}}</div></td>
                <td class="datatable-cell-wrapper">{{ item.post }}</td>
                <td class="datatable-cell-wrapper">{{ item.district_n0 }}</td>
                <td class="datatable-cell-wrapper">{{ item.tel }}</td>
                
                
                <!-- </tr> -->
              </template>
            </v-data-table>
      </v-flex>
      </v-layout>
  </div>
</template>
<script>
// import navbar from '../components/DashViews/NavBar'
import axios from 'axios'
  export default {
   
    data(){
    
      return {
        search: '',
      headers: [
        { text: 'N/0', value: 'index' },
        { text: 'District Admininstrator Name', value: 'admin_Name' },
        { text: 'District Administrator Email', value: 'admin_email' },
          { text: 'Staff', value: 'post' },
          { text: 'District', value: 'district_n0' },
          { text: 'Telephone', value: 'tel' },
      
      ],
      items: [],
      token: localStorage.getItem('token')
      
    }
    
    },
     created(){
      axios.get('http://127.0.0.1:5000/Alllevelones',{headers:{'x-access-token':this.token}}).then(
        response =>{
          this.items = response.data
        }
      )
    },
  }
</script>
