<template>
  <div class="signup-panel">
    <div class="panel-header"><h2>Create an account with PandaValley</h2></div>
    <div class="panel-form">
      <div class="panel-form-email">
        <el-input style="border-radius: 0" v-model="user.email" placeholder="Email" clearable class="form-data"></el-input>
      </div>
      <div class="panel-form-name">
        <el-row>
          <el-col :span="12"><el-input v-model="user.firstName" placeholder="First Name" clearable></el-input></el-col>
          <el-col :span="12"><el-input v-model="user.lastName" placeholder="Last Name" clearable></el-input></el-col>
        </el-row>
        <el-input v-model="user.telephone" placeholder="Telephone" clearable></el-input>
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
</template>

<script>
export default {
  name: 'Signup',
  data () {
    return {
      // TODO Check input validity by @onfocus
      user: {
        email: '',
        firstName: '',
        lastName: '',
        telephone: '',
        password: ''
      }
    }
  },
  methods: {
    signupAction () {
      let data = this.$qs.stringify({
        email: this.user.email,
        first_name: this.user.firstName,
        last_name: this.user.lastName,
        telephone: this.user.telephone,
        password: this.user.password
      })
      this.$axios.post('http://127.0.0.1:8000/api/join', data)
        .then((response) => {
          console.log(response.data)
          // TODO Check response if the email has been registered with response['code']=101
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>

<style scoped>
  >>> .el-input__inner {
    border-radius: 0;
  }
  .el-button {
    border-radius: 0;
  }
  .signup-panel {
    margin-top: 70px;
    margin-left: 65%;
    margin-right: 10%;
  }
  .panel-form {
    margin-left: 13%;
    margin-right: 13%;
  }
  .panel-form-name {
    margin-top: 10px;
  }
  .panel-form-button {
    margin-top: 10px;
  }
</style>
