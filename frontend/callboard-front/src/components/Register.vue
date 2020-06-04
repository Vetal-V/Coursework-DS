<template >
  <div class="" id="RegisterModal">
    <div class="modal-dialog modal-dialog-centered auth-modal">
        <div class="modal-content">
            <!-- Modal Header -->
            <div class="modal-header">
                <h4 class="modal-title">Реєстрація</h4>
                <button @click="close" type="button" class="close" data-dismiss="modal">x</button>
            </div>

            <!-- Modal body -->
            <div class="modal-body row">

                <div class="col-1"></div>
                <input class="col-10 .col-sm-12 login-field" type="text" placeholder="Логін" value="" v-model="user.username">

                <div class="col-1"></div>
                <input class="col-10 .col-sm-12 login-field" type="password" placeholder="Пароль" value="" v-model="user.password1">

                <div class="col-1"></div>
                <input class="col-10 .col-sm-12 login-field" type="password" placeholder="Підтвердження паролю" value="" v-model="user.password2">

                <div class="col-1"></div>
                <input class="col-10 .col-sm-12 login-field" type="text" placeholder="E-mail" value="" v-model="user.email">
                <div class="col-4"></div>
                <button class="col-4 .col-sm-5 login-field" type="button" @click="setRegister">Зареєструватися</button>
                <div class="col-4"></div>
                <div class="col-12 error-mess text-justify"> {{mess}}  </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'

  export default {
    name: "Register",
    data() {
      return {
        user: {
          username: "",
          password1: "",
          password2: "",
          email: "",
        },
        mess_username: '',
        mess_password1: '',
        mess_password2: '',
        mess_email: '',
        mess: ''
      }
    },
    methods: {
      setRegister() {
        $.ajax({
            url: this.$store.getters.get_url_server + 'rest-auth/registration/',
            type: "POST",
            data: {
                username: this.user.username,
                password1: this.user.password1,
                password2: this.user.password2,
                email: this.user.email,
            },
            success: (response) => {
                this.mess = "Реєстрація успішно завершена. Будь-ласка авторизуйтеся."
                this.close()
            },
            error: (response) => {
              if (response.status === 400) {
                this.mess = "    Помилка, перевірте дані для реєстрації. Пароль повинен містити не менше 8 символів (обов'язково повинні бути літери верхнього регістру та цифри'). Логін повинен бути унікальний (можливо, введений вами логін уже використовується)."
              }
            }

        })
      },
      close() {
          this.$emit("hideRegister")
      }
    }
  }
</script>

<style scoped>
  #RegisterModal {
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
