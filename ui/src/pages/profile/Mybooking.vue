<template>
  <div class="mybooking">
    <h1 style="text-align: center">My Booking</h1>
    <el-card shadow="hover" v-for="(item,index) in list" :key="item.id">
      <el-row>
        <el-col :span="5">
          <el-image
            style="width: 300px; height: 200px; margin: 10px;"
            :src="item.image"
            :fit="fill"></el-image>
        </el-col>
        <el-col :span="16" offset="3">
          <el-row>
            <h2>{{item.title}}</h2>
          </el-row>
          <el-row>
            <i class="el-icon-location"></i>
            address
          </el-row>
          <el-row type="flex" class="row-bg" justify="space-between">
            <el-col :span="10"><p class="dates">From {{item.start_date}} To  {{item.end_date}}</p></el-col>
            <el-col :span="6"><p class="dates">{{item.days}} nights</p></el-col>
            <el-col :span="6"><p class="dates">total cost: ${{item.total_cost}}</p></el-col>
          </el-row>
          <el-row>
            <div style="margin-top: 0px;padding-bottom: 10px;font-size: medium;text-align: left">
              <el-row type="flex" class="row-bg" justify="space-between">
                <el-col :span="10">
                  <el-row>
                    <span style="font-weight: bold">Host contact:</span>
                  </el-row>
                  <el-row>
                    <span>{{item.host_name}}</span>
                  </el-row>
                  <el-row>
                    <span>{{item.contact}}</span>
                  </el-row>
                  <el-row>
                    <span>{{item.email}}</span>
                  </el-row>
                </el-col>
                <el-col :span="10">
                  <el-row>
                    <div style="margin-top: 30px">
                      <el-button v-if="test(item)" @click="showcomment(index,item)">write a comment</el-button>
                    </div>
                    <!--<el-button type="text" @click="dialogVisible = true">click to open the Dialog</el-button>-->
                  </el-row>
                </el-col>
              </el-row>
            </div>
          </el-row>
        </el-col>
      </el-row>
      <el-row>
        <el-dialog
          title="Please write your comment"
          :visible.sync="dialogVisible"
          :before-close="handleClose" class="abow_dialog">
          <div class="review">
            <el-row>
              <el-rate
                v-model="rate"
                :texts="['oops', 'disappointed', 'normal', 'good', 'great']"
                show-text>
              </el-rate>
            </el-row>
            <p></p>
            <el-row>
              <el-input
                type="textarea"
                :rows="3"
                placeholder="Please comment here"
                v-model="review">
              </el-input>
            </el-row>
            <p></p>
            <el-row>
              <el-col :span="6">
                <el-button style="visibility: hidden">确认</el-button>
              </el-col>
              <el-col :span="6">
                <el-button @click="commit(item)"> confirm</el-button>
              </el-col>
              <el-col :span="6">
                <el-button @click="dialogVisible = false"> cancel </el-button>
              </el-col>
              <el-col :span="6">
                <el-button style="visibility: hidden">取消</el-button>
              </el-col>
            </el-row>
          </div>
        </el-dialog>
        <!--
        <div class="review">
          <el-col :span="5">
            <el-rate
              v-model="rate"
              :texts="['oops', 'disappointed', 'normal', 'good', 'great']"
              show-text>
            </el-rate>
          </el-col>
          <el-col :span="14">
            <el-input
              type="textarea"
              :rows="3"
              placeholder="Please comment here"
              v-model="review">
            </el-input>
          </el-col>
          <el-col :span="5">
            <el-button>
              确认
            </el-button>
            <el-button>
              取消
            </el-button>
          </el-col>
        </div>
        -->
      </el-row>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'Mybooking',
  data () {
    return {
      review: '',
      seen: false,
      isactive: -1,
      dialogVisible: false,
      rate: '',
      id: '',
      id2: '',
      url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
      list: [{id: 1, start_date: '03/02/2020', end_date: '04/04/2020', isA: false}, {id: 2, start_date: '03/02/2020', end_date: '03/02/2020', isA: false}]
    }
  },
  created () {
    // for (var i = 0; i < this.list.length; i++) {
    //   var obj = this.list[i]
    //   obj.comment = false
    // }
    this.$axios
      .get('/api/show_booking?email=' + this.$store.getters.getStorage)
      .then(res => {
        this.list = res.data.body
        // this.total = res.data.total
      })
      .catch(function (error) {
        console.log(error)
      })
  },
  methods: {
    test: function (l) {
      var result = true
      // var result = false
      // var date = new Date() // 得到当前日期原始模式
      // var currentyear = date.getFullYear() // 得到当前日期年份
      // var newmonth = date.getMonth() + 1 // 得到当前日期月份（注意： getMonth()方法一月为 0, 二月为 1, 以此类推。）
      // var newday = date.getDate()
      // l.end_date.split('/')
      // if (l.end_date === 1) {
      //   result = true
      // }
      return result
    },
    showcomment (index, item) {
      // this.item.comment = true
      this.isactive = item.id
      let data = this.$qs.stringify({
        // email: this.user.email,
        property_id: this.isactive,
        email: this.list[index].id,
        context: item.id
      })
      this.dialogVisible = true
      this.$axios.post('/api/add_review', data)
    },
    commit (item) {
      let data = this.$qs.stringify({
        // email: this.user.email,
        property: item.booking_id,
        context: this.review,
        rating: this.rate
      })
      this.$axios.post('/api/add_review', data)
    }
    // toggle (item) {
    //   // this.$set(this.list, key, Object.assign({}, item, {isA: !item.isA}))
    //   let data = this.$qs.stringify({
    //     // email: this.user.email,
    //     property_id: this.isactive
    //     // context: this.item.isA
    //   })
    //   this.$axios.post('/api/add_review', data)
    // }
  }
}
</script>

<style scoped>
  .mybooking{
    margin-right: 10%;
    margin-left: 10%;
    text-align: left;
  }
  .mybooking h2 {
    margin: 0px 10px;
    font-size: 20px;
    font-weight: 600;
    color: #333;
    text-align: center;
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
  }
  .dates {
    font-size: 16px;
    font-weight: 600;
    color: #333;
    text-align: left;
    text-overflow: ellipsis;
  }
  .abow_dialog {
    display: flex;
    justify-content: center;
    align-items: Center;
    overflow: hidden;
  }
  .abow_dialog el-dialog {
    margin: 0 auto !important;
    height: 90%;
    overflow: hidden;
  }
  .abow_dialog el-dialog  el-dialog__body {
    position: absolute;
    left: 0;
    top: 54px;
    bottom: 0;
    right: 0;
    padding: 0;
    z-index: 1;
    overflow: hidden;
    overflow-y: auto;
  }
  .review{
    text-align: center;
  }
</style>
