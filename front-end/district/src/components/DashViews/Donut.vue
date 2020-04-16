<template>
  <div class="small">
    <pie-chart :data="chartData" :options="chartOptions" width="100%" height="90px" ></pie-chart>
  </div>
</template>

<script>
import PieChart from "../Donut.js";
import VueCharts from 'vue-chartjs'
export default {
  name: "App",
  components: {
    PieChart
  },
  data() {
    return {
      chartOptions: {
        hoverBorderWidth: 10,
        
      },
      chartData: {
        hoverBackgroundColor: "red",
        hoverBorderWidth: 10,
        
        labels: ["x", "x", "x"],
        datasets: [
          {
            label: "Data One",
            backgroundColor: ["#004080", "#E65100", "#00D8FF"],
            data: [1, 10, 5]
          }
        ]
      }
    };
  }
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
