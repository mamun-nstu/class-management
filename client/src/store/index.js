import Vue from 'vue'
import Vuex from 'vuex'
import test_module from "./modules/test";
import students from "./modules/students";
import user from "./modules/user";
import instructors from "./modules/instructors";
import courses from "./modules/courses";
import batches from "./modules/batches";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    test_module,
    students,
    courses,
    batches,
    instructors,
    user,
  }
})
