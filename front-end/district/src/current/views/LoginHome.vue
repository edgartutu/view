<!-- This is the file that will render any external pages you do not want inside the dash, like login form-->
<template>
 
  <v-app
    id="login-home"
    class="green lighten-4">
    <v-container
  fill-height
    fluid
    grid-list-xl>

    <transition mode="out-in">
      <router-view/>
    </transition>
    <v-spacer></v-spacer>
    <h2 class="teal--text">FINAL YEAR PROJECTS PLATFORM </h2>
  </v-container>
  </v-app>
 
</template>

<script>
export default {
}
</script>

<style>
</style>
