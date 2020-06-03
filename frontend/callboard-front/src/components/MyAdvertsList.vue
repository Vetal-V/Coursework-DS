<template>
  <div class="MyAdvertsList">
    <div class="row advert">
      <div class="container ">
        <div class="msg-one col-11 offset-sm-2">
          <div class="msg-inner">
            <div class="w-image" v-if="advert_data.images">
              <img class="image-home" :src="$store.getters.get_url_media + advert_data.images.photos[0].image" alt="Image not found.">
            </div>
            <div v-else class="w-image">
              <a href="#"><img class="image-home" src="../../public/default-adv-photo.png" alt="Image not found."></a>
            </div>
            <div class="w-body">
              <div class="container-fluid">
                <div class="row align-items-start">
                  <div class="col">
                    <h3 class="adv-subject "><a href="#" class="text-decoration-none text-reset" @click="goPage('AdvertDet', advert_data.id, advert_data.slug)">{{advert_data.subject}}</a></h3>
                  </div>

                  <div class="row align-items-end">
                    <div class="col">
                      <a href="#" @click="goPage('EditMyAdvert', advert_data.id, advert_data.slug)"> <i class="fas fa-edit"></i></a>
                    </div>
                  </div>
                </div>
              </div>

              <div><h3 class="font-weight-bold">Ціна: {{advert_data.price}} <i class="fas fa-hryvnia"></i></h3></div>
              <div><h5><i class="fas fa-clock"></i> Дата публікації: {{advert_data.created|filterDateTime}}</h5></div>
              <div><h6>Тип пропозиції: {{advert_data.filters.name}}</h6></div>
              <div v-if="advert_data.moderation === true"><h6>Модерація: опубліковано.</h6></div>
              <div v-else><h6>Модерація: в процесі модерації.</h6></div>
              <div class="col align-self-end">
                <h6 class="text-right"><a href="#" class="" @click="goPage('AdvertDet', advert_data.id, advert_data.slug)">Детальніше</a></h6>
              </div>
              <!-- <p>{{advert_data.slug}}</p> -->
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
    name: "MyAdvertsList",
    props: {
      advert_data: ""
    },
    filters: {
      filterDateTime(item) {
        let old_date = new Date(item)
        return `
          ${old_date.getHours()}:${old_date.getMinutes()} - ${old_date.getDate()}.${old_date.getMonth()}.${old_date.getFullYear()}`
      },
    },
    methods: {
      goPage(item, number, slug) {
        this.$router.push({name: item, params: {id: number, slug: slug}})
      },
      // goEdit(item, number) {
      //   this.$router.push({name: item, params: {id: number}})
      // }
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
</style>
