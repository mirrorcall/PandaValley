<template>
  <div>
    <div class="user-avatar-container">
      <div class="user-avatar">
        <el-upload
          class="avatar-uploader"
          action="upload"
          :http-request="uploadAction"
          :show-file-list="false"
          :on-success="handleAvatarSuccess"
          :before-upload="beforeAvatarUpload">
          <img v-if="imageUrl!==''" :src="imageUrl" class="avatar" alt="">
<!--          <i v-else class="el-icon-plus avatar-uploader-icon"></i>-->
        </el-upload>
      </div>
      <div class="user-avatar-indicator">
        <span>Update your avatar</span>
      </div>
      <div class="user-filler"></div>
    </div>
<!--    The following container should be only visible to the user itself-->
<!--    That is saying that other user won't be able to see it-->
    <div class="user-profile">
      <div class="user-welcome"><span>Hi, I'm {{ before.firstName }}</span></div>
      <div class="user-joindate"><span>Joined in {{ dateJoined }} · </span><span class="edit-button">Edit profile</span></div>
      <div class="user-profile-form">
        <template v-if="!editName">
          <div class="user-profile-form-slot">
            <div class="user-profile-form-slot-left">
              <div class="user-profile-form-slot-kind"><span>Name</span></div>
              <div class="user-profile-form-slot-content"><span>{{ nameForm.firstName + ' ' + nameForm.lastName }}</span></div>
            </div>
            <div class="user-profile-form-slot-right">
              <span class="edit-button" @click="editAction(kindName)">Edit</span>
            </div>
          </div>
        </template>
        <template v-else>
          <div class="user-profile-form-edit" id="form-name">
            <div class="user-profile-form-edit-top">
              <div class="top-kind">
                <span>Legal name</span>
              </div>
              <div class="top-button">
                <span class="cancel-button" @click="cancelAction(kindName)">Cancel</span>
              </div>
              <div style="clear: both"></div>
            </div>
            <div class="edit-explanation"><span>This is the name on your travel document, which could be a licence or a passport.</span></div>
            <div class="edit-form">
              <div class="edit-first-name">
                <span>First name</span>
                <el-input id="first-name" v-model="nameForm.firstName"></el-input>
              </div>
              <div class="edit-last-name">
                <span>Last name</span>
                <el-input id="last-name" v-model="nameForm.lastName"></el-input>
              </div>
            </div>
            <div style="clear: both"></div>
            <div class="save-button">
              <el-button type="primary" @click="modifyAction(kindName)">Save</el-button>
            </div>
            <div class="border-line"></div>
          </div>
        </template>
        <template v-if="!editGender">
          <div class="user-profile-form-slot">
            <div class="user-profile-form-slot-left">
              <div class="user-profile-form-slot-kind"><span>Gender</span></div>
              <div class="user-profile-form-slot-content"><span>{{ myGender }}</span></div>
            </div>
            <div class="user-profile-form-slot-right">
              <span class="edit-button" @click="editAction(kindGender)">Edit</span>
            </div>
          </div>
        </template>
        <template v-else>
          <div class="user-profile-form-edit" id="form-gender">
            <div class="user-profile-form-edit-top">
              <div class="top-kind">
                <span>Gender</span>
              </div>
              <div class="top-button">
                <span class="cancel-button" @click="cancelAction(kindGender)">Cancel</span>
              </div>
              <div style="clear: both"></div>
            </div>
<!--            <div class="edit-explanation"><span>This is the name on your travel document, which could be a licence or a passport.</span></div>-->
            <div class="edit-form">
              <div class="edit-gender">
                <el-select v-model="myGender" placeholder="Select" style="width: 100%">
                  <el-option
                    v-for="item in genderOptions"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                    :disabled="item.disabled">
                  </el-option>
                </el-select>
              </div>
            </div>
            <div class="save-button">
              <el-button type="primary" @click="modifyAction(kindGender)">Save</el-button>
            </div>
            <div class="border-line"></div>
          </div>
        </template>
        <template v-if="!editDoB">
          <div class="user-profile-form-slot">
            <div class="user-profile-form-slot-left">
              <div class="user-profile-form-slot-kind"><span>Date of birth</span></div>
              <div class="user-profile-form-slot-content"><span>{{ myDoB }}</span></div>
            </div>
            <div class="user-profile-form-slot-right">
              <span class="edit-button" @click="editAction(kindDoB)">Edit</span>
            </div>
          </div>
        </template>
        <template v-else>
          <div class="user-profile-form-edit" id="form-dob">
            <div class="user-profile-form-edit-top">
              <div class="top-kind">
                <span>Date of birth</span>
              </div>
              <div class="top-button">
                <span class="cancel-button" @click="cancelAction(kindDoB)">Cancel</span>
              </div>
              <div style="clear: both"></div>
            </div>
            <!--            <div class="edit-explanation"><span>This is the name on your travel document, which could be a licence or a passport.</span></div>-->
            <div class="edit-form">
              <div class="edit-gender">
                <el-date-picker
                  v-model="myDoB"
                  type="date"
                  placeholder="Birthday"
                  value-format="yyyy-MM-dd"
                  :picker-options="doBOptions"
                  style="width: 100%">
                </el-date-picker>
              </div>
            </div>
            <div class="save-button">
              <el-button type="primary" @click="modifyAction(kindDoB)">Save</el-button>
            </div>
            <div class="border-line"></div>
          </div>
        </template>
        <template v-if="!editPhone">
          <div class="user-profile-form-slot">
            <div class="user-profile-form-slot-left">
              <div class="user-profile-form-slot-kind"><span>Phone number</span></div>
              <div class="user-profile-form-slot-content"><span>{{ myPhone }}</span></div>
            </div>
            <div class="user-profile-form-slot-right">
<!--              Does not support change phone at the moment-->
<!--              <span class="edit-button" @click="editAction(kindPhone)">Edit</span>-->
            </div>
          </div>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import bus from '../../assets/eventBus'
export default {
  name: 'Profile.vue',
  data () {
    return {
      imageUrl: '',
      dateJoined: '',
      kindName: 'NAME',
      before: {
        firstName: '',
        lastName: '',
        gender: '',
        dob: ''
      },
      nameForm: {
        firstName: '',
        lastName: ''
      },
      editName: false,
      kindGender: 'GENDER',
      editGender: false,
      genderOptions: [
        {
          value: 'select',
          label: 'Select',
          disabled: true
        },
        {
          value: 'Male',
          label: 'Male'
        },
        {
          value: 'Female',
          label: 'Female'
        },
        {
          value: 'Other',
          label: 'Other'
        }
      ],
      myGender: '',
      kindDoB: 'DOB',
      editDoB: false,
      myDoB: '',
      doBOptions: {
        disabledDate (time) {
          return time.getTime() > Date.now() - 8.64e7
        }
      },
      kindPhone: 'PHONE',
      editPhone: false,
      myPhone: ''
    }
  },
  created () {
    this.$axios.get('/api/pass_user_info?email=' + this.$store.getters.getStorage)
      .then((response) => {
        this.imageUrl = response.data.avatar_url
        this.dateJoined = response.data.c_time
        this.nameForm.firstName = response.data.first_name
        this.before.firstName = response.data.first_name
        this.nameForm.lastName = response.data.last_name
        this.before.lastName = response.data.last_name
        this.myGender = response.data.gender
        this.before.gender = response.data.gender
        this.myDoB = response.data.dob
        this.before.dob = response.data.dob
        this.myPhone = response.data.phone
      })
      .catch(function (error) {
        console.log(error)
      })
  },
  methods: {
    beforeAvatarUpload (file) {
      const isJPG = file.type === 'image/jpeg'
      const isPNG = file.type === 'image/png'
      const isLt2M = file.size / 1024 / 1024 < 2

      if (!isJPG && !isPNG) {
        this.$message.error('The upload action only supports JPEG/PNG format!')
      }
      if (!isLt2M) {
        this.$message.error('The upload action only supports image file small than 2MB!')
      }
      return (isJPG || isPNG) && isLt2M
    },
    uploadAction (avatar) {
      let formData = new FormData()
      formData.append('email', this.$store.state.user)
      formData.append('avatar', avatar.file)
      this.$axios.post('/api/upload_avatar', formData)
        .then((response) => {
          if (response.data.code === 0) {
            this.imageUrl = URL.createObjectURL(avatar.file)
            bus.$emit('updateUserAvatar', this.imageUrl)
          }
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    editAction (kind) {
      if (kind === this.kindName) {
        this.editName = true
      } else if (kind === this.kindGender) {
        this.editGender = true
      } else if (kind === this.kindDoB) {
        this.editDoB = true
      } else if (kind === this.kindPhone) {
        this.editPhone = true
      }
    },
    cancelAction (kind) {
      if (kind === this.kindName) {
        this.editName = false
        this.nameForm.firstName = this.before.firstName
        this.nameForm.lastName = this.before.lastName
      } else if (kind === this.kindGender) {
        this.editGender = false
        this.myGender = this.before.gender
      } else if (kind === this.kindDoB) {
        this.editDoB = false
        this.myDoB = this.before.dob
      }
    },
    modifyAction (kind) {
      let data = null
      if (kind === this.kindName) {
        this.editName = false
        data = this.$qs.stringify({
          'email': this.$store.getters.getStorage,
          'profile_key': this.kindName,
          'profile_value_1': this.nameForm.firstName,
          'profile_value_2': this.nameForm.lastName
        })
        this.before.firstName = this.nameForm.firstName
        this.before.lastName = this.nameForm.lastName
      } else if (kind === this.kindGender) {
        this.editGender = false
        data = this.$qs.stringify({
          'email': this.$store.getters.getStorage,
          'profile_key': this.kindGender,
          'profile_value_1': this.myGender
        })
        this.before.gender = this.myGender
      } else if (kind === this.kindDoB) {
        this.editDoB = false
        data = this.$qs.stringify({
          'email': this.$store.getters.getStorage,
          'profile_key': this.kindDoB,
          'profile_value_1': this.myDoB
        })
        this.before.dob = this.myDoB
      }
      this.$axios.post('/api/modify_user_info', data)
        .then((response) => {
          console.log(response)
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>

<style scoped>
  .user-avatar-container {
    position: absolute;
    top: 180px;
    left: 15%;
    width: 20%;
    border: 1px solid #d9d9d9;
  }
  .user-avatar {
    margin-top: 30px;
  }
  .user-avatar-indicator {
    margin-top: 15px;
    font-size: 15px;
    font-weight: bold;
  }
  .user-filler {
    margin-top: 30px;
  }
  .user-profile {
    margin-top: 100px;
    margin-left: 45%;
    margin-right: 20%;
    height: 100%;
  }
  .user-welcome {
    text-align: left;
    font-size: 40px;
    font-weight: 400;
  }
  .user-joindate {
    text-align: left;
  }
  .edit-button {
    font-weight: bold;
    color: #42b983;
    cursor: pointer;
  }
  .edit-button:hover {
    text-decoration: underline;
  }
  .user-profile-form {
    margin-top: 40px;
  }
  .user-profile-form-slot {
    margin-top: 20px;
    margin-right: 7%;
    height: 100px;
  }
  .user-profile-form-slot-left {
    text-align: left;
    float: left;
    width: 90%;
    height: 80px;
    border-bottom: 1px solid #d9d9d9;
  }
  .user-profile-form-slot-right {
    float: left;
    height: 80px;
    border-bottom: 1px solid #d9d9d9;
  }
  .user-profile-form-slot-kind {
    font-weight: bold;
  }
  .user-profile-form-slot-content {
    margin-top: 8px;
  }
  .user-profile-form-edit {
    margin-top: 20px;
    margin-right: 7%;
  }
  #form-name { height: 230px; }
  #form-gender { height: 180px; }
  #form-dob { height: 180px; }
  #form-phone { height: 180px; }
  .top-kind {
    font-weight: bold;
    text-align: left;
    float: left;
    width: 87%;
  }
  .top-button {
    float: left;
  }
  .edit-explanation {
    clear: both;
    margin-top: 8px;
    text-align: left;
  }
  .cancel-button {
    font-weight: bold;
    color: #42b983;
    cursor: pointer;
  }
  .cancel-button:hover {
    text-decoration: underline;
  }
  .edit-form {
    margin-top: 20px;
    margin-right: 6%;
    text-align: center;
  }
  .edit-first-name {
    text-align: left;
    float: left;
    width: 45%;
    padding-right: 5%;
  }
  .edit-last-name {
    text-align: left;
    float: left;
    width: 45%;
  }
  .save-button {
    text-align: left;
    margin-top: 20px;
  }
  .border-line {
    margin-top: 20px;
    margin-right: 5%;
    border-bottom: 1px solid #d9d9d9;
  }
  .avatar-uploader >>> .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 50%;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader >>> .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 120px;
    height: 120px;
    line-height: 120px;
    text-align: center;
  }
  .avatar {
    width: 120px;
    height: 120px;
    display: block;
  }
</style>
