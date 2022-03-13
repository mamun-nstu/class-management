<template>
  <div class="home">

      <v-layout row wrap class="">
        <v-flex xs12 md6 class="">
          <v-img class="white--text text-center text-capitalize ml-4" src="@/assets/bg1.jpg" height="450" style="border-radius: 12px;">
            <div class="mt-16">
              <p class="text-h4">
                <span>Welcome</span> <br>to <br><span>ICE Attendance Management System</span>
              </p>
              <p class="text-h5 mt-12 text-decoration-underline">
                Here You can :
              </p>

              <v-container style="margin-top: 40px; background: #E7F5F7FF" >
                 <VueTyper class="white--text text-h5" :text='["Take attendance with QR code","See the attenance Summary","See the assigned courses","Calculate attendance percentage automatically"]' />
              </v-container>
            </div>
          </v-img>
        </v-flex>

        <v-flex xs12 md6 class="">
          <v-carousel show-arrows-on-hover  cycle interval="3000" class="text-center ml-2 " height="450" style="width: 720px; border-radius: 20px; align-content: center;">
            <v-carousel-item
              v-for="(item,i) in items"
              :key="i"
              :src="item.src"
              reverse-transition="fade-transition"
              transition="fade-transition"
            >
            </v-carousel-item>
          </v-carousel>
        </v-flex>
      </v-layout>

    <div class=" middle mt-16" style="height: 700px;">
      <v-row>
        <v-col class=" col-md-3 full-height mt-11 mr-2 ml-13" style="background: #E7F5F7FF; border-radius:5px; height: 550px;">
          <p class=" text-decoration-underline text-h5 text-bold text-center"><b>All Faculty Members:</b></p>
          <v-card shaped v-scroll.self="onScroll" class="text overflow-y-auto" color="#E7F5F7FF" height="550" max-height="550">
            <v-card-text>
              <div class="text-uppercase mt-6" style="font-size: 17px;">
                 <b>
                   <ul>
                    <li v-for="instructor in data.instructors || []" :key="`${Math.random()}-${instructor.full_name}`">
                      <p>{{instructor.full_name}}</p>
                    </li>
                   </ul>
                 </b>
              </div>
            </v-card-text>
          </v-card>
        </v-col>

        <v-col class="col-md-4 full-height mt-11 mr-2" style="background: #ECF7EDFF; border-radius:5px; height: 550px;">
          <p class=" text-decoration-underline text-h5 text-bold text-center"><b>All Courses:</b></p>
          <v-card shaped v-scroll.self="onScroll" class="text overflow-y-auto" color="#ECF7EDFF" height="550" max-height="550">
          <v-card-text>
              <div class="text-uppercase mt-6" style="font-size: 15px;">
                <b>
                  <ul>
                    <li v-for="course in data.courses || []" :key="`${Math.random()}-${course.code}`">
                      <p>{{course.code}}: {{course.name}}</p>
                    </li>
                  </ul>
                </b>
              </div>
            </v-card-text>
          </v-card>
        </v-col>

        <v-col class="col-md-4 full-height mt-11" style="background: #E7F5F7FF; border-radius:5px; height: 550px;">
          <p class=" text-decoration-underline text-h5 text-bold text-center"><b>Notice Board:</b></p>
          <v-card shaped v-scroll.self="onScroll" color="#E7F5F7FF" class="text overflow-y-auto" height="550" max-height="550">
            <v-card-text>
              <p><a class="text-decoration-none " href="#">NSTU ICE Festival. Seminar on future IT technology.</a></p>
              <p><a class="text-decoration-none " href="#">NSTU ICE Fest programming contest. Registration going on.</a></p>
              <p><a class="text-decoration-none " href="#">Admission circular for ICE department</a></p>
              <p><a class="text-decoration-none " href="#">About 2021-22 session 1st year admission related Notice</a></p>
              <p><a class="text-decoration-none " href="#">About International women's day 2022 celebration in NSTU</a></p>
              <p><a class="text-decoration-none " href="#">Historical 7th March celebration in NSTU</a></p>
              <p><a class="text-decoration-none " href="#">International PI Day celebration Contest by ICE department.</a></p>
              <p><a class="text-decoration-none " href="#">NSTU ICE Festival. Seminar on future IT technology.</a></p>
              <p><a class="text-decoration-none " href="#">NSTU ICE Fest programming contest. Registration going on.</a></p>
              <p><a class="text-decoration-none " href="#">Admission circular for ICE department</a></p>
              <p><a class="text-decoration-none " href="#">About 2021-22 session 1st year admission related Notice</a></p>
              <p><a class="text-decoration-none " href="#">About International women's day 2022 celebration in NSTU</a></p>
              <p><a class="text-decoration-none " href="#">Historical 7th March celebration in NSTU</a></p>
              <p><a class="text-decoration-none " href="#">International PI Day celebration Contest by ICE department.</a></p>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </div>

    <div class=" mt-16" style="height: 350px; background: #202C46;">
      <v-row  class="" style="margin-left: 200px;">
        <v-col class="col-md-4 full-height mt-11">
          <p >
            <span class="white--text text-h5 ml-13" >Total</span>  <br> <span class="white--text text-h5" >Faculty Member</span>
          </p>
          <v-avatar class="text-h3" size="150" color="white" style="opacity: .8">
            {{ data.total_instructors }}
          </v-avatar>
        </v-col>

        <v-col class="col-md-4 full-height mt-11">
          <p>
            <span class="white--text text-h5 ml-10">Total</span> <br> <span
            class="white--text text-h5 ml-6">Students</span>
          </p>
          <v-avatar class="text-h3" size="150" color="white" style="opacity: .8">
            {{ data.total_students }}
          </v-avatar>
        </v-col>

        <v-col class="col-md-4 full-height mt-11">
          <p>
            <span class="white--text text-h5 ml-10">Total</span> <br> <span
            class="white--text text-h5 ml-6">Courses</span>
          </p>
          <v-avatar class="text-h3" size="150" color="white" style="opacity: .8">
            {{ data.total_courses }}
          </v-avatar>
        </v-col>

      </v-row>

    </div>
    <div class=" " style="height: 600px; background: #F0E9FBFF;">
      <p class="pa-10 text-center text-decoration-underline text-h4 text-bold"><b>Why this site </b></p>
      <div class=" text-center justify-text">
        <p class="whythis" style=" text-align: justify">
          An attendance System is an information system that monitors the presence of someone in an organization. Student Attendance
          Management System is used only for educational institutions. Nowadays managing the attendance of people may be a difficult task for many of the big organizations or institutions where there
          are hundreds of people. Maintaining their attendance record is a vital thing about people management. When considering the
          educational institute, this is even more difficult because of having thousands of students. Taking the attendance of students of
          various academic sessions manually on paper is time-consuming and we need to deal with a lot of paperwork here.
          In this project, I will develop a student attendance management system for the Information & Communication Engineering (ICE) department of Noakhali Science & Technology University. It’s a web-based application software developed for taking daily attendance of a particular student in a particular class, monitoring all the students, calculating attendance summaries, and making periodical attendance reports. By using this application our teachers can easily manage student attendance and student can also view their attendance reports at any time from anywhere.
          In an educational institute maintaining the records of students is a major task in the academic period so if it can be done only by using some sort
          of application or software then it will be so time-saving. We also don’t need to deal with a lot of paperwork, storing them and
          managing them for attendance record analysis. For this reason, I have proposed an efficient system in this project proposal to solve
          the problem of manual attendance. This system takes attendance electronically with the help of a web-based application by using a
          QR code which stands for “Quick Response” checking mechanism, and all the records are stored in a server for subsequent
          operations. This software "Student Attendance Management System" allows us to leave the manual process of attendance and bring it
          online for both teachers and students so that the attendance records can be managed and accessed easily from anywhere at any time.
          This online attendance system also employs an automated system to calculate the attendance of students and give an attendance summary.The system will help course
          instructors to manage attendance very efficiently.
        </p>
      </div>
    </div>

  </div>
</template>

<script>
import Backend from "../js/backend";
import { VueTyper } from 'vue-typer'
import slider1 from '@/assets/slider1.jpg';
import slider2 from '@/assets/slider2.jpg';
import slider3 from '@/assets/slider3.jpg';
import slider4 from '@/assets/slider4.jpg';
import slider5 from '@/assets/slider5.jpg';
import slider6 from '@/assets/slider6.jpg';
export default {
  name: "Home",
  components: {
    VueTyper,
  },
  async created() {
    try {
      this.data = await Backend.generic.get({
        url: '/api/app-info'
      })
      this.data = this.data.data;
    } catch (e) {
      console.error(e);
    }
    this.data = this.data || {};
  },
  data() {
    return {
      data: {},
      onScroll: false,
      items: [
        {
          src: slider1,
        },
        {
          src: slider2,
        },
        {
          src: slider3,
        },
        {
          src: slider4,
        },
        {
          src: slider5,
        },
        {
          src: slider6,
        },
      ],
    }
  },
};
</script>

<style scoped lang="scss">
.middle, .whythis{
  max-width: 1200px;
  margin: auto;
}

</style>
