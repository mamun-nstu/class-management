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
        <v-btn dark @click="add_course">Add Course</v-btn>
        <div v-for="detail in instructor.course_details" :key="`${detail.random_id}`">
          <div class="row">
            <div class="col-md-5">
              <SelectField
                dark
                v-model="detail.course"
                no-data-text="No course found"
                placeholder="Select course"
                item-text="text"
                item-value="value"
                :items="courses"
                :rules="{required: true}"
              />
            </div>
            <div class="col-md-5">
              <SelectField
                dark
                v-model="detail.batch"
                no-data-text="No batch found"
                placeholder="Select batch"
                item-text="text"
                item-value="value"
                :items="batches"
                :rules="{required: true}"
              />
            </div>
            <div class="col-md-2">
              <v-btn dark @click="delete_course(detail)" >Delete Course</v-btn>
            </div>
          </div>
        </div>
        <v-file-input
          v-model="instructor.image"
          dark
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
import SelectField from "../elements/SelectField";

export default {
  name: "InstructorForm",
  components: {
    SelectField,
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
    this.instructor.course_details = this.instructor.course_details || [];
    this.instructor.image = null;
    this.instructor.course_details = this.instructor.course_details.map(detail => {
      this.random_id += 1;
      return {
        ...detail,
        random_id: this.random_id
      }
    })
    
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
      instructor: {
        course_details: []
      },
      random_id: 0,
    }
  },
  methods: {
    add_course(){
      this.random_id += 1;
      this.instructor.course_details = [{random_id: this.random_id}, ...this.instructor.course_details];
      console.log(this.random_id, this.instructor.course_details);
    },
    delete_course(detail){
      this.instructor.course_details = this.instructor.course_details.filter(val => val.random_id !== detail.random_id);
      this.instructor.course_details = [...this.instructor.course_details];
    }
  }
};
</script>
<style lang="scss">

</style>
