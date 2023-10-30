<template>
    <div>
        <h1>signup</h1>
        <button type="button" @click="register()">login</button>
    </div>
</template>

<script>
import { reactive, getCurrentInstance, toRefs } from "vue";
export default {
    setup(){
        const register = ()=>{
            alter("register success, jump to login");
        }
        return{

        }
    }
}
</script>