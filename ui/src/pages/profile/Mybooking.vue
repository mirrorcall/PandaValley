<template>
  <div class="mybooking">
    <h1 style="text-align: center">My Booking</h1>
    <el-tabs v-model="activeName" type="card" stretch="true" @tab-click="handleClick">
      <el-tab-pane label="Upcoming" name="first">
    <el-card shadow="hover" v-for="item in uncompleted" :key="item.id">
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
            <h3><i class="el-icon-location"></i>
              {{item.street}}, {{item.suburb}}, NSW</h3>
          </el-row>
          <el-row>
            <el-col :span="12">
              <i class="icon iconfont iconrenshu"><span>{{item.guests}}</span></i>
              <el-divider direction="vertical"></el-divider>
              <i class="icon iconfont iconchuang"><span>{{item.bedrooms}}</span></i>
              <el-divider direction="vertical"></el-divider>
              <i class="icon iconfont iconyushiyongpin"><span>{{item.bathrooms}}</span></i>
            </el-col>
            <el-col :span="12">
              ${{item.price}}/night
            </el-col>
          </el-row>
          <el-row type="flex" class="row-bg" justify="space-between">
            <el-col :span="6"><p class="dates">Check-in:</p></el-col>
            <el-col :span="6"><p class="dates">{{item.start_date}}</p></el-col>
            <el-col :span="6"><p class="dates">Checkout:</p></el-col>
            <el-col :span="6"><p class="dates">{{item.end_date}}</p></el-col>
          </el-row>
          <el-row type="flex" justify="space-between">
            <el-col :span="12"><span class="dates">{{item.days}} nights</span></el-col>
            <el-col :span="12"><span class="dates">total cost: ${{item.total_cost}}</span></el-col>
          </el-row>
          <el-row>
            <div style="margin-top: 10px;padding-bottom: 10px;font-size: medium;text-align: left">
              <el-row type="flex" class="row-bg" justify="space-between">
                <el-col :span="4">
                  <span style="font-weight: bold">Host:</span>
                </el-col>
                <el-col :span="8">
                  {{item.host_name}}
                </el-col>
                <el-col :span="4">
                  <span style="font-weight: bold">Phone:</span>
                </el-col>
                <el-col :span="8">
                  {{item.contact}}
                </el-col>
              </el-row>
            </div>
          </el-row>
          <el-row>
            <div style="text-align: right"><el-button type="danger" @click="cancel_order(item)">Cancel</el-button></div>
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
      </el-row>
    </el-card>
      </el-tab-pane>
      <el-tab-pane label="In progress" name="second">
<!--        In progress-->
        <el-card shadow="hover" v-for="item in inprogress" :key="item.id">
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
                <h3><i class="el-icon-location"></i>
                  {{item.street}}, {{item.suburb}}, NSW</h3>
              </el-row>
              <el-row>
                <el-col :span="12">
                  <i class="icon iconfont iconrenshu"><span>{{item.guests}}</span></i>
                  <el-divider direction="vertical"></el-divider>
                  <i class="icon iconfont iconchuang"><span>{{item.bedrooms}}</span></i>
                  <el-divider direction="vertical"></el-divider>
                  <i class="icon iconfont iconyushiyongpin"><span>{{item.bathrooms}}</span></i>
                </el-col>
                <el-col :span="12">
                  ${{item.price}}/night
                </el-col>
              </el-row>
              <el-row type="flex" class="row-bg" justify="space-between">
                <el-col :span="6"><p class="dates">Check-in:</p></el-col>
                <el-col :span="6"><p class="dates">{{item.start_date}}</p></el-col>
                <el-col :span="6"><p class="dates">Checkout:</p></el-col>
                <el-col :span="6"><p class="dates">{{item.end_date}}</p></el-col>
              </el-row>
              <el-row type="flex" justify="space-between">
                <el-col :span="12"><span class="dates">{{item.days}} nights</span></el-col>
                <el-col :span="12"><span class="dates">total cost: ${{item.total_cost}}</span></el-col>
              </el-row>
              <el-row>
                <div style="margin-top: 10px;padding-bottom: 10px;font-size: medium;text-align: left">
                  <el-row type="flex" class="row-bg" justify="space-between">
                    <el-col :span="4">
                      <span style="font-weight: bold">Host:</span>
                    </el-col>
                    <el-col :span="8">
                      {{item.host_name}}
                    </el-col>
                    <el-col :span="4">
                      <span style="font-weight: bold">Phone:</span>
                    </el-col>
                    <el-col :span="8">
                      {{item.contact}}
                    </el-col>
                  </el-row>
                </div>
              </el-row>
            </el-col>
          </el-row>
          <el-row>
          </el-row>
        </el-card>
      </el-tab-pane>
      <el-tab-pane label="Uncommented" name="third">
        <el-card shadow="hover" v-for="item in uncommented" :key="item.id">
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
                <h3><i class="el-icon-location"></i>
                  {{item.street}}, {{item.suburb}}, NSW</h3>
              </el-row>
              <el-row>
                <el-col :span="12">
                  <i class="icon iconfont iconrenshu"><span>{{item.guests}}</span></i>
                  <el-divider direction="vertical"></el-divider>
                  <i class="icon iconfont iconchuang"><span>{{item.bedrooms}}</span></i>
                  <el-divider direction="vertical"></el-divider>
                  <i class="icon iconfont iconyushiyongpin"><span>{{item.bathrooms}}</span></i>
                </el-col>
                <el-col :span="12">
                  ${{item.price}}/night
                </el-col>
              </el-row>
              <el-row type="flex" class="row-bg" justify="space-between">
                <el-col :span="6"><p class="dates">Check-in:</p></el-col>
                <el-col :span="6"><p class="dates">{{item.start_date}}</p></el-col>
                <el-col :span="6"><p class="dates">Checkout:</p></el-col>
                <el-col :span="6"><p class="dates">{{item.end_date}}</p></el-col>
              </el-row>
              <el-row type="flex" justify="space-between">
                <el-col :span="12"><span class="dates">{{item.days}} nights</span></el-col>
                <el-col :span="12"><span class="dates">total cost: ${{item.total_cost}}</span></el-col>
              </el-row>
              <el-row>
                <div style="margin-top: 10px;padding-bottom: 10px;font-size: medium;text-align: left">
                  <el-row type="flex" class="row-bg" justify="space-between">
                    <el-col :span="4">
                      <span style="font-weight: bold">Host:</span>
                    </el-col>
                    <el-col :span="8">
                      {{item.host_name}}
                    </el-col>
                    <el-col :span="4">
                      <span style="font-weight: bold">Phone:</span>
                    </el-col>
                    <el-col :span="8">
                      {{item.contact}}
                    </el-col>

                    <!--                <el-col :span="10">-->
                    <!--                  <el-row>-->
                    <!--                    <span style="font-weight: bold">Host contact:</span>-->
                    <!--                  </el-row>-->
                    <!--                  <el-row>-->
                    <!--                    <span>{{item.host_name}}</span>-->
                    <!--                  </el-row>-->
                    <!--                  <el-row>-->
                    <!--                    <span>{{item.contact}}</span>-->
                    <!--                  </el-row>-->
                    <!--                  <el-row>-->
                    <!--                    <span>{{item.email}}</span>-->
                    <!--                  </el-row>-->
                    <!--                </el-col>-->
                    <!--                <el-col :span="10">-->
                    <!--                  <el-row>-->
                    <!--                    <div style="margin-top: 30px">-->
                    <!--                      <el-button v-if="test(item)" @click="showcomment(index,item)">write a comment</el-button>-->
                    <!--                    </div>-->
                    <!--<el-button type="text" @click="dialogVisible = true">click to open the Dialog</el-button>-->
                    <!--                  </el-row>-->
                    <!--                </el-col>-->
                  </el-row>
                </div>
              </el-row>
              <el-row>
                <div style="text-align: right"><el-button type="warning" @click="showcomment(item)">write a comment</el-button></div>
              </el-row>
            </el-col>
          </el-row>
          <el-row>
            <el-dialog
              title="Please write your comment about your experience"
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
                    <el-button type="primary" @click="commit(item)">Confirm</el-button>
                  </el-col>
                  <el-col :span="6">
                    <el-button @click="dialogVisible = false"> Cancel </el-button>
                  </el-col>
                  <el-col :span="6">
                    <el-button style="visibility: hidden">取消</el-button>
                  </el-col>
                </el-row>
              </div>
            </el-dialog>
          </el-row>
        </el-card>
      </el-tab-pane>
      <el-tab-pane label="Completed" name="fourth">
<!--        Complete-->
        <el-card shadow="hover" v-for="item in completed" :key="item.id">
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
                <h3><span style="visibility: hidden">location</span></h3>
                <!--                <h3><i class="el-icon-location"></i>-->
                <!--                  {{item.street}}, {{item.suburb}}, NSW</h3>-->
              </el-row>
              <el-row>
                <el-col :span="12">
                  <i class="icon iconfont iconrenshu"><span>{{item.guests}}</span></i>
                  <el-divider direction="vertical"></el-divider>
                  <i class="icon iconfont iconchuang"><span>{{item.bedrooms}}</span></i>
                  <el-divider direction="vertical"></el-divider>
                  <i class="icon iconfont iconyushiyongpin"><span>{{item.bathrooms}}</span></i>
                </el-col>
                <el-col :span="12">
                  ${{item.price}}/night
                </el-col>
              </el-row>
              <p></p>
              <el-row type="flex" class="row-bg" justify="space-between">
                <el-col :span="6"><p class="dates">Check-in:</p></el-col>
                <el-col :span="6"><p class="dates">{{item.start_date}}</p></el-col>
                <el-col :span="6"><p class="dates">Checkout:</p></el-col>
                <el-col :span="6"><p class="dates">{{item.end_date}}</p></el-col>
              </el-row>
              <el-row type="flex" justify="space-between">
                <el-col :span="12"><span class="dates">{{item.days}} nights</span></el-col>
                <el-col :span="12"><span class="dates">total cost: ${{item.total_cost}}</span></el-col>
              </el-row>
              <el-row>
                <div style="margin-top: 10px;padding-bottom: 10px;font-size: medium;text-align: left">
                  <el-row type="flex" class="row-bg" justify="space-between">
                    <!--                    <el-col :span="4">-->
                    <!--                      <span style="font-weight: bold">Host:</span>-->
                    <!--                    </el-col>-->
                    <!--                    <el-col :span="8">-->
                    <!--                      {{item.host_name}}-->
                    <!--                    </el-col>-->
                    <!--                    <el-col :span="4">-->
                    <!--                      <span style="font-weight: bold">Phone:</span>-->
                    <!--                    </el-col>-->
                    <!--                    <el-col :span="8">-->
                    <!--                      {{item.contact}}-->
                    <!--                    </el-col>-->
                  </el-row>
                </div>
              </el-row>
            </el-col>
          </el-row>
          <el-row>
          </el-row>
        </el-card>
      </el-tab-pane>
      <el-tab-pane label="Canceling" name="fifth">
        <el-card shadow="hover" v-for="item in cancelling" :key="item.id">
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
                <h3><i class="el-icon-location"></i>
                  {{item.street}}, {{item.suburb}}, NSW</h3>
              </el-row>
              <el-row>
                <el-col :span="12">
                  <i class="icon iconfont iconrenshu"><span>{{item.guests}}</span></i>
                  <el-divider direction="vertical"></el-divider>
                  <i class="icon iconfont iconchuang"><span>{{item.bedrooms}}</span></i>
                  <el-divider direction="vertical"></el-divider>
                  <i class="icon iconfont iconyushiyongpin"><span>{{item.bathrooms}}</span></i>
                </el-col>
                <el-col :span="12">
                  ${{item.price}}/night
                </el-col>
              </el-row>
              <el-row type="flex" class="row-bg" justify="space-between">
                <el-col :span="6"><p class="dates">Check-in:</p></el-col>
                <el-col :span="6"><p class="dates">{{item.start_date}}</p></el-col>
                <el-col :span="6"><p class="dates">Checkout:</p></el-col>
                <el-col :span="6"><p class="dates">{{item.end_date}}</p></el-col>
              </el-row>
              <el-row type="flex" justify="space-between">
                <el-col :span="12"><span class="dates">{{item.days}} nights</span></el-col>
                <el-col :span="12"><span class="dates">total cost: ${{item.total_cost}}</span></el-col>
              </el-row>
              <el-row>
                <div style="margin-top: 10px;padding-bottom: 10px;font-size: medium;text-align: left">
                  <el-row type="flex" class="row-bg" justify="space-between">
                    <el-col :span="4">
                      <span style="font-weight: bold">Host:</span>
                    </el-col>
                    <el-col :span="8">
                      {{item.host_name}}
                    </el-col>
                    <el-col :span="4">
                      <span style="font-weight: bold">Phone:</span>
                    </el-col>
                    <el-col :span="8">
                      {{item.contact}}
                    </el-col>
                  </el-row>
                </div>
              </el-row>
            </el-col>
          </el-row>
          <el-row>
          </el-row>
        </el-card>
      </el-tab-pane>
      <el-tab-pane label="Cancelled" name="sixth">
        <el-card shadow="hover" v-for="item in cancelled" :key="item.id">
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
                <h3><span style="visibility: hidden">location</span></h3>
<!--                <h3><i class="el-icon-location"></i>-->
<!--                  {{item.street}}, {{item.suburb}}, NSW</h3>-->
              </el-row>
              <el-row>
                <el-col :span="12">
                  <i class="icon iconfont iconrenshu"><span>{{item.guests}}</span></i>
                  <el-divider direction="vertical"></el-divider>
                  <i class="icon iconfont iconchuang"><span>{{item.bedrooms}}</span></i>
                  <el-divider direction="vertical"></el-divider>
                  <i class="icon iconfont iconyushiyongpin"><span>{{item.bathrooms}}</span></i>
                </el-col>
                <el-col :span="12">
                  ${{item.price}}/night
                </el-col>
              </el-row>
              <p></p>
              <el-row type="flex" class="row-bg" justify="space-between">
                <el-col :span="6"><p class="dates">Check-in:</p></el-col>
                <el-col :span="6"><p class="dates">{{item.start_date}}</p></el-col>
                <el-col :span="6"><p class="dates">Checkout:</p></el-col>
                <el-col :span="6"><p class="dates">{{item.end_date}}</p></el-col>
              </el-row>
              <el-row type="flex" justify="space-between">
                <el-col :span="12"><span class="dates">{{item.days}} nights</span></el-col>
                <el-col :span="12"><span class="dates">total cost: ${{item.total_cost}}</span></el-col>
              </el-row>
              <el-row>
                <div style="margin-top: 10px;padding-bottom: 10px;font-size: medium;text-align: left">
                  <el-row type="flex" class="row-bg" justify="space-between">
<!--                    <el-col :span="4">-->
<!--                      <span style="font-weight: bold">Host:</span>-->
<!--                    </el-col>-->
<!--                    <el-col :span="8">-->
<!--                      {{item.host_name}}-->
<!--                    </el-col>-->
<!--                    <el-col :span="4">-->
<!--                      <span style="font-weight: bold">Phone:</span>-->
<!--                    </el-col>-->
<!--                    <el-col :span="8">-->
<!--                      {{item.contact}}-->
<!--                    </el-col>-->
                  </el-row>
                </div>
              </el-row>
            </el-col>
          </el-row>
          <el-row>
          </el-row>
        </el-card>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
export default {
  name: 'Mybooking',
  data () {
    return {
      activeName: 'first',
      uncompleted: '',
      inprogress: '',
      cancelling: '',
      cancelled: '',
      uncommented: '',
      completed: '',
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
        this.uncompleted = res.data.body.uncompleted
        this.cancelling = res.data.body.canceling
        this.inprogress = res.data.body.checkedin
        this.cancelled = res.data.body.canceled
        this.uncommented = res.data.body.uncommented
        this.completed = res.data.body.completed
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
    showcomment (item) {
      // this.item.comment = true
      // this.isactive = item.property_id
      // let data = this.$qs.stringify({
      //   // email: this.user.email,
      //   property: this.item.property_id,
      //   email: this.this.$store.getters.getStorage,
      //   context: item.id,
      // })
      this.dialogVisible = true
      // this.$axios.post('/api/add_review', data)
    },
    commit (item) {
      let data = this.$qs.stringify({
        email: this.$store.getters.getStorage,
        property: item.property_id,
        booking_id: item.booking_id,
        context: this.review,
        rating: this.rate
      })
      this.$axios.post('/api/add_review', data)
        .then((response) => {
          if (response.data.code === 0) {
            this.$message('Thank you!')
            this.dialogVisible = false
            this.$router.go(0)
          } else {
            this.$message.error('Please try again.')
            console.log(response.data.msg)
          }
        })
        .catch((res) => {
          console.log('error ', res)
        })
    },
    cancel_order (item) {
      let data = this.$qs.stringify({
        booking_id: item.booking_id
      })
      this.$axios.post('/api/canceling', data)
        .then((response) => {
          if (response.data.code === 0) {
            this.$message('Your application has been sent to the host.')
            // this.$router.push({name: 'Home'})
            this.$router.go(0)
          } else {
            this.$message.error('Please try again.')
            console.log(response.data.msg)
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
  .mybooking{
    margin-right: 9%;
    margin-left: 9%;
    text-align: left;
  }
  .mybooking h2 {
    margin: 5px 10px;
    font-size: 20px;
    font-weight: 600;
    color: #333;
    text-align: center;
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
  }
  .mybooking h3 {
    margin: 0px 0px 10px 0px;
    font-size: 16px;
    font-weight: 400;
    color: #666666;
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
