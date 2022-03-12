<template>
  <GenericView
      title="Instructors"
      :data="instructors"
      :headers="headers"
      @delete="delete_instructor"
      class="mb-16"
  >
    <template #edit-data="edit_data">
      <InstructorForm :key="edit_data.edit_item.id || Math.random()" :data="edit_data.edit_item" :update_data="Boolean(edit_data.edit_item.id)"/>
    </template>
    <template #delete-data="{delete_item}">
      <InstructorForm :key="delete_item.id" :data="delete_item" :update_data="true" :view_only="true" />
    </template>
  </GenericView>
</template>

<script>
import GenericView from "./GenericView";
import BackendApi from "../js/backend";
import instructor_mixin from "../mixins/Instructor";
import course_mixin from "../mixins/Course";
import InstructorForm from "../components/forms/InstructorForm";
import batch_mixin from "../mixins/Batch";

export default {
  name: "InstructorView",
  components: { InstructorForm, GenericView},
  mixins: [instructor_mixin, course_mixin, batch_mixin],
  methods: {
    delete_instructor(item) {
      return BackendApi.instructor.delete(item.id)
          .then(res => {
            console.log(res);
            this.success = true;
          }).catch(err => {
            console.error(err);
          }).finally(() => this.show_confirm = true);
    }
  },
  data: function () {
    return {
      headers: [
        {text: 'Email Address', value: 'username'},
        {text: 'Full Name', value: 'full_name'},
        {text: 'Actions', value: 'actions', sortable: false},
      ],
    }
  }
}
</script>