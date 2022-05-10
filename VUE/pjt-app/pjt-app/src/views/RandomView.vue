<template>
  <div class="random container">
    <button @click="pickOne" type="button" class="btn btn-outline-success btn-sm mb-3">
    <p class="text-style">PICK</p>
    </button>
    <div class="d-flex justify-content-center">
      <div class="card d-flex flex-wrap" style="width: 18rem;">
        <img :src="image(movie.poster_path)" class="card-img-top" alt="#">
        <div class="card-body card-custom">
          <h4 class="card-title text-style">{{ movie.title }}</h4>
          <p class="card-text text-style">{{movie.overview}}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash';

export default {
  name: 'RandomView',
  props: ['movieList'],
  data() {
    return {
      movie: _.sample(this.movieList)
    }
  },
  methods: {
    pickOne() {
      this.movie = _.sample(this.movieList)
    },
    image(img) {
      return `https://image.tmdb.org/t/p/w300/${img}`
    }
  } 
}

</script>

<style>
  .text-style {
    font-family: Cafe24Oneprettynight;
    font-size: 10px;
    line-height: auto;
    margin: 0 auto;
  }

  .card-custom {
    object-fit: cover;
  }
</style>
