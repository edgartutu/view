<template>
	<div >
		<v-flex>
		<v-container>
			
       <material-card 
        title="Updated Methodology"
        color="red lighten-3"
        >
			
				<div class="font-weight-bold">New Methodology
				<v-text-field  placeholder="Methodology" v-model="methodology"></v-text-field>
        </div>
				<v-btn flat class="teal" @click="update">Submit</v-btn>
				
			
      </material-card>
		</v-container>
    </v-flex>
		
	</div>

</template>
<script>
import axios from 'axios'
export default {
	
	data(){
        return {
            methodology: '',
            user: '',

		}
	},
        methodes: {
            update() {
                this.user = localStorage.getItem('user')
                axios.post('http://127.0.0.1:5000/UpdateMethodology', {
                    'reg_no': this.user, 'methodology': this.methodology
                }).then(window.location.reload())
            }
        }

}
</script>