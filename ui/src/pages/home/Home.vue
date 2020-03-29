<template>
  <div class="home">
    <search></search>
  </div>
</template>

<style scoped>
  .home {
    margin-top: 100px;
    margin-left: 40%;
    margin-right: 60%;
  }
</style>

<script>
import Search from '../../components/Search'
export default {
  name: 'Home.vue',
  components: {
    Search
  },
  data () {
    return {
    }
  }
}
</script>
