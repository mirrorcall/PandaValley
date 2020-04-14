<template>
  <div class="home">
    <search></search>
    <h1>Homes guests love</h1>
    <PropertyList :list="list" :start_date="start_date" :end_date="end_date"></PropertyList>

<!--    <advertisement></advertisement>-->
  </div>
</template>

<style scoped>
  .home {
  }
</style>

<script>
import Search from '../../components/Search'
// import Advertisement from '../../components/Advertisement'
import PropertyList from '../property/PropertyList'
export default {
  name: 'Home.vue',
  components: {
    PropertyList,
    Search
    // Advertisement
  },
  data () {
    return {
      list: '',
      start_date: '',
      end_date: ''
    }
  },
  created () {
    let day1 = new Date()
    day1.setTime(day1.getTime())
    let s1 = day1.getDate() + '/' + (day1.getMonth() + 1) + '/' + day1.getFullYear()
    let day2 = new Date()
    day2.setTime(day2.getTime() + 24 * 60 * 60 * 1000)
    let s2 = day2.getDate() + '/' + (day2.getMonth() + 1) + '/' + day1.getFullYear()
    this.start_date = s1
    this.end_date = s2
    this.$axios.get('/api/recommended')
      .then((response) => {
        this.list = response.data.body
      })
      .catch(function (error) {
        console.log(error)
      })
  }
}
</script>
