import Vue from 'vue'
import Vuex from 'vuex'
import test_module from "./modules/test";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    test_module
  }
})
