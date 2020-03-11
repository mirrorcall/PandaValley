<template>
    <el-container>
    <el-header style="font-size: 20px; height: 70px; border-bottom: 1px solid rgb(220, 223, 230)">
<!--      <span>Username</span>-->
<!--      <el-dropdown>-->
<!--        <i class="el-icon-setting"></i>-->
<!--        <el-dropdown-menu slot="dropdown">-->
<!--          <el-dropdown-item>Profile</el-dropdown-item>-->
<!--          <el-dropdown-item>Transaction</el-dropdown-item>-->
<!--          <el-dropdown-item>Log out</el-dropdown-item>-->
<!--        </el-dropdown-menu>-->
<!--      </el-dropdown>-->
      <div class="top-navigator">
        <el-row :gutter="20">
          <el-col :span="4" :offset="1">
            <div class="top-logo">
              <img @click="linkToBack" src="@/assets/panda.png" alt="render failure"
                   style="width: 60px; height: 60px; cursor: pointer">
            </div>
          </el-col>
          <el-col :span="10">
            <div class="top-search">
              <el-row>
                <el-col :span="10">
                  <el-input
                      v-model="searchArea"
                      placeholder="Search Suburbs within NSW"
                      prefix-icon="el-icon-search"
                      @click="searchAction"
                      @keyup.enter="searchAction"></el-input>
                </el-col>
                <el-col :span="13" :offset="1">
                  <el-button icon="el-icon-search" circle></el-button>
                </el-col>
              </el-row>
            </div>
          </el-col>
          <el-col :span="5" :offset="4">
            <div class="top-action">
              <el-button @click="linkToSignup" type="primary" round>Sign up</el-button>
              <el-button @click="linkToLogin" type="primary" round>Log in</el-button>
            </div>
          </el-col>
        </el-row>
      </div>
    </el-header>
    </el-container>
</template>

<script>
export default {
  name: 'Toolbar',
  data () {
    return {
      searchArea: ''
    }
  },
  methods: {
    // functions that map routers for buttons
    linkToBack () {
      this.$router.push({path: '/'})
    },
    linkToSignup () {
      this.$router.push({path: '/signup'})
      console.log('signup')
    },
    linkToLogin () {
      this.$router.push({path: '/login'})
      console.log('login')
    }
  }
}
</script>

<style scoped>
  .top-navigator {
    margin-left: 5%;
    margin-right: 5%;
    min-height: 60px;
  }
  .top-logo {
    text-align: left;
    margin-top: 3px;
  }
  .top-search {
    text-align: left;
    margin-top: 12px;
  }
  .top-action {
    text-align: left;
    margin-top: 10px;
  }
</style>
