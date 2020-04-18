<template>
  <el-container>
    <el-header style="font-size: 20px; height: 70px; border-bottom: 1px solid rgb(220, 223, 230)">
      <div class="top-navigator">
        <el-row :gutter="20">
          <el-col :span="2">
            <div class="top-logo">
              <img @click="linkToBack" src="@/assets/logosimple.png" alt="render failure"
                   style="width: 60px; height:60px; cursor: pointer">
            </div>
          </el-col>
          <!--
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
          !-->
          <el-col :span="12">
            <div class="slogan">
              <h4 style="font-family:Georgia;color: #222222">PANDA VALLEY</h4>
              <!--
              <img @click="linkToBack" src="@/assets/slogan.png" alt=""
                   style="width: 180px; height: 70px; cursor: pointer">
                    -->
            </div>
          </el-col>
          <el-col :span="6" :offset="4">
            <div v-if="!this.$store.state.user" class="top-action">
              <el-button @click="linkToLogin" style="border: none; width: 100px;" round>
                <i class="iconfont icondenglu"></i>
                <span>Log in</span>
              </el-button>
              <el-button @click="linkToSignup" type="primary" style="width: 100px;" round>
                <i class="iconfont iconzhuce"></i>
                <span>Sign up</span>
              </el-button>
            </div>
            <div v-else class="top-user">
              <el-dropdown>
                <div class="user-dropdown">
                  <el-avatar id="toolbar-avatar" :src="imageUrl" style="vertical-align: middle"></el-avatar>
                   {{ this.$store.state.user }}
                </div>
                <el-dropdown-menu slot="dropdown">
                  <el-dropdown-item @click.native="linkToProfile">Profile</el-dropdown-item>
                  <el-dropdown-item @click.native="linkToAddProperty">Add property</el-dropdown-item>
                  <el-dropdown-item @click.native="linkToProperty">My Properties</el-dropdown-item>
                  <el-dropdown-item @click.native="linkToBooking">My Bookings</el-dropdown-item>
<!--                  <el-dropdown-item>Messages</el-dropdown-item>-->
                  <el-dropdown-item @click.native="linkToWishlist">Watchlist</el-dropdown-item>
<!--                  <el-dropdown-item>English (AU)</el-dropdown-item>-->
<!--                  <el-dropdown-item>$ AUD</el-dropdown-item>-->
                  <el-dropdown-item @click.native="logoutAction">Logout</el-dropdown-item>
                </el-dropdown-menu>
              </el-dropdown>
            </div>
          </el-col>
        </el-row>
      </div>
    </el-header>
    </el-container>
</template>

<script>
import bus from '../assets/eventBus'
export default {
  name: 'Toolbar',
  data () {
    return {
      searchArea: '',
      imageUrl: ''
    }
  },
  created () {
    this.$axios.get('/api/pass_user_info?email=' + this.$store.getters.getStorage)
      .then((response) => {
        if (response.data.code === 0) {
          this.imageUrl = response.data.avatar_url
          console.log(this.imageUrl)
        }
      })
      .catch(function (error) {
        console.log(error)
      })
    bus.$on('updateUserAvatar', (params) => {
      this.imageUrl = params
      console.log(params)
    })
    bus.$on('displayUserAvatar', (params) => {
      this.imageUrl = params
    })
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
    },
    linkToProfile () {
      this.$router.push({path: '/profile'})
    },
    linkToAddProperty () {
      this.$router.push({path: '/add_property'})
    },
    linkToBooking () {
      this.$router.push({path: '/booking'})
    },
    linkToWishlist () {
      this.$router.push({path: '/wishlist'})
    },
    linkToProperty () {
      this.$router.push({path: '/myproperty'})
    },
    searchAction () {

    },
    logoutAction () {
      this.$store.commit('$_removeStorage')
      this.$router.push({path: '/'})
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
    margin-top: 0px;
  }
  .slogan{
    text-align: left;
    margin-top: 0px;
  }
  .top-search {
    text-align: left;
    margin-top: 12px;
  }
  .top-action {
    text-align: left;
    margin-top: 10px;
  }
  .top-user {
    text-align: center;
    margin-top: 12px;
  }
  .user-dropdown {
    cursor: pointer;
    color: #409EFF;
  }
</style>
