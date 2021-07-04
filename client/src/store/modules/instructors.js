import {UPDATE_INSTRUCTORS} from "../mutation_types";
import BackendApi from "../../js/backend";

const instructors = {
  state: {
    data: []
  },
  mutations: {
    [UPDATE_INSTRUCTORS](state, instructors) {
      state.data = instructors;
    },
  },
  actions: {
    [UPDATE_INSTRUCTORS]({commit}) {
      return BackendApi.instructor.get_all()
          .then(response => {
            commit(UPDATE_INSTRUCTORS, response.data || []);
          }).catch((err) => {
            console.log(err);
          });
    }
  },
};
export default instructors;
