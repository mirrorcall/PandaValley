<template>
  <div id="map-container">
    <div id="map-sidebar" style="text-align: left">
      <el-scrollbar style="height: 400px; width: 100%">
      <el-menu>
        <el-submenu index="1">
          <template slot="title">
            <i class="iconfont icon-bank"></i>
            <span>Banks</span>
          </template>
          <el-menu-item v-if="atmMarkers.length===0">0 Result</el-menu-item>
          <el-menu-item
            :key="index + 'menu' + 'bank'"
            v-for="(m,index) in bankMarkers">
            <div @mouseover="highlightMarker(1, index)" @mouseleave="dehighlightMarker(1, index)">
              <div style="height: 30px; font-weight: 500">{{ m.infoText }}</div>
              <div style="height: 30px">{{ m.infoAddr }}</div>
              <div style="height: 30px">{{ m.infoRate }}</div>
            </div>
          </el-menu-item>
        </el-submenu>
        <el-submenu index="2">
          <template slot="title">
            <i class="iconfont icon-ios-cafe"></i>
            <span>Cafes</span>
          </template>
          <el-menu-item v-if="cafeMarkers.length===0">0 Result</el-menu-item>
          <el-menu-item
            :key="index + 'menu' + 'cafe'"
            v-for="(m,index) in cafeMarkers">
            <div @mouseover="highlightMarker(2, index)" @mouseleave="dehighlightMarker(2, index)">
              <div style="height: 30px; font-weight: 500">{{ m.infoText }}</div>
              <div style="height: 30px">{{ m.infoAddr }}</div>
              <div style="height: 30px">{{ m.infoRate }}</div>
            </div>
          </el-menu-item>
        </el-submenu>
        <el-submenu index="3">
          <template slot="title">
            <i class="iconfont icon-local_convenience_store_px_rounded"></i>
            <span>Convenience Stores</span>
          </template>
          <el-menu-item v-if="convstoreMarkers.length===0">0 Result</el-menu-item>
          <el-menu-item
            :key="index + 'menu' + 'cvStore'"
            v-for="(m,index) in convstoreMarkers">
            <div @mouseover="highlightMarker(3, index)" @mouseleave="dehighlightMarker(3, index)">
              <div style="height: 30px; font-weight: 500">{{ m.infoText }}</div>
              <div style="height: 30px">{{ m.infoAddr }}</div>
              <div style="height: 30px">{{ m.infoRate }}</div>
            </div>
          </el-menu-item>
        </el-submenu>
        <el-submenu index="4">
          <template slot="title">
            <i class="iconfont icon-restaurant-line"></i>
            <span>Restaurants</span>
          </template>
          <el-menu-item v-if="restaurantMarkers.length===0">0 Result</el-menu-item>
          <el-menu-item
            :key="index + 'menu' + 'restaurant'"
            v-for="(m,index) in restaurantMarkers">
            <div @mouseover="highlightMarker(4, index)" @mouseleave="dehighlightMarker(4, index)">
              <div style="height: 30px; font-weight: 500">{{ m.infoText }}</div>
              <div style="height: 30px">{{ m.infoAddr }}</div>
              <div style="height: 30px">{{ m.infoRate }}</div>
            </div>
          </el-menu-item>
        </el-submenu>
        <el-submenu index="5">
          <template slot="title">
            <i class="iconfont icon-Supermarket"></i>
            <span>Supermarkets</span>
          </template>
          <el-menu-item v-if="supermarketMarkers.length===0">0 Result</el-menu-item>
          <el-menu-item
            :key="index + 'menu' + 'supermarket'"
            v-for="(m,index) in supermarketMarkers">
            <div @mouseover="highlightMarker(5, index)" @mouseleave="dehighlightMarker(5, index)">
              <div style="height: 30px; font-weight: 500">{{ m.infoText }}</div>
              <div style="height: 30px">{{ m.infoAddr }}</div>
              <div style="height: 30px">{{ m.infoRate }}</div>
            </div>
          </el-menu-item>
        </el-submenu>
        <el-submenu index="6">
          <template slot="title">
            <i class="iconfont icon-jingdian"></i>
            <span>Tourists Attractions</span>
          </template>
          <el-menu-item v-if="touristMarkers.length===0">0 Result</el-menu-item>
          <el-menu-item
            :key="index + 'menu' + 'tourist'"
            v-for="(m,index) in touristMarkers">
            <div @mouseover="highlightMarker(6, index)" @mouseleave="dehighlightMarker(6, index)">
              <div style="height: 30px; font-weight: 500">{{ m.infoText }}</div>
              <div style="height: 30px">{{ m.infoAddr }}</div>
              <div style="height: 30px">{{ m.infoRate }}</div>
            </div>
          </el-menu-item>
        </el-submenu>
      </el-menu>
      </el-scrollbar>
    </div>
    <div id="map-view">
      <gmap-map
        ref="mapRef"
        :center="center"
        :zoom="16"
        style="width: 640px; height: 400px">
        <gmap-info-window
          :options="infoOptions"
          :position="infoWindowPos"
          :opened="infoWinOpen"
          @closeclick="infoWinOpen=false">
          <div class="marker-content">
            <div style="font: 600 14px Arial, sans-serif;">{{ infoContent.name }}</div>
            <div style="font: 400 11px Arial, sans-serif;">{{ infoContent.address }}</div>
            <div style="font: 400 11px Arial, sans-serif;">{{ infoContent.rating }}</div>
          </div>
        </gmap-info-window>
        <gmap-marker
          :key="index"
          v-for="(m,index) in centerMarker"
          :position="m.position"
          :clickable="true"
          @click="toggleInfoWindow(m,index)"
        />
<!--        <gmap-marker-->
<!--          v-if="atmMarkers"-->
<!--          :key="index + 'atm'"-->
<!--          v-for="(m,index) in atmMarkers"-->
<!--          :icon="{url: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'}"-->
<!--          :position="m.position"-->
<!--          :clickable="true"-->
<!--          @click="toggleInfoWindow(m,index)"-->
<!--        />-->
        <gmap-marker
          v-if="bankMarkers"
          :key="index + 'bank'"
          v-for="(m,index) in bankMarkers"
          ref="bkMarkers"
          :icon="{url: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'}"
          :position="m.position"
          :clickable="true"
          @click="toggleInfoWindow(m,index)"
        />
        <gmap-marker
          v-if="cafeMarkers"
          :key="index + 'cafe'"
          v-for="(m,index) in cafeMarkers"
          ref="cfMarkers"
          :icon="{url: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'}"
          :position="m.position"
          :clickable="true"
          @click="toggleInfoWindow(m,index)"
        />
        <gmap-marker
          v-if="convstoreMarkers"
          :key="index + 'cvstore'"
          v-for="(m,index) in convstoreMarkers"
          ref="cvMarkers"
          :icon="{url: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'}"
          :position="m.position"
          :clickable="true"
          @click="toggleInfoWindow(m,index)"
        />
        <gmap-marker
          v-if="restaurantMarkers"
          :key="index + 'restaurant'"
          v-for="(m,index) in restaurantMarkers"
          ref="rtMarkers"
          :icon="{url: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'}"
          :position="m.position"
          :clickable="true"
          @click="toggleInfoWindow(m,index)"
        />
        <gmap-marker
          v-if="supermarketMarkers"
          :key="index + 'supermarket'"
          v-for="(m,index) in supermarketMarkers"
          ref="smMarkers"
          :icon="{url: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'}"
          :position="m.position"
          :clickable="true"
          @click="toggleInfoWindow(m,index)"
        />
        <gmap-marker
          v-if="touristMarkers"
          :key="index + 'tourist'"
          v-for="(m,index) in touristMarkers"
          ref="taMarkers"
          :icon="{url: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'}"
          :position="m.position"
          :clickable="true"
          @click="toggleInfoWindow(m,index)"
        />
      </gmap-map>
    </div>
<!--    <div id="map-icon">-->
<!--      <div id="top-icon">-->
<!--        <el-row>-->
<!--          <el-col :span="8"><i id="bank" class="iconfont icon-bank" style="size: 100px"></i><span>{{ bankMarkers.length }}</span></el-col>-->
<!--          <el-col :span="8"><i id="cafe" class="iconfont icon-ios-cafe"></i><span>{{ cafeMarkers.length }}</span></el-col>-->
<!--          <el-col :span="8"><i id="cv-store" class="iconfont icon-local_convenience_store_px_rounded"></i><span>{{ convstoreMarkers.length }}</span></el-col>-->
<!--        </el-row>-->
<!--      </div>-->
<!--      <div id="bot-icon">-->
<!--        <el-row>-->
<!--          <el-col :span="8"><i id="restaurant" class="iconfont icon-restaurant-line"></i><span>{{ restaurantMarkers.length }}</span></el-col>-->
<!--          <el-col :span="8"><i id="supermarket" class="iconfont icon-Supermarket"></i><span>{{supermarketMarkers.length }}</span></el-col>-->
<!--          <el-col :span="8"><i id="tourist" class="iconfont icon-jingdian"></i><span>{{ touristMarkers.length }}</span></el-col>-->
<!--        </el-row>-->
<!--      </div>-->
<!--    </div>-->
  </div>
</template>

<script>
import {gmapApi} from 'vue2-google-maps'
export default {
  name: 'MapView',
  data () {
    return {
      center: {
        lat: 0,
        lng: 0
      },
      centerMarker: [
        {
          position: {
            lat: 0,
            lng: 0
          },
          infoText: 'Property',
          infoAddr: '',
          infoRate: 0
        }
      ],
      searchType: [
        // 'atm',
        'bank',
        'cafe',
        'convenience_store',
        'restaurant',
        'supermarket',
        'tourist_attraction'
      ],
      atmMarkers: [],
      bankMarkers: [],
      cafeMarkers: [],
      convstoreMarkers: [],
      restaurantMarkers: [],
      supermarketMarkers: [],
      touristMarkers: [],
      infoOptions: {
        pixelOffset: {
          width: 0,
          height: -30
        }
      },
      infoContent: {
        name: '',
        address: '',
        rating: ''
      },
      infoWindowPos: null,
      infoWinOpen: false,
      currentMidx: null
    }
  },
  created () {
  },
  mounted () {
    this.center = {lat: -33.870064, lng: 151.206959}
    this.centerMarker[0].position = this.center
    for (let i = 0; i < this.searchType.length; i++) {
      this.searchNearBy(this.searchType[i])
    }
  },
  computed: {
    google: gmapApi,
    collectResults: function () {
      return [].concat(this.bankMarkers.concat(this.cafeMarkers.concat(this.convstoreMarkers.concat(this.restaurantMarkers.concat(this.supermarketMarkers.concat(this.touristMarkers))))))
    }
  },
  methods: {
    searchNearBy (type) {
      let request = {
        location: this.center,
        radius: '230',
        type: [ type ]
      }
      this.$refs.mapRef.$mapPromise.then((map) => {
        let service = new this.google.maps.places.PlacesService(map)
        service.nearbySearch(request, (results, status) => {
          if (status === 'OK') {
            console.log(results)
            if (type === 'atm') {
              for (let i = 0; i < results.length; i++) {
                let marker = {
                  position: results[i].geometry.location,
                  infoText: results[i].name,
                  infoAddr: results[i].vicinity,
                  infoRate: 'Rating: ' + results[i].rating
                }
                this.atmMarkers.push(marker)
              }
            } else if (type === 'bank') {
              for (let i = 0; i < results.length; i++) {
                let marker = {
                  position: results[i].geometry.location,
                  infoText: results[i].name,
                  infoAddr: results[i].vicinity,
                  infoRate: 'Rating: ' + results[i].rating
                }
                this.bankMarkers.push(marker)
              }
            } else if (type === 'cafe') {
              for (let i = 0; i < results.length; i++) {
                let marker = {
                  position: results[i].geometry.location,
                  infoText: results[i].name,
                  infoAddr: results[i].vicinity,
                  infoRate: 'Rating: ' + results[i].rating
                }
                this.cafeMarkers.push(marker)
              }
            } else if (type === 'convenience_store') {
              for (let i = 0; i < results.length; i++) {
                let marker = {
                  position: results[i].geometry.location,
                  infoText: results[i].name,
                  infoAddr: results[i].vicinity,
                  infoRate: 'Rating: ' + results[i].rating
                }
                this.convstoreMarkers.push(marker)
              }
            } else if (type === 'restaurant') {
              for (let i = 0; i < results.length; i++) {
                let marker = {
                  position: results[i].geometry.location,
                  infoText: results[i].name,
                  infoAddr: results[i].vicinity,
                  infoRate: 'Rating: ' + results[i].rating
                }
                this.restaurantMarkers.push(marker)
              }
            } else if (type === 'supermarket') {
              for (let i = 0; i < results.length; i++) {
                let marker = {
                  position: results[i].geometry.location,
                  infoText: results[i].name,
                  infoAddr: results[i].vicinity,
                  infoRate: 'Rating: ' + results[i].rating
                }
                this.supermarketMarkers.push(marker)
              }
            } else {
              for (let i = 0; i < results.length; i++) {
                let marker = {
                  position: results[i].geometry.location,
                  infoText: results[i].name,
                  infoAddr: results[i].vicinity,
                  infoRate: 'Rating: ' + results[i].rating
                }
                this.touristMarkers.push(marker)
              }
            }
          }
        })
      })
    },
    toggleInfoWindow: function (marker, idx) {
      this.infoWindowPos = marker.position
      this.infoContent = {
        name: marker.infoText,
        address: marker.infoAddr,
        rating: marker.infoRate
      }

      if (this.currentMidx === idx) {
        this.infoWinOpen = !this.infoWinOpen
      } else {
        this.infoWinOpen = true
        this.currentMidx = idx
      }
    },
    highlightMarker: function (markerNo, index) {
      let hlIcon = {
        url: 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png'
      }
      if (markerNo === 1) {
        this.$refs.bkMarkers[index].$markerObject.setIcon(hlIcon)
      } else if (markerNo === 2) {
        this.$refs.cfMarkers[index].$markerObject.setIcon(hlIcon)
      } else if (markerNo === 3) {
        this.$refs.cvMarkers[index].$markerObject.setIcon(hlIcon)
      } else if (markerNo === 4) {
        this.$refs.rtMarkers[index].$markerObject.setIcon(hlIcon)
      } else if (markerNo === 5) {
        this.$refs.smMarkers[index].$markerObject.setIcon(hlIcon)
      } else if (markerNo === 6) {
        this.$refs.taMarkers[index].$markerObject.setIcon(hlIcon)
      }
    },
    dehighlightMarker: function (markerNo, index) {
      let defaultIcon = {
        url: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'
      }
      if (markerNo === 1) {
        this.$refs.bkMarkers[index].$markerObject.setIcon(defaultIcon)
      } else if (markerNo === 2) {
        this.$refs.cfMarkers[index].$markerObject.setIcon(defaultIcon)
      } else if (markerNo === 3) {
        this.$refs.cvMarkers[index].$markerObject.setIcon(defaultIcon)
      } else if (markerNo === 4) {
        this.$refs.rtMarkers[index].$markerObject.setIcon(defaultIcon)
      } else if (markerNo === 5) {
        this.$refs.smMarkers[index].$markerObject.setIcon(defaultIcon)
      } else if (markerNo === 6) {
        this.$refs.taMarkers[index].$markerObject.setIcon(defaultIcon)
      }
    }
  }
}
</script>

<style scoped>
  #map-container {
    margin: 20px 20%;
  }
  #map-sidebar {
    position: absolute;
    height: 400px;
    width: 300px;
  }
  #map-view {
    margin-left: 320px;
    width: 640px;
    height: 400px;
  }
  #map-icon {
    margin-left: 960px;
  }
  #top-icon, #bot-icon {
    padding-top: 50px;
    height: 100px;
    padding-bottom: 50px;
    text-align: center;
    line-height: 100px;
  }
  >>> .el-menu-item {
    color: black;
    height: 100px;
  }
  >>> .el-scrollbar__wrap {
    overflow-x: hidden;
  }
</style>
