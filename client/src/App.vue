<template>
  <v-app>
    <v-main>
      <v-card>
        <v-navigation-drawer
          class="white--text"
          color="#202C46"
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
            <v-list-item
              @click.prevent="goto_route(route)"
              :key="route.name"
              v-for="route in routes"
              link
              :disabled="$route.name === route.name"
              :class="[$route.name === route.name? 'active-route': '']"
              :dark="true"
            >
              <v-list-item-icon>
                <v-icon >mdi-{{ route.icon }}</v-icon>
              </v-list-item-icon>
              <v-list-item-title class="white--text"> {{ route.title }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-navigation-drawer>
      </v-card>
      <Header/>
      <div class="main-app">
        <router-view class="pt-10 mt-10"/>
      </div>
      <Footer/>
    </v-main>
  </v-app>
</template>

<script>
import { INCREMENT, UPDATE_USER } from "./store/mutation_types";
import Footer from "./components/Footer";
import BackendApi from "./js/backend";
import Header from "./components/Header";
import user_mixin from "./mixins/User";
import route_mixin from "./mixins/Route";

export default {
  name: "App",
  components: { Header, Footer },
  mixins: [user_mixin, route_mixin],
  async beforeMount() {
    await this.fetch_user();
  },
  methods: {
    async fetch_user() {
      await this.$store.dispatch(UPDATE_USER);
    },
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
  margin: auto;
  align-content: center;
}
.main-app {
  max-width: 1200px;
  width: 100%;
  margin: auto;
  min-height: 400px;
}
.active-route {
  background-color: darkred;
}
</style>