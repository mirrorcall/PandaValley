<template>
  <div class="goods" id="goods" name="goods">
    <!-- 分类标签 -->
    <div class="filter">
      <el-row  :gutter="3" type="flex" justify="space-between">
        <el-col :span="8" offset="1">
          <el-date-picker
              v-model="date"
              type="daterange"
              range-separator="To"
              format="dd/MM/yyyy"
              value-format="dd/MM/yyyy"
              :start-placeholder= start_date
              :end-placeholder= end_date :picker-options="pickerOptions" :default-value="[d1,d2]" @change="dateChange">
          </el-date-picker>
        </el-col>
        <el-col :span="7">
          <el-dropdown :hide-on-click="false" placement="bottom">
            <el-button round type="primary">
             {{number_of_people}} Guests<i class="el-icon-arrow-down el-icon--right"></i>
            </el-button>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>
                <i class="icon iconfont iconrenshu"></i><el-input-number v-model="number_of_people" @change="handleChange" :min="1" :max="10"></el-input-number>
              </el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </el-col>
        <el-col :span="7">
          <el-dropdown :placement="bottom" @command = "handleCommand">
            <el-button round type="primary">
              Type: {{type | capitalize}}<i class="el-icon-arrow-down el-icon--right"></i>
            </el-button>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item command="All">
                All
              </el-dropdown-item>
              <el-dropdown-item command="Apartment">
                Apartment
              </el-dropdown-item>
              <el-dropdown-item command="Unit">
                Unit
              </el-dropdown-item>
              <el-dropdown-item command="House">
                House
              </el-dropdown-item>
              <el-dropdown-item command="Studio">
                Studio
              </el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </el-col>
        <el-col :span="6">
          <el-dropdown :hide-on-click="false" placement="bottom">
            <el-button round type="primary">
              Rooms<i class="el-icon-arrow-down el-icon--right"></i>
            </el-button>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>
                <div>bedrooms</div>
                <el-input-number v-model="bedrooms" @change="handleChange" :min="1" :max="10" size="small"></el-input-number>
              </el-dropdown-item>
              <el-dropdown-item>
                <div>bathrooms</div>
                <el-input-number v-model="bathrooms" @change="handleChange" :min="1" :max="10" size="small"></el-input-number>
              </el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </el-col>
        <el-col :span="6">
          <el-dropdown :hide-on-click="false" placement="bottom">
            <el-button round type="primary">
              Price<i class="el-icon-arrow-down el-icon--right"></i>
            </el-button>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>
                <div>min</div>
                <el-input-number v-model="min_price" @change="handleChange" :min="0" :max="10000" size="small"></el-input-number>
              </el-dropdown-item>
              <el-dropdown-item>
                <div>max</div>
                <el-input-number v-model="max_price" @change="handleChange" :min="0" :max="10000" size="small"></el-input-number>
              </el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </el-col>
        <el-col :span="6">
          <el-dropdown :hide-on-click="false" placement="bottom" @command = "handleCommand2">
            <el-button round type="primary">
              Sort<i class="el-icon-arrow-down el-icon--right"></i>
            </el-button>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item command="0">
                Recommended
              </el-dropdown-item>
              <el-dropdown-item command="+">
                Price: Low to High
              </el-dropdown-item>
              <el-dropdown-item command="-">
                Price: High to Low
              </el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </el-col>
        <el-col>
          <el-button type="primary" plain @click="handlesearch">Apply</el-button>
        </el-col>
      </el-row>
    </div>
    <!-- 主要内容区 -->
    <div class="main">
      <div class="list">
        <PropertyList :list="product" :start_date="start_date" :end_date="end_date" v-if="total>0"></PropertyList>
        <div v-else class="none-product">no result</div>
      </div>
      <div style=""></div>
      <!-- 分页 -->
      <div class="pagination">
        <el-pagination
          background
          layout="prev, pager, next"
          :page-size="pageSize"
          :total="total"
          @current-change="currentChange"
        ></el-pagination>
      </div>
      <!-- 分页END -->
    </div>
    <!-- 主要内容区END -->
  </div>
</template>
<script>
import PropertyList from './PropertyList'
export default {
  components: {PropertyList},
  data () {
    return {
      pickerOptions: {
        disabledDate: function (time) {
          return time.getTime() < Date.now() - 8.64e7
        }
      },
      date: '',
      d1: '',
      d2: '',
      start_date: '',
      end_date: '',
      number_of_people: '',
      min_price: 0,
      max_price: 10000,
      type: 'All',
      bedrooms: 1,
      bathrooms: 1,
      order: '',
      product: '', // 商品列表
      productList: '',
      total: 0, // 商品总量
      pageSize: 8, // 每页显示的商品数量
      page: 1, // 当前页码
      search: '' // 搜索条件
    }
  },
  created () {
    // 获取列表
    this.start_date = this.$route.query.start_date
    this.end_date = this.$route.query.end_date
    this.type = this.$route.query.property_type
    this.d1 = this.start_date.split('/')[1] + '/' + this.start_date.split('/')[0] + '/' + this.start_date.split('/')[2]
    this.d2 = this.end_date.split('/')[1] + '/' + this.end_date.split('/')[0] + '/' + this.end_date.split('/')[2]
    this.location = this.$route.query.location
    this.number_of_people = this.$route.query.number_of_people
    // this.getPropertylist()
    this.getProductBySearch()
  },
  filters: {
    capitalize: function (value) {
      if (!value) return ''
      value = value.toString()
      return value.charAt(0).toUpperCase() + value.slice(1)
    }
  },
  methods: {
    // 返回顶部
    dateChange () {
      // this.start_date = new Date(this.date[0]).toLocaleDateString('en-AU')
      // this.end_date = new Date(this.date[1]).toLocaleDateString('en-AU')
      this.start_date = this.date[0]
      this.end_date = this.date[1]
    },
    handleCommand (command) {
      this.type = command
    },
    handleCommand2 (command) {
      if (command === '+') {
        this.order = 'price'
      }
      if (command === '-') {
        this.order = '-price'
      }
    },
    handlesearch () {
      this.getProductBySearch()
    },
    getPropertylist () {
      this.$axios.get('/api/search_property?start_date=' + this.start_date + '&end_date=' + this.end_date + '&location=' + this.location + '&number_of_people=' + this.number_of_people)
        .then((response) => {
          this.product = response.data.body
          this.total = response.data.total
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    backtop () {
      const timer = setInterval(function () {
        const top = document.documentElement.scrollTop || document.body.scrollTop
        const speed = Math.floor(-top / 5)
        document.documentElement.scrollTop = document.body.scrollTop =
            top + speed
        if (top === 0) {
          clearInterval(timer)
        }
      }, 20)
    },
    // 页码变化调用currentChange方法
    currentChange (currentPage) {
      this.page = currentPage
      this.getProductBySearch()
      this.backtop()
    },
    // 通过搜索条件向后端请求商品数据
    getProductBySearch () {
      this.search = 'start_date=' + this.start_date + '&end_date=' + this.end_date + '&location=' + this.location + '&number_of_people=' + this.number_of_people
      if (this.min_price > 0) {
        this.search = this.search + '&min_price=' + this.min_price
      }
      if (this.max_price < 10000) {
        this.search = this.search + '&max_price=' + this.max_price
      }
      if (this.bedrooms !== '') {
        this.search = this.search + '&bedrooms=' + this.bedrooms
      }
      if (this.bathrooms !== '') {
        this.search = this.search + '&bathrooms=' + this.bathrooms
      }
      if (this.order !== '') {
        this.search = this.search + '&order=' + this.order
      }
      if (this.$store.getters.getStorage) {
        this.search = this.search + '&email=' + this.$store.getters.getStorage
      }
      if (this.type !== 'All') {
        this.search = this.search + '&property_type=' + this.type
      }
      // type
      this.$axios
        .get('/api/search_property?' + this.search + '&page=' + this.page)
        .then(res => {
          this.product = res.data.body
          this.product.forEach(function (item) {
            if (item['rating'] === '5.00') {
              item['rating'] = '5'
            }
          })
          this.total = res.data.total
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>

<style scoped>
  .goods {
    background-color: #f5f5f5;
    padding-top: 20px;
  }
  /* 面包屑CSS */
  .el-tabs--card .el-tabs__header {
    border-bottom: none;
  }
  .goods .breadcrumb {
    height: 50px;
    background-color: white;
  }
  .goods .breadcrumb .el-breadcrumb {
    width: 1225px;
    line-height: 30px;
    font-size: 16px;
    margin: 0 auto;
  }
  /* 面包屑CSS END */
  /* 分类标签CSS */
  .goods .nav {
    background-color: white;
  }
  .goods .nav .product-nav {
    width: 1225px;
    height: 40px;
    line-height: 40px;
    margin: 0 auto;
  }
  .nav .product-nav .title {
    width: 50px;
    font-size: 16px;
    font-weight: 700;
    float: left;
  }
  /* 分类标签CSS END */
  /* 主要内容区CSS */
  .goods .main {
    margin: 0 auto;
    max-width: 1400px;
  }
  .goods .main .list {
    min-height: 650px;
    padding-top: 14.5px;
    margin-left: -13.7px;
    overflow: auto;
  }
  .goods .main .pagination {
    height: 50px;
    text-align: center;
  }
  .goods .main .none-product {
    color: #333;
    margin-left: 13.7px;
  }
  /* 主要内容区CSS END */
</style>
