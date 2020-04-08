<template>
  <div>
    <div><h2>My Wishlist</h2></div>
    <div id="myList" class="myList">
      <ul>
        <li v-for="(item,index) in list" :key="item.id" @mouseenter="enter()" @mouseleave="leave()">
          <div class="wishlist">
            <el-button type="danger" icon="el-icon-delete" size="mini" @click="deletewishlist(item,index)"></el-button>
          </div>
          <img v-if="imageUrl!==''" :src="item.image" class="image" alt="" @click="gotoDetails(item)">
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
  name: 'Wishlist',
  data () {
    return {
      list: ''
    }
  },
  created () {
    this.$axios
      .get('/api/show_wishlist?email=' + this.$store.getters.getStorage)
      .then(res => {
        this.list = res.data.body
        this.total = res.data.total
      })
      .catch(function (error) {
        console.log(error)
      })
  },
  methods: {
    deletewishlist (item, index) {
      let data = this.$qs.stringify({
        wishlist_id: item.wishlist_id
      })
      this.$axios.post('/api/delete_wishlist', data)
        .then((response) => {
          if (response.data.code === 0) {
            this.$message('Successfully deleted')
            this.list.splice(index, 1)
          } else {
            this.$message.error('error')
          }
        })
        .catch((res) => {
          console.log('error ', res)
        })
    }
  }
}
</script>

<style scoped>
  .icon {
    width: 18px;
    height:18px;
    fill: currentColor;
    overflow: hidden;
    margin: 5px;
  }
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
    padding-left: 240px;
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
