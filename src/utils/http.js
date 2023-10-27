/****   http.js   ****/
// 导入封装好的axios实例
import axios from "axios";
import qs from "qs";

// axios.defaults.baseURL = ''  //正式
// axios.defaults.baseURL = 'http://localhost:8000' //测试

// //post请求头
// axios.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded;charset=UTF-8";
// //允许跨域携带cookie信息
// axios.defaults.withCredentials = true; 
// //设置超时
// axios.defaults.timeout = 15000;
const axios_instance = axios.create({
    baseURL:'http://localhost:8000',
    timeout:2000,
    withCredentials:true
})

axios_instance.interceptors.request.use(
    config => {
        let regex = /.*csrftoken=([^;.]*).*$/;
        console.log('匹配csrftoken: ',document.cookie.match(regex))
        config.headers['X-CSRFTOKEN']= document.cookie.match(regex) === null? null : document.cookie.match(regex)[1]
        return config;
    },
    error => {
        return Promise.reject(error);
    }
);

axios_instance.interceptors.response.use(
    response => {
        // if (response.status == 200) {
        //     return Promise.resolve(response);
        // } else {
        //     return Promise.reject(response);
        // }
        // 该返回的数据则是axios.then(res)中接收的数据
        return response
    },
    error => {

        alert(JSON.stringify(error), '请求异常', {
            confirmButtonText: '确定',
            callback: (action) => {
                console.log(action)
            }
        });
        // 该返回的数据则是axios.catch(err)中接收的数据
        return Promise.reject(err)
    }
);
export {axios_instance}

//链接：https://juejin.cn/post/7083797249611792391
//链接：https://www.jianshu.com/p/6e10aaf4688b