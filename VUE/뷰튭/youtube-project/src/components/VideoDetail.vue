// VideoDetail.vue

<template>
  <div v-if="video" class="video-detail">
    <div id="video-detail">
      <iframe :src="videoURI" frameborder="0" class="d-flex justify-content-center w-100 h-75"></iframe>
      <h4>{{ video.snippet.title}}</h4>
      <p>{{ video.snippet.description}}</p>
    </div>
  </div>
</template>

<script>
  //import _ from 'lodash'

  export default {
    name: 'VideoDetail',
    props: {
      video: {
        type: Object,
      },
    },
    computed: {
      videoURI: function() {
        const videoId = this.video.id.videoId
        return `https://www.youtube.com/embed/${videoId}`
      },
    },
  }
</script>

<style>
#video-detail {
  width: 50rem;
  height: 50rem;
}
</style>
