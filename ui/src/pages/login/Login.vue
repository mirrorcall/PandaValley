<template>
  <div class="login-panel">
    <div class="panel-header"><h2>Sign in to PandaValley</h2></div>
    <div class="panel-form">
      <el-input v-model="user.email" placeholder="Enter your email" clearable class="form-data overlap-bottom"></el-input>
      <el-input v-model="user.password" show-password placeholder="Enter your password" clearable class="form-data"></el-input>
      <div class="panel-form-button">
        <el-button type="primary" style="width: 100%; height: 100%" @click="loginAction">
          <el-row>
            <el-col :span="12"><div style="text-align: left"><span>Next</span></div></el-col>
            <el-col :span="12">
              <div style="text-align: right"><span><i class="el-icon-right"></i></span></div>
            </el-col>
          </el-row>
        </el-button>
      </div>
    </div>
  </div>
</template>

<script>
import bus from '../../assets/eventBus'
export default {
  name: 'Login',
  data () {
    return {
      user: {
        email: '',
        password: ''
      }
    }
  },
  methods: {
    loginAction () {
      let data = this.$qs.stringify(this.user)
      this.$axios.post('/api/login', data)
        .then((response) => {
          this.$store.commit('$_setStorage', response.data.email)
          if (response.data.code === 0) {
            console.log('login successfully')
            this.$axios.get('/api/pass_user_info?email=' + this.$store.getters.getStorage)
              .then((response) => {
                console.log(response)
                bus.$emit('displayUserAvatar', response.data.avatar_url)
              })
            this.$router.push({name: 'Home'})
          } else if (response.data.code === 1) { // TODO handle incorrect password
            console.log(response.data.msg)
          }
        })
        .catch(function (error) {
          console.log('ERROR')
          console.log(error)
        })
    }
  }
}
</script>

<style scoped>
  .overlap-bottom >>> .el-input__inner {
    border-bottom: 1px;
  }
  >>> .el-input__inner {
    border-radius: 0;
  }
  .el-button {
    border-radius: 0;
  }
  .login-panel {
    margin-top: 70px;
    margin-right: 10%;
    margin-left: 65%;
  }
  .panel-form {
    margin-right: 13%;
    margin-left: 13%;
  }
  .panel-form-button {
    margin-top: 10px;
  }
</style>
