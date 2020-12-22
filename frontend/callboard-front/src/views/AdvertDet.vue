<template>
  <div class="AdvertDet">
    <!-- {{advert_detail}}
    {{profile}}
    {{advert_detail.user.id}} -->
    <div class="container">
      <div class="adv-subject">
        <h2 class="font-weight-bold border-dark text-advert">{{advert_detail.subject}}</h2>
        <hr>
      </div>
      <div class="row">
          <div class="col col-9">
            <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel" v-if="advert_detail.images !== null">
              <ol class="carousel-indicators">
                <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                <li data-target="#carouselExampleIndicators" data-slide-to="3"></li>
                <li data-target="#carouselExampleIndicators" data-slide-to="4"></li>
              </ol>
              <div class="carousel-inner">
                <div class="photos">
                  <div class="carousel-item active" v-if="advert_detail.images.photos[0]">
                    <img class="d-block w-100" :src="advert_detail.images.photos[0].image" alt="Фото слайд">
                  </div>
                  <div v-else class="carousel-item active">
                    <img class="" src="../../public/default-adv-photo.png" alt="Image not found.">
                  </div>
                  <div class="carousel-item" v-if="advert_detail.images.photos[1]">
                    <img class="d-block w-100" :src="advert_detail.images.photos[1].image" alt="Другий слайд">
                  </div>
                  <div v-else class="carousel-item">
                    <img class="" src="../../public/default-adv-photo.png" alt="Image not found.">
                  </div>
                  <div class="carousel-item" v-if="advert_detail.images.photos[2]">
                    <img class="d-block w-100" :src="advert_detail.images.photos[2].image" alt="Третій слайд">
                  </div>
                  <div v-else class="carousel-item">
                    <img class="w-100" src="../../public/default-adv-photo.png" alt="Image not found.">
                  </div>
                  <div class="carousel-item" v-if="advert_detail.images.photos[3]">
                    <img class="d-block w-100" :src="advert_detail.images.photos[3].image" alt="Четвертий слайд">
                  </div>
                  <div v-else class="carousel-item">
                    <img class="w-100" src="../../public/default-adv-photo.png" alt="Image not found.">
                  </div>
                  <div class="carousel-item" v-if="advert_detail.images.photos[4]">
                    <img class="d-block w-100" :src="advert_detail.images.photos[4].image" alt="П'ятий слайд">
                  </div>
                  <div v-else class="carousel-item">
                    <img class="w-100" src="../../public/default-adv-photo.png" alt="Image not found.">
                  </div>
                </div>
              </div>
              <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="sr-only">Назад</span>
              </a>
              <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only">Вперед</span>
              </a>
            </div>
            <div class="no-images" v-else>
                <img class="image-home" src="../../public/default-adv-photo.png" alt="Image not found.">
            </div>
          </div>
          <div class="col col-3" v-if="$store.getters.get_auth === true">
            <button class="btn btn-lg btn-primary right-button"  @click="loadProfile(advert_detail.user.id)" type="submit"><h5>Показати деталі про автора оголошення</h5></button>
            <div class="user-info" v-if="profile !== ''">
              <div v-if="profile.phone !== '' && profile.email_two !== '' && profile.first_name !== ''">
                <hr>
                <h4 class="text-center">Ім'я: {{profile.first_name}}</h4>
                <h4 class="text-center">Телефон: {{profile.phone}}</h4>
                <h4 class="text-center">Пошта: {{profile.email_two}}</h4>
              </div>
              <div v-else>
                  <hr>
                  <h4 class="text-center">Користувач не вказав контактної інформації.</h4>
              </div>
            </div>
          </div>
          <div class="col col-3" v-else>
            <p class="text-justify  pb-3">Щоб побачити контактні дані автора оголошення, будь ласка авторизуйтеся або зареєструйтеся.</p>
          </div>
      </div>
      <div class="info">
        <hr>
        <div class="row">
          <div class="col col-3">
              <h3>Категорія:</h3>
          </div>
          <div class="col col-9">
            <span class="description-text"><h4 class=" border-bottom">{{advert_detail.category.name}}</h4> </span>
          </div>
        </div>

        <div class="row">
          <div class="col col-3">
              <h3>Тип пропозиції:</h3>
          </div>
          <div class="col col-9">
            <span class="description-text"><h4 class=" border-bottom">{{advert_detail.filters.name}}</h4> </span>
          </div>
        </div>
        <div class="row">
          <div class="col col-3">
              <h3>Опис:</h3>
          </div>
          <div class="col col-9">
            <span class="description-text"><h4 class=" border-bottom">{{advert_detail.description}}</h4> </span>
          </div>
        </div>

        <div class="row">
          <div class="col col-3">
              <h3>Ціна:</h3>
          </div>
          <div class="col col-9">
            <span class="description-text"><h4 class=" border-bottom">{{advert_detail.price}} <i class="fas fa-hryvnia"></i></h4> </span>
          </div>
        </div>

        <div class="row">
          <div class="col col-3">
              <h3>Дата публікації:</h3>
          </div>
          <div class="col col-9">
            <span class="description-text"><h4 class=" border-bottom">{{advert_detail.created | filterDateTime}} року.</h4> </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'
  // import ProfileDetail from '../components/AdvertDetail'
  export default {
    name: "AdvertDet",
    data() {
      return {
        advert_detail: "",
        user_id: '',
        profile: '',
      }
    },
    created() {
      //do something after creating vue instance
      this.loadAdvert(this.$route.params.slug)
    },
    methods: {
      loadAdvert(slug){
        $.ajax({
            url: this.$store.getters.get_url_server + slug,
            type: "GET",
            success: (response) => {
                this.advert_detail = response
            },
            error: (response) => {
                if (response.status === 400) {
                    this.mess = response.responseJSON.non_field_errors[0]
                }
            }
        })
      },
      loadProfile(id){
        $.ajax({
            url: this.$store.getters.get_url_server + 'profile/'+ id ,
            type: "GET",
            success: (response) => {
                this.profile = response
            },
            error: (response) => {
                if (response.status === 400) {
                    this.mess = response.responseJSON.non_field_errors[0]
                }
            }
        })
      },
    },
    filters: {
      filterDateTime(item) {
        let old_date = new Date(item)
        return `
          ${old_date.getHours()}:${old_date.getMinutes()} - ${old_date.getDate()}.${old_date.getMonth()}.${old_date.getFullYear()}`
      },
    },
  }
</script>

<style scoped>
  img{
    height: 750px;
  }
  .image-home{
    height: 750px;
    border: 1px solid black;
  }
  .text-advert{
    margin-top: 10px;
  }
  .right-button{
    margin-top: 250px;
  }
  h4{
    padding-left: 10px;
  }
  border-bottom{
   padding-bottom: 20px;
  }
  .text-justify {
    text-align: justify!important;
    margin-top: 20rem;
    font-size: 25px;
    text-indent: 1.5em;
  }
</style>
