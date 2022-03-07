<template>
  <div>
    <v-text-field v-model="username" placeholder="Enter username"></v-text-field>
    <v-btn @click="get_token">Get Token</v-btn>
  </div>
</template>
<script>
import BackendApi from "../js/backend";

export default {
  name: 'TestView',
  data(){
    return {
      username: ''
    }
  },
  methods: {
    get_token(){
      BackendApi.auth.get_token(this.username).then((res) => alert('success'))
      .catch((e) => alert(`Error -> ${e}`));
    },
  }
}
</script>