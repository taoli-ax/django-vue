import axios from "axios";

const service=axios.create({
    //基础路径URL配置
    baseURL:"http://localhost:5173",
    //五秒未响应提示
    timeout:5000,
})


//请求拦截
service.interceptors.request.use(config => {
    config.headers['token'] = Vue.cookie.get('token') // 请求头带上token，一般后端的请求都要带上token才能成功的，没有token会被判断未登录，这里根据个人不同改获取token的方式。不需要的直接删掉这行代码就行，其他不动
    return config
  }, error => {
    return Promise.reject(error)
  })
  

//响应拦截器
service.interceptors.response.use((response)=>{
    //只返回config内的data的数据，其他的不展示
    const res=response.data
    return res
},(error)=>{
    //如果请求出错会有弹框提示
        return Promise.reject(error)
})

export default service

// 原文链接：https://blog.csdn.net/seeeeeeeeeee/article/details/123378844