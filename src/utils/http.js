/****   http.js   ****/
// 导入封装好的axios实例
import axios from "axios";
import qs from "qs";
import router from '../router/index'

// axios.defaults.baseURL = ''  //正式
// axios.defaults.baseURL = 'http://localhost:8000' //测试

// //post请求头
// axios.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded;charset=UTF-8";
// //允许跨域携带cookie信息
// axios.defaults.withCredentials = true; 
// //设置超时
// axios.defaults.timeout = 15000;
const axios_instance = axios.create({
    baseURL:'http://localhost:8080',
    timeout:2000,
    withCredentials:true
})

axios_instance.interceptors.request.use(
    config => {
        let regex = /.*csrftoken=([^;.]*).*$/;
        console.log('匹配csrftoken: ',document.cookie.match(regex))
        config.headers['X-CSRFTOKEN']= document.cookie.match(regex) === null? null : document.cookie.match(regex)[1]

        let token = localStorage.getItem('token') || sessionStorage.getItem('token')
        console.log("interceptor token: ",token)
        if (token) {
            config.headers['Authorization'] = 'Bearer ' + token;
        }

        return config;
    },
    error => {
        return Promise.reject(error);
    }
);

axios_instance.interceptors.response.use(
    response => {
        if(response.data.token) {
            localStorage.setItem('token',response.data.token.access)
            router.push('/')
        }
        return response
    },
    error => {
        if (error.response) {
            switch (error.response.status) {
              case 401:
                localStorage.removeItem('token')
                router.replace({
                  path: '/login',
                  query: {redirect: router.currentRoute.fullPath}   //登录成功后跳入浏览的当前页面
                })
            }
        }
      
        return Promise.reject(error)
    }
);
export {axios_instance}

//链接：https://juejin.cn/post/7083797249611792391
//链接：https://www.jianshu.com/p/6e10aaf4688b