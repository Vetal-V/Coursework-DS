<template>
  <div class="ProfileDetail">
    <div class="container">
      <div class="msg-one col-12">
        <div class="msg-inner">
          <div class="">
            <hr>
            <br>
            <h4>Фото профілю:</h4>
          </div>
            <div class="w-image" v-if="profile_data.avatar === null">
              <img class="image-home" src="../../public/default-avatar.png" alt="Image not found.">
              <button class="btn btn-lg btn-primary" type="submit"><h5> Змінити фото </h5></button>
            </div>
            <div v-else class="w-image">
              <img class="image-home" :src="profile_data.avatar" alt="Image not found.">
            </div>

            <div class="w-body">
              <div class="text-subj">
                <h4>Дані користувача:</h4>
              </div>
              <div><h5>Ім'я користувача: {{$store.getters.get_user_info.username}}</h5> </div>
              <div><h5>Пошта користувача: {{$store.getters.get_user_info.email}}</h5> </div>
              <hr>
              <div class="text-subj">
                <h4>Дані профілю:</h4>
              </div>
              <div><h5>Додаткова пошта: {{profile_data.email_two}}</h5> </div>
              <div><h5>Номер телефону: {{profile_data.phone}}</h5> </div>
              <div><h5>Ім'я': {{profile_data.first_name}}</h5> </div>
              <div><h5>Прізвище: {{profile_data.last_name}}</h5> </div>
              <button class="btn btn-lg btn-primary  right-button" type="submit"><h5>Редагувати дані профілю</h5></button>
            </div>
            <br>
            <hr>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default{
    name: "ProfileDetail",
    props: {
      profile_data: ""
    },
  }
</script>

<style scoped>
  .content{
    /* min-height: calc(100vh-131px-100px); */
    padding-bottom: 8rem;
  }
  .right-button{
    padding-bottom: 1rem;
  }
  .h4, h4 {
    font-size: 2.0vw;
    font-weight: bold;
    padding-left: 0.7vw;
  }
  .h5, h5 {
    font-size: 1.2vw;
  }
  .adv-subject{
    border-bottom: 1px solid #aaa;
  }
  .adv-subject:hover{
    color: blue;
  }

  .image-home{
    height: 12vw;
    width: 12vw;
  }

  .msg-one:not(.bar) .msg-inner {
    padding: 20px;
    padding-bottom: 8.5rem;
  }
  .msg-one:not(.bar) .w-image {
    width: 12vw;
    float: left;
  }
  .btn.btn-lg {
    margin-top: 1vw;
    padding: 0.5vw 1.8vw;
    /* font-size: 0.94rem; */
  }

  .w-image {
    height: 160px;
    border: 1px solid #dcdcdc;
    background: #ededed;
    margin-left: 30px;
  }
  .msg-one:not(.bar) .w-body {
    /* width: calc(100% - 210px); */
    padding: 0 100px 0 100px;
    height: 135px;
  }
  .msg-inner {
    width: 100%;
    border: 1px solid #e1e1e1;
    background: #fff;
    border-radius: 4px;
    position: relative;
    padding-bottom: 20px;
    /* font-size: 2vw; */
    /* margin-bottom: 20rem; */
  }
  .w-body {
      display: inline-block;
      position: relative;
  }

  .advert {
    padding: 10px;
    background: #fff;
    border-left: 1px solid #e6ecf0;
    border-right: 1px solid #e6ecf0;
    border-bottom: 1px solid #e6ecf0;
    margin-right: 0;
    margin-left: 0;
  }

  .advert:hover {
    background: #f5f8fa;
    cursor: pointer;
  }
</style>
