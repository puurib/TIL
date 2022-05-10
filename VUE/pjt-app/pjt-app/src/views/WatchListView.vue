<template>
  <div>
    <h1>
      <i class="fa-solid fa-clapperboard"></i>
      My Move List
    </h1>
    <watch-list-form></watch-list-form>
    <!-- <watch-list-item v-for="movie in myMovies" :key="movie.date" :movie="movie"></watch-list-item> -->
    <watch-list-item :myMovies="myMovies"></watch-list-item>
  </div>
</template>

<script>
import WatchListForm from '@/components/WatchListForm.vue'
import WatchListItem from '@/components/WatchListItem.vue'
import EventBus from '@/EventBus'

export default {
  name: 'WatchListView',
  data() {
    return {
      myMovies: [],
    }
  },
  components: {
    WatchListForm,
    WatchListItem,
  },
  created() {
    EventBus.$on('addMovie', (payload) =>{
      this.myMovies.push(payload)
    })
  }
}

</script>

<style>
  h1 {
    font-family: Cafe24Oneprettynight;
  }
</style>