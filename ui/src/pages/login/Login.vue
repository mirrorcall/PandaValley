<template>
  <div class="img_box">
  <div class="login-panel">
    <div class="panel-header"><h2>Sign in to PandaValley</h2></div>
    <div class="panel-form">
      <el-form :model="user" :rules="rules" ref="ruleForm">
        <el-form-item prop="email">
          <el-input v-model="user.email" placeholder="Enter your email" clearable></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input v-model="user.password" show-password placeholder="Enter your password" clearable class="form-data"></el-input>
        </el-form-item>
      </el-form>
      <div class="panel-form-button">
        <el-button type="primary" style="width: 100%; height: 100%" @click="loginAction">
<!--          <el-row>-->
<!--            <el-col :span="12"><div style="text-align: left"><span>Next</span></div></el-col>-->
<!--            <el-col :span="12">-->
<!--              <div style="text-align: right"><span><i class="el-icon-right"></i></span></div>-->
<!--            </el-col>-->
<!--          </el-row>-->
          <span>Next&nbsp;</span><i class="el-icon-right"></i>
        </el-button>
      </div>
      <div class="forget-password">
        <el-button type="info" style="width: 100%; height: 100%" @click="forgotPassword">Forgot Password ?</el-button>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data () {
    function isEmail (rule, value, callback) {
      const reg = /^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$/
      const email = reg.test(value)
      if (!email) {
        callback(new Error('invalid email format'))
      } else {
        callback()
      }
    }
    return {
      user: {
        email: '',
        password: ''
      },
      rules: {
        email: [{ required: true, message: 'please enter the email', trigger: 'blur' }, { validator: isEmail, trigger: 'blur' }],
        password: [{ required: true, message: 'please enter the password', trigger: 'blur' }]
      }
    }
  },
  methods: {
    loginAction () {
      let data = this.$qs.stringify(this.user)
      this.$axios.post('/api/login', data)
        .then((response) => {
          if (response.data.code === 0) {
            console.log('login successfully')
            this.$store.commit('$_setStorage', response.data.email)
            this.$router.push({name: 'Home'})
          } else if (response.data.code === 1) { // TODO handle incorrect password
            this.$message.error('Wrong email or password')
            console.log(response.data.msg)
          }
        })
        .catch(function (error) {
          console.log('ERROR')
          console.log(error)
        })
    },
    forgotPassword () {
      let data = this.$qs.stringify({email: this.user.email})
      this.$axios.post('/api/forget_password', data)
        .then((response) => {
          if (response.data.code === 0) {
            this.$message('The confirmation email has been sent to your email address.')
            console.log('email is correct')
          } else if (response.data.code === 1) {
            this.$message('Your email is incorrect')
            console.log(response.data.msg)
          }
        })
        .catch((res) => {
          console.log('error ', res)
          this.$message({
            type: 'error',
            message: 'email is incorrect'
          })
        })
    }
  }
}
</script>

<style scoped>
  .img_box{
    margin-left: 25px;
    width: 100% ;
    height: 100%;
    background-image: url(/static/hello.jpg);
    /*background-size: cover;  使图片平铺满整个浏览器（从宽和高的最大需求方面来满足，会使某些部分无法显示在区域中） */
    position: absolute; /* 不可缺少 */
    z-index: -1;
    background-repeat: no-repeat;
    /* overflow: hidden; */
    /* overflow: auto; */
  }
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
    margin-left: 50%;
  }
  .panel-form {
    margin-right: 13%;
    margin-left: 13%;
  }
  .panel-form-button {
    margin-top: 10px;
  }
  .forget-password {
    margin-top: 15px;
    text-align: left;
  }
</style>
