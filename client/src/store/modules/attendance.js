import {UPDATE_STUDENTS} from "../mutation_types";
import BackendApi from "../../js/backend";

const students = {
  state: {
    data: []
  },
  mutations: {
    [UPDATE_STUDENTS](state, students) {
      state.data = students;
    },
  },
  actions: {
    [UPDATE_STUDENTS]({commit}) {
      return BackendApi.student.get_all()
          .then(response => {
            commit(UPDATE_STUDENTS, response.data || []);
          }).catch((err) => {
            console.log(err);
          });
    }
  },
};
export default students;
