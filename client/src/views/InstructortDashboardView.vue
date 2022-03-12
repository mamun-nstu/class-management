<template>
  <div class="attendances">
    <v-container class="student-dashboard">
      <v-row>
        <v-col class="col-md-4 full-height">
          <v-card class="full-height">
            <v-card-title class="card-heading" style="background-color: #202C46">Instructor Details</v-card-title>
            <v-card-text>
              <div class="instructor-detail">
                <img height="100%" width="100%" v-if="instructor.image" :src="instructor.image"
                     :alt="instructor.full_name"/>
                <p class="name mt-6">{{ instructor.full_name }}</p>
                <p>Email: {{ instructor.username }}</p>
              </div>
            </v-card-text>
            <v-divider class="mb-1"></v-divider>
            <div>
              <v-btn
                width="100%"
                :style="{borderRadius: '0!important'}"
                :color="cur_tab === 'running_courses'? '#202C46' : '' "
                :class="cur_tab === 'running_courses'? 'white--text' : '' "
                @click="cur_tab='running_courses'"
              >Running Courses
              </v-btn>
              <v-btn
                width="100%"
                :style="{borderRadius: '0!important'}"
                :color="cur_tab === 'student_attendance_detail'? '#202C46' : '' "
                :class="cur_tab === 'student_attendance_detail'? 'white--text' : '' "
                
                @click="cur_tab='student_attendance_detail'"
              >Student Attendance Detail
              </v-btn>
              <v-btn
                width="100%"
                :style="{borderRadius: '0!important'}"
                :color="cur_tab === 'attendance_summary'? '#202C46' : '' "
                :class="cur_tab === 'attendance_summary'? 'white--text' : '' "
                @click="cur_tab='attendance_summary'"
              >Attendance Summary
              </v-btn>
            </div>
          </v-card>
        </v-col>
        <v-col class="col-md-8 full-height">
          <v-card class="pb-3">
            <div v-show="cur_tab === 'running_courses'">
              <v-card-title class="card-heading" style="background-color: #202C46">My Running Courses</v-card-title>
              <v-card-text class="m-0 p-0">
                <v-data-table
                  :headers="running_courses_config.headers"
                  :items="running_courses_config.value"
                >
                  <template v-slot:default>
                    <thead>
                    <tr>
                      <th class="p-3 text-center">Course</th>
                      <th class="text-center">Batch</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr
                      v-for="course_detail in course_details"
                      :key="course_detail.id"
                    >
                      <td class="text-center">{{ course_detail.course.code }}:{{ course_detail.course.name }}</td>
                      <td class="text-center">{{ course_detail.batch.name }}</td>
                    </tr>
                    </tbody>
                  </template>
                </v-data-table>
              </v-card-text>
            </div>
            <div v-show="cur_tab === 'student_attendance_detail'">
              <v-card-title class="card-heading" style="background-color: #202C46">Student Attendance details for each
                Course
              </v-card-title>
              <v-card-text>
                <div class="d-flex mt-4">
                  <span class="label pr-5 col-4">Select Course</span>
                  <v-select
                    outlined
                    dense
                    class="pt-4 pr-md-8"
                    v-model="selected_course"
                    no-data-text="No course found"
                    placeholder="Select course"
                    item-text="text"
                    item-value="value"
                    :items="unique_courses"
                  />
                </div>
                <div class="d-flex">
                  <span class="col-4 label pr-5">Select Batch</span>
                  <v-select
                    outlined
                    dense
                    class="pt-4 pr-md-8"
                    v-model="selected_batch"
                    no-data-text="No batch in this course"
                    placeholder="Select batch"
                    item-text="text"
                    item-value="value"
                    :items="batches_for_selected_course"
                  />
                </div>
                <div class="d-flex">
                  <span class="col-4 label pr-5">Select Student</span>
                  <v-select
                    outlined
                    dense
                    class="pt-4 pr-md-8"
                    v-model="selected_student"
                    no-data-text="No student in this course"
                    placeholder="Select student"
                    item-text="text"
                    item-value="value"
                    :items="students"
                  />
                </div>
                <div class="d-flex justify-start p-4">
                  <v-btn class=" white--text" @click.prevent="get_course_student_summary"
                         style="background-color: #202C46">Show Attendance
                  </v-btn>
                </div>
                <v-divider></v-divider>
                <div v-if="attendance_summary && attendance_summary.classes && attendance_summary.classes.length">
                  <v-card-title>Showing Attendance of {{ selected_student.student_id }} {{ selected_student.full_name }}
                  </v-card-title>
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
                        v-for="course_class in attendance_summary.classes"
                        :key="course_class.id"
                      >
                        <td>{{ course_class.date }}</td>
                        <td>{{ course_class.present ? 'Present' : 'Absent' }}</td>
                      </tr>
                      </tbody>
                    </template>
                  </v-simple-table>
                  <v-card class="m-2 p-3">
                    <v-card-text><b>Total Classes:</b> {{ attendance_summary.total_classes }}</v-card-text>
                    <v-card-text><b>Present:</b> {{ attendance_summary.total_present }}</v-card-text>
                    <v-card-text><b>Percentage(%):</b> {{ attendance_summary.percentage }}%</v-card-text>
                  </v-card>
                </div>
              </v-card-text>
            </div>
            <div v-show="cur_tab === 'attendance_summary'">
              <v-card-title class="card-heading white--text" style="background-color: #202C46">Attendance Summary
              </v-card-title>
              <v-card-text class="pb-3">
                <div class="d-flex mt-4">
                  <span class="label pr-5">Select Course</span>
                  <v-select
                    outlined
                    dense
                    class="pt-4 pr-md-8"
                    v-model="selected_course"
                    no-data-text="No course has been selected"
                    placeholder="Select course"
                    item-text="text"
                    item-value="value"
                    :items="unique_courses"
                  />
                </div>
                <div class="d-flex mt-4">
                  <span class="label pr-5">Select Batch</span>
                  <v-select
                    outlined
                    dense
                    class="pt-4 pr-md-8"
                    v-model="selected_batch"
                    no-data-text="No batch has been selected"
                    placeholder="Select batch"
                    item-text="text"
                    item-value="value"
                    :items="batches_for_selected_course"
                  />
                </div>
                <div class="d-flex justify-start p-4">
                  <v-btn color="#202C46" class="white--text" @click.prevent="get_attendances">View Summary</v-btn>
                </div>
                <div v-if="attendances.length">
                  <v-simple-table>
                    <template v-slot:default>
                      <thead>
                      <tr>
                        <th class="text-left">
                          Student ID
                        </th>
                        <th class="text-left">
                          Student Name
                        </th>
                        <th class="text-left">
                          Total Class
                        </th>
                        <th class="text-left">
                          Class Attended
                        </th>
                        <th class="text-left">
                          Percentage(%)
                        </th>
                      </tr>
                      </thead>
                      <tbody>
                      <tr
                        v-for="attendance in attendances"
                        :key="attendance.id"
                      >
                        <td>{{ attendance.student_id }}</td>
                        <td>{{ attendance.student_name }}</td>
                        <td>{{ attendance.total_classes }}</td>
                        <td>{{ attendance.total_present }}</td>
                        <td>{{ attendance.percentage }}%</td>
                      </tr>
                      </tbody>
                    </template>
                  </v-simple-table>
                </div>
              </v-card-text>
            </div>
          </v-card>
        </v-col>
      </v-row>
      <v-divider></v-divider>
      <v-row class="full-height">
        <v-col class="col-md-4">
        
        </v-col>
        <v-col class="col-md-8">
          <v-card>
          
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import BackendApi from "../js/backend";

export default {
  name: "InstructorDashboardView",
  data() {
    return {
      instructor: {},
      cur_tab: 'running_courses',
      unique_courses: [],
      course_details: [],
      unique_batches: [],
      attendances: [],
      attendance_summary: [],
      students: [],
      selected_course: {},
      selected_batch: {},
      selected_student: ''
    }
  },
  watch: {
    selected_course_batch_tab(new_val) {
      if(new_val && new_val.cur_tab !== 'student_attendance_detail'){
        return;
      }
      if (new_val && new_val.course && new_val.batch && new_val.batch.id) {
        console.log('NEW VAL', new_val);
        BackendApi.instructor.get_students(new_val.course.id, new_val.batch.id)
          .then(res => {
            this.students = res.data;
            this.students = this.students.map((student) => {
              return {
                'text': `${student.student_id}-${student.full_name}`,
                'value': student
              }
            })
          }).catch(console.error);
      }
    }
  },
  beforeMount() {
    return BackendApi.instructor.me()
      .then(res => {
        console.log(res);
        this.success = true;
        this.instructor = res.data;
        this.course_details = [...this.instructor.course_details] || [];
        const unique_courses = new Set();
        const unique_batches = new Set();
        for (let i = 0; i < this.course_details.length; i += 1) {
          const course = this.course_details[i].course;
          const batch = this.course_details[i].batch;
          unique_courses.add({
            text: course.name,
            value: course,
            toString: function (){
              return course.id
            }
          });
          unique_batches.add({
            text: batch.name,
            value: batch,
            toString: function (){
              return batch.id
            }
          })
        }
        this.unique_courses = [...unique_courses];
        this.unique_batches = [...unique_batches];
      }).catch(err => {
        console.error(err);
      }).finally(() => this.show_confirm = true);
  },
  computed: {
    batches_for_selected_course(){
      let course_details = this.course_details.filter(detail => detail.course.id === this.selected_course.id);
      const batches = course_details.map(detail => {
        return {
          text: detail.batch.name,
          value: detail.batch
        }
      });
      return batches;
    },
    selected_course_batch_tab(){
      return {
        course: this.selected_course,
        batch: this.selected_batch || {},
        cur_tab: this.cur_tab,
      }
    },
    running_courses_config(){
      const headers = [
        {
          text: 'Course',
          align: 'center',
          value: 'course',
        },
        {
          text: 'Batch',
          align: 'center',
          value: 'batch'
        }
      ];
      const course_details = this.course_details.map(course_detail => {
        return {
          course: `${course_detail.course.code}-${course_detail.course.name}`,
          batch: `${course_detail.batch.name}`
        }
      });
      return {
        headers,
        value: course_details
      };
    }
  },
  methods: {
    get_attendances() {
      return BackendApi.instructor.get_attendances(this.selected_course.id, this.selected_batch.id)
        .then(res => {
          this.attendances = res.data;
        }).catch((err) => {
          console.error(err);
        })
    },
    get_course_student_summary() {
      return BackendApi.instructor.get_course_student_view(
        this.selected_course.id,
        this.selected_student.id
      )
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

.instructor-detail {
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