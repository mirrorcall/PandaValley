import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/pages/home/Home'
import Signup from '@/pages/singup/Signup'
import Login from '@/pages/login/Login'
import Profile from '@/pages/profile/Profile'
import AddProperty from '@/pages/property/AddProperty'
import PropertyList from '@/pages/property/PropertyList'
import FilterProperty from '@/pages/property/FilterProperty'
import Resetpassword from '../pages/login/Resetpassword'
import MapView from '../components/MapView'

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
    },
    {
      path: '/profile',
      name: 'Profile',
      // meta: {
      //   requireAuth: true,
      // },
      component: Profile
    },
    {
      path: '/property_list',
      name: 'ProperList',
      component: PropertyList
    },
    {
      path: '/add_property',
      name: 'AddProperty',
      component: AddProperty
    },
    {
      path: '/filter',
      name: 'Filter',
      component: FilterProperty
    },
    {
      path: '/resetpassword',
      name: 'RestPassword',
      component: Resetpassword
    },
    {
      path: '/map_view',
      name: 'MapView',
      component: MapView
    }
  ]
})
