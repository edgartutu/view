<template>
    <v-time-picker
      v-model="timeStep"
      :allowed-minutes="allowedStep"
      
      format="24hr"
    ></v-time-picker>
 
</template>
<script>
  export default {
    data () {
      return {
        time: '11:15',
        timeStep: '10:10',
      }
    },
    methods: {
      allowedHours: v => v % 2,
      allowedMinutes: v => v >= 10 && v <= 50,
      allowedStep: m => m % 10 === 0,
    },
  }
</script>
