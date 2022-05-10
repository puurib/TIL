<template>
  <div>
    <h1>로또</h1>
    <button @click="getLottoNumbers">Get Lucky Numbers</button>
    <p>{{ lottoNumber }} </p>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'LottoView',
  data : function(){
    return {
      lottoNumber : [],
    }
  },
  //클릭했을 때 동작할 메서드 선언
  methods : {
    getLottoNumbers : function(){
      // const numbers = _.range(1,46)
      // this.lottoNumber = _.sampleSize(_.range(1, 46), 6)
      //url에서 라우팅 된 변수를 얻어 오기
      const numOfLotto = this.$route.params.lottoNum
      this.lottoNumber = _.sortBy(_.sampleSize(_.range(1, 46), numOfLotto))
    }
  }
}
</script>
