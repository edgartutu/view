<template>
    <v-app>
	   <v-card class="#dee9ff" style="background-color:#dee9ff;margin-top:0px" width="100%" height="100%">
      <v-content  class="mx-1 mb-1">
			  <router-view />  
      </v-content>
			 <v-snackbar
      v-model="snackbar"
      color="purple"
    >
   this is sys
    <v-btn @click="snackbar=false" class="purple white--text" >close</v-btn>
    </v-snackbar>
	 </v-card>
    </v-app>
 
</template>

<style lang="scss">
	@import "@/styles/index.scss";

	/* Remove in 1.2 */
	.v-datatable thead th.column.sortable i {
		vertical-align: unset;
	}
	.clock{
		font-size: 2px;
	}
</style>
<script>
import navbar from './components/DashViews/NavBar'
import Clock from 'vue-clock2';
import {
  
  mapState
} from 'vuex'
	// checks to see if auth jwt token is valid or has expired, if it gets back 401 error log out
	export default {
		components:{
    			 components: { Clock },
				},
				
				computed:{
					...mapState(['snackbar'])
				},

		





		created: function () {
			this.$http.interceptors.response.use( (response) => {
        return response;
      }, (error) => {
          if (401 === error.response.status) {
						if (this.$store.getters.authorized) {
							this.$store.dispatch('refreshtoken')
							}else {
              return Promise.reject(error);
          }
						
					} else {
              return Promise.reject(error);
          }
				});
		}
	};
</script>
