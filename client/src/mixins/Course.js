import {UPDATE_COURSES} from "../store/mutation_types";

const course_mixin = {
  created() {
    return this.$store.dispatch(UPDATE_COURSES);
  },
  computed: {
    courses() {
      return this.$store.state.courses.data;
    },
  }
};

export default course_mixin;
