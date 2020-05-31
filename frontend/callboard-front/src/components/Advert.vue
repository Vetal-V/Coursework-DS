<template>
  <div class="main-adverts">
    <div class="row advert">
      <div class="col-12"><p>{{advert_data.subject}}</p></div>
      <div class="col-12" v-if="advert_data.images">
        <img class="image-home" :src="advert_data.images.photos[0].image" alt="Image not found.">
      </div>
      <div v-else>
        <img class="image-home" src="../../public/default-adv-photo.png" alt="Image not found.">
      </div>
      <div class="col-12">{{advert_data.category.name}}</div>
      <div class="col-12">{{advert_data.filters.name}}</div>
      <div class="col-12">{{advert_data.price}}</div>
      <div class="col-12">{{advert_data.created}}</div>
      <hr>
    </div>
 </div>
</template>

<script>
  export default{
    name: "Advert",
    props: {
      advert_data: ""
    }
  }
</script>

<style scoped>
  .image-home{
    height: 110px;
    width: 150px;
  }

  .main-advert {
    margin: 0 auto;
    max-width: 700px;
    box-shadow: 0px 2px 20px 1px #cddae2
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
