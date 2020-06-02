<template>
  <div class="Profile">
    <ProfileDetail
           v-bind:profile_data="profile">
    </ProfileDetail>
  </div>
</template>

<script>
  import $ from 'jquery'
  import ProfileDetail from '../components/ProfileDetail'
  export default {
    name: "Profile",
    components: {
      ProfileDetail,
    },
    data() {
      return {
        profile: "",
      }
    },
    created() {
      //do something after creating vue instance
      this.loadProfile()
    },
    methods: {
      loadProfile(){
        $.ajax({
            url: this.$store.getters.get_url_server + 'profile/'+this.$store.getters.get_user_info.pk,
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
  }
</script>

<style scoped>

</style>
