// App.vue
<template>
  <div id="app" class="container">
    <h1 class="test">💜My First Youtube Project💜</h1>
    <header class="py-3">
      <the-search-bar @input-change="onInputChange" class="my-1 input"></the-search-bar>
    </header>
    <section class="d-flex justify-content-center">
      <video-detail :video="selectedVideo"></video-detail>
    </section>
    <section>
      <video-list :videos="videos" @select-video="onVideoSelect"></video-list>
    </section>

  </div>
</template>

<script>
import axios from 'axios'
import TheSearchBar from './components/TheSearchBar.vue'
import VideoList from './components/VideoList.vue'
import VideoDetail from './components/VideoDetail.vue'

// API
//const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_KEY = 'AIzaSyB8Vti_XlFN-lQHStsiYKnPtTerR-P3TIY'
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  data: function() {
    return {
      inputValue: null,
      videos: [],
      selectedVideo: null,
    }
  },
  methods: {
    onInputChange: function (inputText) {
      this.inputValue = inputText

      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: this.inputValue,
      }

      axios({
        method: 'get',
        url: API_URL,
        params,
      })
        .then (res => {
          console.log(res)
          this.videos = res.data.items
        })
        .catch (err => {
          console.log(err)
        })
    },
    onVideoSelect: function(video) {
      this.selectedVideo = video
    },
  },
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail,
  }

}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.test {
  color: rgb(161, 53, 228);
}

</style>
