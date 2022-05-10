import Vue from 'vue'
import VueRouter from 'vue-router'
import LottoView from '../views/LottoView.vue'
import LunchView from '../views/LunchView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/lunch',
    name: 'LunchView',
    component: LunchView
  },
  {
    path: '/lotto/:lottoNum',
    name: 'LottoView',
    component: LottoView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
