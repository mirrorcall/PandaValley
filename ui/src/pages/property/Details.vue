<template>
  <!--  <el-container>-->
  <!--  </el-container>-->
  <div style="margin-left: 40px" class="img_box">
    <el-main>
      <el-col :span="15" style="margin-top: 20px">
        <el-row>
          <h1>{{title}}</h1>
        </el-row>
        <el-row>
          <el-col :span="18"><i class="el-icon-location-information"></i>{{suburb}}, NSW</el-col>
          <el-col :span="6"><el-rate
            v-model="rate"
            disabled
            show-score
            text-color="#ff9900"
            score-template="{value}">
          </el-rate>
          </el-col>
        </el-row>
      </el-col>
    </el-main>
    <el-row>
      <el-col :span="14" style="margin-top: 20px;margin-left: 20px"><el-container>
        <el-col >
          <div id="banner">
            <!--动态将图片轮播图的容器高度设置成与图片一致-->
            <el-carousel :height="bannerHeight + 'px'" interval="1200">
              <!--遍历图片地址,动态生成轮播图-->
              <el-carousel-item v-for="item in img_list" :key="item">
                <img :src="item" alt="">
              </el-carousel-item>
            </el-carousel>
          </div>
        </el-col>
      </el-container></el-col>
      <el-col :span="9" ><div class="grid-content bg-purple-light"><el-main><el-container>

        <el-form :model="ruleForm" ref="ruleForm" label-width="100px" class="demo-ruleForm">
          <el-form-item style="margin-left: -65px;margin-right: 25px; margin-top: 20px">
            <td>
              <el-avatar id="toolbar-avatar" :size="80" :src="host_avatar" style="vertical-align: middle;margin-left: 120px;margin-top: 16px;margin-bottom: 20px"></el-avatar>
              {{host_name}}
            </td>
            <el-date-picker
              v-model="ruleForm.date1"
              type="daterange"
              range-separator="To"
              format="dd/MM/yyyy"
              value-format="dd/MM/yyyy"
              :start-placeholder= "start_date"
              :end-placeholder= "end_date" :picker-options="pickerOptions" :default-value="[ruleForm.d1,ruleForm.d2]" @change="dateChange"></el-date-picker>
            <h2 style="margin-top: 10px;margin-bottom: 10px">{{period}} nights</h2>
            <el-divider></el-divider>
            <h3 style="margin-top: 20px;margin-bottom: 20px"><el-col :span="10">{{price}} * {{period}} nights</el-col><el-row>{{price*period}}</el-row></h3>
            <h3 style="margin-top: 20px;margin-bottom: 20px"><el-col :span="10">cleaning fee</el-col><el-row>{{cleaning_fee}}</el-row></h3>
            <el-divider></el-divider>
            <h3 style="margin-top: 10px;margin-bottom: -30px"><el-col :span="10">total</el-col><el-row>{{total}}</el-row></h3>
          </el-form-item>
          <el-form-item style="margin-top: -10px">
            <el-button style="margin-left: -100px" type="primary" @click="submitForm('ruleForm')">Reserve</el-button>
          </el-form-item>
        </el-form>

      </el-container></el-main></div></el-col>
    </el-row>
    <!--      <el-row>-->
    <!--        <el-col :span="12"><div class="grid-content bg-purple"><el-main></el-main></div></el-col>-->
    <!--        <el-col :span="12"><div class="grid-content bg-purple-light"><el-main>-->
    <!--          bbb-->
    <!--          <el-divider></el-divider>-->
    <!--        </el-main></div></el-col>-->
    <!--      </el-row>-->
    <el-container>
      <el-aside width="900px">
        <div class="box_fixed" id="boxFixed" :class="{'is_fixed' :isFixed}">
          <!--          <el-col :span="6"><el-button label="content-0" name="third" :class="{active: active===1}" @click="jump('aaa')" >Overview</el-button></el-col>-->
          <!--          <el-col :span="6"><el-button label="content-1" name="third" :class="{active: active===2}" @click="jump('bbb')">Amenities</el-button></el-col>-->
          <!--          <el-col :span="6"><el-button label="content-2" name="third" :class="{active: active===3}" @click="jump('ccc')">Reviews</el-button></el-col>-->
          <!--          <el-col :span="6"><el-button label="content-3" name="third" :class="{active: active===4}" @click="jump('ddd')">Map</el-button></el-col>-->
          <el-col :span="6"><span class="a"  @click="jump ('aaa')" >Overview</span></el-col>
          <el-col :span="6"><span class="a" @click="jump('bbb')">Amenities</span></el-col>
          <el-col :span="6"><span  class="a" @click="jump('ccc')">Reviews</span></el-col>
          <el-col :span="6"><span class="a" @click="jump('ddd')">Map</span></el-col>
        </div>
        <el-tabs v-model="activeName" @tab-click="handleClick">
          <template>
            <div>
              <!--                <el-card id="photo"></el-card>-->
              <!-- 内容区域 -->
              <!--                <div  style="text-align:left;margin-left: 40px">-->

              <el-card id="aaa" align="left">
                <h1 align="center">Overview</h1>
                <h4><i class = "el-icon-document"></i> Description</h4>
                <el-main>{{description}}</el-main>
                <h4><i class="el-icon-house"></i> Type: {{property_type}}</h4>
                <h4><i class="icon iconfont iconrenshu"></i> Guests: {{guests}}</h4>
                <el-row>
                  <el-col :span="12" align="middle"><span><i class="icon iconfont iconchuang"></i> Bedroom: {{bedrooms}}</span></el-col>
                  <el-col :span="12" align="middle"><span><i class="icon iconfont iconyushiyongpin"></i> Bathrooms: {{bathrooms}}</span></el-col>
                </el-row>
                <el-row>
                  <el-col :span="6" align="middle"><span>Single bed: {{single_bed}}</span></el-col>
                  <el-col :span="6" align="middle"><span>Double bed: {{double_bed}}</span></el-col>
                  <el-col :span="12"></el-col>
                </el-row>
                <el-row>
                  <el-col :span="6" align="middle"><span>Queen bed: {{queen_bed}}</span></el-col>
                  <el-col :span="6" align="middle"><span>King bed: {{king_bed}}</span></el-col>
                  <el-col :span="12"></el-col>
                </el-row>

                <!--                    <el-divider></el-divider>-->
              </el-card>
              <el-card id="bbb">
                <h1>Amenities</h1>
                <el-row>
                  <el-col :span="12" align="left"><i class="iconicon-test1" style="font-size: 25px"><span v-if="show_amentities('TV')"> television</span><span v-else><del> television</del></span></i></el-col>
                  <el-col :span="12" align="left"><i class="el-icon-thirdgarage" style="font-size: 25px"><span v-if="show_amentities('Garage')"> Garage</span><span v-else><del> Garage</del></span></i></el-col>
                </el-row>
                <el-row>
                  <el-col :span="12" align="left"><i class="el-icon-thirdhongganji" style="font-size: 25px"><span v-if="show_amentities('Clothes dryer')"> Clothes dryer</span><span v-else><del> Clothes dryer</del></span></i></el-col>
                  <el-col :span="12" align="left"><i class="el-icon-thirdbeidangenghuan" style="font-size: 25px"><span v-if="show_amentities('Linens provided')"> Linens provided</span><span v-else><del> Linens provided</del></span></i></el-col>
                </el-row>
                <el-row>
                  <el-col :span="12" align="left"><i class="el-icon-thirdairconditioning" style="font-size: 25px"><span v-if="show_amentities('Air conditioning')"> Air conditioning</span><span v-else><del> Air conditioning</del></span></i></el-col>
                  <el-col :span="12" align="left"><i class="el-icon-thirdweibolu" style="font-size: 25px"><span v-if="show_amentities('Microwave')"> Microwave</span><span v-else><del> Microwave</del></span></i></el-col>
                </el-row>
                <el-row>
                  <el-col :span="12" align="left"><i class="el-icon-thirdkaoxiang" style="font-size: 25px"><span v-if="show_amentities('Oven')"> Oven</span><span v-else><del> Oven</del></span></i></el-col>
                  <el-col :span="12" align="left"><i class="el-icon-thirdcarpark" style="font-size: 25px"><span v-if="show_amentities('Parking')"> Parking</span><span v-else><del> Parking</del></span></i></el-col>
                </el-row>
                <el-row>
                  <el-col :span="12" align="left"><i class="el-icon-thirdicon-test10" style="font-size: 25px"><span v-if="show_amentities('No Smoking')"> No Smoking</span><span v-else><del> No Smoking</del></span></i></el-col>
                  <el-col :span="12" align="left"><i class="el-icon-thirdHairdryer" style="font-size: 25px"><span v-if="show_amentities('Hair dryer')"> Hair dryer</span><span v-else><del> Hair dryer</del></span></i></el-col>
                </el-row>
                <el-row>
                  <el-col :span="12" align="left"><i class="el-icon-thirdwuzhangaisheshi" style="font-size: 25px"><span v-if="show_amentities('Accessible')"> Accessible</span><span v-else><del> Accessible</del></span></i></el-col>
                  <el-col :span="12" align="left"><i class="el-icon-thirdbingxiang" style="font-size: 25px"><span v-if="show_amentities('Fridge')"> Fridge</span><span v-else><del> Fridge</del></span></i></el-col>
                </el-row>
                <el-row>
                  <el-col :span="12" align="left"><i class="el-icon-thirdicon-test4" style="font-size: 25px"><span v-if="show_amentities('Wireless Internet')"> Wireless Internet</span><span v-else><del> Wireless Internet</del></span></i></el-col>
                  <el-col :span="12" align="left"><i class="el-icon-thirdWashingmachine" style="font-size: 25px"><span v-if="show_amentities('Washing machine')"> Washing machine</span><span v-else><del> Washing machine</del></span></i></el-col>
                </el-row>
                <el-row>
                  <el-col :span="12" align="left"><i class="el-icon-thirdnuanqi" style="font-size: 25px"><span v-if="show_amentities('Heating')"> Heating</span><span v-else><del> Heating</del></span></i></el-col>
                  <el-col :span="12" align="left"><i class="el-icon-thirdindoorpool" style="font-size: 25px"><span v-if="show_amentities('Swimming pool')"> Swimming pool</span><span v-else><del> Swimming pool</del></span></i></el-col>
                </el-row>
                <el-row>
                  <el-col :span="12" align="left"><i class="el-icon-thirdBathtub" style="font-size: 25px"><span v-if="show_amentities('Hot Tub')"> Hot Tub</span><span v-else><del> Hot Tub</del></span></i></el-col>
                  <el-col :span="12" align="left"><i class="el-icon-thirdicon-test1" style="font-size: 25px"><span v-if="show_amentities('Elevator')"> Elevator</span><span v-else><del> Elevator</del></span></i></el-col>
                </el-row>
                <el-row>
                  <el-col :span="12" align="left"><i class="el-icon-thirdBlendermixer" style="font-size: 25px"><span v-if="show_amentities('Blender')"> Blender</span><span v-else><del> Blender</del></span></i></el-col>
                  <el-col :span="12" align="left"><i class="el-icon-thirdkexiedaichongwu" style="font-size: 25px"><span v-if="show_amentities('Pets Welcome')"> Pets Welcome</span><span v-else><del> Pets Welcome</del></span></i></el-col>
                </el-row>
                <el-row>
                  <el-col :span="12" align="left"><i class="el-icon-thirdToaster" style="font-size: 25px"><span v-if="show_amentities('Toaster')"> Toaster</span><span v-else><del> Toaster</del></span></i></el-col>
                  <el-col :span="12" align="left"><i class="el-icon-thirdshaokaoqiju" style="font-size: 25px"><span v-if="show_amentities('BBQ')"> BBQ</span><span v-else><del> BBQ</del></span></i></el-col>
                </el-row>
                <!--                    <i class="el-icon-thirdicon-test">television</i>       <i class="el-icon-thirdicon-test">television</i>-->
              </el-card>
              <el-card id="ccc">
                <h1>Review</h1>
                <el-row style="border-top: none;">
                  <el-col style="border-top: none;">
                    <!--                        <el-carousel height="300px" :autoplay="false" indicator-position=none :loop="false">-->
                    <!--                          &lt;!&ndash;遍历图片地址,动态生成轮播图&ndash;&gt;-->
                    <!--                          <el-carousel-item v-for="item in word_list" :key="item">-->
                    <!--                            <el-main align="left">-->
                    <!--                              <td><el-avatar id="toolbar-avatar1" :size="50" :src="img0" style="margin-top: 0px"></el-avatar></td>-->
                    <!--                              <td>-->
                    <!--                                <el-main style="margin-top: 0px">HOSTNAME-->
                    <!--                                  December 2019</el-main>-->
                    <!--                              </td>{{item}}-->
                    <!--                            </el-main>-->
                    <!--                          </el-carousel-item>-->
                    <!--                        </el-carousel>-->
                    <div id="example">
                      <!-- 利用v-if…v-else切换 展开 和 收起 两个画面，template包裹多个元素 -->
                      <template v-if="isHide">
                        <!-- 只显示摘要的画面 -->
                        <div class="hideBg">
                          <p class="summary">{{ content }}</p>
                          <div class="showBtn">
                            <!-- 绑定点击事件onShow，点击展开全文 -->
                            <a href="#" @click.stop.prevent="onShow">read more&nbsp;
                              <!-- 向下的角箭头符号，用css画 -->
                              <span class="downArrow"></span>
                            </a>
                          </div>
                        </div>
                      </template>
                      <template v-else>
                        <!-- 显示完整内容的画面 -->
                        <div class="showBg">
                          <p>{{ content }}</p>
                          <div class="hideBtn">
                            <!-- 绑定点击事件onHide，点击收起内容 -->
                            <a href="#" @click.stop.prevent="onHide">hide&nbsp;
                              <!-- 向上的角箭头符号 -->
                              <span class="upArrow"></span>
                            </a>
                          </div>
                        </div>
                      </template>
                    </div>
                  </el-col>
                </el-row>
              </el-card>
              <el-card id="ddd">
                <h1>Map</h1>
                <MapView></MapView>
              </el-card>
              <div style="border: none;height: 0;width: 0">
              </div>
            </div>
          </template>
        </el-tabs>
      </el-aside>
      <el-main style="margin-right: 80px;margin-top: 100px">
        <el-divider><h3>Related recommendations</h3></el-divider>
      </el-main>
    </el-container>
  </div>
</template>

<script>
// import MapView from './MapView'
export default {
  components: {},
  offsetTop: 0,
  name: 'Details',
  props: {},
  data () {
    return {
      rate: '',
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
      img_list: '',
      amentities: '#bar#pick up#wifi#TV#BBQ',
      isFixed: '',
      pickerOptions: {
        disabledDate: function (time) {
          return time.getTime() < Date.now() - 8.64e7
        }
      },
      start_date: '10/04/2020',
      end_date: '09/06/2020',
      period: '',
      host_name: '',
      host_avatar: '',
      price: '',
      total: '',
      property_type: '',
      cleaning_fee: '',
      ruleForm: {
        name: '',
        region: '',
        d1: '11/10/2020',
        d2: '06/08/2020',
        date1: '',
        date_s: '',
        date_e: '',
        date2: ''
      },
      active: 0, // 当前激活的导航索引

      content: 'Nice appartment, small but ok. But the communication was non existent. My elevator key card didn\'t work properly. so it closed me out of the building three times, once even at 2.00am. The owners (these are investors who have people that work for them) do not really care that you are constantly locked out. Asking for a new key card is no use they tell you that things are all right. I asked for a refund since it was impossible to get to the appartment. They didn\'t give any. This is a place to a place to bypass. 中华人民共和国位于亚洲东部，太平洋西岸 [1]  ，是工人阶级领导的、以工农联盟为基础的人民民主专政的社会主义国家 [2]  。1949年（己丑年）10月1日成立 [3-4]  ，以五星红旗为国旗 [5]  ，《义勇军进行曲》为国歌 [6]  ，国徽内容包括国旗、天安门、齿轮和麦稻穗 [7]  ，首都北京 [8]  ，省级行政区划为23个省、5个自治区、4个直辖市、2个特别行政区 [9]  ，是一个以汉族为主体民族，由56个民族构成的统一多民族国家，汉族占总人口的91.51% [10]  。新中国成立后，随即开展经济恢复与建设 [11]  ，1953年开始三大改造 [12]  ，到1956年确立了社会主义制度，进入社会主义探索阶段 [13]  。文化大革命之后开始改革开放，逐步确立了中国特色社会主义制度。 [14] 中华人民共和国陆地面积约960万平方公里，大陆海岸线1.8万多千米，岛屿岸线1.4万多千米，内海和边海的水域面积约470多万平方千米。海域分布有大小岛屿7600多个，其中台湾岛最大，面积35798平方千米。 [1]  陆地同14国接壤，与6国海上相邻。Nice appartment, small but ok. But the communication was non existent. My elevator key card didn\'t work properly. so it closed me out of the building three times, once even at 2.00am. The owners (these are investors who have people that work for them) do not really care that you are constantly locked out. Asking for a new key card is no use they tell you that things are all right. I asked for a refund since it was impossible to get to the appartment. They didn\'t give any. This is a place to a place to bypass. 中华人民共和国位于亚洲东部，太平洋西岸 [1]  ，是工人阶级领导的、以工农联盟为基础的人民民主专政的社会主义国家 [2]  。1949年（己丑年）10月1日成立 [3-4]  ，以五星红旗为国旗 [5]  ，《义勇军进行曲》为国歌 [6]  ，国徽内容包括国旗、天安门、齿轮和麦稻穗 [7]  ，首都北京 [8]  ，省级行政区划为23个省、5个自治区、4个直辖市、2个特别行政区 [9]  ，是一个以汉族为主体民族，由56个民族构成的统一多民族国家，汉族占总人口的91.51% [10]  。新中国成立后，随即开展经济恢复与建设 [11]  ，1953年开始三大改造 [12]  ，到1956年确立了社会主义制度，进入社会主义探索阶段 [13]  。文化大革命之后开始改革开放，逐步确立了中国特色社会主义制度。 [14] 中华人民共和国陆地面积约960万平方公里，大陆海岸线1.8万多千米，岛屿岸线1.4万多千米，内海和边海的水域面积约470多万平方千米。海域分布有大小岛屿7600多个，其中台湾岛最大，面积35798平方千米。 [1]  陆地同14国接壤，与6国海上相邻。',
      isHide: true, // 初始值为true，显示为折叠画面
      word_list: [
        'Nice appartment, small but ok. But the communication was non existent. My elevator key card didn\'t work properly. so it closed me out of the building three times, once even at 2.00am. The owners (these are investors who have people that work for them) do not really care that you are constantly locked out. Asking for a new key card is no use they tell you that things are all right. I asked for a refund since it was impossible to get to the appartment. They didn\'t give any. This is a place to a place to bypass.',
        'dear Emma…Thank you for choosing us. Sometimes because of bugs in the airbnb system, we are often unable to get the message out and are a little late in responding. If you have any questions, please call our service number at any time. I think that might be more conducive to timely communication. But anyway, thanks for your support.',
        'This place was an amazing place to stay in Bangkok! The area feels safe and within walking distance to BTS and MRT (a bit of a walk but it\'s worth it!) The room was clean and the check in process was easy. The host give you all the information you need before the time.',
        'Amazing place! Will definitely stay again!',
        'In a great location! Only thing missing was a iron and ironing board. Clothes were fresh out the suitcase and wrinkled! There is space to hang fold ironing board from wall unit.',
        'The apartment is a small one, but it is perfect for staying with friends. The pool was nice too and so was the view. Parking was also perfect.'
      ],

      // 图片地址数组
      img0: '/static/image/111.png',
      img1: '/static/image/222.png',
      // 图片父容器高度
      bannerHeight: 1000,
      // 浏览器宽度
      screenWidth: 0
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
    this.getDetails()
    this.ruleForm.d1 = this.start_date.split('/')[1] + '/' + this.start_date.split('/')[0] + '/' + this.start_date.split('/')[2]
    this.ruleForm.d2 = this.end_date.split('/')[1] + '/' + this.end_date.split('/')[0] + '/' + this.end_date.split('/')[2]
    this.list_amenities = this.amentities.split('#')
  },
  methods: {
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
          this.amentities = res.data.body.amentities
          this.host_avatar = res.data.body.host_avatar
          this.suburb = res.data.body.suburb
          this.property_type = res.data.body.property_type
          this.rate = res.data.body.rating
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
      // console.log(height)
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
      if (scrollTop > this.offsetTop) {
        this.isFixed = true
      } else {
        this.isFixed = false
      }
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
    window.addEventListener('scroll', this.initHeight)
    this.$nextTick(() => {
      this.offsetTop = document.querySelector('#boxFixed').offsetTop
    })
    // 监听滚动事件
    window.addEventListener('scroll', this.onScroll, false)
    // 首次加载时,需要调用一次
    this.screenWidth = window.innerWidth
    this.setSize()
    // 窗口大小发生改变时,调用一次
    window.onresize = () => {
      this.screenWidth = window.innerWidth
      this.setSize()
    }
  }
}
</script>

<style scoped>
  /* 内容区的样式 */
  .demo-ruleForm{
    margin-top: -140px;
    margin-left: 60px;
    top: 100px;
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
    background-color: #e9ecef;
    /*margin: 1.5rem;*/
    /*padding: 1.5rem;*/
    /*padding-bottom: 0;    !* 方便渐变层遮挡 *!*/
    position: relative;    /* 用于子元素定位 */
  }
  /* 全文背景板，基本与摘要相同 */
  .showBg {
    /*width: 500px;*/
    background-color: #e9ecef;
    /*margin: 1.5rem;*/
    /*padding: 1.5rem;*/
  }
  /* 摘要内容 */
  .summary {
    overflow: hidden;    /* 隐藏溢出内容 */
    text-overflow: clip;    /* 修剪文本 */
    display: -webkit-box;    /* 弹性布局 */
    -webkit-box-orient: vertical;    /* 从上向下垂直排列子元素 */
    -webkit-line-clamp: 5;    /* 限制文本仅显示前三行 */
  }
  #example p {
    text-indent: 2em;
  }
  /* 展开按钮 */
  .showBtn {
    width: 100%;    /* 与背景宽度一致 */
    height: 3rem;
    position: absolute;    /* 相对父元素定位 */
    top: 3rem;    /* 刚好遮挡在最后两行 */
    left: 0;
    z-index: 0;    /* 正序堆叠，覆盖在p元素上方 */
    text-align: center;
    background: linear-gradient(rgba(233,236,239,.5), white);    /* 背景色半透明到白色的渐变层 */
    padding-top: 3rem;
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
