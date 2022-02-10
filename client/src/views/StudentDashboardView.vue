<template>
  <div class="attendances">
    <v-container class="student-dashboard">
      <v-card-title>Student ID</v-card-title>
      <v-card-text>{{ student.student_id }}</v-card-text>
      <v-card-title>Username/Email Address</v-card-title>
      <v-card-text>{{ student.username }}</v-card-text>
      <v-card-title>Full Name</v-card-title>
      <v-card-text>{{ student.full_name }}</v-card-text>
      <v-card-title>Secret QR</v-card-title>
      <QRCodeGenerator class="pl-4 pt-8 pb-8" :value="JSON.stringify(generalized_student)" :margin="10" />
      <v-card-title class="pt-4">Select a course to view attendance dashboard</v-card-title>
      <v-select
          outlined
          dense
          class="col-3 pt-4"
          v-model="selected_course"
          no-data-text="No course has been selected"
          item-text="text"
          item-value="value"
          :items="courses"
      />
      <v-btn @click.prevent="get_attendances">Get Attendances</v-btn>
      <div v-if="attendances.length">
        <v-card-title>{{ selected_course.name }}</v-card-title>
        <v-list>
          <v-list-item :key="attendance.id" v-for="attendance in attendances">
            {{ attendance.date }} -> {{ attendance.present ? 'present' : 'absent' }}
          </v-list-item>
        </v-list>
        <v-card-title>Total Classes: {{ attendances.length }}</v-card-title>
        <v-card-title>Present counts: {{ presents }}</v-card-title>
        <v-card-title>Present Percentage: {{ attendance_percentange }}%</v-card-title>
      </div>
    </v-container>
  </div>
</template>

<script>


import BackendApi from "../js/backend";
import QRCodeGenerator from "../components/QRCodeGenerator";

export default {
  name: "StudentDashboardView",
  components: { QRCodeGenerator },
  data() {
    return {
      student: {},
      courses: [],
      attendances: [],
      selected_course: '',
    }
  },
  computed: {
    presents() {
      return this.attendances.reduce((prev, cur) => {
        console.log(prev, cur);
        return prev + (cur.present === true ? 1 : 0);
      }, 0);
    },
    generalized_student() {
      return {
        id: this.student.id,
        student_id: this.student.student_id,
        username: this.student.username,
        full_name: this.student.full_name
      }
    },
    attendance_percentange() {
      if (this.attendances.length === 0) return 0;
      return (this.presents/this.attendances.length * 100).toFixed(2);
    }
  },
  beforeMount() {
    return BackendApi.student.get(1)
        .then(res => {
          console.log(res);
          this.success = true;
          this.student = res.data;
          this.courses = this.student.courses;
          this.courses = this.courses.map((course) => {
            return {
              text: course.name,
              value: course
            }
          });
          this.selected_course = this.student.courses.length ? this.student.courses[0] : {};
        }).catch(err => {
          console.error(err);
        }).finally(() => this.show_confirm = true);
  },
  methods: {
    get_attendances() {
      console.log('Here attendances');
      return BackendApi.student.get_attendances(this.student.id, this.selected_course.id)
          .then(res => {
            this.attendances = res.data;
          }).catch((err) => {
            console.error(err);
          })
    }
  },
}
</script>

<style scoped>

.v-card__title {
  font-size: 1.10rem;
  font-weight: 500;
  letter-spacing: 0.0125em;
  line-height: 1.2rem;
}

.v-card__text {
  padding-top: 0;
  padding-bottom: 0;
}
</style>