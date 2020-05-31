<template>
  <div id="app">
    <Menu @showLogin="setLogin(true)"></Menu>
    <Login v-if="login" @hideLogin="setLogin(false)"></Login>
    <router-view/>
  </div>
</template>

<script>
  import Menu from '@/components/Menu.vue'
  import Login from '@/components/Login.vue'
  import $ from 'jquery'

  export default {
    name: 'app',
    components: {
      Menu,
      Login,
    },
    data(){
      return{
        login: false,
      }
    },
    created() {
      if (sessionStorage.getItem("token")) {
        this.$store.commit("set_auth", true)
        $.ajaxSetup({
          headers: {'Authorization': "Token " + sessionStorage.getItem('token')},
        });
        // this.$store.dispatch('user_info')
      } else {
        this.$store.commit("set_auth", false)
      }
    },
    methods: {
      setLogin(value) {
        this.login = value
      }
    }
  }
</script>

<style lang="scss">
$image-path: '~@/../mdb/mdbvue/img';
@import '~@/../mdb/mdbvue/scss/mdb-free.scss';

  body {
    background: #e6ecf0;
  }
</style>
