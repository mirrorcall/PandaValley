<template>
  <div class="myproperty">
    <h1 style="text-align: center">Manage My Properties</h1>
    <el-card shadow="hover" v-for="(item,index) in list" :key="item.id">
      <el-row>
        <el-col :span="8">
          <el-image
            style="width: 300px; height: 200px; margin: 10px"
            :src="item.image[0]"
            :fit="fill"></el-image>
        </el-col>
        <el-col :span="13">
          <p></p>
          <el-row>
            <span style="text-align: left;font-size: 20px;font-weight: bold">{{item.title}}</span>
          </el-row>
          <el-row>
            <i class="el-icon-location"></i>
                    {{item.street}}, {{item.suburb}}
          </el-row>
          <el-row>
            <el-col :span="8">
            <p><i class="icon iconfont iconrenshu"></i> Guest: {{item.guests}}</p>
            </el-col>
            <el-col :span="8">
            <p><i class="icon iconfont iconchuang"></i> Bedrooms: {{item.bedrooms}}</p>
            </el-col>
            <el-col :span="8">
              <p><i class="icon iconfont iconyushiyongpin"></i> Bathrooms: {{item.bathrooms}}</p>
            </el-col>
          </el-row>
          <el-row>
            Type: {{item.property_type}}
          </el-row>
          <el-row>
            <el-col :span="12">
              <p>Cleaning fee: {{item.cleaning_fee}}</p>
            </el-col>
            <el-col :span="12">
              <p>Price: ${{item.price}} per night</p>
            </el-col>
          </el-row>
        </el-col>
        <el-col :span="3">
          <el-aside width="200px">
            <div>
<!--              <el-row><el-button type="success" round>Edit</el-button></el-row>-->
              <el-row><el-button type="warning" round @click="checkProperty (item)">Check</el-button></el-row>
              <el-dialog title="Orders" :visible.sync="dialogTableVisible" customClass="customWidth">
                  <el-table :data="list_order">
                    <el-table-column property="id" label="BookingID" width="100"></el-table-column>
                    <el-table-column property="guest_id" label="Guest" width="180"></el-table-column>
                    <el-table-column property="start_date" label="Start" width="150"></el-table-column>
                    <el-table-column property="end_date" label="End" width="150"></el-table-column>
                    <el-table-column property="days" label="Days" width="100"></el-table-column>
                    <el-table-column property="total_cost" label="Cost" width="150"></el-table-column>
                    <el-table-column property="state" label="State" width="150"></el-table-column>
                    <el-table-column label="Operations" >
                      <template slot-scope="scope">
                        <div v-show="scope.row.state==='canceling'">
                        <el-button type="primary" icon="el-icon-circle-check" @click="agreeCancellation(scope.row.state, scope.row.id)">Agree</el-button>
                        <el-button type="primary" icon="el-icon-circle-close" @click="refuseCancellation(scope.row.state, scope.row.id)">Refuse</el-button>
                        </div>
                      </template>
                    </el-table-column>
                  </el-table>
              </el-dialog>
              <el-row><el-button type="danger" round @click="deleteProperty(item,index)">Delete</el-button></el-row>
            </div>
          </el-aside>
        </el-col>
      </el-row>
    </el-card>
    <div style="margin-top: 20px;text-align: center">
      <el-button type="danger" @click="linktoAdd">Add</el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Myproperty',
  data () {
    return {
      list: '',
      list_order: '',
      dialogTableVisible: false
    }
  },
  created () {
    this.$axios
      .get('/api/my_property?email=' + this.$store.getters.getStorage)
      .then(res => {
        this.list = res.data.body
      })
      .catch(function (error) {
        console.log(error)
      })
  },
  methods: {
    deleteProperty (item, index) {
      this.$axios.post('/api/drop_property', this.$qs.stringify({
        property_id: item.property_id
      }))
        .then((response) => {
          if (response.data.code === 1) {
            this.$message.error('You are not allowed to delete the property while it is under booking now.')
          } else if (response.data.code === 127) {
            this.$message.error('Internal server failure. Please contact the administration.')
          } else {
            this.list.splice(index, 1)
            this.$message.success('Operating successfully.')
          }
        })
    },
    linktoAdd () {
      this.$router.push({path: '/add_property'})
    },
    checkProperty (item) {
      this.dialogTableVisible = true
      this.$axios
        .get('/api/my_order?property_id=' + item.property_id)
        .then(res => {
          this.list_order = res.data.body
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    agreeCancellation (state, id) {
      if (state === 'canceling') {
        let data = this.$qs.stringify({
          booking_id: id
        })
        this.$axios.post('/api/canceled', data)
          .then((response) => {
            if (response.data.code === 0) {
              this.$message('Successfully cancelled')
            } else {
              this.$message.error('error')
            }
          })
          .catch((res) => {
            console.log('error ', res)
          })
      }
    },
    refuseCancellation (state, id) {
      if (state === 'canceling') {
        let data = this.$qs.stringify({
          booking_id: id
        })
        this.$axios.post('/api/refused_cancel', data)
          .then((response) => {
            if (response.data.code === 0) {
              this.$message('You have refused the cancellation.')
            } else {
              this.$message.error('error')
            }
          })
          .catch((res) => {
            console.log('error ', res)
          })
      }
    }
    // refund () {
    //   this.$axios
    //     .post(‘/api/cancled?booking_id=‘ + item.booking_id)
    // .catch(function (error) {
    //     console.log(error)
    //   })
  }
}
</script>

<style scoped>
  .myproperty{
    margin-right: 10%;
    margin-left: 10%;
    text-align: left;
  }
  .myproperty h2 {
    margin: 0px 10px;
    font-size: 20px;
    font-weight: 600;
    color: #333;
    text-align: center;
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
  }
  .dates {
    font-size: 16px;
    font-weight: 600;
    color: #333;
    text-align: center;
    text-overflow: ellipsis;
  }
  .el-aside {
    color: #333;
    text-align: center;
    line-height: 50px;
    margin-top: 50px;
  }
  .customWidth{
    width:90%;
  }
  >>> .el-dialog {
    width: 65%;
  }
</style>
