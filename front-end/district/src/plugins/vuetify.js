import Vue from 'vue'
import Vuetify from 'vuetify'
import theme from './theme'
import 'vuetify/dist/vuetify.min.css'
import '@mdi/font/css/materialdesignicons.css'

// This is here just in case you prefer to have all your plugins in a folder like this, otherwise its currently unused

Vue.use(Vuetify, {
  iconfont: 'mdi',
  theme:{
    primary: '#3ae01f',
    secondary: '#424242',
    accent: '#82B1FF',
    error: '#FF5252',
    info: '#31b81c',
    success: '#4CAF50',
    warning: '#FFC107'
  }
})
