<template>
  <div class="Search">
    <!-- {{adverts}} -->
    <div id="content">
      <div class="container ">
        <div class="row">
          <div class="col col-md-6 offset-md-3 align-self-center">
            <h1 class="font-weight-bold border border-dark rounded-pill align-middle text-advert">Результати пошуку:</h1>
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
    name: 'Search',
    components: {
      Advert,
    },
    data() {
      return {
        adverts: '',
        mess: '',
      }
    },
    created() {
      //do something after creating vue instance
      this.searchAdv(this.$route.params.elem)
      // concole.log(this.$store.getter.get_user_info)
    },
    methods: {
      searchAdv(item){
        $.ajax({
            url: this.$store.getters.get_url_server + 'search/?search=' + item,
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
      },
    },
  }
</script>

<style media="screen">
  #content {
    /* padding-bottom: 131px; */
    /* Height of the footer element */
    min-height: calc(100vh - 131px - 130px);
  }
  .text-advert {
    text-align: center;
    margin-top: 0.3rem;
  }
</style>
