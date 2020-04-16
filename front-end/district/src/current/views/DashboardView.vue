<template>

  <v-content>
    
    <v-app
      id="dashboard-view"
      >
      <v-card class="rounded-card" >
      <core-filter />

      

      <core-drawer />

      <v-fade-transition mode="out-in">
        <router-view />
      </v-fade-transition>

      <core-footer v-if="$route.name !== 'Maps'" />
      </v-card>

    </v-app>
    
  </v-content>
  
</template>

<script>
export default {
  name: 'DashboardView',
  metaInfo () {
    return {
      title: 'FYP'
    }
  }
}
</script>

<style>
  .rounded-card{
    border-radius:50px;
    border-color: blueviolet;
}

</style>
