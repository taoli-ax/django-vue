import { createApp } from 'vue';
import App from './App.vue';
import {axios_instance} from "./utils/http";
import router from './router/index'
import "./assets/style.css";
import "@popperjs/core";
import "bootstrap";
import "bootstrap-icons/font/bootstrap-icons.css";



const app = createApp(App)
app.use(router)
app.mount('#app')
app.config.globalProperties.$http = axios_instance;
