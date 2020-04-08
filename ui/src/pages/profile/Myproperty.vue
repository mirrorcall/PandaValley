<template>
  <div class="myproperty">
    <el-card shadow="hover" v-for="(item,index) in list" :key="item.id">
      <el-row>
        <el-col :span="8">
          <el-image
            style="width: 450px; height: 300px; margin: 10px"
            :src="item.image"
            :fit="fill"></el-image>
        </el-col>
        <el-col :span="13">
          <p></p>
          <el-row>
            <h2>{{item.title}}</h2>
          </el-row>
          <el-row>
            <i class="el-icon-location"></i>
            <!--            {{item.address}}-->
          </el-row>
          <el-row>
            <p><i class="icon iconfont iconrenshu"></i> Guest: {{item.guests}}</p>
          </el-row>
          <el-row>
            <i class="icon iconfont iconchuang"></i> Bedrooms: {{item.bedrooms}}
          </el-row>
          <el-row>
            <p><i class="icon iconfont iconyushiyongpin"></i> Bathrooms: {{item.bathrooms}}</p>
          </el-row>
          <el-row>
            ${{item.price}} per night
          </el-row>
        </el-col>
        <el-col :span="3">
          <el-aside width="200px">
            <div>
              <el-row><el-button type="success" round>Edit</el-button></el-row>
              <el-row><el-button type="warning" round>Check</el-button></el-row>
              <el-row><el-button type="danger" round @click="deleteProperty(item,index)">Delete</el-button></el-row>
            </div>
          </el-aside>
        </el-col>
      </el-row>
    </el-card>
    <div style="margin-top: 20px">
      <el-button type="danger" @click="linktoAdd">Add</el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Myproperty',
  data () {
    return {
      list: ''
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
      this.list.splice(index, 1)
      console.log(this.list)
    },
    linktoAdd () {
      this.$router.push({path: '/add_property'})
    }
  }
}
</script>

<style scoped>
  .myproperty{
    margin-right: 10%;
    margin-left: 10%;
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
    line-height: 80px;
    margin-top: 50px;
  }
</style>
