<template >
  <nav class="navbar navbar-expand-xl navbar-dark menu">
      <!-- Collapse button -->
      <button class="navbar-toggler" type="button" data-toggle="collapse"
              data-target="#navbarNav"
              aria-controls="navbarNav" aria-expanded="false"
              aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav mr-auto">
              <li class="nav-item">
                  <a class="nav-link" href="" @click="goPage('home')">
                    <img src="../assets/logo.png" alt="LOGO SITE" class="logo-site">
                  </a>
              </li>
              <li class="nav-item elem-first-nav">
                  <a class="nav-link" href="" @click="goPage('home')">Головна</a>
              </li>
              <li class="nav-item elem-first-nav">
                  <a v-if="auth" @click="goPage('MyAdverts')" class="nav-link" href="#">
                      Мої оголошення
                  </a>
                  <a v-else @click="goLogin()" class="nav-link " href="#">Мої оголошення</a>
              </li>
              <li class="nav-item elem-first-nav">
                  <a v-if="auth" @click="goPage('Create')" class="nav-link" href="#">
                      Створити оголошення
                  </a>
                  <a v-else @click="goLogin()" class="nav-link " href="#">Створити оголошення</a>
              </li>
              <li class="nav-item elem-first-nav">
                  <a @click="goProfile('Profile', $store.getters.get_user_info.pk)"
                     v-if="auth"
                     class="nav-link"
                     href="#">
                     Профіль,
                      <span>{{$store.getters.get_user_info.first_name }}</span>
                  </a>
                  <a v-else @click="goLogin()" class="nav-link " href="#">Профіль</a>
              </li>
              <!-- <li class="nav-item my-0">
                  <img v-if="auth" class="avatar"
                       :src="$store.getters.get_url_media + $store.getters.get_user_info.avatar">
              </li> -->
              <li class="nav-item elem-first-nav">
                  <a v-if="auth" @click="logout()" class="nav-link" href="#">Вихід</a>
              </li>
              <li class="nav-item elem-first-nav">
                  <a v-if="!auth"
                     @click="goLogin()"
                     class="nav-link"
                     href="#"
                     data-toggle="modal"
                     data-target="#loginModal">
                      Вхід
                  </a>
              </li>
              <li class="nav-item elem-first-nav">
                  <a v-if="!auth"
                     @click="goRegister()"
                     class="nav-link"
                     href="#"
                     data-toggle="modal"
                     data-target="#loginModal">
                      Реєстрація
                  </a>
              </li>
          </ul>
          <!-- <ul class="navbar-nav mr-2 mt-lg-0">

          </ul> -->
          <form class="form-inline my-2 my-lg-0">
            <input class="form-control mr-sm-2" type="search" placeholder="Пошук" v-model="text" aria-label="Search">
            <button class="btn btn-lg btn-primary" @click="goSearch('Search', '')" type="submit">Знайти</button>
          </form>
      </div>
    </nav>
</template>

<script>
  import auth from '@/mixins/computedAuth.js'
  import $ from 'jquery'

  export default{
    name: "Menu",
    mixins: [
      auth
    ],
    data() {
      return {
        text: ''
      }
    },
    methods: {
      goPage(item) {
        this.$router.push({name: item})
      },
      goProfile(item, number) {
        this.$router.push({name: item, params: {id: number}})
      },
      goSearch(item, text) {
        this.$router.push({name: item, params: {elem: this.text}})
      },
      goLogin(){
        this.$emit("showLogin")
      },
      goRegister(){
        this.$emit("showRegister")
      },
      logout() {
        this.$store.commit("set_auth", false)
        sessionStorage.removeItem("token")
        $.ajaxSetup({
            headers: {'Authorization': ""},
        });
        window.location = '/'
      }
    }
  }
</script>

<style scoped>
  .navbar-expand-lg .navbar-collapse {
    min-width: 1100px;
  }

  .navbar-nav{
    display:flex;
    align-items:center;
  }

  .logo-site {
    height: 5rem;
  }
  #navbarNav {
    font-size: 1.3rem;
    padding-left: 1rem;
    padding-right: 2rem;
  }
  .nav-item {
    margin-left: 1rem;
  }
  .btn.btn-lg {
    padding: 0.7rem 1rem;
    font-size: 1rem;
    font-weight: bold;
  }
  .navbar-toggler-icon {
      display: inline-block;
      width: 1.5em;
      height: 1.5em;
      vertical-align: middle;
      content: "";
      background: no-repeat center center;
      background-size: 100% 100%;
  }
  .menu {
    margin: 0 auto;
    background: #2a2a2a;
    display: flex;
    flex: 0 0 auto;
    width: 100%;
  }


</style>
