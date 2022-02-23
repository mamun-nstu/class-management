<template>
  <GenericView
      title="Student"
      :data="students"
      :headers="headers"
      @delete="delete_student"
  >
    <template #edit-data="edit_data">
      <StudentForm :key="edit_data.edit_item.id" :data="edit_data.edit_item" :update_data="Boolean(edit_data.edit_item.id)"/>
    </template>
    <template #delete-data="{delete_item}">
      <StudentForm :key="delete_item.id" :data="delete_item" :update_data="true" :view_only="true" />
    </template>
  </GenericView>
</template>

<script>
import GenericView from "./GenericView";
import StudentForm from "../components/forms/StudentForm";
import BackendApi from "../js/backend";
import student_mixin from "../mixins/Student";
import course_mixin from "../mixins/Course";

export default {
  name: "StudentView",
  components: {StudentForm, GenericView},
  mixins: [student_mixin, course_mixin],
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
      {text: 'Full Name', value: 'full_name'},
      {text: 'Actions', value: 'actions', sortable: false},
    ],
  }
}

}
</script>