<!-- This is the file that will render any external pages you do not want inside the dash, like login form-->
<template>
  <v-app
    id="login-home"
    class="purple lighten-2">

    <transition mode="out-in">
      <router-view/>
    </transition>

  </v-app>
</template>

<script>
export default {
}
</script>

<style>
</style>
