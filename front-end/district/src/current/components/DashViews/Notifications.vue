<template>
	<div >
    <v-container
	 fill-height
    fluid
    grid-list-xl>
		
    <v-layout
     >
      
    
    <v-flex xs12
        md10 >

		
			
			<v-card class="rounded-card" >
				<v-flex >
				</v-flex>
				<v-flex xs12 sm4 text-xs-center>
                    <v-text-field label="Comment" placeholder="comment" v-model="comment"></v-text-field>
                    <input type="file" name="Upload File"  @change="uploadfile" />
				
					<v-btn flat class="teal" @click="submit()">Submit</v-btn>
					</v-flex><br>
					<v-card-text v-for="repo in reports" :key="repo.reg_no">
					 <div >{{repo.files}}</div>
					 <div >{{repo.datestamp}}</div>

				</v-card-text>
				
			</v-card><br>
			
			
			
		</v-flex>
     </v-layout>
     </v-container>
  
		
	</div>
	
</template>

<script>
import axios from 'axios'
    import { Script } from 'vm'
    export default {
        data() {
            return {
                reports: {},
                file: null,
                reg_no: "",
                comment: "",
            }
        },
        methods: {
            submit() {
                this.reg_no = localStorage.getItem('user')
                const fd = new FormData();
                fd.append('foo', 'bar')
                fd.append('file', this.file)
                fd.append('reg_no', this.reg_no)
                fd.append('comment', this.comment)
                axios.post("http://127.0.0.1:5000/postprogressreport", fd)
                    .then(response => {
                        console.log(response)
                        window.location.reload()
                    })
            },
            uploadfile() {
                this.file = event.target.files[0]
            }

        }

}
</script>
<style >

 .rounded-card{
    border-radius:50px;
}
	
</style>