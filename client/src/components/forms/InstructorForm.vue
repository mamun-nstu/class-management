<template>
  <FormContainer
    :url="'/api/instructors/'"
    :data="instructor"
    :key="instructor.id"
    :method="update_data ? 'put': 'post'"
  >
    <template #form>
      <div class="instructor register">
        <TextField
            label="Username/Email Address"
            v-model="instructor.username"
            :rules="{required: true}"
        />
        <TextField
            label="Name"
            v-model="instructor.full_name"
            :rules="{required: true}"
        />
        <v-select
          multiple
          v-model="instructor.courses"
          no-data-text="No course has been selected"
          :chips="true"
          :deletable-chips="true"
          item-text="text"
          item-value="value"
          :items="courses"
        />
      </div>
    </template>
  </FormContainer>
</template>

<script>
import FormContainer from "./FormContainer";
import TextField from "../elements/TextField";
import _ from 'lodash';

export default {
  name: "InstructorForm",
  components: {
    TextField,
    FormContainer,
  },
  props: {
    data: {
      type: Object,
      required: false,
      default: () => {}
    },
    update_data: {
      type: Boolean,
      required: false,
      default: false,
    },
    view_only: {
      type: Boolean,
      required: false,
      default: false
    }
  },
  mounted() {
    this.instructor = _.cloneDeep(this.data) || {};
  },
  computed: {
    courses() {
      return this.$store.state.courses.data.map((course) => {
        return {
          text: course.code,
          value: _.cloneDeep(course)
        }
      }).sort((a, b) => a.text < b.text ? -1 : 1);
    },
    selected_courses() {
      const courses = _.cloneDeep(this.student.courses);
      return courses.sort((a, b) => a.code < b.code ? -1 : 1);
    }
  },
  data: function () {
    return {
      instructor: {
      },
    }
  }
};
</script>

