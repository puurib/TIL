// VideoListItem.vue

<template>
  <li @click="selectVideo" class="list-group-item d-flex justify-content-start">
    <img :src="video.snippet.thumbnails.default.url" alt="youtube-thumbnail-image">
    <p class="d-flex align-items-center ms-3"> {{ video.snippet.title }} </p>
  </li> 
</template>

<script>

export default {
  name: 'VideoListItem',
  props: {
    video: {
      type: Object,
      required: true,
    },
  },
  methods: {
    selectVideo: function() {
      this.$emit('select-video', this.video)
    }
  },
  
}
</script>