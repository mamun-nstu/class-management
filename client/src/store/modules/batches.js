import { UPDATE_BATCHES } from "../mutation_types";
import BackendApi from "../../js/backend";

const batches = {
  state: {
    data: []
  },
  mutations: {
    [UPDATE_BATCHES](state, batches) {
      state.data = batches;
    },
  },
  actions: {
    [UPDATE_BATCHES]({ commit }) {
      return BackendApi.batch.get_all()
        .then(response => {
          commit(UPDATE_BATCHES, response.data || []);
        }).catch((err) => {
          console.log(err);
        });
    }
  },
};
export default batches;
