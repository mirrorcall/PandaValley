<template>
  <!--
  <div class="signup-panel">
    <div class="panel-header"><h2>Create an account with PandaValley</h2></div>
    <div class="panel-form" @keyup.enter="signupAction">
      <div class="panel-form-email">
        <el-input style="border-radius: 0" v-model="user.email" placeholder="Email" clearable class="form-data"></el-input>
      </div>
      <div class="panel-form-name">
        <el-row>
          <el-col :span="12"><el-input class="overlap-bottom" v-model="user.firstName" placeholder="First Name" clearable></el-input></el-col>
          <el-col :span="12"><el-input class="overlap-bottom overlap-left" v-model="user.lastName" placeholder="Last Name" clearable></el-input></el-col>
        </el-row>
        <el-input class="overlap-bottom" v-model="user.telephone" placeholder="Telephone" clearable></el-input>
        <el-input v-model="user.password" show-password placeholder="Create Password" clearable></el-input>
      </div>
      <div class="panel-form-button">
        <el-button type="primary" style="width: 100%; height: 100%" @click="signupAction">
          <el-row>
            <el-col :span="12"><div style="text-align: left;"><span>Next</span></div></el-col>
            <el-col :span="12">
              <div style="text-align: right"><span><i class="el-icon-right"></i></span></div>
            </el-col>
          </el-row>
        </el-button>
      </div>
    </div>
  </div>
  -->
  <div class="img_box">
  <div class="signup-panel">
    <div class="panel-header"><h2>Create an account with PandaValley</h2></div>
    <div class="panel-form" @keyup.enter="signupAction">
      <el-form :model="user" status-icon :rules="rules" ref="user">
        <el-form-item prop="email">
          <el-input style="border-radius: 0" v-model="user.email" placeholder="Email" clearable class="form-data"></el-input>
        </el-form-item>
        <el-row>
          <el-col :span="12">
            <el-form-item prop="firstName">
              <el-input class="overlap-bottom" v-model="user.firstName" placeholder="First Name" clearable></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item prop="lastName">
              <el-input class="overlap-bottom overlap-left" v-model="user.lastName" placeholder="Last Name" clearable></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-form-item prop="telephone">
          <el-input class="overlap-bottom" v-model="user.telephone" placeholder="Telephone" clearable></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input v-model="user.password" show-password placeholder="Create Password with 6 to 20 characters" clearable></el-input>
        </el-form-item>
        <el-form-item prop="password2">
          <el-input v-model="user.password2" show-password placeholder="Confirm Password" clearable></el-input>
        </el-form-item>
        <div class="panel-form-button">
          <el-button type="primary" style="width: 100%; height: 100%" @click="signupAction">
<!--            <el-row>-->
<!--              <el-col :span="12"><div style="text-align: left;"><span>Next</span></div></el-col>-->
<!--              <el-col :span="12">-->
<!--                <div style="text-align: right"><span><i class="el-icon-right"></i></span></div>-->
<!--              </el-col>-->
<!--            </el-row>-->
            <span>Next&nbsp;</span><i class="el-icon-right"></i>
          </el-button>
        </div>
      </el-form>
    </div>
  </div>
  </div>
</template>

<script>
export default {
  name: 'Signup',
  data () {
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
    var validatePhone = (rule, value, callback) => {
      const reg = /^(?:\+?61|0)4 ?(?:(?:[01] ?[0-9]|2 ?[0-57-9]|3 ?[1-9]|4 ?[7-9]|5 ?[018]) ?[0-9]|3 ?0 ?[0-5])(?: ?[0-9]){5}$/
      const phone = reg.test(value)
      if (value === '') {
        callback(new Error('Please enter the phone number'))
      } else if (!phone) {
        callback(new Error('invalid phone number'))
      } else {
        callback()
      }
    }
    return {
      // TODO Check input validity by @onfocus
      user: {
        email: '',
        firstName: '',
        lastName: '',
        telephone: '',
        password: '',
        password2: ''
      },
      rules: {
        email: [{ required: true, message: 'please enter the email', trigger: 'blur' }, { validator: isEmail, trigger: 'blur' }],
        password: [{ validator: validatePass, trigger: 'blur' }],
        password2: [{ validator: validatePass2, trigger: 'blur' }],
        firstName: [{ required: true, trigger: 'blur' }],
        lastName: [{ required: true, trigger: 'blur' }],
        telephone: [{ required: true, message: 'please enter the telephone', trigger: 'blur' }, { validator: validatePhone, trigger: 'blur' }]
      }
    }
    function isEmail (rule, value, callback) {
      const reg = /^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$/
      const email = reg.test(value)
      if (!email) {
        callback(new Error('invalid email format'))
      } else {
        callback()
      }
    }
  },
  methods: {
    signupAction () {
      if (this.user.email === '' || this.user.firstName === '' || this.user.lastName === '' || this.user.telephone === '' || this.user.password === '') {
        this.$message.error('please enter each input.')
      } else {
        let data = this.$qs.stringify({
          email: this.user.email,
          first_name: this.user.firstName,
          last_name: this.user.lastName,
          telephone: this.user.telephone,
          password: this.user.password
        })
        this.$axios.post('/api/join', data)
          .then((response) => {
            console.log(response.data)
            // TODO Check response if the email has been registered with response['code']=101
            if (response.data.code === 1) {
              this.$message.error('This email has been registered')
            } else {
              this.$router.push({path: '/'})
            }
          })
          .catch(function (error) {
            console.log(error)
          })
      }
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
  .signup-panel {
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
</style>
