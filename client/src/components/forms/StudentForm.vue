<template>
  <FormContainer
      :url="'/api/students/'"
      :data="student"
      :method="update_data ? 'put': 'post'"
      :view_only="view_only"
  >
    <template #form>
      <div class="student register">
        <div class="d-flex justify-center mb-6">
          <img :style="{maxHeight: '250px', maxWidth: '250px'}" height="100%" width="100%" v-if="data.image"
               :src="data.image" :alt="data.full_name"/>
        </div>
        <TextField
            label="Student ID"
            v-model="student.student_id"
            :rules="{required: true}"
        />
        <TextField
            label="Username/Email Address"
            v-model="student.username"
            :rules="{required: true}"
        />
        <TextField
            label="Full Name"
            v-model="student.full_name"
            :rules="{required: true}"
        />
        <v-file-input
          v-model="student.image"
          accept="image/png, image/jpeg, image/bmp"
          label="Upload image"
          show-size
          outlined
          dense
          dark
          prepend-icon=""
      ></v-file-input>
        <v-select
          dark
          multiple
          label="Courses"
          v-model="student.courses"
          no-data-text="No course found"
          placeholder="Select courses"
          :chips="true"
          :deletable-chips="true"
          item-text="text"
          item-value="value"
          :items="courses"
        />
        <SelectField
            dark
            label="Batch"
            v-model="student.batch"
            no-data-text="No batch found"
            placeholder="Select batch"
            item-text="text"
            item-value="value"
            :items="batches"
            :rules="{required: true}"
        />
      </div>
    </template>
  </FormContainer>
</template>

<script>
import FormContainer from "./FormContainer";
import TextField from "../elements/TextField";
import _ from 'lodash';
import SelectField from "../elements/SelectField";

export default {
  name: "StudentForm",
  components: {
    SelectField,
    TextField,
    FormContainer,
  },
  props: {
    data: {
      type: Object,
      required: false,
      default: () => {
      }
    },
    view_only: {
      type: Boolean,
      required: false,
      default: false
    },
    // whether data should be created or updated
    update_data: {
      type: Boolean,
      required: false,
      default: false,
    }
  },
  mounted() {
    this.student = _.cloneDeep(this.data) || {courses: []};
    this.student.courses = this.student.courses || [];
    this.student.image = null;
    console.log('Mounted', this.student.courses);
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
    },
    batches() {
      return this.$store.state.batches.data.map((batch) => {
        return {
          text: batch.name,
          value: _.cloneDeep(batch)
        }
      }).sort((a, b) => a.text < b.text ? -1 : 1);
    },
  },
  data: function () {
    return {
      student: {
        courses: []
      },
    }
  }
};
</script>

