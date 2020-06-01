<template>
  <div class="home">
    <div id="content">
      <div class="container ">
        <div class="row">
          <div class="col col-md-6 offset-md-3 align-self-center">
            <h1 class="font-weight-bold border border-dark rounded-pill align-middle text-advert">Усі оголошення</h1>
          </div>
        </div>
      </div>
      <Advert v-for="(advert, index) in adverts.slice().reverse()"
             :key="index"
             v-bind:advert_data="advert">
      </Advert>
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'
  import Advert from '../components/Advert';


  export default {
    name: 'home',
    components: {
      Advert,
    },
    props: {},
    data() {
      return {
        adverts: "",
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
            url: this.$store.getters.get_url_server + '',
            type: "GET",
            success: (response) => {
                this.adverts = response.results
            },
            error: (response) => {
                if (response.status === 400) {
                    this.mess = response.responseJSON.non_field_errors[0]
                }
            }
        })
      }
    },
    // filters: {
    //   reverse(value) {
    //     return value.slice().reverse();
    //   },
    // }
  }
</script>

<style media="screen">
  #content {
    /* padding-bottom: 131px; */
    /* Height of the footer element */
  }
  .text-advert {
    text-align: center;
    margin-top: 0.3rem;
  }
</style>
