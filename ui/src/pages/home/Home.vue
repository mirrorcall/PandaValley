<template>
  <div class="home">
    <search></search>
    <advertisement></advertisement>
    <page-footer></page-footer>
  </div>
</template>

<style scoped>
  .home {
  }
</style>

<script>
import Search from '../../components/Search'
import Advertisement from '../../components/Advertisement'
import PageFooter from '../../components/PageFooter'
export default {
  name: 'Home.vue',
  components: {
    PageFooter,
    Search,
    Advertisement
  },
  data () {
    return {
    }
  }
}
</script>
