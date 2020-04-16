<template>
    <v-app>
	   <v-card class="#dee9ff" style="background-color:#dee9ff;margin-top:0px" width="100%" height="100%">
      <v-content  >
			  <router-view />  
      </v-content>
	 </v-card>
    </v-app>
 
</template>

<style lang="scss">
	@import "@/styles/index.scss";

	/* Remove in 1.2 */
	.v-datatable thead th.column.sortable i {
		vertical-align: unset;
	}
</style>
<script>
import navbar from './components/DashViews/NavBar'
	// checks to see if auth jwt token is valid or has expired, if it gets back 401 error log out
	export default {
		components:{
    			
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
