<template>
  <FormContainer :url="'/api/students/'" :data="student" :key="student.student_id">
    <template #form>
      <div class="student register">
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
            label="First Name"
            v-model="student.first_name"
            :rules="{required: true}"
        />
        <TextField
            label="Last Name"
            v-model="student.last_name"
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

export default {
  name: "StudentForm",
  components: {
    TextField,
    FormContainer,
  },
  props: {
    student_data: {
      type: Object,
      required: false,
      default: () => {}
    },
    view_only: {
      type: Boolean,
      required: false,
      default: false
    }
  },
  mounted() {
    this.student = _.cloneDeep(this.student_data) || {};
  },
  data: function () {
    return {
      student: {
      },
    }
  }
};
</script>

