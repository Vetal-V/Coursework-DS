<template>
  <div class="MyAdvert">
    <!-- {{myadverts}}
    {{mess}} -->
    <div id="content">
      <div class="container ">
        <div class="row">
          <div class="col col-md-6 offset-md-3 align-self-center">
            <h1 class="font-weight-bold border border-dark rounded-pill align-middle text-advert">Мої оголошення</h1>
          </div>
        </div>
      </div>
      <Advert v-for="(advert, index) in myadverts"
             :key="index"
             v-bind:advert_data="advert">
      </Advert>
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'
  import Advert from '../components/MyAdvertsList';

  export default {
    name: 'MyAdvert',
    components: {
      Advert,
    },
    data() {
      return {
        myadverts: '',
        mess: '',
      }
    },
    created() {
      //do something after creating vue instance
      this.loadAdv()
      // concole.log(this.$store.getter.get_user_info)
    },
    methods: {
      loadAdv() {
        $.ajax({
            url: this.$store.getters.get_url_server +'profile/adverts/',
            type: "GET",
            success: (response) => {
                this.myadverts = response
            },
            error: (response) => {
                if (response.status === 400) {
                    this.mess = response.responseJSON.non_field_errors[0]
                }
            }
        })
      },
    },
  }
</script>

<style media="screen">
  #content {
    min-height: calc(100vh - 131px - 130px);
  }
  .text-advert {
    text-align: center;
    margin-top: 0.3rem;
  }
</style>
