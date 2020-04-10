<template>
  <!--
  <div>
    <div>please choose a period</div>
    <div class="block">
      <span class="demonstration">默认</span>
      <el-date-picker
        v-model="value1"
        type="datetimerange"
        range-separator="To"
        start-placeholder="Start date"
        end-placeholder="End date">
      </el-date-picker>
    </div>
    <div style="margin-top: 20px;margin-bottom: 20px">
      <el-form>
        <el-input
          placeholder="请输入内容"
          prefix-icon="el-icon-search"
          v-model="input2" style="width:360px" clearable>
        </el-input>
      </el-form>
      <span>Adults</span>
      <el-select v-model="value" placeholder="请选择">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
    </div>
  </div>
-->
  <div class="search-background">
    <div class="search">
      <el-form ref="form" model="form">
        <el-row type="flex" class="row-bg" justify="start" :gutter="20">
          <el-col :span="15">
            <el-form-item label="Location">
              <el-input v-model="form.location" placeholder="please enter a location"
                        prefix-icon="el-icon-search"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="10">
            <div class="grid-content bg-purple-light">
              <el-form-item label="Time">
                <el-date-picker
                  v-model="form.date1"
                  type="daterange"
                  range-separator="To"
                  format="dd/MM/yyyy"
                  value-format="dd/MM/yyyy"
                  start-placeholder="Check-in date"
                  end-placeholder="Checkout date" :picker-options="pickerOptions">
                </el-date-picker>
              </el-form-item>
            </div>
          </el-col>
          <el-col :span="8">
            <el-form-item label="Person">
              <el-select v-model="form.people" placeholder="Adults">
                <el-option
                  v-for="item in options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <!-- 占位为了对齐-->
            <el-row style="visibility:hidden" >
              <el-button type="primary" >SEARCH</el-button>
            </el-row>
            <el-row>
              <el-form-item>
                <el-button @click="onSubmit" type="primary" >SEARCH</el-button>
              </el-form-item>
            </el-row>
          </el-col>
        </el-row>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      options: [{
        value: 1,
        label: '1 Adult'
      }, {
        value: 2,
        label: '2 Adults'
      }, {
        value: 3,
        label: '3 Adults'
      }, {
        value: 4,
        label: '4 Adults'
      }, {
        value: 5,
        label: '5 Adults'
      }],
      pickerOptions: {
        disabledDate: function (time) {
          return time.getTime() < Date.now() - 8.64e7
        }
      },
      form: {
        location: '',
        people: '',
        date1: ''
      }
    }
  },
  methods: {
    onSubmit: function () {
      // let formData = new FormData()
      // formData.append('location', this.form.location)
      // formData.append('num_of_people', this.form.people)
      // formData.append('data', this.form.date1)
      // let data = this.$qs.stringify({
      //   location: this.form.location,
      //   number_of_people: this.form.people,
      //   date: this.form.date1
      // })
      // document.write(this.form.date1.split(',')[0])
      // var sd = new Date(this.form.date1[0])
      // var ed = new Date(this.form.date1[1])
      this.$router.push(
        {
          path: '/filter',
          query:
            {
              // format dd/mm/yy
              // start_date: sd.toLocaleDateString('en-AU'),
              // end_date: ed.toLocaleDateString('en-AU'),
              start_date: this.form.date1[0],
              end_date: this.form.date1[1],
              location: this.form.location,
              number_of_people: this.form.people
            }
        }
      )
    }
  }
}
</script>
<style scoped>
  .search-background{
    border: #42b983;
  }
  .search{
    float: left;
    margin-left :-330px;
    margin-top :80px;
    padding: 0;
    background: #bbbbbb;
    width: 1000px;
    position: center;
    align-items:stretch;
    padding: 10px;
  }
  .search el-form{
    margin: 10px;
  }

</style>
