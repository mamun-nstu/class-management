import { ADMIN_ROUTES, COMMON_ROUTES, INSTRUCTOR_ROUTES, LOGIN, STUDENT_ROUTES } from "../router";
import user_mixin from "./User";

const route_mixin = {
  mixins: [user_mixin],
  data(){
    return {
      routes: COMMON_ROUTES,
    }
  },
  beforeMount() {
    this.update_routes();
  },
  computed: {
    cur_route() {
      return this.routes.filter((route) => route.name === this.$route.name)[0];
    },
  },
  watch: {
    user(){
      this.update_routes();
    }
  },
  methods: {
    update_routes() {
      let routes_to_add = [];
      this.routes = COMMON_ROUTES;
      if (this.user.type === 'student') {
        routes_to_add = STUDENT_ROUTES;
      } else if (this.user.type === 'instructor') {
        routes_to_add = INSTRUCTOR_ROUTES;
      } else if (this.user.type === 'admin') {
        routes_to_add = ADMIN_ROUTES;
      } else {
        routes_to_add = [LOGIN];
      }
      this.routes = [...this.routes, ...routes_to_add];
    },
    goto_route(route) {
      if(this.$route.name === route.name) {
        return;
      }
      this.$router.push({ name: route.name });
    },
  }
};

export default route_mixin;
