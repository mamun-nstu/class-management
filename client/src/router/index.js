import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const HOME = {
  path: '/',
  name: 'Home',
  title: 'Home',
  component: Home,
  icon: 'home'
};

const ABOUT = {
  path: '/about',
  title: 'About',
  name: 'About',
  icon: 'help-circle',
  // route level code-splitting
  // this generates a separate chunk (about.[hash].js) for this route
  // which is lazy-loaded when the route is visited.
  component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
};

const STUDENTS = {
  path: '/students',
  title: 'Students',
  name: 'Student',
  icon: 'account',
  // route level code-splitting
  // this generates a separate chunk (about.[hash].js) for this route
  // which is lazy-loaded when the route is visited.
  component: () => import(/* webpackChunkName: "student_form" */ '../views/StudentView.vue')
};

const COURSES = {
  path: '/courses',
  title: 'Courses',
  name: 'Course',
  icon: 'text-subject',
  // route level code-splitting
  // this generates a separate chunk (about.[hash].js) for this route
  // which is lazy-loaded when the route is visited.
  component: () => import(/* webpackChunkName: "student_form" */ '../views/CourseView.vue')
};

const BATCHES = {
  path: '/batches',
  title: 'Batches',
  name: 'Batch',
  icon: 'account-multiple-outline',
  // route level code-splitting
  // this generates a separate chunk (about.[hash].js) for this route
  // which is lazy-loaded when the route is visited.
  component: () => import(/* webpackChunkName: "student_form" */ '../views/BatchView.vue')
};

const ATTENDANCES = {
  path: '/attendances',
  title: 'Attendances',
  name: 'Attendance',
  icon: 'calendar-check-outline',
  // route level code-splitting
  // this generates a separate chunk (about.[hash].js) for this route
  // which is lazy-loaded when the route is visited.
  component: () => import(/* webpackChunkName: "student_form" */ '../views/AttendanceView.vue')
};

const INSTRUCTORS = {
  path: '/instructors',
  title: 'Instructors',
  name: 'Instructor',
  icon: 'card-text',
  component: () => import(/* webpackChunkName: "instructor_form" */ '../views/InstructorView.vue')
};

const STUDENT_DASHBOARD = {
  path: '/student-dashboard',
  title: 'Dashboard',
  name: 'StudentDashboard',
  icon: 'view-dashboard',
  component: () => import(/* webpackChunkName: "instructor_form" */ '../views/StudentDashboardView.vue')
};

const INSTRUCTOR_DASHBOARD = {
  path: '/instructor-dashboard',
  title: 'Dashboard',
  name: 'InstructorDashboard',
  icon: 'view-dashboard',
  component: () => import(/* webpackChunkName: "instructor_form" */ '../views/InstructortDashboardView.vue')
};

export const LOGIN = {
  path: '/login',
  title: 'Login',
  name: 'Login',
  icon: 'login-variant',
  component: () => import(/* webpackChunkName: "instructor_form" */ '../views/LoginView.vue')
};

const LOGOUT = {
  path: '/logout',
  title: 'Logout',
  name: 'Logout',
  icon: 'login-variant',
  component: () => import(/* webpackChunkName: "instructor_form" */ '../views/LogoutView.vue')
};

const TEST_VIEW = {
  path: '/test',
  title: 'Test',
  name: 'Test',
  icon: 'bug-check-outline',
  component: () => import(/* webpackChunkName: "instructor_form" */ '../views/TestView.vue')
};

export const COMMON_ROUTES = [
  HOME,
  ABOUT,
  TEST_VIEW,
];

export const STUDENT_ROUTES = [
  STUDENT_DASHBOARD,
  LOGOUT,
];

export const INSTRUCTOR_ROUTES = [
  ATTENDANCES,
  INSTRUCTOR_DASHBOARD,
  LOGOUT,
];

export const ADMIN_ROUTES = [
  STUDENTS,
  COURSES,
  BATCHES,
  INSTRUCTORS,
  LOGOUT,
];

export const routes = [
  HOME,
  ABOUT,
  STUDENTS,
  COURSES,
  BATCHES,
  ATTENDANCES,
  INSTRUCTORS,
  STUDENT_DASHBOARD,
  INSTRUCTOR_DASHBOARD,
  TEST_VIEW,
  LOGIN,
  LOGOUT,
];

export const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: routes
})
