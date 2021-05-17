<template>
  <img alt="Vue logo" src="./assets/logo.png"/>
  <router-link to="/">Home</router-link>
  <router-link to="/about">About</router-link>
  <router-view/>
  <p>{{ $store.state.test_module.count }}</p>
  <button @click="$store.commit(INCREMENT)">Click me</button>
</template>

<script>
import {INCREMENT} from "./store/mutation_types";

export default {
  name: "App",
  components: {},
  data() {
    return {
      INCREMENT
  };
}
}
;
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
