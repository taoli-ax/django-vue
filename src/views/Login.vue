<template>
    <div>
        username:<input type="text" v-model="username">
        password<input type="text" v-model="password">
        <button type="button" @click="login()">login</button>
        
    </div>
</template>

<script>
import { reactive, getCurrentInstance, toRefs } from "vue"
export default {
    setup(){
        const { proxy } = getCurrentInstance();
        const userinfo = reactive({
                username:'',
                password:'',
        })
   
        const login=()=>{
            proxy.$http.post('/api/accounts/login/',{'username':userinfo.username,'password':userinfo.password}).
            then(response=>{
                console.log(response)
                sessionStorage.clear()
                localStorage.token = response.data.token;     // 存储token
                localStorage.id = response.data.id;
                localStorage.username = response.data.username;

                //原文链接：https://blog.csdn.net/Karse_/article/details/129910708
            }).
            catch(err=>console.log(err))
        }
        return{
            login,
            ...toRefs(userinfo),
        }
    }
}
</script>