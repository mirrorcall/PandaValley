<template>
  <div class="home">
    <search></search>
    <advertisement></advertisement>
  </div>
</template>

<style scoped>
  .home {
  }
</style>

<script>
import Search from '../../components/Search'
import Advertisement from '../../components/Advertisement'
export default {
  name: 'Home.vue',
  components: {
    Search,
    Advertisement
  },
  data () {
    return {
    }
  }
}
</script>
