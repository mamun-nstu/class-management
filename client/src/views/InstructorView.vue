<template>
  <GenericView
    title="Student"
    :data="students"
    component_name="StudentForm"
    :headers="headers"
  >
    <template #edit-data="edit_data">
      <StudentForm :data="edit_data.edit_item" />
    </template>
  </GenericView>
</template>

<script>
import {UPDATE_STUDENTS} from "../store/mutation_types";
import GenericView from "./GenericView";
import StudentForm from "../components/forms/StudentForm";

export default {
  name: "InstructorView",
  components: {StudentForm, GenericView},
  created() {
    this.$store.dispatch(UPDATE_STUDENTS);
  },
  computed: {
    students() {
      return this.$store.state.students.data;
    }
  },
  data: function () {
    return {
      headers: [
        {
          text: 'Student ID',
          align: 'start',
          value: 'student_id',
        },
        {text: 'Email Address', value: 'username'},
        {text: 'First Name', value: 'first_name'},
        {text: 'Last Name', value: 'last_name'},
        {text: 'Actions', value: 'actions', sortable: false},
      ],
    }
  }

}
</script>