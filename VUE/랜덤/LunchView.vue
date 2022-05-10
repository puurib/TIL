<template>
  <div >
    <h1>점심메뉴</h1>
    <button @click="pickLunch">Pick Lunch</button>
    <p>{{ selectedMenu }}</p>
    <h2>로또 ㄱㄱ</h2>
    <button @click="pickLotto">로또 고고</button>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'LunchView',
  data : function(){
    return {
      menu : ['오리훈제','국밥','라면'],
      selectedMenu : null,
    }
  },
  methods : {
    pickLunch : function(){
      this.selectedMenu = _.sample(this.menu)
    },
    pickLotto : function(){
      this.$router.push({name : 'LottoView', params:{ lottoNum:6 }})
    }
  }
}
</script>

<style>

</style>
