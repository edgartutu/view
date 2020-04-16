<template>
  <div class="small">
    <v-layout row>
         <v-flex xs12 md6>
                  <!-- <v-select
                  v-model="district"
                  :items="items"
                  label="Classification"
                   required
                    ></v-select> -->
                     <v-autocomplete
                       v-model="district"
                        label="Districts"
                        :items="items"
                        style="overflow-y: auto;"
                        max-height="300px"
                      ></v-autocomplete>
              </v-flex>
              <v-spacer></v-spacer>
               <v-btn class="right purple" small @click="pulldata()">Get District</v-btn>
    </v-layout>
    
              
    <pie-chart :data="chartData" :options="chartOptions" width="60%" height="45px" ></pie-chart>
  </div>
</template>

<script>
import PieChart from "../Donut.js";
import VueCharts from 'vue-chartjs'
import axios from 'axios'
export default {
  name: "App",
  components: {
    PieChart
  },
  data() {
    return {
      district:'',
      stuff:null,
      items: null,
      chartOptions: {
        hoverBorderWidth: 10,
        
      },
      chartData: {
        hoverBackgroundColor: "red",
        hoverBorderWidth: 10,
        
        labels: ["Resolved", "Unresolved", "Pending"],
        datasets: [
          {
            label: "Data One",
            backgroundColor: ["green", "#E65100", "#004080"],
            data: this.stuff
          }
        ]
      }
    };
  },  created(){
    axios.post('http://127.0.0.1:5000/CodeDistrict',{},
    {
       headers:{
       'x-access-token': localStorage.getItem('token')
     }
     }
    ).then(response =>{
     
      let result= response.data
      this.items=result
      console.log(localStorage.getItem('token'))
      

    })
  },
  methods:{
    pulldata(){
      axios.post('http://127.0.0.1:5000/PieChartsdistrict',{'district_n0':this.district},
    {
       headers:{
       'x-access-token':localStorage.getItem('token')
     }
     }
    ).then(response =>{
     
      let result= response.data.data
      this.stuff=result
      console.log(this.district)
      

    })

    }
  },
   watch:{
    stuff(newData){
      const data =this.chartData
      data.datasets[0].data=newData
      this.chartData={...data}
    }
  },
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.small {
    max-width: 400px;
    margin:  auto auto;
  }
</style>
