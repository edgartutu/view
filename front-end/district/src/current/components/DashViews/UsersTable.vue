<template>
	<div >
	
		<v-container >
			<v-card class="rounded-card">
                
                <v-card-text>
                    <h4 class="red--text">***Make sure your partner has confirmed your request before submiting.*** </h4>
                    <h4 class="red--text">***Only ignore if you have no project partner.***</h4>  
                    <v-text-field label="Project Reference Number" placeholder="Project Reference Number" v-model="project_ref"></v-text-field>
                    <v-text-field label="Title" placeholder="Title" v-model="title"></v-text-field>
                    <v-text-field label="Problem Statment" placeholder="Problem Statment" v-model="problem_statment"></v-text-field>
                    <v-text-field label="Methodology" placeholder="Methodology" v-model="methodology"></v-text-field>
                    <input type="file" name="Upload File" accept=".pdf" @change="uploadfile" />
                    <v-btn flat class="green my-5" @click="postproposal()">Submit</v-btn>

                </v-card-text>
			</v-card>
			
		</v-container>
		
	</div>
	
</template>
<script>
import axios from 'axios'
    export default {
        data() {
            return {
      
                project_ref: "",

                title: "",
                problem_statment: "",
                methodology: "",
                file: null,
                reg_nox: ""
            }
        },
        methods: {

            postproposal() {
                this.reg_nox = localStorage.getItem('user')
                const fd = new FormData();
                fd.append('foo', 'bar')
                fd.append('file', this.file)
                fd.append('title', this.title)
                fd.append('problem_statement', this.problem_statment)
                fd.append('methodology', this.methodology)
                fd.append('proposal_ref', this.project_ref)
                fd.append('reg_nox',this.reg_nox)

                axios.post("http://127.0.0.1:5000/postproposals", fd).then(response => {
                    console.log(response) ;
                    window.location.reload()
                })
                
            },
            uploadfile(event) {
                this.file = event.target.files[0]
            }
        }
}
</script>
<style>
.rounded-card{
    border-radius:50px;
}
    
</style>
