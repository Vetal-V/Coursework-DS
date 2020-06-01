<template>
  <div class="main-adverts">
    <div class="row advert">
      <!-- <div class="col-12"><p>{{advert_data.subject}}</p></div>
      <div class="col-12" v-if="advert_data.images">
        <img class="image-home" :src="advert_data.images.photos[0].image" alt="Image not found.">
      </div>
      <div v-else>
        <img class="image-home" src="../../public/default-adv-photo.png" alt="Image not found.">
      </div>
      <div class="col-12">{{advert_data.category.name}}</div>
      <div class="col-12">{{advert_data.filters.name}}</div>
      <div class="col-12">{{advert_data.price}}</div>
      <div class="col-12">{{advert_data.user}}</div>
      <div class="col-12">{{advert_data.created|filterDateTime}}</div>
      <hr> -->
      <div class="container ">
        <div class="msg-one col-12 offset-md-2">
          <div class="msg-inner">
            <div class="w-image" v-if="advert_data.images">
              <img class="image-home" :src="advert_data.images.photos[0].image" alt="Image not found.">
            </div>
            <div v-else class="w-image">
              <a href="#"><img class="image-home" src="../../public/default-adv-photo.png" alt="Image not found."></a>
            </div>
            <div class="w-body">
              <div><h3 class="adv-subject "><a href="#" class="text-decoration-none text-reset">{{advert_data.subject}}</a></h3></div>
              <div><h3 class="font-weight-bold">Ціна: {{advert_data.price}} <i class="fas fa-hryvnia"></i></h3></div>
              <div><h5><i class="fas fa-clock"></i> Дата публікації: {{advert_data.created|filterDateTime}}</h5></div>
              <div><h6>Тип пропозиції: {{advert_data.filters.name}}</h6></div>
              <div class="col align-self-end">
                <h6 class="text-right"><a href="#" class="">Детальніше</a></h6>
              </div>
              <p>{{advert_data.slug}}</p>
            </div>
          </div>
        </div>
      </div>
      <hr>
    </div>
 </div>
</template>

<script>
  export default{
    name: "Advert",
    props: {
      advert_data: ""
    },
    filters: {
      filterDateTime(item) {
        let old_date = new Date(item)
        return `
          ${old_date.getHours()}:${old_date.getMinutes()} - ${old_date.getDate()}.${old_date.getMonth()}.${old_date.getFullYear()}`
      },
    }
  }
</script>

<style scoped>
  .adv-subject{
    border-bottom: 1px solid #aaa;
  }
  .adv-subject:hover{
    color: blue;
  }

  .image-home{
    height: 160px;
    width: 210px;
  }

  .msg-one:not(.bar) .msg-inner {
    padding: 20px;
    padding-bottom: 25px;
  }
  .msg-one:not(.bar) .w-image {
    width: 210px;
    float: left;
  }
  .w-image {
    height: 160px;
    border: 1px solid #dcdcdc;
    background: #ededed;
  }
  .msg-one:not(.bar) .w-body {
    width: calc(100% - 210px);
    padding: 0 100px 0 30px;
    height: 135px;
  }
  .msg-inner {
    width: 100%;
    border: 1px solid #e1e1e1;
    background: #fff;
    border-radius: 4px;
    position: relative;
    padding-bottom: 20px;
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

  .form-twit {
    width: 100%;
    height: auto;
    padding: 15px;
    margin: 15px auto;
    background: #fff;
  }

  .btn-tweet {
    border-radius: 100px;
    box-shadow: none;
    cursor: pointer;
    font-size: 14px;
    font-weight: bold;
    line-height: 20px;
    padding: 6px 16px;
    position: relative;
    text-align: center;
    white-space: nowrap;
    background: #46D89E;
  }

  .btn-follow {
    padding: 6px 16px;
    border-radius: 100px;
    background: #00acd8;
  }
</style>
