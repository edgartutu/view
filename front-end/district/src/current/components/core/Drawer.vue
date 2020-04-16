<template>
  <v-card class="rounded-card">
  <v-navigation-drawer
    app
    v-model="drawer"
    :mini-variant.sync="mini"
    hide-overlay
    stateless
    class="teal darken-2"
    mobile-break-point="991"
    width="260"
  >
    <v-toolbar flat class="teal darken-2">
      <v-list class="pa-0">
        <v-list-tile avatar>
          <v-list-tile-avatar>
            <img src="https://randomuser.me/api/portraits/men/85.jpg">
          </v-list-tile-avatar>

          <v-list-tile-content>
            <v-list-tile-title class="orange--text">{{user}}</v-list-tile-title>
          </v-list-tile-content>

          <v-list-tile-action>
            <v-btn
            fab dark color ="teal"
              icon
              @click.stop="mini = !mini"
            >
              <v-icon dark>chevron_left</v-icon>
            </v-btn>
          </v-list-tile-action>
        </v-list-tile>
      </v-list>
    </v-toolbar>

    <v-list class="pt-0" dense>
      <v-divider></v-divider>

       <v-list-tile
          v-for="(link, i) in links"
          :key="i"
          :to="link.to"
          :active-class="small"
          avatar
          class="v-list-item"
          
        >
          <v-list-tile-action >
            <v-icon >{{ link.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-title 
            class="white--text"
            v-text="link.text"
          />
        </v-list-tile>
    </v-list>
  </v-navigation-drawer>
  </v-card>
</template>
  


<script>
// Utilities
import {
  mapMutations,
  mapState
} from 'vuex'

export default {
  data: () => ({
    user: '',
    logo: require('@/assets/img/redditicon.png'),
    links: [
      {
        to: '/dashboards',
        icon: 'mdi-view-dashboard',
        text: 'Dashboard'
      },
      {
        to: '/dashboards/user-profile',
        icon: 'mdi-account',
        text: 'Posted Proposals'
      },
      {
        to: '/dashboards/table-list',
        icon: 'mdi-clipboard-outline',
        text: 'View Projects'
      },
      {
        to: '/dashboards/user-tables',
        icon: 'mdi-table-edit',
        text: 'Submit Proposal'
      },
      {
        to: '/dashboard/stypography',
        icon: 'mdi-format-font',
        text: 'Update Methodology'
      },
      {
        to: '/dashboards/rejected',
        icon: 'folder',
        text: 'Previous Projects'
      },
      {
        to: '/dashboards/notifications',
        icon: 'report',
        text: 'Progress Report'
      },
       {
        to: '/dashboards/logout',
        icon: 'mdi-power',
        text: 'Log out'
      }
    ],
    responsive: false,
    drawer:true,
    mini: true,
    right: null
  }),
  computed: {
    ...mapState('app', ['image', 'color']),
        inputValue: {
      get () {
        return this.$store.state.app.drawer

      },
      set (val) {
        this.setDrawer(val)
      },
    },
    items () {
      return this.$t('Layout.View.items')
    }
  },
        mounted() {
      this.user = localStorage.getItem('user')
    this.onResponsiveInverted()
    window.addEventListener('resize', this.onResponsiveInverted)
  },
  beforeDestroy () {
    window.removeEventListener('resize', this.onResponsiveInverted)
  },
  methods: {
    ...mapMutations('app', ['setDrawer', 'toggleDrawer']),
    onResponsiveInverted () {
      if (window.innerWidth < 991) {
        this.responsive = true
      } else {
        this.responsive = false
      }
    }
  }
}
</script>

<style lang="scss">
  .rounded-card{
    border-radius:50px;
}
  #app-drawer {
    .v-list__tile {
      border-radius: 4px;

      &--buy {
        margin-top: auto;
        margin-bottom: 17px;
      }
    }

    .v-image__image--contain {
      top: 9px;
      height: 60%;
    }

    .search-input {
      margin-bottom: 30px !important;
      padding-left: 15px;
      padding-right: 15px;
    }
  }
</style>
