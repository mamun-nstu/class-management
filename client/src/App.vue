<template>
  <Header />
  <router-link to="/">Home</router-link>
  <router-link to="/about">About</router-link>
  <router-view/>
  <p>{{ $store.state.test_module.count }}</p>
  <button @click="$store.commit(INCREMENT)">Click me</button>
  <Footer />
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
      INCREMENT
  };
}
}
;
</script>

