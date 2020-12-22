<template >
  <div class="" id="loginModal">
    <div class="modal-dialog modal-dialog-centered auth-modal">
        <div class="modal-content">
            <!-- Modal Header -->
            <div class="modal-header">
                <h4 class="modal-title">Вхід</h4>
                <button @click="close" type="button" class="close" data-dismiss="modal">x</button>
            </div>

            <!-- Modal body -->
            <div class="modal-body row">
                <input class="col-5 .col-sm-12 login-field" type="text" placeholder="Логін" value="" v-model="user.username">
                <input class="col-5 .col-sm-12 login-field" type="password" placeholder="Пароль" value="" v-model="user.password">
                <button class="col-2 .col-sm-12 login-field" type="button" @click="setLogin">Увійти</button>
                <div class="error-mess"> {{mess}} </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'
  export default {
    name: "Login",
    data() {
      return {
        user: {
          username: "",
          password: ""
        },
        mess: '',
      }
    },
    methods: {
      setLogin() {
        $.ajax({
            url: this.$store.getters.get_url_server + 'auth/token/login/',
            type: "POST",
            data: {
                username: this.user.username,
                password: this.user.password
            },
            success: (response) => {
                sessionStorage.setItem("token", response.auth_token)
                this.$store.commit("set_auth", true)
                $.ajaxSetup({
                    headers: {'Authorization': "Token " + sessionStorage.getItem('token')},
                });
                this.close()
                window.location = '/'
            },
            error: (response) => {
                if (response.status === 400) {
                    this.mess = response.responseJSON.non_field_errors[0]
                }
            }
        })
      },
      close() {
          this.$emit("hideLogin")
      },
    }
  }
</script>

<style scoped>
  #loginModal {
     position: fixed;
     z-index: 1100;
     top: -30px;
     left: 40%;
  }
  .col-5 {
    flex: 0 0 41.666667%;
    max-width: 38.666667%;
  }
  .login-field {
    padding-left: 0.4rem;
    margin-left: 0.4rem;
  }
  .modal-body {
    position: relative;
    flex: 1 1 auto;
    padding: 1rem;
    margin-left: 0.1rem;
    margin-right: 0.1rem;
  }
  .error-mess {
    margin-top: 0.5rem;
  }
</style>
