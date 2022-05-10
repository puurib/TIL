// VideoList.vue

<template>
  <ul class="list-group list-group-flush">
    <video-list-item 
    v-for="video in videos"
    :key="video.id.videoId"
    :video="video"
    @select-video="onSelectVideo">
      {{video.snippet.title}}
    </video-list-item>
  </ul>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'
export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: {
      type: Array,
      required: true,
    },
  },
  methods: {
    onSelectVideo: function(video) {
      this.$emit('select-video', video)
    }
  }
}
</script>


<style>
  ul {
    cursor : pointer;
  } 
</style>