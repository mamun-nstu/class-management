import { UPDATE_STUDENTS } from "../store/mutation_types";

const student_mixin = {
  created() {
    return this.$store.dispatch(UPDATE_STUDENTS);
  },
  computed: {
    students() {
      return this.$store.state.students.data;
    },
    students_list_view() {
      return this.students.map(student => {
        return {
          ...student,
          batch_name: student.batch? student.batch.name: ''
        }


      })
    }
  }
};

export default student_mixin;
