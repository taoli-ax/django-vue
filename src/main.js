import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import {axios_instance} from "./utils/http";
import "./assets/style.css";
import "@popperjs/core";
import "bootstrap";
import "bootstrap-icons/font/bootstrap-icons.css";



const app = createApp(App)
app.mount('#app')
app.config.globalProperties.$http = axios_instance;
