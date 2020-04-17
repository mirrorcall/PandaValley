<template>
  <div>
    <div class="icon-banner">
      <div class="icons">
        <a href="https://www.facebook.com/" target="_blank"><i class="iconfont iconfacebook icon"></i></a>
        <a href="https://twitter.com/explore" target="_blank"><i class="iconfont icontwitter icon"></i></a>
        <a href="https://www.pinterest.com.au/" target="_blank"><i class="iconfont iconpinterest icon"></i></a>
      </div>
    </div>
    <div class="brand-banner">
      <div class="brand-relate">
        <el-row class="banner-row">
          <el-col :span="8">
            <el-row class="banner-title">EXPLORE PANDAVALLEY</el-row>
            <el-row class="banner-text">Travel Extras</el-row>
            <el-row class="banner-text">Travel Ideas</el-row>
            <el-row class="banner-text">Trust & Safety</el-row>
            <el-row class="banner-text">Help & Support</el-row>
            <el-row class="banner-text">List Your Property</el-row>
            <el-row class="banner-text">Booking Management Software</el-row>
            <el-row class="banner-text">Travel Guides</el-row>
          </el-col>
          <el-col :span="8">
            <el-row class="banner-title">COMPANY</el-row>
            <el-row class="banner-text">Careers</el-row>
            <el-row class="banner-text">Terms & Conditions</el-row>
            <el-row class="banner-text">Privacy Policy</el-row>
            <el-row class="banner-text">Media Center</el-row>
            <el-row class="banner-text">Media Sales</el-row>
          </el-col>
          <el-col :span="8">
            <el-row class="banner-title">ABOUT US</el-row>
            <el-row class="banner-text">The PandaValley History</el-row>
            <el-row class="banner-text">PandaValley in Australia</el-row>
          </el-col>
        </el-row>
        <el-row class="banner-row">
          <el-col :span="8">
            <el-row class="banner-title">CONTACT US</el-row>
            <el-row class="banner-text">Contact Details</el-row>
          </el-col>
          <el-col :span="8">
            <el-row class="banner-title">CAREERS AT PANDAVALLEY</el-row>
            <el-row class="banner-text">Join The PandaValley Australia Team</el-row>
            <el-row class="banner-text">Learning & Development</el-row>
          </el-col>
          <el-col :span="8">
            <el-row class="banner-title">GLOBAL RESPONSIBILITY</el-row>
            <el-row class="banner-text">Ethical Sourcing</el-row>
            <el-row class="banner-text">Environmental Stewardship</el-row>
            <el-row class="banner-text">Community Involvement</el-row>
          </el-col>
        </el-row>
      </div>
      <div class="copyright">
        <div>
          Copyright &copy; 2020 PandaValley Australia. All Rights Reversed.
        </div>
        <div>
          Term of Use | Privacy Policy
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PageFooter'
}
</script>

<style scoped>
.icon-banner {
  width: 100%;
  height: 100px;
  background-color: #e7e7e7;
}
.icons {
  padding-top: 35px;
  margin-left: 50px;
  text-align: left;
}
a { color: inherit; }
.icon {
  padding-left: 20px;
}
.brand-banner {
  background-color: #ededed;
  text-align: left;
  width: 100%;
  height: 480px;
}
.brand-relate {
  margin-left: 50px;
}
.banner-row {
  padding-top: 20px;
}
.banner-title {
  font-weight: 800;
  font-size: 20px;
}
.banner-text {
  padding-top: 10px;
}
.copyright {
  margin-left: 50px;
}
</style>
