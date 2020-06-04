<template >
  <div class="ChangeProfile" id="loginModal">
    <div class="modal-dialog modal-dialog-centered auth-modal">
        <div class="modal-content">
            <!-- Modal Header -->
            <div class="modal-header">
                <h4 class="modal-title">Змінити дані профілю</h4>
                <button @click="close" type="button" class="close" data-dismiss="modal">x</button>
            </div>

            <!-- Modal body -->
            <div class="modal-body row">
                <div class="col col-5"><h4>Додаткова пошта:</h4> </div>
                <div class="col col-7 .col-sm-12 ">
                  <h5>{{this.profile_data.email_two}}</h5>
                  <button class="btn btn-info"  type="submit"  @click="setChangeEmail()" ><h5>Змінити</h5></button>
                  <input v-if="changeEmail" class="login-field" type="text" placeholder="Введіть вашу нову пошту" value="" v-model="profile.email_two">
                </div>

                <div class="col col-12">
                  <hr>
                </div>

                <div class="col col-5"><h4>Телефон:</h4> </div>
                <div class="col col-7 .col-sm-12 ">
                  <h5>{{this.profile_data.phone}}</h5>
                  <button class="btn btn-info"  type="submit"  @click="setChangePhone()" ><h5>Змінити</h5></button>
                  <input v-if="changePhone" class="login-field" type="text" placeholder="Введіть ваш новий номер" value="" v-model="profile.phone">
                </div>

                <div class="col col-12">
                  <hr>
                </div>

                <div class="col col-5"><h4>Ім'я:</h4> </div>
                <div class="col col-7 .col-sm-12 ">
                  <h5>{{this.profile_data.first_name}}</h5>
                  <button class="btn btn-info"  type="submit"  @click="setChangeFirst()" ><h5>Змінити</h5></button>
                  <input v-if="changeFirst" class="login-field" type="text" placeholder="Введіть ваше нове ім'я" value="" v-model="profile.first_name">
                </div>

                <div class="col col-12">
                  <hr>
                </div>

                <div class="col col-5"><h4>Прізвище:</h4> </div>
                <div class="col col-7 .col-sm-12 ">
                  <h5>{{this.profile_data.last_name}}</h5>
                  <button class="btn btn-info"  type="submit"  @click="setChangeSecond()" ><h5>Змінити</h5></button>
                  <input v-if="changeSecond" class="login-field" type="text" placeholder="Введіть нове прізвище" value="" v-model="profile.last_name">
                </div>

                <div class="col col-12">
                  <hr>
                </div>

                <div class="col col-3"></div>
                <button class="col col-6 login-field" type="button" @click="changeProfile">Підтвердити зміни</button>
                <div class="error-mess"> {{mess}} </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'
  export default {
    name: "ChangeProfile",
    data() {
      return {
        profile: {
          email_two: "",
          phone: "",
          first_name: "",
          last_name: "",
        },
        // profile_data: '',

        mess: '',
        changeEmail: false,
        changePhone: false,
        changeFirst: false,
        changeSecond: false,
      }
    },
    props: {
      profile_id: '',
      profile_data: '',
      show: ''
    },
    methods: {
      setChangeEmail(){
        this.changeEmail = true;
      },
      setChangePhone(){
        this.changePhone = true;
      },
      setChangeFirst(){
        this.changeFirst = true;
      },
      setChangeSecond(){
        this.changeSecond = true;
      },
      changeProfile() {
        if (this.changeEmail) {
          this.profile_data.email_two = this.profile.email_two ;
        }
        if (this.changePhone) {
          this.profile_data.phone = this.profile.phone;
        }
        if (this.changeFirst) {
          this.profile_data.first_name = this.profile.first_name;
        }
        if (this.changeSecond) {
          this.profile_data.last_name = this.profile.last_name;
        }

        $.ajax({
            url: this.$store.getters.get_url_server + 'profile/update/' + this.profile_id + '/',
            type: "PUT",
            data: {
                email_two: this.profile_data.email_two,
                phone: this.profile_data.phone,
                first_name: this.profile_data.first_name,
                last_name: this.profile_data.last_name,
            },
            success: (response) => {
                this.$emit("setnotShow")
                window.location =  '/profile/'+this.profile_id
            },
            error: (response) => {
                if (response.status === 400) {
                    this.mess = response.responseJSON.non_field_errors[0]
                }
            }
        })
      },
      close() {
          this.$emit("setnotShow")
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
  .modal-dialog {
    max-width: 600px;
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
