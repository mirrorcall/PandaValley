<template>
  <div>
  <div id="myList" class="myList">
    <ul>
      <li v-for="item in list" :key="item.id" @mouseenter="enter()" @mouseleave="leave()">
        <div class="wishlist" ><i class="custom-icon el-icon-star-off" v-show="seen"></i></div>
        <img :src="item.image" alt />
        <div class="group_icon">
          <i class="icon iconfont iconrenshu"><span>{{item.guests}}</span></i>
          <el-divider direction="vertical"></el-divider>
          <i class="icon iconfont iconchuang"><span>{{item.bedrooms}}</span></i>
          <el-divider direction="vertical"></el-divider>
          <i class="icon iconfont iconyushiyongpin"><span>{{item.bathrooms}}</span></i>
        </div>
        <h2>{{item.title}}</h2>
        <p>
          <el-row type="flex" justify="space-between">
            <el-col>
              <el-rate
                v-model="item.rating"
                disabled
                show-score
                text-color="#ff9900"
                score-template="{value}">
              </el-rate>
            </el-col >
            <el-col>
              ${{item.price}}/night
            </el-col>
          </el-row>
        </p>
      </li>
    </ul>
  </div>
    <!-- 分页
    <div class="pagination">
        <el-pagination
          background
          layout="prev, pager, next"
          :page-size="pageSize"
          :total="total"
          @current-change="currentChange"
        ></el-pagination>
    </div>
    分页END -->
  </div>
</template>

<script>

export default {
  name: 'Property_list',
  props: ['list'],
  data: function () {
    return {
      queryInfo: {
        query: '',
        pagenum: 1,
        pagesize: 10
      },
      seen: false,
      // the property list
      goodslist: [
        {
          product_id: '1',
          product_name: '1',
          product_title: 'zetland cozy room with 2 bedroom and 1 bathroom',
          product_picture: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
          product_price: '100',
          value: 3.7
        },
        {
          product_id: '2',
          product_name: '1',
          product_title: '1',
          product_selling_price: '1',
          product_picture: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
          product_price: '1',
          value: 3.8
        },
        {
          product_id: '3',
          product_name: '1',
          product_title: '1',
          product_selling_price: '1',
          product_picture: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
          product_price: '1',
          value: 4.0
        },
        {
          product_id: '4',
          product_name: '1',
          product_title: '1',
          product_selling_price: '1',
          product_picture: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
          product_price: '1',
          value: 3.7
        },
        {
          product_id: '5',
          product_name: '1',
          product_title: '1',
          product_selling_price: '1',
          product_picture: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
          product_price: '1',
          value: 3.7
        },
        {
          product_id: '6',
          product_name: '1',
          product_title: '1',
          product_selling_price: '1',
          product_picture: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
          product_price: '1',
          value: 3.7
        },
        {
          product_id: '7',
          product_name: '1',
          product_title: '1',
          product_selling_price: '1',
          product_picture: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
          product_price: '1',
          value: 3.7
        },
        {
          product_id: '8',
          product_name: '1',
          product_title: '1',
          product_selling_price: '1',
          product_picture: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
          product_price: '1',
          value: 3.7
        },
        {
          product_id: '9',
          product_name: '1',
          product_title: '1',
          product_selling_price: '1',
          product_picture: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
          product_price: '1',
          value: 3.7
        }
      ]
      // total number of the properties
      // total: 0,
      // pageSize: 8,
      // start_date: '',
      // end_date: '',
      // location: '',
      // number_of_people: 0
    }
  },
  // created () {
  //   this.start_date = this.$route.query.start_date
  //   this.end_date = this.$route.query.end_date
  //   this.location = this.$route.query.location
  //   this.number_of_people = this.$route.query.number_of_people
  //   this.getPropertylist()
  // },
  methods: {
    enter () {
      this.seen = true
    },
    leave () {
      this.seen = false
    },
    async getGoodlist () {
      const {data: res} = await this.$http.get('goods', {params: this.queryInfo})
      if (res.meta.status !== 200) {
        return this.$message.error('failure to get property list')
      }
      this.$message.success('success to get list')
      console.log(res.data)
      this.goodslist = res.data.goods
      this.total = res.data.total
    },
    handleSizeChange (newSize) {
      this.queryInfo.pagesize = newSize
      this.getGoodlist()
    },
    handleCurrentChange (newPage) {
      this.queryInfo.pagenum = newPage
      this.getGoodlist()
    }
  }
}

</script>

<style scoped>
  .box-card {
    width: 320px;
  }
  .time {
    font-size: 13px;
    color: #999;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
    width: 300px;
    height: 200px;
  }
  .wishlist {
    position: absolute; /*设置为绝对定位*/
    z-index:999;
    float:left;
    padding-left: 250px;
    padding-top:15px;
  }
  .custom-icon{
    font-size: 25px;
    margin-right: 0px;
  }
  .myList ul li {
    z-index: 1;
    float: left;
    width: 320px;
    height: 310px;
    padding: 10px 0px;
    margin: 0 0 14.5px 13px;
    background-color: white;
    -webkit-transition: all 0.2s linear;
    transition: all 0.2s linear;
    position: relative;
    list-style-type:none;
  }
  .myList ul li:hover {
    z-index: 2;
    -webkit-box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
    -webkit-transform: translate3d(0, -2px, 0);
    transform: translate3d(0, -2px, 0);
  }
  .myList ul li img {
    width: 260px;
    height: 200px;
    display: block;
    margin: 10px auto;
  }
  .myList ul li h2 {
    margin: 0px 10px;
    font-size: 14px;
    font-weight: 600;
    color: #333;
    text-align: center;
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
  }
  .group_icon{
    margin: 10px 10px 10px;
  }
  .myList ul li p {
    margin: 10px 10px 10px;
    text-align: center;
    color: #ff6700;
  }
  .myList ul li p .del {
    margin-left: 0.5em;
    color: #b0b0b0;
    text-decoration: line-through;
  }
  .myList #more {
    text-align: center;
    line-height: 280px;
  }
  .myList #more a {
    font-size: 18px;
    color: #333;
  }
  .myList #more a:hover {
    color: #ff6700;
  }
  .myList ul li .delete {
    position: absolute;
    top: 10px;
    right: 10px;
    display: none;
  }
  .myList ul li:hover .delete {
    display: block
  }
  .myList ul li .delete:hover {
    color: #ff6700;
  }
  .group_icon{
    margin-left: -100px;
  }
  .myList el-rate{
    position: relative;
    float: right;
  }

</style>
