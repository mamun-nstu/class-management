<template>
  <div class="attendances">
    <v-container fluid>
      <v-row>
        <v-col class="col-lg-3 col-md-6 d-flex">
          <span class="heading">Select Batch</span>
          <v-select :items="batches" v-model="selected_batch" item-text="name" item-value="id"></v-select>
        </v-col>
        <v-col class="col-lg-3 col-md-6 d-flex">
          <span class="heading">Select Course</span>
          <v-select :items="courses" v-model="selected_course" item-text="code" item-value="id"></v-select>
        </v-col>
        <v-col class="col-lg-4 col-md-6">
          <v-dialog
            v-model="dialog"
            persistent
            max-width="290"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                color="primary"
                dark
                v-bind="attrs"
                v-on="on"
              >
                <span class="heading">Choose Date</span>
              </v-btn>
            </template>
            <v-card>
              <v-date-picker @input="dialog=false" v-model="date"></v-date-picker>
            </v-card>
          </v-dialog>
        </v-col>
      </v-row>
      <!--      <v-btn @click="fetch_attendances" class="mb-8">Fetch</v-btn>-->
      <v-divider></v-divider>
      <v-row>
        <v-col class="col-md-6">
          <v-card>
            <v-card-title class="card-title">Scan your QR code</v-card-title>
            <v-card-text>
              <QRCodeReader @success="update_attendance" />
            </v-card-text>
          </v-card>
        </v-col>
        <v-col class="col-md-6">
          <v-card :style="{height: '100%'}">
            <v-card-title class="card-title" >Scanned Information</v-card-title>
            <v-card-text>
              <v-row class="student-info">
                <v-col class="col-5">Course Title</v-col>
                <v-col class="col-7">{{selected_course}}</v-col>
                <v-divider></v-divider>
                <v-col class="col-5">Student ID</v-col>
                <v-col class="col-7">{{qr_result.student_id}}</v-col>
                <v-col class="col-5">Student Name</v-col>
                <v-col class="col-7">{{qr_result.full_name}}</v-col>
                <v-col class="col-5">Email</v-col>
                <v-col class="col-7">{{qr_result.username}}</v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
      <v-divider></v-divider>
      <div class="student-attendances">
        <div class="heading mb-5 mt-5">Showing attendance of {{date}}</div>
        <StudentAttendance
            v-for="attendance in attendances"
            :key="`${attendance.student.id}|${attendance.present}`"
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
import QRCodeReader from "../components/QRCodeReader";

export default {
  name: "AttendanceView",
  components: { QRCodeReader, StudentAttendance },
  data() {
    return {
      qr_result: {},
      dialog: false,
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
    update_attendance(val){
      let res = {};
      try {
        res = JSON.parse(val);
      } catch (e) {
      
      }
      if(!res.id) {
        alert(`Not valid QR code. Decoded val: ${val}`);
        return;
      }
      this.qr_result = res;
      this.update_present(this.qr_result);
    },
    update_present(val) {
      const attendance = this.attendances.filter(data => data.student.id === val.id)[0];
      attendance.present = val.value || true;
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

<style scoped lang="scss">
.heading {
  font-weight: 700;
  padding-right: 5px;
}
.card-title {
  background-color: #1976D2;
  color: white;
}

.student-info {
  font-size: 16px;
  font-weight: 700;
}
</style>