import {UPDATE_USER} from "../mutation_types";
import BackendApi from "../../js/backend";

const user = {
  state: {
    data: []
  },
  mutations: {
    [UPDATE_USER](state, user) {
      state.data = user;
    },
  },
  actions: {
    [UPDATE_USER]({commit}) {
      return BackendApi.auth.get_user_info()
          .then(response => {
            commit(UPDATE_USER, response.data || {});
          }).catch((err) => {
            console.log(err);
          });
    }
  },
};
export default user;
