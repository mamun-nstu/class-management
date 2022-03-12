<template>
  <div class="login">
     <v-alert
       v-model="show_alert"
       dense
       outlined
       type="error"
     >
       <div v-html="error"></div>
    </v-alert>
    <v-card>
      <v-card-title class="text-center mx-auto">
        Login with your NSTU email
      </v-card-title>
      <v-card-text>
        <div class="g-signin2 text-center" data-onsuccess="onSignIn"></div>
      </v-card-text>
    </v-card>
    
  </div>
</template>
<script>
import BackendApi from "../js/backend";

export default {
  name: 'LoginView',
  data(){
    return {
      show_alert: false,
      error: '',
      username: '',
    }
  },
  beforeMount(){
    const app = this;
    window.onSignIn = function (googleUser) {
      var profile = googleUser.getBasicProfile();
      console.log('ID: ' + profile.getId());
      console.log('Name: ' + profile.getName());
      console.log('Image URL: ' + profile.getImageUrl());
      console.log('Email: ' + profile.getEmail());
      const auth_resp = googleUser.getAuthResponse();
      app.username = profile.getEmail();
      const token = auth_resp.id_token;
      console.log('Token: ', token, 'auth_response', auth_resp);
      return app.validate_user(token);
    }
    const script = document.createElement('script');
    script.src = "https://apis.google.com/js/platform.js";
    script.async = true;
    script.defer = true;
    document.body.appendChild(script);
  },
  methods: {
    async validate_user(token){
      try {
        let res = await BackendApi.generic.post({
          url: '/api/session',
          data: {
            token,
          }
        });
        res = res.data;
        console.log(res);
        window.location.href = '/';
      } catch (e) {
        console.error(e);
        const code = e.response.status;
        this.show_alert = true;
        const app = this;
        if(code === 404) {
          this.error = `User not found with <b>${this.username}</b>. Click the button again to sign in with a different user.`;
        } else {
          this.error = `Unknown error occurred. Error code: ${code}. Reason: ${JSON.stringify(e.message)}`;
        }
      }
    }
  }
}
</script>
<style lang="scss" scoped>
.login{
  max-width: 600px;
  margin: auto;
  .g-signin2 {
    margin: auto;
    width: 120px;
  }
}
</style>