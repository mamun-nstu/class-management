<template>
  <FormContainer
    :url="'/api/instructors/'"
    :data="instructor"
    :key="instructor.id"
    :method="update_data ? 'put': 'post'"
  >
    <template #form>
      <div class="instructor register">
        <div class="d-flex justify-center mb-6">
          <img :style="{maxHeight: '250px', maxWidth: '250px'}" height="100%" width="100%" v-if="data.image"
               :src="data.image" :alt="data.full_name"/>
        </div>
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
          no-data-text="No course found"
          placeholder="Select courses"
          :chips="true"
          :deletable-chips="true"
          item-text="text"
          item-value="value"
          :items="courses"
        />
        <v-file-input
          v-model="instructor.image"
          accept="image/png, image/jpeg, image/bmp"
          label="Upload image"
          show-size
          outlined
          dense
          prepend-icon=""
      ></v-file-input>
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
    this.instructor.image = null;
    
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

