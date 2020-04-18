<template>
  <el-container>
    <el-col :span="15" offset="1">
<!--    <el-aside width="1000px" style="margin-left: 35px">-->
<!--      <el-scrollbar style="width: 100%">-->
        <el-row>
          <div style="padding-top: 20px">
          <p style="font-weight: bolder;font-size: 25px" > {{title}} <img src="@/assets/whiteheart.png" style="width: 25px;height: 20px;margin-top: 0px;" v-if="!this.saved" @click="addTowishlist(item)">
            <img src="@/assets/heart.png" style="width: 25px;height: 20px;margin-top: 0px;" v-if="this.saved" @click="addTowishlist(item)">
          </p>
          </div>
        </el-row>
        <el-row>
          <div>
            <el-col :span="18"><i class="el-icon-location-information"></i>{{suburb}}, NSW</el-col>
            <el-col :span="6">
              <el-rate
                v-model="rating"
                disabled
                show-score
                text-color="#ff9900"
                score-template="{value}">
              </el-rate>
            </el-col>
          </div>
        </el-row>
      <el-row >
        <div id="banner" style="margin-top: 10px">
          <!--动态将图片轮播图的容器高度设置成与图片一致-->
          <el-carousel height="450px">
            <!--遍历图片地址,动态生成轮播图-->
            <el-carousel-item v-for="item in img_list" :key="item">
              <img :src="item" alt="">
            </el-carousel-item>
          </el-carousel>
        </div>
      </el-row>
      <el-row>
        <div class="box_fixed" id="boxFixed" :class="{'is_fixed' :isFixed}">
          <el-col :span="6"><span class="a"  @click="jump ('aaa')" >Overview</span></el-col>
          <el-col :span="6"><span class="a" @click="jump('bbb')">Amenities</span></el-col>
          <el-col :span="6"><span  class="a" @click="jump('ccc')">Reviews</span></el-col>
          <el-col :span="6"><span class="a" @click="jump('ddd')">Map</span></el-col>
        </div>
      </el-row>
      <el-row>
        <el-card id="aaa" align="left" style="padding-left: 20px">
          <h2 align="center">Overview</h2>
          <h2><i class = "el-icon-document"></i> Description</h2>
          <el-main>{{description}}</el-main>
          <h2><i class="el-icon-house"></i> Type: {{property_type | capitalize}}</h2>
          <h2><i class="icon iconfont iconrenshu" style="font-size: 25px"></i> Guests: {{guests}}</h2>
          <el-row style="font-size: 20px; padding-bottom: 10px">
            <el-col :offset="1"><div><i class="iconfont iconfangjian"></i><span>Rooms</span></div></el-col>
            <el-col :span="10" align="left" :offset="2"><span><i class="icon iconfont iconchuang" style="font-size: 23px"></i> Bedroom: {{bedrooms}}</span></el-col>
            <el-col :span="12" align="left"><span><i class="icon iconfont iconyushiyongpin" style="font-size: 23px"></i> Bathrooms: {{bathrooms}}</span></el-col>
          </el-row >
          <el-row style="font-size: 20px;">
            <el-col :offset="1"><div><i class="iconfont iconic_bedroom"></i><span>Beds</span></div></el-col>
            <el-col :span="10" align="left" :offset="2"><i class="iconfont icondanrenchuang"></i><span>Single bed: {{single_bed}}</span></el-col>
            <el-col :span="12" align="left"><i class="iconfont iconshuangrenchuang"></i><span>Double bed: {{double_bed}}</span></el-col>
          </el-row>
          <el-row style="font-size: 20px; text-align: left;">
            <el-col><div><span></span></div></el-col>
            <el-col :span="10" align="left" :offset="2"><i class="iconfont iconshuangrenchuang"></i><span>Queen bed: {{queen_bed}}</span></el-col>
            <el-col :span="12" align="left"><i class="iconfont iconshuangrenchuang"></i><span>King bed: {{king_bed}}</span></el-col>
          </el-row>
        </el-card>
        <el-card id="bbb" style="padding-left: 20px">
          <h2>Amenities</h2>
          <el-row v-for="item in this.lennum" :key="item" style="padding-bottom: 10px">
            <el-col :span="12" align="left"><i :class="occuam[2*item-2].classname" style="font-size: 25px"><span > {{occuam[2*item-2].name}}</span></i></el-col>
            <el-col :span="12" align="left"><i :class="occuam[2*item-1].classname" style="font-size: 25px"><span > {{occuam[2*item-1].name}}</span></i>
            </el-col>
          </el-row>
          <el-row v-show="this.oddnum" style="padding-bottom: 10px">
            <el-col :span="12" align="left"><i :class="occuam[this.occuam.length-1].classname" style="font-size: 25px"><span > {{occuam[this.occuam.length-1].name}}</span></i></el-col>
            <el-col :span="12" align="left"></el-col>
          </el-row>
        </el-card>
        <el-card id="ccc" style="padding-left: 20px">
          <h2>Review</h2>
          <el-row style="border-top: none;">
            <el-col style="border-top: none;">
              <div id="example" style="font-size: 20px">
                <!-- 利用v-if…v-else切换 展开 和 收起 两个画面，template包裹多个元素 -->
                <template v-if="isHide">
                  <!-- 只显示摘要的画面 -->
                  <div class="hideBg">
                    <div class="summary" >
                      <div style="text-align: left;padding-left: 20px" v-for="item in this.listshow" :key="item">
                        <el-row type="flex" justify="space-between" style="padding-bottom: 10px">
                          <el-col :span="12"><span style="font-weight: bold">{{item.username}}</span></el-col>
                          <el-col :span="12" style="text-align: right"><el-rate
                            v-model="item.rating"
                            disabled
                            show-score
                            text-color="#ff9900"
                            score-template="{value}">
                          </el-rate>
                          </el-col>
                        </el-row>
                        <el-row style="padding-bottom: 25px">
                          <el-col :span="24">{{item.context}}</el-col>
                        </el-row>
                      </div>
                      <el-row>
                      <div style="text-align: right">
                        <el-col style="height: 20px">
                          <a  href="#" @click.stop.prevent="onShow">More&nbsp;
                            <!-- 向下的角箭头符号，用css画 -->
                            <span class="downArrow"></span>
                          </a>
                        </el-col>
                      </div>
                      </el-row>
                    </div>
                  </div>
                </template>
                <template v-else>
                  <!-- 显示完整内容的画面 -->
                  <div class="showBg">
                    <div style="text-align: left;padding-left: 20px" v-for="item in this.reviewdata" :key="item">
                      <el-row type="flex" justify="space-between">
                        <el-col :span="12"><span style="font-weight: bold">{{item.username}}</span></el-col>
                        <el-col :span="12" style="text-align: right"><el-rate
                          v-model="item.rating"
                          disabled
                          show-score
                          text-color="#ff9900"
                          score-template="{value}">
                        </el-rate>
                        </el-col>
                      </el-row>
                      <el-row>
                        <el-col :span="24">{{item.context}}</el-col>
                       </el-row>
                    </div>
                    <el-row>
                      <el-col style="height: 20px">
                        <div class="hideBtn">
                          <!-- 绑定点击事件onHide，点击收起内容 -->
                          <a href="#" @click.stop.prevent="onHide">Hide&nbsp;
                            <!-- 向上的角箭头符号 -->
                            <span class="upArrow"></span>
                          </a>
                        </div>
                      </el-col>
                    </el-row>
                    </div>
                </template>
              </div>
            </el-col>
          </el-row>
        </el-card>
        <el-card id="ddd" style="padding-left: 0px">
          <h2>Map</h2>
          <map-view :center="center"></map-view>
        </el-card>
      </el-row>
<!--      </el-scrollbar>-->
<!--    </el-aside>-->
    </el-col>
    <el-col :span="8">
    <el-main>
      <el-card style="margin-top: 110px;height: 450px" shadow="never">
        <el-row>
          <el-avatar :size="80" :src="host_avatar" style="vertical-align: middle;margin-top: 16px;margin-bottom: 20px"></el-avatar>
          {{host_name}}
        </el-row>
        <el-row>
          <el-date-picker
            v-model="ruleForm.date1"
            type="daterange"
            range-separator="To"
            format="dd/MM/yyyy"
            value-format="dd/MM/yyyy"
            size="medium"
            :start-placeholder= "start_date"
            :end-placeholder= "end_date" :picker-options="pickerOptions" :default-value="[ruleForm.d1,ruleForm.d2]" @change="dateChange"></el-date-picker>
        </el-row>
        <h2 style="margin-top: 10px;margin-bottom: 10px; padding-top: 10px;">{{period}} Nights</h2>
        <el-divider></el-divider>
        <el-row>
          <div style="text-align: left;font-size: medium" >
            <el-col :span="12">
              <el-row>
                <span>{{price}} * {{period}} nights</span>
              </el-row>
              <el-row>
                <div style="margin-top: 10px">Cleaning fee</div>
              </el-row>
              <el-row>
                <div style="margin-top: 10px;font-weight: bold"> Total</div>
              </el-row>
            </el-col>
          </div>
          <div style="text-align: right">
            <el-col :span="12">
              <el-row>
                $
                {{price*period}}
              </el-row>
              <el-row>
                <div style="margin-top: 10px">
                  $
                  {{cleaning_fee}}
                </div>
              </el-row>
              <el-row>
                <div style="margin-top: 10px;font-weight: bold;margin-bottom: 20px">
                  $
                  {{total}}
                </div>
              </el-row>
            </el-col>
          </div>
        </el-row>
        <el-button type="primary" @click="submitForm('ruleForm')">Reserve</el-button>
      </el-card>
      <el-row style="height:50px"></el-row>
      <el-divider><h3>Nearby recommendations</h3></el-divider>
      <related :list="related" :start_date="start_date" :end_date="end_date"></related>
    </el-main>
    </el-col>
  </el-container>
</template>

<script>
// import MapView from './MapView'
import Related from './Related'
import MapView from '../../components/MapView'
export default {
  components: {MapView, Related},
  offsetTop: 0,
  name: 'Details',
  props: {
    size: { // 父组件传值设置字体大小
      type: String,
      default: '16px'
    },
    value: { // 绑定value，与$emit实现双向绑定
      type: Number,
      default: 0
    }
  },
  data () {
    return {
      saved: '',
      rating: '',
      related: '',
      reviewdata: [{'id': 5, 'username': 'Rita', 'Rating': 4.0, 'context': 'Beatiful Places!'}, {'id': 6, 'username': 'Jeff', 'Rating': 5.0, 'context': 'Nice house!'}],
      listshow: '',
      listamen: [
        {classname: 'el-icon-thirdhongganji', name: 'Clothes dryer'},
        {classname: 'el-icon-thirdbeidangenghuan', name: 'Linens provided'},
        {classname: 'el-icon-thirdairconditioning', name: 'Air conditioning'},
        {classname: 'el-icon-thirdweibolu', name: 'Microwave'},
        {classname: 'el-icon-thirdkaoxiang', name: 'Oven'},
        {classname: 'el-icon-thirdcarpark', name: 'Parking'},
        {classname: 'el-icon-thirdicon-test10', name: 'No Smoking'},
        {classname: 'el-icon-thirdHairdryer', name: 'Hair dryer'},
        {classname: 'el-icon-thirdwuzhangaisheshi', name: 'Accessible'},
        {classname: 'el-icon-thirdbingxiang', name: 'Fridge'},
        {classname: 'el-icon-thirdicon-test4', name: 'Wireless Internet'},
        {classname: 'el-icon-thirdWashingmachine', name: 'Washing machine'},
        {classname: 'el-icon-thirdnuanqi', name: 'Heating'},
        {classname: 'el-icon-thirdindoorpool', name: 'Swimming pool'},
        {classname: 'el-icon-thirdBathtub', name: 'Hot Tub'},
        {classname: 'el-icon-thirdicon-test1', name: 'Elevator'},
        {classname: 'el-icon-thirdBlendermixer', name: 'Blender'},
        {classname: 'el-icon-thirdkexiedaichongwu', name: 'Pets Welcome'},
        {classname: 'el-icon-thirdToaster', name: 'Toaster'},
        {classname: 'el-icon-thirdshaokaoqiju', name: 'BBQ'}
      ],
      oddnum: '',
      occuam: '',
      lennum: '',
      title: 'titkl',
      suburb: '',
      description: 'djnakjsnkjasndasmdnms',
      guests: '4',
      bedrooms: '1',
      bathrooms: '1',
      single_bed: '1',
      double_bed: '1',
      queen_bed: '1',
      king_bed: '1',
      list_amenities: '',
      property: '',
      img_list: ['/static/image/111.png', '/static/image/222.png', '/static/image/333.png'],
      // amenities: 'Microwave#Fridge',
      amenities: '',
      isFixed: '',
      start_date: '5/12/2020',
      end_date: '6/12/2020',
      sdata: '2020-6-12',
      edata: '2020-7-13',
      period: '',
      host_name: '',
      host_avatar: '',
      price: '',
      total: '',
      property_type: '',
      cleaning_fee: '',
      pickerOptions: {
        disabledDate: function (time) {
          return time.getTime() < Date.now() - 8.64e7
        }
      },
      ruleForm: {
        name: '',
        region: '',
        d1: '5/12/2020',
        d2: '6/12/2020',
        date1: '',
        date_s: '',
        date_e: '',
        date2: ''
      },
      active: 0, // 当前激活的导航索引
      content: 'Nice appartment\n\t, small but ok. But the communication was non existent. My elevator key card didn\'t work properly. so it closed me out of the building three times, once even at 2.00am. The owners (these are investors who have people that work for them) do not really care that you are constantly locked out. Asking for a new key card is no use they tell you that things are all right. I asked for a refund since it was impossible to get to the appartment. They didn\'t give any. This is a place to a place to bypass. 中华人民共和国位于亚洲东部，太平洋西岸 [1]  ，是工人阶级领导的、以工农联盟为基础的人民民主专政的社会主义国家 [2]  。1949年（己丑年）10月1日成立 [3-4]  ，以五星红旗为国旗 [5]  ，《义勇军进行曲》为国歌 [6]  ，国徽内容包括国旗、天安门、齿轮和麦稻穗 [7]  ，首都北京 [8]  ，省级行政区划为23个省、5个自治区、4个直辖市、2个特别行政区 [9]  ，是一个以汉族为主体民族，由56个民族构成的统一多民族国家，汉族占总人口的91.51% [10]  。新中国成立后，随即开展经济恢复与建设 [11]  ，1953年开始三大改造 [12]  ，到1956年确立了社会主义制度，进入社会主义探索阶段 [13]  。文化大革命之后开始改革开放，逐步确立了中国特色社会主义制度。 [14] 中华人民共和国陆地面积约960万平方公里，大陆海岸线1.8万多千米，岛屿岸线1.4万多千米，内海和边海的水域面积约470多万平方千米。海域分布有大小岛屿7600多个，其中台湾岛最大，面积35798平方千米。 [1]  陆地同14国接壤，与6国海上相邻。Nice appartment, small but ok. But the communication was non existent. My elevator key card didn\'t work properly. so it closed me out of the building three times, once even at 2.00am. The owners (these are investors who have people that work for them) do not really care that you are constantly locked out. Asking for a new key card is no use they tell you that things are all right. I asked for a refund since it was impossible to get to the appartment. They didn\'t give any. This is a place to a place to bypass. 中华人民共和国位于亚洲东部，太平洋西岸 [1]  ，是工人阶级领导的、以工农联盟为基础的人民民主专政的社会主义国家 [2]  。1949年（己丑年）10月1日成立 [3-4]  ，以五星红旗为国旗 [5]  ，《义勇军进行曲》为国歌 [6]  ，国徽内容包括国旗、天安门、齿轮和麦稻穗 [7]  ，首都北京 [8]  ，省级行政区划为23个省、5个自治区、4个直辖市、2个特别行政区 [9]  ，是一个以汉族为主体民族，由56个民族构成的统一多民族国家，汉族占总人口的91.51% [10]  。新中国成立后，随即开展经济恢复与建设 [11]  ，1953年开始三大改造 [12]  ，到1956年确立了社会主义制度，进入社会主义探索阶段 [13]  。文化大革命之后开始改革开放，逐步确立了中国特色社会主义制度。 [14] 中华人民共和国陆地面积约960万平方公里，大陆海岸线1.8万多千米，岛屿岸线1.4万多千米，内海和边海的水域面积约470多万平方千米。海域分布有大小岛屿7600多个，其中台湾岛最大，面积35798平方千米。 [1]  陆地同14国接壤，与6国海上相邻。',
      isHide: true, // 初始值为true，显示为折叠画面
      word_list: [],
      // 图片地址数组
      img0: '/static/image/111.png',
      img1: '/static/image/222.png',
      imgslist: [this.img0, this.img1, this.img0, this.img1, this.img0],
      // 图片父容器高度
      bannerHeight: 1000,
      // 浏览器宽度
      screenWidth: 0,
      center: {
        lat: '',
        lng: ''
      }
    }
  },
  destroy () {
    // 必须移除监听器，不然当该vue组件被销毁了，监听器还在就会出错
    window.removeEventListener('scroll', this.onScroll)
    // window.removeEventListener('scroll', this.initHeight)
  },
  created () {
    this.start_date = this.$route.query.start_date
    this.end_date = this.$route.query.end_date
    this.property = this.$route.query.property
    this.$axios
      .get('/api/show_property?property=' + this.property + '&start_date=' + this.start_date + '&end_date=' + this.end_date + '&email=' + this.$store.getters.getStorage)
      .then(res => {
        this.title = res.data.body.title
        this.description = res.data.body.description
        this.guests = res.data.body.guests
        this.bedrooms = res.data.body.bedrooms
        this.bathrooms = res.data.body.bathrooms
        this.single_bed = res.data.body.single_bed
        this.double_bed = res.data.body.double_bed
        this.queen_bed = res.data.body.queen_bed
        this.king_bed = res.data.body.king_bed
        this.period = res.data.body.period
        this.host_name = res.data.body.host_name
        this.price = res.data.body.price
        this.total = res.data.body.total_cost
        this.cleaning_fee = res.data.body.cleaning_fee
        this.img_list = res.data.body.image
        this.amenities = res.data.body.amenities
        this.host_avatar = res.data.body.host_avatar
        this.suburb = res.data.body.suburb
        this.rating = res.data.body.rating
        this.center = {
          lat: res.data.body.latitude,
          lng: res.data.body.longitude
        }
        if (this.rating === '5.00') {
          this.rating = '5'
        }
        this.property_type = res.data.body.property_type
        this.saved = res.data.body.saved
        this.list_amenities = this.amenities.split('#')
        // console.log(this.list_amenities)
        this.getDetails()
        this.getAm()
        this.getReview()
        this.getNearby()
      })
      .catch(function (error) {
        console.log(error)
      })
    // this.getDetails()
    this.ruleForm.d1 = this.start_date.split('/')[1] + '/' + this.start_date.split('/')[0] + '/' + this.start_date.split('/')[2]
    this.ruleForm.d2 = this.end_date.split('/')[1] + '/' + this.end_date.split('/')[0] + '/' + this.end_date.split('/')[2]
    // eslint-disable-next-line no-unused-vars
    // this.sdata = this.start_date.split('/')[2] + '-' + this.start_date.split('/')[1] + '-' + this.start_date.split('/')[0]
    // this.edata = this.end_date.split('/')[2] + '-' + this.end_date.split('/')[1] + '-' + this.end_date.split('/')[0]
  },
  filters: {
    capitalize: function (value) {
      if (!value) return ''
      value = value.toString()
      return value.charAt(0).toUpperCase() + value.slice(1)
    }
  },
  methods: {
    addTowishlist () {
      if (!this.$store.getters.getStorage) {
        alert('Please login')
      } else {
        if (this.saved === true) {
          this.$message('already saved')
        } else {
          let data = this.$qs.stringify({
            property: this.property,
            email: this.$store.getters.getStorage
          })
          this.$axios.post('/api/add_wishlist', data)
            .then((response) => {
              if (response.data.code === 0) {
                this.$message('saved to wishlist')
                // console.log('saved to wishlist')
                this.saved = true
              } else {
                this.$message('error')
                // console.log(response.data.msg)
              }
            })
        }
      }
    },
    getNearby () {
      this.$axios
        .get('/api/nearby_property?property_id=' + this.property + '&start_date=' + this.start_date + '&end_date=' + this.end_date)
        .then(res => {
          this.related = res.data.body
        })
    },
    checkReview () {
      if (this.reviewdata.length > 0) {
        return true
      }
      return false
    },
    changeRate (s) {
      this.star = s // 更新当前星星数量
      this.$emit('input', s) // 将当前星星数量s与v-model绑定
    },
    getReview () {
      this.$axios
        .get('/api/show_reviews?property=' + this.property)
        .then(res => {
          this.reviewdata = res.data.body
          this.reviewdata.forEach(function (item) {
            if (item['rating'] === '5.00') {
              item['rating'] = '5'
            }
            if (item['rating'] === '4.00') {
              item['rating'] = '4'
            }
            if (item['rating'] === '3.00') {
              item['rating'] = '3'
            }
            if (item['rating'] === '2.00') {
              item['rating'] = '2'
            }
            if (item['rating'] === '1.00') {
              item['rating'] = '1'
            }
          })
          this.listshow = this.reviewdata.sort(function (a, b) { return b['context'].length - a['context'].length })
          this.listshow = this.listshow.slice(0, 2)
        })
        .catch(function (error) {
          console.log(error)
        })
      // for (var value of this.reviewdata) {
      //   this.word_list.push(value)
      // }
    },
    check_len (item) {
      if (this.ccuam.length > 2 * item) {
        return true
      } else {
        return false
      }
    },
    getAm () {
      this.occuam = []
      for (var value of this.listamen) {
        if (this.list_amenities.includes(value.name)) {
          this.occuam.push(value)
        }
      }
      let len = this.occuam.length
      let tmp = len % 2
      this.lennum = parseInt(this.occuam.length / 2)
      if (tmp === 1) {
        this.oddnum = true
      } else {
        this.oddnum = false
      }
      if (this.occuam.length > 0) {
        this.shown = true
      }
    },
    getDetails () {
      this.$axios
        .get('/api/show_property?property=' + this.property + '&start_date=' + this.start_date + '&end_date=' + this.end_date)
        .then(res => {
          this.title = res.data.body.title
          this.description = res.data.body.description
          this.guests = res.data.body.guests
          this.bedrooms = res.data.body.bedrooms
          this.bathrooms = res.data.body.bathrooms
          this.single_bed = res.data.body.single_bed
          this.double_bed = res.data.body.double_bed
          this.queen_bed = res.data.body.queen_bed
          this.king_bed = res.data.body.king_bed
          this.period = res.data.body.period
          this.host_name = res.data.body.host_name
          this.price = res.data.body.price
          this.total = res.data.body.total_cost
          this.cleaning_fee = res.data.body.cleaning_fee
          this.img_list = res.data.body.image
          this.amenities = res.data.body.amenities
          this.host_avatar = res.data.body.host_avatar
          this.suburb = res.data.body.suburb
          this.property_type = res.data.body.property_type
          // this.list_amenities = this.amenities.split('#')
          // console.log(this.list_amenities)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    show_amentities (item) {
      return this.list_amenities.includes(item)
    },
    onShow: function () {
      this.isHide = false // 点击onShow切换为false，显示为展开画面
    },
    onHide: function () {
      this.isHide = true // 点击onHide切换为true，显示为折叠画面
    },
    jump (domId) {
      // 当前窗口正中心位置到指定dom位置的距离

      // 页面滚动了的距离
      let height = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
      // 指定dom到页面顶端的距离
      let dom = document.getElementById(domId)
      let domHeight = dom.offsetTop + 60

      // 滚动距离计算
      var S = Number(height) - Number(domHeight) - 600

      // 判断上滚还是下滚
      if (S < 0) {
        // 下滚
        S = Math.abs(S)
        window.scrollBy({ top: S, behavior: 'smooth' })
        // eslint-disable-next-line eqeqeq
      } else if (S == 0) {
        // 不滚
        window.scrollBy({ top: 0, behavior: 'smooth' })
      } else {
        // 上滚
        S = -S
        window.scrollBy({ top: S, behavior: 'smooth' })
      }
    },
    dateChange () {
      // this.ruleForm.data_s = new Date(this.ruleForm.date1[0]).toLocaleDateString('en-AU')
      // this.ruleForm.data_e = new Date(this.ruleForm.date1[1]).toLocaleDateString('en-AU')
      this.ruleForm.data_s = this.ruleForm.date1[0]
      this.ruleForm.data_e = this.ruleForm.date1[1]
      // var oDate1, oDate2
      // oDate1 = this.ruleForm.data_e.split('/')
      // oDate2 = this.ruleForm.data_s.split('/')
      // this.ruleForm.intervel = parseInt(oDate1[1]) - parseInt(oDate2[1])
      let data = this.$qs.stringify({property: this.property, start_date: this.ruleForm.data_s, end_date: this.ruleForm.data_e})
      this.$axios.post('/api/varify_booking', data)
        .then((response) => {
          if (response.data.code === 0) {
            this.start_date = this.ruleForm.data_s
            this.end_date = this.ruleForm.data_e
            this.period = response.data.body.period
            this.total = response.data.body.total_cost
          } else {
            this.$message.error('this period is unavailable, please change the date')
            console.log('this period is unavailable')
          }
        })
        .catch((res) => {
          console.log('error ', res)
        })
    },
    submitForm (formName) {
      if (!this.$store.getters.getStorage) {
        this.$message.error('please login')
      } else {
        let data = this.$qs.stringify({
          email: this.$store.getters.getStorage,
          property_id: this.property,
          start_date: this.start_date,
          end_date: this.end_date,
          period: this.period,
          total_cost: this.total
        })
        this.$axios.post('/api/reserve', data)
          .then((response) => {
            if (response.data.code === 0) {
              this.$message('Successfully booked, a conformation email will be sent later')
            } else {
              this.$message.error('this period is unavailable, please change the date')
              console.log('this period is unavailable')
            }
          })
          .catch((res) => {
            console.log('error ', res)
          })
      }
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    },
    initHeight () {
      var scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
      // let height = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop

      // 指定dom到页面顶端的距离
      // let dom = document.getElementById('aaa')
      // let a = scrollTop > 600
      // eslint-disable-next-line eqeqeq
      if (scrollTop > this.offsetTop + 600) {
        this.isFixed = true
      } else {
        this.isFixed = false
      }
      // console.log(this.occuam)
      // this.isFixed = Number(scrollTop) > 600 ? true ; false
      // this.isFixed = false
    },
    setSize: function () {
      // 通过浏览器宽度(图片宽度)计算高度
      this.bannerHeight = 600 / 1920 * this.screenWidth
    },
    // 滚动监听器
    onScroll () {
      // 获取所有锚点元素
      const navContents = document.querySelectorAll('.content div')
      // 所有锚点元素的 offsetTop
      const offsetTopArr = []
      navContents.forEach(item => {
        offsetTopArr.push(item.offsetTop)
      })
      // 获取当前文档流的 scrollTop
      const scrollTop = document.documentElement.scrollTop || document.body.scrollTop
      // 定义当前点亮的导航下标
      let navIndex = 0
      for (let n = 0; n < offsetTopArr.length; n++) {
        // 如果 scrollTop 大于等于第n个元素的 offsetTop 则说明 n-1 的内容已经完全不可见
        // 那么此时导航索引就应该是n了
        if (scrollTop >= offsetTopArr[n]) {
          navIndex = n
        }
      }
      this.active = navIndex
    },
    // 跳转到指定索引的元素
    scrollTo (index) {
      // 获取目标的 offsetTop
      // css选择器是从 1 开始计数，我们是从 0 开始，所以要 +1
      const targetOffsetTop = document.querySelector(`.content div:nth-child(${index + 1})`).offsetTop
      // 获取当前 offsetTop
      let scrollTop = document.documentElement.scrollTop || document.body.scrollTop
      // 定义一次跳 50 个像素，数字越大跳得越快，但是会有掉帧得感觉，步子迈大了会扯到蛋
      const STEP = 50
      // 判断是往下滑还是往上滑
      if (scrollTop > targetOffsetTop) {
        // 往上滑
        smoothUp()
      } else {
        // 往下滑
        smoothDown()
      }
      // 定义往下滑函数
      function smoothDown () {
        // 如果当前 scrollTop 小于 targetOffsetTop 说明视口还没滑到指定位置
        if (scrollTop < targetOffsetTop) {
          // 如果和目标相差距离大于等于 STEP 就跳 STEP
          // 否则直接跳到目标点，目标是为了防止跳过了。
          if (targetOffsetTop - scrollTop >= STEP) {
            scrollTop += STEP
          } else {
            scrollTop = targetOffsetTop
          }
          document.body.scrollTop = scrollTop
          document.documentElement.scrollTop = scrollTop
          // 关于 requestAnimationFrame 可以自己查一下，在这种场景下，相比 setInterval 性价比更高
          requestAnimationFrame(smoothDown)
        }
      }
      // 定义往上滑函数
      function smoothUp () {
        if (scrollTop > targetOffsetTop) {
          if (scrollTop - targetOffsetTop >= STEP) {
            scrollTop -= STEP
          } else {
            scrollTop = targetOffsetTop
          }
          document.body.scrollTop = scrollTop
          document.documentElement.scrollTop = scrollTop
          requestAnimationFrame(smoothUp)
        }
      }
    }
  },
  handleClick () {
    scrollTo(1)
  },
  mounted () {
    // window.addEventListener('scroll', this.initHeight)
    // this.$nextTick(() => {
    //   this.offsetTop = document.querySelector('#boxFixed').offsetTop
    // })
    // // 监听滚动事件
    // window.addEventListener('scroll', this.onScroll, false)
    // // 首次加载时,需要调用一次
    // this.screenWidth = window.innerWidth
    // this.setSize()
    // // 窗口大小发生改变时,调用一次
    // window.onresize = () => {
    //   this.screenWidth = window.innerWidth
    //   this.setSize()
    // }
    document.documentElement.style.overflowY = 'scroll'
  }
}
</script>

<style scoped>
  /* 内容区的样式 */
  .demo-ruleForm{
    margin-top: 80px;
    /*margin-left: 60px;*/
    /*top: 80px;  */
    /*height: 400px;*/
    border: 2px dashed pink;
    border-radius: 20px;
    position: absolute;
    /*line-height: 20px;*/
    /*background-color: #efefef;*/
  }
  .content {
    /*margin-left: 60px;*/
    /*background-color: white;*/
    width: 700px;
  }
  .content div {
    margin-top: 5px;
    border-width: thin;
    border-style: solid;
    border-left: none;
    border-right: none;
    border-bottom: none;
    width: 100%;
    height: 400px;
    /*font-size: 36px;*/
    /*padding: 20px;*/
    /*background-color: #7ec384;*/
  }
  .content div:nth-child(2n) {
    /*background-color: #847ec3;*/
  }
  /* 导航栏的样式 */
  .navs {
    position: fixed;
    top: 100px;
    left: 200px;
    background-color: #f5f7fa;
  }
  /* 当导航被点亮后改变颜色 */
  .navs .active{
    color: #847ec3;
    background-color: #e2e2e2;
  }
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
  img{
    /*设置图片宽度和浏览器宽度一致*/
    width: 100%;
    height: inherit;
  }
  .box_fixed{
    padding-top: 15px;
    padding-bottom: -5px;
    margin-left: 1000px;
    opacity: 0;
    width: 0.01px;
    height: 0.01px;
    /*border: 2px dashed pink;*/
    /*border-radius: 20px;*/
    /*margin: 0 auto;*/
    line-height: 20px;
    background: #f5f7fa;
  }
  .is_fixed{
    padding-top: 15px;
    padding-bottom: -5px;
    width: 900px;
    height: 40px;
    opacity: 100;
    position: fixed;
    top: 0;
    /*left: 50%;*/
    margin-left: 0px;
    z-index: 999;
  }
  .stepBtn{
    margin-bottom: 15px;
  }
  /* 摘要背景板 */
  .hideBg {
    /*width: 500px;*/
    /*background-color: #e9ecef;*/
    /*margin: 1.5rem;*/
    /*padding: 1.5rem;*/
    /*padding-bottom: 0;    !* 方便渐变层遮挡 *!*/
    position: relative;    /* 用于子元素定位 */
  }
  /* 全文背景板，基本与摘要相同 */
  .showBg {
    /*width: 500px;*/
    /*background-color: #e9ecef;*/
    /*margin: 1.5rem;*/
    /*padding: 1.5rem;*/
  }
  /* 摘要内容 */
  .summary {
    overflow: hidden;    /* 隐藏溢出内容 */
    text-overflow: clip;    /* 修剪文本 */
    display: -webkit-box;    /* 弹性布局 */
    -webkit-box-orient: vertical;    /* 从上向下垂直排列子元素 */
    /*-webkit-line-clamp: 5;    /* 限制文本仅显示前三行 */
    -webkit-line-clamp: 5;
  }
  #example p {
    text-indent: 2em;
  }
  /* 展开按钮 */
  .showBtn {
    width: 100%;    /* 与背景宽度一致 */
    /*height: 3rem;*/
    height: 10rem;
    position: absolute;    /* 相对父元素定位 */
    /*top: 3rem;    !* 刚好遮挡在最后两行 *!*/
    top: 4rem;
    left: 0;
    z-index: 0;    /* 正序堆叠，覆盖在p元素上方 */
    text-align: right;
    /*background: linear-gradient(rgba(233,236,239,.5), white);    !* 背景色半透明到白色的渐变层 *!*/
    /*padding-top: 3rem;*/
    padding-top: 5rem;
  }
  /* 收起按钮 */
  .hideBtn {
    text-align: right;
  }
  #example a {
    text-decoration: none;    /* 清除链接默认的下划线 */
  }
  /* 向下角箭头 */
  .downArrow {
    display: inline-block;
    width: 8px;    /* 尺寸不超过字号的一半为宜 */
    height: 8px;
    border-right: 1px solid;    /* 画两条相邻边框 */
    border-bottom: 1px solid;
    transform: rotate(45deg);    /* 顺时针旋转45° */
    margin-bottom: 3px;
  }
  /* 向上角箭头，原理与下箭头相同 */
  .upArrow {
    display: inline-block;
    width: 8px;
    height: 8px;
    border-left: 1px solid;
    border-top: 1px solid;
    transform: rotate(45deg);
    margin-top: 3px;
  }
  .a:hover{
    color: orange;
    border-bottom: 1px solid orange;
  }
  /*
  .a:active {
    text-decoration:underline;
  }
  .a:visited {
    text-decoration:underline;
  }
  */
</style>
