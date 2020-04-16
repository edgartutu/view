/**
 * Define all of your application routes here
 * for more information on routes, see the
 * official documentation https://router.vuejs.org/en/
 */
import store from '../store'
export default [
  {
    path: '*',
    meta: {
      name: '',
      requiresAuth: false
    },
    redirect: {
      path: '/dashboard'
    }
  },
  // This  allows you to have pages apart of the app but no rendered inside the dash
   {
     path: '/',
     meta: {
       name: '',
       requiresAuth: false
     },
  
    
     component: () =>
       import(/* webpackChunkName: "routes" */ `@/views/Login.vue`),
    // redirect if already signed in
     beforeEnter: (to, from, next) => {
       if (store.getters.authorized) {
         next('/dashboard')
        
       }
     
      
       else {
           next()
       }
     },
     children: [
       {
         path: '/',
         component: () => import(`@/views/Login.vue`)
       }
     ]
   },
  // add any extra routes that you want rendered in the dashboard as a child below. Change toolbar names here
  {
    path: '/dashboard',
    meta: {
      name: 'Dashboard',
      requiresAuth: true
    },
    component: () => import(`@/views/DashboardView.vue`),
    
  },
  {
    path: '/projects',
    meta: {
      name: 'Complaints',
      requiresAuth: true
    },
    component: () => import(`@/views/Complaints.vue`),
  },
  {
    path: '/team',
    meta: {
      name: 'Registry',
      requiresAuth: true
    },
    component: () => import(`@/views/Team.vue`),
  },
  {
    path: '/resolve/:userData',
    name: 'Stepperview',
    meta: {
      
   
      requiresAuth: true
    },
    component: () => import(`@/views/Stepperview.vue`),
    
  },
  {
    path: '/resolves/:userData',
    name: 'Step',
    meta: {
      
   
      requiresAuth: true
    },
    component: () => import(`@/views/Step.vue`),
    
  },
  {
    path: '/Login',
    name: 'login',
    meta: {
      
   
      requiresAuth: false
    },
    component: () => import(`@/views/Login.vue`),
    
  },
  {
    path: '/register',
    name: 'register',
    meta: {
      
   
      requiresAuth: false
    },
    component: () => import(`@/views/Register.vue`),
    
  },
  {
    path: '/time',
    name: 'schedule',
    meta: {
      
   
      requiresAuth: true
    },
    component: () => import(`@/views/Schedule.vue`),
    
  },
  {
    path: '/reports',
    name: 'reports',
    meta: {
      
   
      requiresAuth: true
    },
    component: () => import(`@/views/Comps.vue`),
    
  },
  {
    path: '/resolved',
    name: 'resolved',
    meta: {
      
   
      requiresAuth: true
    },
    component: () => import(`@/views/Stored.vue`),
    
  },
  {
    path: '/manager',
    name: 'manager',
    meta: {
      
   
      requiresAuth: false
    },
    component: () => import(`@/views/Manager.vue`),
    
  },
  {
    path: '/allcompaints/:userDeta',
    name: 'allcompaints',
    meta: {
      
   
      requiresAuth: true
    },
    component: () => import(`@/views/Allcompaints.vue`),
    
  }



  
]
