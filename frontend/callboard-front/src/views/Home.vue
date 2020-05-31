<template>
  <div class="home">
    <Advert v-for="(advert, index) in adverts"
           :key="index"
           v-bind:advert_data="advert">
    </Advert>
  </div>
</template>

<script>
  import $ from 'jquery'
  import Advert from '../components/Advert';

  export default {
    name: 'home',
    components: {
      Advert
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
    }
  }
</script>

<style media="screen">

</style>
