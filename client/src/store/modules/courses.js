import {UPDATE_COURSES} from "../mutation_types";
import BackendApi from "../../js/backend";

const courses = {
  state: {
    data: []
  },
  mutations: {
    [UPDATE_COURSES](state, courses) {
      state.data = courses;
    },
  },
  actions: {
    [UPDATE_COURSES]({commit}) {
      return BackendApi.course.get_all()
          .then(response => {
            commit(UPDATE_COURSES, response.data || []);
          }).catch((err) => {
            console.log(err);
          });
    }
  },
};
export default courses;
