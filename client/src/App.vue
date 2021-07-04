<template>
  <v-app>

    <v-main>
      <Header/>
      <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link>
      <router-view/>
      <p>{{ $store.state.test_module.count }}</p>
      <button @click="$store.commit(INCREMENT)">Click me</button>
      <Footer/>
    </v-main>
  </v-app>
</template>

<script>
import {INCREMENT} from "./store/mutation_types";
import Header from "./components/Header";
import Footer from "./components/Footer";
import BackendApi from "./js/backend";
export default {
  name: "App",
  components: {Footer, Header},
  beforeMount() {
    window.onSignIn = function (googleUser) {
      var profile = googleUser.getBasicProfile();
      console.log('ID: ' + profile.getId());
      console.log('Name: ' + profile.getName());
      console.log('Image URL: ' + profile.getImageUrl());
      console.log('Email: ' + profile.getEmail());
      const auth_resp = googleUser.getAuthResponse();
      const token = auth_resp.id_token;
      console.log('Token: ', token, 'auth_response', auth_resp);
      return BackendApi.generic.post({
        url: '/api/session',
        data: {
          token,
        }
      })
    }
  },
  data() {
    return {
      INCREMENT,
    };
  },
};
</script>
<style lang="scss">
body {
  background-color: #FFFFFF !important;
}

#app {
  max-width: 1000px;
  margin: auto;
  align-content: center;
}
</style>