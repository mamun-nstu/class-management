<template>
  <v-app>
    <Header/>
    <v-main>
      <v-card>
        <v-navigation-drawer class="white--text" color="#202C46"
          permanent
          expand-on-hover
          :app="true"
          :bottom="true"
        >
          <v-list>
            <v-list-item class="px-2">
              <v-list-item-avatar>
                <img v-if="user.image" :src="user.image"/>
              </v-list-item-avatar>
            </v-list-item>

            <v-list-item link>
              <v-list-item-content>
                <v-list-item-title class="text-h6 white--text">
                  {{ user.full_name }}
                </v-list-item-title>
                <v-list-item-subtitle class="white--text">{{ user.username }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-list>

          <v-divider></v-divider>

          <v-list
            nav
            dense
            class="white--text"
          >
            <v-list-item @click.prevent="goto_route(route)" :key="route.name" v-for="route in routes" link>
              <v-list-item-icon>
                <v-icon class="white--text">mdi-{{ route.icon }}</v-icon>
              </v-list-item-icon>
              <v-list-item-title class="white--text"> {{ route.title }}</v-list-item-title>
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
import { INCREMENT, UPDATE_USER } from "./store/mutation_types";
import Footer from "./components/Footer";
import BackendApi from "./js/backend";
import { ADMIN_ROUTES, COMMON_ROUTES, INSTRUCTOR_ROUTES, STUDENT_ROUTES } from "./router";
import Header from "./components/Header";
import user_mixin from "./mixins/User";

export default {
  name: "App",
  components: { Header, Footer },
  mixins: [user_mixin],
  async beforeMount() {
    await this.fetch_user();
    await this.update_routes();
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
    },
  },
  methods: {
    goto_route(route) {
      this.$router.push({ name: route.name });
    },
    async fetch_user() {
      await this.$store.dispatch(UPDATE_USER);
    },
    update_routes() {
      let routes_to_add = [];
      if (this.user.type === 'student') {
        routes_to_add = STUDENT_ROUTES;
      } else if (this.user.type === 'instructor') {
        routes_to_add = INSTRUCTOR_ROUTES;
      } else if (this.user.type === 'admin') {
        routes_to_add = ADMIN_ROUTES;
      }
      this.routes = [...this.routes, ...routes_to_add];
    }
  },
  data() {
    return {
      INCREMENT,
      routes: COMMON_ROUTES,
    };
  },
};
</script>
<style lang="scss">
body {
  background-color: #FFFFFF !important;
}

#app {
  //max-width: 1410px;
  margin: auto;
  align-content: center;
}
</style>