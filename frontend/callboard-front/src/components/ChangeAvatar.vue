<template >
  <div v-if="this.show" class="ChangeAvatar" id="AvatarModal">
    <div class="modal-dialog modal-dialog-centered auth-modal">
        <div class="modal-content">
            <!-- Modal Header -->
            <div class="modal-header">
                <h4 class="modal-title">Змінити фото профілю</h4>
                <button @click="close"type="button" class="close" data-dismiss="modal">x</button>
            </div>

            <!-- Modal body -->
            <div class="modal-body row" id="myApp">
              <div class="input-group">
                <div class="custom-file">
                  <label>Вибрати файл
                    <input type="file" id="profile-photo" ref="file" v-on:change="handleFile1Upload()"/>
                  </label>
                  <!-- <form action="core/update.php" method="post" enctype="multipart/form-data" id="profile-photo" name="profile-photo-form">
                    <input type="file" id="photo-filename" name="avatar" class="edit-show panel photo-upload">
                  </form> -->
                </div>
              </div>
              <div class="col-5"></div>
              <button class="col-2 .col-sm-12 login-field" type="button" @click="change">Змінити</button>
              <div class="col-5"></div>
              <div class="error-mess"> {{mess}} </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'
  // import avatarSend from '@/mixins/SendAvatar.js'
  import axios from 'axios';

  export default {
    name: "ChangeAvatar",
    // mixins: [
    //   avatarSend
    // ],
    data() {
      return {
        avatar: "",
        mess: '',
        // photo: ''
      }
    },
    props: {
      profile_id: '',
      show: ''
    },
    methods: {
      handleFile1Upload() {
        this.avatar = this.$refs.file.files[0];
      },
      change() {
        let photo = new FormData();
        photo.append('avatar', this.$refs.file.files[0], '1234.jpg');

        $.ajax({
            url: this.$store.getters.get_url_server + 'profile/update/avatar/' + this.profile_id + '/',
            type: 'PUT',
            data: photo,
            contentType: false,
            processData: false,
            cache: false,
            success: (response) => {
                this.$emit("setnotShow")
                window.location = '/profile/'+this.profile_id
            },
            error: (response) => {
                this.mess = response.responseJSON.non_field_errors[0]
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
  #AvatarModal {
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
