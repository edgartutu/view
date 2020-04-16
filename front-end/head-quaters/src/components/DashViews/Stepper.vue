<template>
  <v-stepper v-model="e1">
    <v-stepper-header>
      <v-stepper-step :complete="e1 > 1" step="1">Complaint Details</v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step :complete="e1 > 2" step="2">Complaint Resolution</v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step step="3">Review</v-stepper-step>
    </v-stepper-header>

    <v-stepper-items>
      <v-stepper-content step="1">
        
        <v-container fluid grid-list-md>
          <v-layout row wrap>
            <v-flex
              xs12
              md12  
            >
            <v-card
          class="mb-12"
          color="grey lighten-1"
          height="200px">
              
             {{ id }}
               </v-card>

            </v-flex>
          </v-layout>
        </v-container>
        
       
        <v-btn
          color="primary"
          @click="e1 = 2"
        >
          Continue
        </v-btn>

        <v-btn text>Cancel</v-btn>
      </v-stepper-content>

      <v-stepper-content step="2">
        <v-card
          class="mb-12"
          color="grey lighten-1"
          height="200px"
        ></v-card>

        <v-btn
          color="primary"
          @click="e1 = 3"
        >
          Continue
        </v-btn>

        <v-btn text>Cancel</v-btn>
      </v-stepper-content>

      <v-stepper-content step="3">
        <v-card
          class="mb-12"
          color="grey lighten-1"
          height="200px"
        ></v-card>

        <v-btn
          color="primary"
          @click="e1 = 1"
        >
          Continue
        </v-btn>

        <v-btn text>Cancel</v-btn>
      </v-stepper-content>
    </v-stepper-items>
  </v-stepper>
</template>
<script>
import data1 from '@/views/Complaints.vue'
  export default {
 
    components:{
      data1
    },
    data () {
      return {
        e1: 0,
        id: 0,
        debug: false,
      }
    },
    created() {
            this.id = this.$route.params.id;
        },
    
  }
</script>