<template>
  <div class="col-6 mx-auto text-center">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>|
      <router-link v-if="!isLoggedIn" to="/login">Login</router-link>
      <button v-if="isLoggedIn" class="btn btn-danger" @click="logout">Logout</button>
    </nav>
  </div>
  <router-view/>
  <footer class="col-6 mx-auto text-center">
    © Yassine Kharrat
  </footer>
</template>

<script>
export default{
  data(){
    return{
      isLoggedIn:false
    }
  },
  created(){
    if(localStorage.getItem("token")){
      this.isLoggedIn=true
    }
  },
  methods:{
    logout(){
      localStorage.removeItem("token")
      window.location.href="/login"
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
