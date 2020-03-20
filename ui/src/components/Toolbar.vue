<template>
  <el-container>
    <el-header style="font-size: 20px; height: 70px; border-bottom: 1px solid rgb(220, 223, 230)">
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
          <el-col :span="6" :offset="3">
            <div v-if="!this.$store.state.user" class="top-action">
              <el-button @click="linkToSignup" type="primary" round>Sign up</el-button>
              <el-button @click="linkToLogin" type="primary" round>Log in</el-button>
            </div>
            <div v-else class="top-user">
              <el-dropdown>
                <div class="user-dropdown">
                  <el-avatar id="toolbar-avatar" :src="imageUrl" style="vertical-align: middle"></el-avatar>
                   {{ this.$store.state.user }}
                </div>
                <el-dropdown-menu slot="dropdown">
                  <el-dropdown-item @click.native="linkToProfile">Profile</el-dropdown-item>
                  <el-dropdown-item>My Properties</el-dropdown-item>
                  <el-dropdown-item>My Bookings</el-dropdown-item>
                  <el-dropdown-item>Messages</el-dropdown-item>
                  <el-dropdown-item>Watchlist</el-dropdown-item>
                  <el-dropdown-item>English (AU)</el-dropdown-item>
                  <el-dropdown-item>$ AUD</el-dropdown-item>
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
        }
      })
      .catch(function (error) {
        console.log(error)
      })
    bus.$on('updateUserAvatar', (params) => {
      this.imageUrl = params
      console.log(params)
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
  .top-user {
    text-align: center;
    margin-top: 12px;
  }
  .user-dropdown {
    cursor: pointer;
    color: #409EFF;
  }

</style>
