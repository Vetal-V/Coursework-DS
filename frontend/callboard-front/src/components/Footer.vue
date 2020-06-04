<template >
  <!-- Footer -->
  <footer class="page-footer font-medium special-color-dark pt-4 ">

    <!-- Footer Elements -->
    <div class="container">

      <!-- Social buttons -->
      <ul class="list-unstyled list-inline text-center">
        <li class="list-inline-item">
          <a class="btn-floating btn-fb mx-1" href="https://facebook.com" target="_blank">
            <i id="facebook" class="fab fa-facebook-f icons"> </i>
          </a>
        </li>
        <li class="list-inline-item">
          <a class="btn-floating btn-gplus mx-1" href="https://google.com.ua" target="_blank">
            <i id="google" class="fab fa-google-plus-g icons"> </i>
          </a>
        </li>
        <li class="list-inline-item">
          <a class="btn-floating btn-tw mx-1" href="https://twitter.com/" target="_blank">
            <i id="twitter" class="fab fa-twitter icons" > </i>
          </a>
        </li>
        <li class="list-inline-item">
          <a class="btn-floating btn-li mx-1" href="https://linkedin.com/" target="_blank">
            <i id="linkedin" class="fab fa-linkedin icons"> </i>
          </a>
        </li>
        <li class="list-inline-item">
          <a class="btn-floating btn-dribbble mx-1" href="https://www.instagram.com/?hl=uk" target="_blank">
            <i id="instagram" class="fab fa-instagram icons"> </i>
          </a>
        </li>
      </ul>
      <!-- Social buttons -->

    </div>
    <!-- Footer Elements -->

    <!-- Copyright -->
    <div class="footer-copyright text-center py-3">© 2020 Copyright:
      <a href="#"> Дошка оголошень. Курсова робота.</a>
    </div>
    <!-- Copyright -->

  </footer>
  <!-- Footer -->
</template>


<script>
  export default{
    name: "Footer",
  }
</script>


<style scoped>
  #google:hover {
    color:#d50f25;
  }
  #linkedin:hover {
    color:#0e76a8;
  }
  #twitter:hover {
    color:#1EA1F3;
  }

  #facebook:hover{
    color:#4267B2;
  }

  #instagram:hover{
    color:#FDCC65;
  }
  .icons {
    font-size: 2.4rem;
    margin-left: 1.45rem;
    margin-right: 1.45rem;
  }
  .pt-4, .py-4 {
    padding-top: 1.5rem!important;
    margin-top: 0.8rem;
  }
  .page-footer{
    margin-top: calc(100vh-131px)
  }
</style>
