import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

export const routes = [
  {
    path: '/',
    name: 'Home',
    title: 'Home',
    component: Home,
    icon: 'home'
  },
  {
    path: '/about',
    title: 'About',
    name: 'About',
    icon: 'help-circle',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/students',
    title: 'Students',
    name: 'Student',
    icon: 'account',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "student_form" */ '../views/StudentView.vue')
  },
  {
    path: '/courses',
    title: 'Courses',
    name: 'Course',
    icon: 'text-subject',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "student_form" */ '../views/CourseView.vue')
  },
  {
    path: '/attendances',
    title: 'Attendances',
    name: 'Attendance',
    icon: 'calendar-check-outline',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "student_form" */ '../views/AttendanceView.vue')
  },
  {
    path: '/instructors',
    title: 'Instructors',
    name: 'Instructor',
    icon: 'card-text',
    component: () => import(/* webpackChunkName: "instructor_form" */ '../views/InstructorView.vue')
  },
  {
    path: '/student-dashboard',
    title: 'Dashboard',
    name: 'StudentDashboard',
    icon: 'view-dashboard',
    component: () => import(/* webpackChunkName: "instructor_form" */ '../views/StudentDashboardView.vue')
  },
  {
    path: '/instructor-dashboard',
    title: 'Dashboard',
    name: 'InstructorDashboard',
    icon: 'view-dashboard',
    component: () => import(/* webpackChunkName: "instructor_form" */ '../views/InstructortDashboardView.vue')
  }
]

export const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
