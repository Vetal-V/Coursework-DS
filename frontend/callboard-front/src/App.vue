<template>
  <div id="app">
    <div class="wrapper">
      <Menu @showLogin="setLogin(true)" @showRegister="setRegister(true)"></Menu>
      <Login v-if="login" @hideLogin="setLogin(false)"></Login>
      <Register v-if="register" @hideRegister="setRegister(false)" ></Register>
      <router-view/>
      <div id="footer">
        <Footer></Footer>
      </div>
    </div>
  </div>
</template>

<script>
  import Menu from '@/components/Menu.vue'
  import Login from '@/components/Login.vue'
  import Register from '@/components/Register.vue'
  import Footer from '@/components/Footer.vue'

  import $ from 'jquery'

  export default {
    name: 'app',
    components: {
      Menu,
      Login,
      Footer,
      Register,
    },
    data(){
      return{
        login: false,
        register: false,
      }
    },
    created() {
      if (sessionStorage.getItem("token")) {
        this.$store.commit("set_auth", true)
        $.ajaxSetup({
          headers: {'Authorization': "Token " + sessionStorage.getItem('token')},
        });
        this.$store.dispatch('user_info')
      } else {
        this.$store.commit("set_auth", false)
      }
    },
    methods: {
      setLogin(value) {
        this.login = value
      },
      setRegister(value) {
        this.register = value
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

  #wrapper {
    min-height: 100%;
    position: relative;
  }

  #footer {
    width: 100%;
    height: 131px;
    // position: absolute;
    bottom: 0;
    left: 0;
  }
  #footer > .container {
    display: block;
  }
</style>
