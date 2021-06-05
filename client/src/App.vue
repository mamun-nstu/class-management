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

export default {
  name: "App",
  components: {Footer, Header},
  data() {
    return {
      INCREMENT,
    };
  },
};
</script>
<style lang="scss">
body {
  background-color: #0f0f0f !important;
}
</style>