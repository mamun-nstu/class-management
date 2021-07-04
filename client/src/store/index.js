import Vue from 'vue'
import Vuex from 'vuex'
import test_module from "./modules/test";
import students from "./modules/students";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    test_module,
    students
  }
})
