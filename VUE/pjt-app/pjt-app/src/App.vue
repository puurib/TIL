<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'home', params: { movieList: movieList } }">Home</router-link>
      <router-link :to="{ name: 'random', params: { movieList: movieList } }">Random</router-link>
      <router-link :to="{ name: 'watch-list' }">Watch List</router-link>
    </nav>
  <router-view/>
  </div>
</template>

<script>
import axios from 'axios'

const API_KEY = 'e53010cbbbc91dcb3b26e8894f6a8116'
const API_URL = 'https://api.themoviedb.org/3/movie/popular'

export default {
  name: 'App',
  components: {
  },
  data: () => {
    return {
      movieList: [],
    }
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      const params = {
        api_key: API_KEY,
        language: 'ko',
      }
      
      axios({
        method: 'get',
        url: API_URL,
        params,
      })
      .then(res => {
        console.log(res)
        this.movieList = res.data.results
      })
    },
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
}

nav {
  padding: 30px;
}

nav a {
  font-family: HSSaemaul-Regular;
  font-size: 30px;
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

@font-face {
  font-family: 'Cafe24Oneprettynight';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_twelve@1.1/Cafe24Oneprettynight.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'SuseongDotum';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2205@1.0/SuseongDotum.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'HSSaemaul-Regular';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2108@1.1/HSSaemaul-Regular.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}
</style>
