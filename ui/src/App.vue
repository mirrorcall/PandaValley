<template>
  <div id="app">
    <toolbar></toolbar>
<!--    <router-view/>-->
    <keep-alive>
      <router-view v-if="$route.meta.keepAlive" class="router-view">
      </router-view>
    </keep-alive>
    <router-view v-if="!$route.meta.keepAlive" class="router-view" ></router-view>
  </div>
</template>

<script>
import Toolbar from './components/Toolbar'
export default {
  name: 'App',
  components: {Toolbar}
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 10px;
  margin-left: -10px;
  margin-right: -10px;
}
</style>
