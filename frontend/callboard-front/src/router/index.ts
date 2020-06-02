import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Home from '../views/Home.vue'
import MyAdverts from '../views/MyAdvert.vue'
import Profile from '../views/Profile.vue'
import store from '../store/index'
import AdvertDet from '../views/AdvertDet.vue'
import Search from '../views/Search.vue'
Vue.use(VueRouter)

  const routes: Array<RouteConfig> = [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile,
      beforeEnter: (to, from, next) => {
        if (store.getters.get_auth) {
          next()
        } else {
          next({name: 'home'})
        }
      }
    },
    {
      path: '/myadverts',
      name: 'MyAdverts',
      component: MyAdverts,
      // beforeEnter: (to, from, next) => {
      //   if (store.getters.get_auth) {
      //     next()
      //   } else {
      //     next({name: 'home'})
      //   }
      // }
    },
    {
      path: '/advertdetail/:id/:slug',
      name: 'AdvertDet',
      component: AdvertDet,
    },
    {
      path: '/search/:elem',
      name: 'Search',
      component: Search,
    },
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
