import {UPDATE_STUDENTS} from "../store/mutation_types";

const student_mixin = {
  created() {
    return this.$store.dispatch(UPDATE_STUDENTS);
  },
  computed: {
    students() {
      return this.$store.state.students.data;
    },
  }
};

export default student_mixin;
