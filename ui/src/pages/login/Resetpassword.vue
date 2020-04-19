<template>
  <div class="img_box">
    <div class="login-panel">
      <div class="panel-header"><h2>Reset password</h2></div>
      <div class="panel-form">
        <el-form :model="user" :rules="rules" ref="ruleForm">
          <el-form-item prop="email">
            <el-input v-model="user.email" placeholder="user.email" :disabled="true" clearable></el-input>
          </el-form-item>
          <el-form-item prop="password">
            <el-input v-model="user.password" show-password placeholder="Enter your password" clearable class="form-data"></el-input>
          </el-form-item>
          <el-form-item prop="password2">
            <el-input v-model="user.password2" show-password placeholder="Confirm Password" clearable></el-input>
          </el-form-item>
        </el-form>
        <div class="panel-form-button">
          <el-button type="primary" style="width: 100%; height: 100%" @click="resetAction">
<!--            <el-row>-->
<!--              <el-col :span="12"><div style="text-align: left"><span>Next</span></div></el-col>-->
<!--              <el-col :span="12">-->
<!--                <div style="text-align: right"><span><i class="el-icon-right"></i></span></div>-->
<!--              </el-col>-->
<!--            </el-row>-->
              <span>Next&nbsp;</span><i class="el-icon-right"></i>
          </el-button>
        </div>
        <div class="cancel">
          <el-button type="info" style="width: 100%; height: 100%" @click="cancel">cancel</el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Resetpassword',
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
    var validatePass = (rule, value, callback) => {
      const reg = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$/
      const password = reg.test(value)
      if (value === '') {
        callback(new Error('Please input the password'))
      } else if (value.length < 6) {
        callback(new Error('Too short ! enter at least 6 characters'))
      } else if (value.length > 20) {
        callback(new Error('Too long ! enter no more than 20 characters'))
      } else if (!password) {
        callback(new Error('must contain at least one numeric digit, one uppercase and one lowercase letter'))
      } else {
        if (this.user.password2 !== '') {
          this.$refs.user.validateField('checkPass')
        }
        callback()
      }
    }
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('Please input the password again'))
      } else if (value !== this.user.password) {
        callback(new Error('Two passwords don\'t match!'))
      } else {
        callback()
      }
    }
    return {
      user: {
        email: '',
        password: '',
        password2: ''
      },
      rules: {
        email: [{ required: true, message: 'please enter the email', trigger: 'blur' }, { validator: isEmail, trigger: 'blur' }],
        password: [{ required: true, message: 'please enter the password', trigger: 'blur' }, { validator: validatePass, trigger: 'blur' }],
        password2: [{ validator: validatePass2, trigger: 'blur' }]
      }
    }
  },
  created () {
    this.token = this.$route.query.token
    this.$axios.get('/api/emailvalidation?token=' + this.token)
      .then((response) => {
        this.user.email = response.data.email
      })
      .catch(function (error) {
        console.log(error)
      })
  },
  methods: {
    resetAction () {
      if (this.user.email === '' || this.user.password === '') {
        this.$message.error('please enter each input.')
      } else {
        let data = this.$qs.stringify({
          email: this.user.email,
          new_password: this.user.password
        })
        this.$axios.post('/api/reset_password', data)
          .then((response) => {
            console.log(response.data)
            // TODO Check response if the email has been registered with response['code']=101
            if (response.data.code === 0) {
              this.$message('Successful change the password')
              this.$router.push({path: '/login'})
            } else {
              this.$message.error('error')
            }
          })
          .catch(function (error) {
            console.log(error)
          })
      }
    },
    cancel () {
      this.$router.push({path: '/login'})
    }
  }
}
</script>

<style scoped>
  .img_box{
    margin-left: 25px;
    width: 100% ;height: 100%;
    background-image: url(/static/hello.jpg);
    /*background-size: cover;  使图片平铺满整个浏览器（从宽和高的最大需求方面来满足，会使某些部分无法显示在区域中） */
    position: absolute; /* 不可缺少 */
    z-index: -1;
    background-repeat: no-repeat;
    /* overflow: hidden; */
    /* overflow: auto; */
  }
  .overlap-bottom >>> .el-input__inner {
    margin-bottom: 1px;
  }
  .overlap-left >>> .el-input__inner {
    margin-left: -1px;
  }
  >>> .el-input__inner {
    border-radius: 0;
    border-collapse: collapse
  }
  .el-button {
    border-radius: 0;
  }
  .login-panel {
    margin-top: 70px;
    margin-right: 10%;
    margin-left: 45%;
    padding: 0px;
    /* border-radius: 20px;
    background: #e4e4e4; */
  }
  .panel-form {
    margin-right: 13%;
    margin-left: 13%;
  }
  .panel-form-name {
    margin-top: 10px;
  }
  .panel-form-button {
    margin-top: 10px;
  }
  .cancel {
    margin-top: 15px;
    text-align: left;
  }

</style>
