import { Doughnut, mixins } from "vue-chartjs";
const { reactiveProp } = mixins
export default {
  extends: Doughnut,
  props: ["data", "options"],
  mixins: [reactiveProp],
  mounted() {
    // this.chartData is created in the mixin.
    // If you want to pass options please create a local options object
    this.renderChart(this.data, {
      borderWidth: "1000px",
      hoverBackgroundColor: "red",
      hoverBorderWidth: "5px",
      cutoutPercentage:0,
      // responsive: true,
      // maintainAspectRadio: false
    });
  },
  watch: {
    'data' (to, from) {
      this.renderChart(this.data, this.options)
    }
  }
};