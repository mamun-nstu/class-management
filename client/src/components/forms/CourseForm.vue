<template>
  <FormContainer
      :url="'/api/courses/'"
      :data="course"
      :key="data.id"
      :method="update_data ? 'put': 'post'"
      :view_only="view_only"
  >
    <template #form>
      <div class="course register">
        <TextField
            label="Code"
            v-model="course.code"
            :rules="{required: true}"
        />
        <TextField
            label="Name"
            v-model="course.name"
            :rules="{required: true}"
        />

        <v-checkbox class="white--text" dark label="Active" v-model="course.active"/>

      </div>
    </template>
  </FormContainer>
</template>

<script>
import FormContainer from "./FormContainer";
import TextField from "../elements/TextField";
import _ from 'lodash';

export default {
  name: "CourseForm",
  components: {
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
    this.course = _.cloneDeep(this.data) || {};
  },
  data: function () {
    return {
      course: {},
    }
  }
};
</script>

