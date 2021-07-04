<template>
  <GenericView
      title="Student"
      :data="students"
      component_name="StudentForm"
      :headers="headers"
      @delete="delete_student"
  >
    <template #edit-data="edit_data">
      <StudentForm :data="edit_data.edit_item" :update_data="true"/>
    </template>
    <template #delete-data="{delete_item}">
      <StudentForm :data="delete_item" :update_data="true" :view_only="true" />
    </template>
  </GenericView>
</template>

<script>
import {UPDATE_STUDENTS} from "../store/mutation_types";
import GenericView from "./GenericView";
import StudentForm from "../components/forms/StudentForm";
import BackendApi from "../js/backend";

export default {
  name: "StudentView",
  components: {StudentForm, GenericView},
  created() {
    this.$store.dispatch(UPDATE_STUDENTS);
  },
  computed: {
    students() {
      return this.$store.state.students.data;
    }
  },
  methods: {
    delete_student(item) {
      return BackendApi.student.delete(item.id)
          .then(res => {
            console.log(res);
            this.success = true;
          }).catch(err => {
            console.error(err);
          }).finally(() => this.show_confirm = true);
  }
}
,
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