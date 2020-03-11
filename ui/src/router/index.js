import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/pages/home/Home'
import Signup from '@/pages/singup/Signup'
import Login from '@/pages/login/Login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/signup',
      name: 'Signup',
      component: Signup
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ]
})
