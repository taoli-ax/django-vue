import {createRouter, createWebHashHistory}  from "vue-router";
import UserAccount from '../components/UserAccount.vue';
import Car from '../components/Car.vue';
import Home from '../views/Home.vue';
import Login from '../views/Login.vue'
import Signup from '../views/Signup.vue'
const routes = [
    { 
        path: '/', 
        component: Home,
        children:[
            {
                path: 'login',
                components: {default:Login}
            },
            {
                path: 'signup',
                components: {default:Signup}
            },
            { 
                path: 'account',
                components: {default:UserAccount}
            },
            { 
                path: 'cars',
                components: {carsinfo:Car}
            },
        ]
    },
   
    
  ]


const router = createRouter({
    // 4. 内部提供了 history 模式的实现。为了简单起见，我们在这里使用 hash 模式。
    history: createWebHashHistory(),
    routes, // `routes: routes` 的缩写
  })

export default router