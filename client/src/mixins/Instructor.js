import {UPDATE_INSTRUCTORS} from "../store/mutation_types";

const instructor_mixin = {
  created() {
    return this.$store.dispatch(UPDATE_INSTRUCTORS);
  },
  computed: {
    instructors() {
      return this.$store.state.instructors.data;
    },
  }
};

export default instructor_mixin;
