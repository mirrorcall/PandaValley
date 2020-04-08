<template>
  <!--  <span>商品</span>-->
  <div>
    <el-card style="margin-top: 5px;">
      <el-alert
        title="upload property information"
        type="info"
        center
        show-icon
        :closable="false">
      </el-alert>
      <el-steps :active="activateIndex - 0" finish-status="success" align-center style="margin: 20px;">
        <el-step title="Basic"></el-step>
        <el-step title="Interior"></el-step>
        <el-step title="Photo"></el-step>
        <el-step title="Amenity"></el-step>
      </el-steps>
      <el-form :model="addForm" :rules="addFormRules" ref="addFormRef" label-width="80px" label-position="left">
        <el-tabs v-model="activateIndex" :tab-position="'left'" style="margin: 20px; margin-left: 80px;margin-right: 80px" >
          <el-tab-pane label="Basic" name="0">
            <el-form-item label="title" prop="title">
              <el-input v-model="addForm.title" autosize="true" placeholder="title"></el-input>
            </el-form-item>
            <el-form-item label="address" prop="location">
              <el-form-item label="street" prop="title">
                <el-input v-model="addForm.location" placeholder="street"></el-input>
              </el-form-item>
              <td>
                <el-form-item label="suburb" prop="location">
                  <el-input v-model="addForm.suburb" placeholder="suburb"></el-input>
                  <!--
                  <el-select v-model="addForm.value" placeholder="please choose your suburb">
                    <el-option
                      v-for="item in options"
                      :key="item.value"
                      :label="item.label"
                      :value="item.value">
                    </el-option>
                  </el-select>
                  -->
                </el-form-item>
              </td>
              <td>
                <el-input
                  placeholder="NSW"
                  :disabled="true">
                </el-input>
              </td>
              <td>
                <el-form-item label="postcode" prop="location">
                  <el-input v-model="addForm.location1" placeholder="postcode">
                  </el-input>
                </el-form-item>
              </td>
            </el-form-item>
            <el-form-item label="price" prop="price" style="text-align:left">
              <el-input v-model="addForm.price" type="number" style="width: 300px;">
                <template slot="append">/per night</template>
              </el-input>
            </el-form-item>
            <el-form-item label="roomtype" prop="roomtype">
              <el-radio-group v-model="addForm.radio" align="left">
                <el-radio label="apartment">apartment</el-radio>
                <el-radio label="unit">unit</el-radio>
                <el-radio label="house">house</el-radio>
              </el-radio-group>
              <el-form-item >
                <el-button type="primary" @click="submitForm_f1()">next page</el-button>
              </el-form-item>
            </el-form-item>
          </el-tab-pane>
          <el-tab-pane label="Interior" name="1">
            <el-form :model="dynamicValidateForm" ref="dynamicValidateForm" label-width="100px" class="demo-dynamic" >
              <el-form-item
                prop="number_of_bedroom"
                style="text-align:left"
                label="bedroom"
                :rules="[
      { required: true, message: 'please type the number of bed room', trigger: 'blur' },
      { message: 'please type the number of bed room', trigger: ['blur', 'change'] }
    ]"
              >
                <el-input placeholder="please type the number of bedroom" v-model="dynamicValidateForm.number_of_bedroom" type="number" style="width: 500px"><template slot="append">bed room</template></el-input>
              </el-form-item>
              <el-form-item
                prop="number_of_single_bed"
                style="text-align:left"
                label="single bed"
                :rules="[
      { required: true, message: 'please type the number of single bed', trigger: 'blur' },
      { message: 'please type the number of single bed', trigger: ['blur', 'change'] }
    ]"
              >
                <el-input placeholder="please type the number of single bed" v-model="dynamicValidateForm.number_of_single_bed" type="number" style="width: 500px"><template slot="append">bed</template></el-input>
              </el-form-item>
              <el-form-item
                prop="number_of_double_bed"
                style="text-align:left"
                label="double bed"
                :rules="[
      { required: true, message: 'please type the number of double bed', trigger: 'blur' },
      { message: 'please type the number of double bed', trigger: ['blur', 'change'] }
    ]"
              >
                <el-input placeholder="please type the number of double bed" v-model="dynamicValidateForm.number_of_double_bed" type="number" style="width: 500px"><template slot="append">bed</template></el-input>
              </el-form-item>
              <el-form-item
                prop="number_of_king_bed"
                style="text-align:left"
                label="king bed"
                :rules="[
      { required: true, message: 'please type the number of king bed', trigger: 'blur' },
      { message: 'please type the number of king bed', trigger: ['blur', 'change'] }
    ]"
              >
                <el-input placeholder="please type the number of king bed" v-model="dynamicValidateForm.number_of_king_bed" type="number" style="width: 500px"><template slot="append">bed</template></el-input>
              </el-form-item>
              <el-form-item
                prop="number_of_queen_bed"
                style="text-align:left"
                label="queen bed"
                :rules="[
      { required: true, message: 'please type the number of queen bed', trigger: 'blur' },
      { message: 'please type the number of queen bed', trigger: ['blur', 'change'] }
    ]"
              >
                <el-input placeholder="please type the number of queen bed" v-model="dynamicValidateForm.number_of_queen_bed" type="number" style="width: 500px"><template slot="append">bed</template></el-input>
              </el-form-item>
              <!--              <el-form-item-->
              <!--                style="width: 600px;"-->
              <!--                v-for="(domain, index) in dynamicValidateForm.domains"-->
              <!--                :label="'guest bedroom' + index"-->
              <!--                :key="domain.key"-->
              <!--                :prop="'domains.' + index + '.value'"-->
              <!--                :rules="{-->
              <!--      required: true, message: 'the number of bed is not allowed empty', trigger: 'blur'-->
              <!--    }"-->
              <!--              >-->
              <!--                <el-input placeholder="please type the number of beds" v-model="domain.value" type="number"><template slot="append">bed</template></el-input><el-button style="margin-top: 12px;margin-bottom: 15px" @click.prevent="removeDomain(domain)">delete bedroom</el-button>-->
              <!--              </el-form-item>-->
              <el-form-item
                prop="number_of_bathroom"
                style="width: 600px"
                label="bathroom"
                :rules="[
      { required: true, message: 'please type the number', trigger: 'blur' },
      { message: 'please type the number', trigger: ['blur', 'change'] }
    ]"
              >
                <el-input placeholder="please type the number of bathroom" v-model="dynamicValidateForm.number_of_bathroom" type="number" ><template slot="append">bath room</template></el-input>
              </el-form-item>
              <el-form-item
                prop="description"
                style="width: 600px"
                label="description"
                :rules="[
      { required: true, message: 'please type the description', trigger: 'blur' },
      { message: 'please type the description', trigger: ['blur', 'change'] }
    ]">
                <el-input placeholder="please type the description" v-model="dynamicValidateForm.description" type="textarea" ><template slot="append">description</template></el-input>
              </el-form-item>
              <el-form-item
                prop="guests"
                style="width: 600px"
                label="guests"
                :rules="[
      { required: true, message: 'please type the guests', trigger: 'blur' },
      { message: 'please type the guests', trigger: ['blur', 'change'] }
    ]"
              >
                <el-input placeholder="please type the number of guests" v-model="dynamicValidateForm.guests" type="number" ><template slot="append">guests</template></el-input>
              </el-form-item>
              <el-form-item style="margin-left: -500px">
                <el-button type="primary" @click="submitForm(dynamicValidateForm)">next page</el-button>
                <!--                <el-button @click="addDomain">add bedroom</el-button>-->
              </el-form-item>
            </el-form>
          </el-tab-pane>
          <el-tab-pane label="Photo" name="2">
            <el-upload
              :multiple="multiple"
              action="${pageContext.request.contextPath}/lookup/editEvidence/123"
              list-type="picture-card"
              :auto-upload="false"
              :http-request="uploadFile"
              ref="upload"
            >
              <i class="el-icon-plus"></i>
            </el-upload>
            <el-button @click="subPicForm">提交上传</el-button>
          </el-tab-pane>
          <el-tab-pane label="Amenity" name="3">
            <el-header style="text-align:center">Basic Amenity</el-header>
            <el-row type="flex" :gutter="50" justify="center">
              <el-col :span="6">
                <el-card shadow="hover">
                  <el-aside style="text-align:left">TV</el-aside>
                  <el-switch
                    style="display: block;text-align:center"
                    v-model="TV"
                    width="50"
                    height="50"
                    active-color="#13ce66"
                    inactive-color="#ff4949">
                  </el-switch>
                </el-card>
              </el-col>
              <el-col :span="6">
                <el-card shadow="hover">
                  <el-aside style="text-align:left">Garage</el-aside>
                  <el-switch
                    style="display: block;text-align:center"
                    v-model="Garage"
                    width="50"
                    height="50"
                    active-color="#13ce66"
                    inactive-color="#ff4949">
                  </el-switch>
                </el-card>
              </el-col>
              <el-col :span="6">
                <el-card shadow="hover">
                  <el-aside style="text-align:left">Clothes dryer</el-aside>
                  <el-switch
                    style="display: block;text-align:center"
                    v-model="Clothes_dryer"
                    width="50"
                    height="50"
                    active-color="#13ce66"
                    inactive-color="#ff4949">
                  </el-switch>
                </el-card>
              </el-col>
            </el-row>
            <el-row type="flex" :gutter="50" justify="center" style="margin-top: 30px">
              <el-col :span="6">
                <el-card shadow="hover">
                  <el-aside style="text-align:left">Linens provided</el-aside>
                  <el-switch
                    style="display: block;text-align:center"
                    v-model="Linens_provided"
                    width="50"
                    height="50"
                    active-color="#13ce66"
                    inactive-color="#ff4949">
                  </el-switch>
                </el-card>
              </el-col>
              <el-col :span="6">
                <el-card shadow="hover">
                  <el-aside style="text-align:left">Air conditioning</el-aside>
                  <el-switch
                    style="display: block;text-align:center"
                    v-model="Air_conditioning"
                    width="50"
                    height="50"
                    active-color="#13ce66"
                    inactive-color="#ff4949">
                  </el-switch>
                </el-card>
              </el-col>
              <el-col :span="6">
                <el-card shadow="hover">
                  <el-aside style="text-align:left">Microwave</el-aside>
                  <el-switch
                    style="display: block;text-align:center"
                    v-model="Microwave"
                    width="50"
                    height="50"
                    active-color="#13ce66"
                    inactive-color="#ff4949">
                  </el-switch>
                </el-card>
              </el-col>
            </el-row>
            <el-row type="flex" :gutter="50" justify="center" style="margin-top: 30px">
              <el-col :span="6">
                <el-card shadow="hover">
                  <el-aside style="text-align:left">Oven</el-aside>
                  <el-switch
                    style="display: block;text-align:center"
                    v-model="Oven"
                    width="50"
                    height="50"
                    active-color="#13ce66"
                    inactive-color="#ff4949">
                  </el-switch>
                </el-card>
              </el-col>
              <el-col :span="6">
                <el-card shadow="hover">
                  <el-aside style="text-align:left">Parking</el-aside>
                  <el-switch
                    style="display: block;text-align:center"
                    v-model="Parking"
                    width="50"
                    height="50"
                    active-color="#13ce66"
                    inactive-color="#ff4949">
                  </el-switch>
                </el-card>
              </el-col>
              <el-col :span="6">
                <el-card shadow="hover">
                  <el-aside style="text-align:left">No Smoking</el-aside>
                  <el-switch
                    style="display: block;text-align:center"
                    v-model="No_Smoking"
                    width="50"
                    height="50"
                    active-color="#13ce66"
                    inactive-color="#ff4949">
                  </el-switch>
                </el-card>
              </el-col>
            </el-row>
            <el-row type="flex" :gutter="50" justify="center" style="margin-top: 30px">
              <el-col :span="6">
                <el-card shadow="hover">
                  <el-aside style="text-align:left">Hair dryer</el-aside>
                  <el-switch
                    style="display: block;text-align:center"
                    v-model="Hair_dryer"
                    width="50"
                    height="50"
                    active-color="#13ce66"
                    inactive-color="#ff4949">
                  </el-switch>
                </el-card>
              </el-col>
              <el-col :span="6">
                <el-card shadow="hover">
                  <el-aside style="text-align:left">Accessible</el-aside>
                  <el-switch
                    style="display: block;text-align:center"
                    v-model="Accessible"
                    width="50"
                    height="50"
                    active-color="#13ce66"
                    inactive-color="#ff4949">
                  </el-switch>
                </el-card>
              </el-col>
              <el-col :span="6">
                <el-card shadow="hover">
                  <el-aside style="text-align:left">Fridge</el-aside>
                  <el-switch
                    style="display: block;text-align:center"
                    v-model="Fridge"
                    width="50"
                    height="50"
                    active-color="#13ce66"
                    inactive-color="#ff4949">
                  </el-switch>
                </el-card>
              </el-col>
            </el-row>
            <el-row type="flex" :gutter="50" justify="center" style="margin-top: 30px">
              <el-col :span="6">
                <el-card shadow="hover">
                  <el-aside style="text-align:left">Wireless Internet</el-aside>
                  <el-switch
                    style="display: block;text-align:center"
                    v-model="Wireless_Internet"
                    width="50"
                    height="50"
                    active-color="#13ce66"
                    inactive-color="#ff4949">
                  </el-switch>
                </el-card>
              </el-col>
              <el-col :span="6">
                <el-card shadow="hover">
                  <el-aside style="text-align:left">Washing machine</el-aside>
                  <el-switch
                    style="display: block;text-align:center"
                    v-model="Washing_machine"
                    width="50"
                    height="50"
                    active-color="#13ce66"
                    inactive-color="#ff4949">
                  </el-switch>
                </el-card>
              </el-col>
              <el-col :span="6">
                <el-card shadow="hover">
                  <el-aside style="text-align:left">Heating</el-aside>
                  <el-switch
                    style="display: block;text-align:center"
                    v-model="Heating"
                    width="50"
                    height="50"
                    active-color="#13ce66"
                    inactive-color="#ff4949">
                  </el-switch>
                </el-card>
              </el-col>
            </el-row>
            <el-row type="flex" :gutter="50" justify="center" style="margin-top: 30px">
              <el-col :span="6">
                <el-card shadow="hover">
                  <el-aside style="text-align:left">Swimming pool</el-aside>
                  <el-switch
                    style="display: block;text-align:center"
                    v-model="Swimming_pool"
                    width="50"
                    height="50"
                    active-color="#13ce66"
                    inactive-color="#ff4949">
                  </el-switch>
                </el-card>
              </el-col>
              <el-col :span="6">
                <el-card shadow="hover">
                  <el-aside style="text-align:left">Hot Tub</el-aside>
                  <el-switch
                    style="display: block;text-align:center"
                    v-model="Hot_Tub"
                    width="50"
                    height="50"
                    active-color="#13ce66"
                    inactive-color="#ff4949">
                  </el-switch>
                </el-card>
              </el-col>
              <el-col :span="6">
                <el-card shadow="hover">
                  <el-aside style="text-align:left">Elevator</el-aside>
                  <el-switch
                    style="display: block;text-align:center"
                    v-model="Elevator"
                    width="50"
                    height="50"
                    active-color="#13ce66"
                    inactive-color="#ff4949">
                  </el-switch>
                </el-card>
              </el-col>
            </el-row>
            <el-row type="flex" :gutter="50" justify="center" style="margin-top: 30px">
              <el-col :span="6">
                <el-card shadow="hover">
                  <el-aside style="text-align:left">Blender</el-aside>
                  <el-switch
                    style="display: block;text-align:center"
                    v-model="Blender"
                    width="50"
                    height="50"
                    active-color="#13ce66"
                    inactive-color="#ff4949">
                  </el-switch>
                </el-card>
              </el-col>
              <el-col :span="6">
                <el-card shadow="hover">
                  <el-aside style="text-align:left">Pets Welcome</el-aside>
                  <el-switch
                    style="display: block;text-align:center"
                    v-model="Pets_Welcome"
                    width="50"
                    height="50"
                    active-color="#13ce66"
                    inactive-color="#ff4949">
                  </el-switch>
                </el-card>
              </el-col>
              <el-col :span="6">
                <el-card shadow="hover">
                  <el-aside style="text-align:left">Toaster</el-aside>
                  <el-switch
                    style="display: block;text-align:center"
                    v-model="Toaster"
                    width="50"
                    height="50"
                    active-color="#13ce66"
                    inactive-color="#ff4949">
                  </el-switch>
                </el-card>
              </el-col>
            </el-row>
            <el-row type="flex" :gutter="50" justify="center" style="margin-top: 30px">
              <el-col :span="6">
                <el-card shadow="hover">
                  <el-aside style="text-align:left">BBQ</el-aside>
                  <el-switch
                    style="display: block;text-align:center"
                    v-model="BBQ"
                    width="50"
                    height="50"
                    active-color="#13ce66"
                    inactive-color="#ff4949">
                  </el-switch>
                </el-card>
              </el-col>
            </el-row>
            <el-button type="primary" @click="submitFormAll()" style="margin-top: 50px">submit</el-button>
          </el-tab-pane>
        </el-tabs>
      </el-form>
    </el-card>
  </div>
</template>

<script>
export default {
  // name: 'Add'
  data () {
    return {
      email_detail: '',
      multiple: true,
      formData: '',
      wifi: true,
      Washing_machine: true,
      Breakfast: true,
      previewPath: '',
      previewVisible: false,
      dynamicValidateForm: {
        number_of_bathroom: '',
        number_of_bedroom: '',
        number_of_single_bed: '',
        number_of_double_bed: '',
        number_of_king_bed: '',
        number_of_queen_bed: '',
        description: '',
        guests: ''
      },
      activateIndex: '0',
      radio: '1',
      addForm: {
        location: '',
        location1: '',
        title: '',
        value: '',
        radio: '',
        price: '',
        suburb: ''
      },
      addFormRules: {
        title: [{
          required: true,
          message: 'please type the title',
          trigger: 'blur'
        }],
        location: [{
          required: true,
          message: 'please type the address',
          trigger: 'blur'
        }],
        price: [{
          required: true,
          message: 'please type the price',
          trigger: 'blur'
        }],
        roomtype: [{
          required: true,
          message: 'please choose the roomtype',
          trigger: 'blur'
        }]
      },
      value: '',
      options: [{
        value: 'Mascot',
        label: 'Mascot'
      }, {
        value: 'Zetland',
        label: 'Zetland'
      }, {
        value: 'Randwick',
        label: 'Randwick'
      }, {
        value: 'Kingsford',
        label: 'Kingsford'
      }, {
        value: 'Kensington',
        label: 'Kensington'
      }],
      indexindex: 0
    }
  },
  mounted: function () {
  },
  methods: {
    submitFormAll () {
      // let data = this.$qs.stringify(formName.number_of_bedroom)
      // let formData = new FormData()
      // this.$refs.upload.submit()
      let config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      // TODO: add amenities
      this.formData.append('title', this.addForm.title)
      // this.formData.append('suburb', this.addForm.value)
      this.formData.append('suburb', this.addForm.suburb)
      this.formData.append('street', this.addForm.location)
      this.formData.append('postcode', this.addForm.location1)
      this.formData.append('price', this.addForm.price)
      this.formData.append('property_type', this.addForm.radio)
      this.formData.append('bedrooms', this.dynamicValidateForm.number_of_bedroom)
      this.formData.append('single_bed', this.dynamicValidateForm.number_of_single_bed)
      this.formData.append('double_bed', this.dynamicValidateForm.number_of_double_bed)
      this.formData.append('king_bed', this.dynamicValidateForm.number_of_king_bed)
      this.formData.append('queen_bed', this.dynamicValidateForm.number_of_queen_bed)
      this.formData.append('bathrooms', this.dynamicValidateForm.number_of_bathroom)
      this.formData.append('guests', this.dynamicValidateForm.number_of_bathroom)
      this.formData.append('description', this.dynamicValidateForm.description)
      // TODO: send formData altogether
      this.$axios.post('api/add_property', this.formData, config).then(res => {
        if (res.data.code === 0) {
          this.$message({
            message: 'Upload successfully.',
            type: 'success'
          })
        }
      }).catch(res => {
        console.log(res)
      })
    },
    uploadFile (file) {
      // request.POST.get('avatar')
      // this.count += 1
      // 'profile_' + count
      this.formData.append('image', file.file)
    },
    subPicForm () {
      this.formData = new FormData()
      this.$refs.upload.submit()
      this.email_detail = this.$store.getters.getStorage
      this.formData.append('email', this.email_detail)
      this.activateIndex = '3'
      // let config = {
      //   headers: {
      //     'Content-Type': 'multipart/form-data'
      //   }
      // }
      // this.$axios.post('/api/add_property', this.formData, config).then(res => {
      //   console.log(res)
      // }).catch(res => {
      //   console.log(res)
      // })
    },
    handleRemove (file, fileList) {
      console.log(file, fileList)
    },
    handlePreview (file) {
      console.log(file)
      this.previewPath = file.url
      this.previewVisible = true
    },
    submitForm_f1 () {
      // let formData = new FormData()
      this.activateIndex = '1'
      // formData.append('title', this.addForm.title)
      // formData.append('suburb', this.addForm.value)
      // formData.append('street', this.addForm.location)
      // formData.append('postcode', this.addForm.location1)
      // formData.append('price', this.addForm.price)
      // formData.append('roomtype', this.addForm.radio)
      // this.$axios.post('/api/upload', formData)
      //   .then((response) => {
      //     if (response.data.code === 0) {
      //       console.log('login successfully')
      //       this.$store.commit('$_setStorage', response.data.email)
      //       this.$router.push({name: 'Home'})
      //     } else if (response.data.code === 1) { // TODO handle incorrect password
      //       console.log(response.data.msg)
      //     }
      //   })
      //   .catch(function (error) {
      //     console.log('ERROR')
      //     console.log(error)
      //   })
    },
    submitForm (f) {
      // let formData = new FormData()
      // formData.append('bedrooms', f.number_of_bedroom)
      // formData.append('single bed', f.number_of_single_bed)
      // formData.append('double bed', f.number_of_double_bed)
      // formData.append('king bed', f.number_of_king_bed)
      // formData.append('queen bed', f.number_of_queen_bed)
      // formData.append('bathroom', f.number_of_bathroom)
      this.activateIndex = '2'
      // this.$axios.post('/api/upload', formData)
      //   .then((response) => {
      //     if (response.data.code === 0) {
      //       console.log('login successfully')
      //       this.$store.commit('$_setStorage', response.data.email)
      //       this.$router.push({name: 'Home'})
      //     } else if (response.data.code === 1) { // TODO handle incorrect password
      //       console.log(response.data.msg)
      //     }
      //   })
      //   .catch(function (error) {
      //     console.log('ERROR')
      //     console.log(error)
      //   })
    },
    removeDomain (item) {
      var index = this.dynamicValidateForm.domains.indexOf(item)
      if (index !== -1) {
        this.dynamicValidateForm.domains.splice(index, 1)
      }
    }
    // addDomain () {
    //   this.dynamicValidateForm.domains.push({
    //     value: '',
    //     key: Date.now()
    //   })
    // }
  }
}
</script>

<style scoped>

</style>
