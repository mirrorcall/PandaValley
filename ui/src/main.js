// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store/index'
import Element from 'element-ui'
import locale from 'element-ui/lib/locale/lang/en'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'
import qs from 'qs'
import './assets/icon/iconfont.css' // import icon font
import './assets/micon/iconfont.css'
import * as VueGoogleMaps from 'vue2-google-maps'
import './assets/font/iconfont.css' // import icon font

Vue.use(Element, { locale })
Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyDbbgvDvB4iowCBQRxei4ET9CickmaU7PY',
    libraries: 'places',
    installComponents: true
  }
})

Vue.prototype.$axios = axios
// register the default baseURL for axios
axios.defaults.baseURL = 'http://127.0.0.1:8000'

Vue.prototype.$qs = qs

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  axios,
  store,
  components: { App },
  template: '<App/>'
})
