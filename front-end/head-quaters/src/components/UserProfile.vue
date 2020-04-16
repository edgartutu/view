<template>
  <v-container
    fill-height
    fluid
    grid-list-xl>
    <v-layout
      justify-center
      wrap
    > 
      <v-flex
       md12
      >
  
            <v-expansion-panel popout>
              <v-expansion-panel-content v-for="proposal in proposals" :key="proposal.reg_no">
                <template v-slot:header>
               <div>{{proposal.title}}</div>
            </template>
                <v-card-text class="px-16">
                    <h4 class="font-weight-bold">Students</h4>
                    <div>{{proposal.reg_no}}</div>
                    <h4 class="font-weight-bold">Title</h4>
                    <div>{{proposal.title}}</div>
                    <h4 class="font-weight-bold">Problem statment</h4>
                    <div>{{proposal.problem_statment}}</div>
                    <h4 class="font-weight-bold">Abstract</h4>
                    <div>{{proposal.abstract}}</div>
                    <h4 class="font-weight-bold">File</h4>
                    <div>{{proposal.file}}</div>
                    <div>{{proposal.status}}</div>
                    <v-text-field label="Supervisor" placeholder="Supervisor" v-model="supervisor"></v-text-field>
                    <v-text-field label="Email" placeholder="Emain" v-model="email"></v-text-field>
                    <v-text-field label="Comment" placeholder="Comment" v-model="comment"></v-text-field>
                    <v-btn class="green" @click="approve">Approve</v-btn>
                    <v-btn class="red" @click="rejected">Reject</v-btn>

                </v-card-text>
              </v-expansion-panel-content>
            </v-expansion-panel>
      
    
          
        
      </v-flex>
      
      <v-flex
        xs12
        md4
      >
        
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios'
export default {
  components: {
 
  },
    data () {
        return {
            proposals: {},
            supervisor: "",
            email: "",
            comment: "",
            status: "Approved",
            status2: "Rejected"

        }
    
        },
        mounted() {
             this.prop();
            this. approve();
            this.rejected();
            this.intervalFetchData()
        },
        methods: {
          prop(){
              axios.get("https://aaomach.pythonanywhere.com/pendingproposal").then(response => {
                this.proposals = response.data
            })

          },
            approve() {
                axios.post("https://aaomach.pythonanywhere.com/approve", {
                    "reg_no": 1234, "supervisor": this.supervisor, "email": this.email,
                    "comment": this.comment, "status": this.status
                })
            },
            rejected() {
                console.log(this.proposals.reg_no)
                axios.post("https://aaomach.pythonanywhere.com/approve", {
                    "reg_no": 1234,
                    "comment": this.comment, "status": this.status2
                })
            },
             intervalFetchData: function () {
            setInterval(() => { 
                this.prop();
                this. approve();
                this.rejected();

                }, 3000);    
        }
        }
}
</script>
