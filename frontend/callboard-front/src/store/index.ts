import Vue from 'vue'
import Vuex from 'vuex'
import $ from 'jquery'
import axios from "axios";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    url_server: "http://127.0.0.1:8000/",
    url_media: "http://127.0.0.1:8000",
    auth_user: false,
    user: "",
    // adverts: "",
  },
  getters: {
     get_url_server(state) {
         return state.url_server
     },
     get_auth(state) {
        return state.auth_user
     },
     get_user_info(state) {
        return state.user
     },
     get_url_media(state) {
        return state.url_media
     },
     // get_adverts(state){
     //   return state.adverts
     // }
  },
  mutations: {
    set_auth(state, value) {
       state.auth_user = value
    },
    set_user_info(state, value) {
        state.user = value
    },
    // set_adverts(state, value) {
    //     state.adverts = value
    // },
  },
  actions: {
    user_info(context) {
        $.ajax({
            url: context.getters.get_url_server + 'rest-auth/user/',
            type: "GET",
            success: (response) => {
                context.commit('set_user_info', response)
            },
            error: (response) => {
                if (response.status === 400) {
                    // this.mess = response.responseJSON.non_field_errors[0]
                }
            }
        })
     },
     // adverts(context) {
     //     $.ajax({
     //         url: context.getters.get_url_server + '',
     //         type: "GET",
     //         success: (response) => {
     //             context.commit('set_adverts', response)
     //         },
     //         error: (response) => {
     //             if (response.status === 400) {
     //                 // this.mess = response.responseJSON.non_field_errors[0]
     //             }
     //         }
     //     })
     //  }
  },
  modules: {
  }
})
