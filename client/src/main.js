import { createApp } from "vue";
import App from "./App.vue";
import router from './routes';
import store from './store';
import './sass/index.scss';

const app = createApp(App)
// Make sure to _use_ the router instance to make the
// whole app router-aware.
app.use(router)
app.use(store);
app.mount('#app')
