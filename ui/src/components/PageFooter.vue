<template>
  <div>
    <div class="icon-banner">
      <div class="icons">
        <i class="iconfont iconfacebook icon"></i>
        <i class="iconfont icontwitter icon"></i>
        <i class="iconfont iconpinterest icon"></i>
      </div>
    </div>
    <div class="brand-banner">
      <div class="brand-relate">
        <el-row class="banner-row">
          <el-col :span="8">
            <el-row class="banner-title">EXPLORE PANDAVALLEY</el-row>
            <el-row class="banner-text">Travel extras</el-row>
            <el-row class="banner-text">Travel ideas</el-row>
            <el-row class="banner-text">Trust & Safety</el-row>
            <el-row class="banner-text">Help & Support</el-row>
            <el-row class="banner-text">List your property</el-row>
            <el-row class="banner-text">Booking management software</el-row>
            <el-row class="banner-text">Travel guides</el-row>
          </el-col>
          <el-col :span="8">
            <el-row class="banner-title">COMPANY</el-row>
            <el-row class="banner-text">Careers</el-row>
            <el-row class="banner-text">Terms & conditions</el-row>
            <el-row class="banner-text">Privacy Policy</el-row>
            <el-row class="banner-text">Media Center</el-row>
            <el-row class="banner-text">Media sales</el-row>
          </el-col>
          <el-col :span="8">
            <el-row class="banner-title">ABOUT US</el-row>
            <el-row class="banner-text">The PandaValley history</el-row>
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
.icon {
  padding-left: 20px;
}
.brand-banner {
  background-color: #ededed;
  text-align: left;
  width: 100%;
  height: 450px;
}
.brand-relate {
  margin-left: 50px;
}
.banner-row {
  padding-top: 20px;
}
.banner-title {
  font-weight: 800;
}
.banner-text {
  padding-top: 10px;
}
.copyright {
  margin-left: 50px;
}
</style>
