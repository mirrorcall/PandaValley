<template>
  <div>
<!--    <div class="recommend">-->
<!--      <h2>Recommended for you</h2>-->
<!--      <div class="carousel">-->
<!--        <el-carousel :interval="4000" type="card" height="200px">-->
<!--          <el-carousel-item v-for="item in 6" :key="item">-->
<!--            <h3 class="medium">{{ item }}</h3>-->
<!--          </el-carousel-item>-->
<!--        </el-carousel>-->
<!--      </div>-->
<!--    </div>-->
    <div class="recommend">
      <h2>Recommended the best for you</h2>
      <div class="carousel">
        <el-carousel :interval="4000" type="card" height="420px">
          <el-carousel-item v-for="(item, i) in bestTen" :key="i">
            <div class="carousel-explain"  @click="goDetails(item)">
              <el-image
                class="prop-overview"
                :src="item.image"
                fir="contain"
                style="height: 320px"></el-image>
            </div>
            <div class="explian-text" style="text-align: center">
              <div style="font-weight: 700; font-size: 17px">{{ item.title | simplify }}</div>
              <div style="font-weight: 300; color: #949494">
                Sleeps
                {{ item.guests }}
                |
                {{ item.bedrooms }}
                BR
                |
                {{ item.bathrooms }}
                BA
              </div>
              <div style="width: 170px; height: auto; text-align: center; margin: auto">
                <div style="font-weight: 700; font-size: 17px; float: left; height: auto;">
                  AU$
                  {{ item.price }}
                </div>
                <div style="font-size: 13px; float: left; height: auto;">&nbsp;avg/night</div>
                <div style="clear: both"></div>
              </div>
            </div>
          </el-carousel-item>
        </el-carousel>
      </div>
    </div>
    <div class="recommend">
      <h2>Find spaces that suit your style</h2>
      <div class="carousel">
        <el-carousel :interval="4000" type="card" height="300px">
          <el-carousel-item
            v-for="(item, i) in propOverview"
            :key="i">
            <div class="carousel-explain" @click="goList(item)">
              <el-image
                class="prop-overview"
                :src="item.url"
                fit="fill"></el-image>
              <div class="explain-text">
                <el-row>
                  <el-col :span="12">
                    <div class="explain-text-left">{{ item.property_type | capitalize | puralise }}</div>
                  </el-col>
                  <el-col :span="12">
                    <div class="explain-text-right">
                      View
                      {{ item.total }}
                      {{ item.property_type | puralise }}
                    </div>
                  </el-col>
                </el-row>
              </div>
            </div>
          </el-carousel-item>
        </el-carousel>
      </div>
    </div>
    <div style="padding-bottom: 100px"></div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      bestTen: '',
      propOverview: '',
      location: '',
      number_of_people: ''
    }
  },
  created () {
    this.$axios.get('/api/recommended_best')
      .then((response) => {
        if (response.data.code === 0) {
          this.bestTen = response.data.body
        }
      })
      .catch(function (error) {
        console.log(error)
      })

    this.$axios.get('/api/property_overview')
      .then((response) => {
        if (response.data.code === 0) {
          let base = 'https://pandavalley-media.s3-ap-southeast-2.amazonaws.com/media/sample_'
          let format = '.jpg'
          this.propOverview = response.data.body
          for (let i = 0; i < this.propOverview.length; i++) {
            switch (this.propOverview[i].property_type) {
              case 'unit':
                this.propOverview[i].url = 'unit'
                break
              case 'apartment':
                this.propOverview[i].url = 'apartment'
                break
              case 'house':
                this.propOverview[i].url = 'house'
                break
              case 'studio':
                this.propOverview[i].url = 'studio'
                break
            }
            this.propOverview[i].url = base + this.propOverview[i].url + format
          }
        }
      })
      .catch(function (error) {
        console.log(error)
      })
  },
  filters: {
    capitalize: function (value) {
      if (!value) return ''
      value = value.toString()
      return value.charAt(0).toUpperCase() + value.slice(1)
    },
    puralise: function (value) {
      if (!value) return ''
      value = value.toString()
      return value + 's'
    },
    simplify: function (value) {
      if (!value) return ''
      value = value.replace(/[`~!@#$%^&*()_|+\-=?;:'",.<>{}[]\\]/gi, '')
      value = value.toString().split(' ')
      return value.slice(0, 4).join(' ')
    }
  },
  methods: {
    goDetails (item) {
      let day1 = new Date()
      day1.setTime(day1.getTime())
      let s1 = day1.getDate() + '/' + (day1.getMonth() + 1) + '/' + day1.getFullYear()
      let day2 = new Date()
      day2.setTime(day2.getTime() + 24 * 60 * 60 * 1000)
      let s2 = day2.getDate() + '/' + (day2.getMonth() + 1) + '/' + day1.getFullYear()
      this.$router.push(
        {
          path: '/detail',
          query:
            {
              property: item.property_id,
              start_date: s1,
              end_date: s2,
              email: this.$store.getters.getStorage
            }
        }
      )
    },
    goList (item) {
      let day1 = new Date()
      day1.setTime(day1.getTime())
      let s1 = day1.getDate() + '/' + (day1.getMonth() + 1) + '/' + day1.getFullYear()
      let day2 = new Date()
      day2.setTime(day2.getTime() + 24 * 60 * 60 * 1000)
      let s2 = day2.getDate() + '/' + (day2.getMonth() + 1) + '/' + day1.getFullYear()
      this.$router.push(
        {
          path: '/filter',
          query:
            {
              property_type: item.property_type,
              start_date: s1,
              end_date: s2,
              location: '',
              number_of_people: ''
            }
        }
      )
    }
  }
}

</script>

<style scoped>
.recommend {
  margin-top: 50px;
  margin-left: 10%;
  text-align: left;
}
.carousel {
  padding-top: 20px;
  width: 95%;
}
.el-carousel__item span {
  color: #475669;
  font-size: 40px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}
>>> .el-carousel__arrow {
  margin-top: -40px;
}
.prop-overview {
  width: 100%;
  height: 275px;
}
.explain-text-left {
  font-weight: 600;
  text-align: left;
}
.explain-text-right {
  color: #777777;
  font-size: 14px;
  font-weight: 300;
  text-align: right;
}
</style>
