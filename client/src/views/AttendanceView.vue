<template>
  <div class="attendances">
    <v-container fluid>
      <v-row>
        <v-col class="col-lg-4 col-md-4">
          <v-date-picker v-model="date"></v-date-picker>
        </v-col>
        <v-row>
          <v-col class="col-lg-3 col-md-6">
            <p>Select Batch</p>
            <v-select :items="batches" v-model="selected_batch" item-text="name" item-value="id"></v-select>
          </v-col>
          <v-col class="col-lg-3 col-md-6">
            <p>Select Course</p>
            <v-select :items="courses" v-model="selected_course" item-text="code" item-value="id"></v-select>
          </v-col>
        </v-row>

      </v-row>
      <!--      <v-btn @click="fetch_attendances" class="mb-8">Fetch</v-btn>-->
      <div class="student-attendances">
        <StudentAttendance
            v-for="attendance in attendances"
            :key="attendance.student.id"
            :attendance_data="attendance"
            @change="update_present"
        />
        <v-btn v-if="attendances.length > 0" @click="update_attendances" class="mb-8">Update</v-btn>
      </div>
    </v-container>
  </div>
</template>

<script>
import BackendApi from "../js/backend";
import moment from 'moment';
import StudentAttendance from "../components/StudentAttendance.vue";

export default {
  name: "AttendanceView",
  components: { StudentAttendance },
  data() {
    return {
      students: [],
      courses: [],
      batches: [],
      selected_course: '',
      selected_batch: '',
      attendances: [],
      date: moment().format("YYYY-MM-DD"),
      instructor: 1
    }
  },
  computed: {
    fetchDependentVars() {
      return `Course:${ this.selected_course }|Batch:${ this.selected_batch }|Date:${ this.date }`
    }
  },
  watch: {
    fetchDependentVars() {
      this.fetch_attendances();
    }
  },
  beforeMount() {
    this.fetch_courses();
    this.fetch_batches();
  },
  methods: {
    update_present(val) {
      const attendance = this.attendances.filter(data => data.student.id === val.id)[0];
      attendance.present = val.value;
      this.attendances = this.attendances.filter(() => true);
    },
    update_attendances() {
      return BackendApi.generic.put({
        url: `/api/attendances/batches/${ this.selected_batch }/courses/${ this.selected_course }/date/${ this.date }`,
        data: this.attendances
      });
    },
    fetch_courses() {
      return BackendApi.course.get_all().then(res => {
        this.courses = res.data || [];
        if (this.courses.length) {
          this.selected_course = this.courses[0].id;
        }

      })
    },
    fetch_batches() {
      return BackendApi.batch.get_all().then(res => {
        this.batches = res.data || [];
        if (this.batches.length) {
          this.selected_batch = this.batches[0].id;
        }
      })
    },
    fetch_attendances() {
      BackendApi.generic.get({
        url: `/api/attendances/batches/${ this.selected_batch }/courses/${ this.selected_course }/date/${ this.date }`
      }).then(res => {
        this.attendances = res.data;
      })
    }
  },
}
</script>

<style scoped>

</style>