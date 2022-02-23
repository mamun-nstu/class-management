<template>
  <v-app>
    <Header/>
<!--    <v-banner dense flat>{{ cur_route.title }}</v-banner>-->
    <v-main>
      <v-card>
        <v-navigation-drawer
          permanent
          expand-on-hover
          :app="true"
          :bottom="true"
          class="indigo lighten-4"
        >
          <v-list class="align-center">
            <v-list-item class="px-2">
              <v-list-item-avatar class="text-xs-ce">
                <v-img src="@/assets/walle.jpg" style="align-center"></v-img>
              </v-list-item-avatar>
            </v-list-item>

            <v-list-item link>
              <v-list-item-content>
                <v-list-item-title class="text-h6">
                  Student's Name
                </v-list-item-title>
                <v-list-item-subtitle>Student's ID</v-list-item-subtitle>

              </v-list-item-content>
            </v-list-item>
          </v-list>

          <v-divider></v-divider>

          <v-list
            nav
            dense
          >
            <v-list-item @click.prevent="goto_route(route)" :key="route.name" v-for="route in routes" link>
              <v-list-item-icon>
                <v-icon>mdi-{{ route.icon }}</v-icon>
              </v-list-item-icon>
              <v-list-item-title> {{ route.title }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-navigation-drawer>
      </v-card>
      <router-view class="pt-10 mt-10"/>
      <Footer/>
    </v-main>
  </v-app>
</template>

<script>
import { INCREMENT } from "./store/mutation_types";
import Footer from "./components/Footer";
import BackendApi from "./js/backend";
import { routes } from "./router";
import Header from "./components/Header";

export default {
  name: "App",
  components: {Header, Footer },
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
  computed: {
    cur_route() {
      return routes.filter((route) => route.name === this.$route.name)[0];
    }
  },
  methods: {
    goto_route(route) {
      this.$router.push({ name: route.name });
    }
  },
  data() {
    return {
      INCREMENT,
      routes,
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