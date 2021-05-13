import {createRouter, createWebHistory} from 'vue-router';
import Home from '../components/Home';
import About from '../components/About';

const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About },
]


const router = createRouter({
  history: createWebHistory(),
  routes, // short for `routes: routes`
})

export default router;
