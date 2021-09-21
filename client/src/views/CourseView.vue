<template>
  <GenericView
      title="Course"
      :data="courses"
      :headers="headers"
      @delete="delete_course"
  >
    <template #edit-data="edit_data">
      <CourseForm :key="Math.random()" :data="edit_data.edit_item" :update_data="Boolean(edit_data.edit_item.id)"/>
    </template>
    <template #delete-data="{delete_item}">
      <CourseForm :key="Math.random()" :data="delete_item" :update_data="true" :view_only="true" />
    </template>
  </GenericView>
</template>

<script>
import GenericView from "./GenericView";
import BackendApi from "../js/backend";
import CourseForm from "../components/forms/CourseForm";
import course_mixin from "../mixins/Course";

export default {
  name: "CourseView",
  components: {CourseForm, GenericView},
  mixins: [course_mixin],
  methods: {
    delete_course(item) {
      return BackendApi.course.delete(item.id)
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
        text: 'Code',
        align: 'start',
        value: 'code',
      },
      {text: 'Name', value: 'name'},
      {text: 'Active', value: 'active'},
      {text: 'Actions', value: 'actions', sortable: false},
    ],
  }
}

}
</script>