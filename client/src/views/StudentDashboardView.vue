<template>
  <div class="attendances">
    <v-container class="student-dashboard mb-10">
      <v-row>
        <v-col class="col-md-4 full-height">
          <v-card class="full-height">
            <v-card-title class="card-heading" style="background-color: #202C46">Student Details</v-card-title>
            <v-card-text>
              <div class="student-detail">
                <img class="mb-8" height="100%" width="100%" v-if="student.image" :src="student.image" :alt="student.full_name" />
                <p class="name">{{ student.full_name }}</p>
                <p>Student ID: {{ student.student_id }}</p>
                <p>Email: {{ student.username }}</p>
              </div>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col class="col-md-8 full-height">
          <v-card class="ml-5">
            <v-card-title class="card-heading" style="background-color: #202C46">Attendance Summary</v-card-title>
            <v-card-text class="m-0 p-0">
              <StudentAttendanceSummary :attendances="attendance_summary"/>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
      <v-divider class="mt-6 mb-6"></v-divider>
      <v-row class="full-height">
        <v-col class="col-md-4">
          <v-card>
            <v-card-title class="card-heading rounded" style="background-color: #202C46">Secret QR Code</v-card-title>
            <v-card-text>
              <QRCodeGenerator id="qrcode" :size="250" class="pt-5" :value="JSON.stringify(generalized_student)"/>
              <div class="d-flex justify-center" >
                <a download="qrcode.png" href="" @click="download_image" class="text-button white--text ma-4 rounded text-decoration-none" style="background-color: #202C46; text-align: center; padding-top: 3px; width: 160px; height: 40px;">Download</a>
              </div>
            </v-card-text>
          </v-card>

        </v-col>
        <v-col class="col-md-8">
          <v-card class="ml-5">
            <v-card-title class="card-heading" style="background-color: #202C46">Attendance Details</v-card-title>
            <v-card-text class="pb-3">
              <div class="d-flex mt-4">
                <span class="label pr-5">Select Course</span>
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
              </div>
              <div class="d-flex justify-center p-4" >
                <v-btn class="white--text" @click.prevent="get_attendances"  style="background-color: #202C46">Get Attendances</v-btn>
              </div>
              <div v-if="attendances.length">
                <v-simple-table>
                  <template v-slot:default>
                    <thead>
                    <tr>
                      <th class="text-left">
                        Date
                      </th>
                      <th class="text-left">
                        Present Status
                      </th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr
                      v-for="attendance in attendances"
                      :key="attendance.id"
                    >
                      <td>{{ attendance.date }}</td>
                      <td>{{ attendance.present ? 'Present' : 'Absent' }}</td>
                    </tr>
                    </tbody>
                  </template>
                </v-simple-table>
                <v-card class="pt-3 pb-3 m-2 " style="background-color: #202C46; opacity: .8">
                  <v-card-text class="white--text"><b>Total Classes:</b> {{ attendances.length }}</v-card-text>
                  <v-card-text class="white--text"><b>Present counts:</b> {{ presents }}</v-card-text>
                  <v-card-text class="white--text"><b>Present Percentage:</b> {{ attendance_percentange }}%</v-card-text>
                </v-card>
              
              </div>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>


import BackendApi from "../js/backend";
import QRCodeGenerator from "../components/QRCodeGenerator";
import StudentAttendanceSummary from "../components/StudentAttendanceSummary";

export default {
  name: "StudentDashboardView",
  components: { StudentAttendanceSummary, QRCodeGenerator },
  data() {
    return {
      student: {},
      courses: [],
      attendances: [],
      attendance_summary: [],
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
      const val =  {
        id: this.student.id,
        student_id: this.student.student_id,
        username: this.student.username,
        full_name: this.student.full_name
      };
      console.log(JSON.stringify(val));
      return val;
    },
    attendance_percentange() {
      if (this.attendances.length === 0) return 0;
      return (this.presents / this.attendances.length * 100).toFixed(2);
    }
  },
  beforeMount() {
    return BackendApi.student.me()
      .then(res => {
        console.log(res);
        this.success = true;
        this.student = res.data;
        this.get_attendance_summary();
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
    download_image(event) {
      const el = event.srcElement;
      console.log(el);
      const canvas = document.querySelector('#qrcode > canvas');
      const img = canvas.toDataURL("image/png");
      el.href = img;
    },
    get_attendances() {
      return BackendApi.student.get_attendances(this.selected_course.id)
        .then(res => {
          this.attendances = res.data;
        }).catch((err) => {
          console.error(err);
        })
    },
    get_attendance_summary() {
      return BackendApi.student.get_attendance_summary()
        .then(res => {
          console.log(res);
          this.attendance_summary = res.data;
        }).catch((err) => {
          console.error(err);
        })
    }
  },
}
</script>

<style scoped lang="scss">

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

.student-detail {
  padding: 15px;
  margin: auto;
  font-weight: 400;
  text-align: center;
  
  .name {
    font-size: 18px;
    font-weight: 600;
  }
  
}

.label {
  font-size: 16px;
  font-weight: 700;
  padding-top: 25px;
}

.text-button {
  font-size: 18px !important;
}

</style>