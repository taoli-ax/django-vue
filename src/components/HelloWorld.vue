<script setup>

</script>

<template>
     {{ carinfo }}
  <div class="row">
    <div class="col-md-8">
      <table  class="table">
        <thead>
          <tr>
            <td>car name</td>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in carinfo" :key="item.id">
            <td>{{item.name}}</td>
            <button class="btn btn-success" title="edit">
              <i class="bi bi-pen-fill"></i>
            </button>
            <button class="btn btn-danger" title="delete">
              <i class="bi bi-trash"></i>
            </button>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="col-md-2">
          <button type="button" @click="getCarinfo()">get</button>
    </div>
    <div class="col-md-2">
     
     <input type="text" v-model="carName">
     <button type="button" @click="addCarinfo()">add</button>

</div>
 
  </div>
</template>
<script>
import { reactive, getCurrentInstance, toRefs } from "vue"
export default {
  name: 'carinfo',

  setup(){
    const car = reactive({
      carinfo:[],
      carName:''
    })
    const { proxy } = getCurrentInstance();
    const getCarinfo = () => {
      proxy.$http
        .get("/cars/carinfo/")
        .then((res) => {
          //请求成功
          console.log(res.data)
          car.carinfo = res.data
          console.log(res)
        })
        .catch( err => {
          console.log(err)
        })
    };
    const addCarinfo = () => {
      proxy.$http
        .post("/cars/carinfo/", {'name':car.carName})
        .then((res) => {
          //请求成功
          console.log(res.data)
        })
        .catch( err => {
          console.log(err)
        })
    };
    return {
      getCarinfo,
      addCarinfo,
      ...toRefs(car)
    };


// 链接：https://juejin.cn/post/7083797249611792391

  }
  // data(){
  //   return {
  //       car_list:[],
  //       car_name: ''
  //   }
  // },
  // mounted(){
  //   this.send()
  // },
  // methods:{
  //   getCookid(cookie){
  //   let reg = /csrftoken=([\w]+)[;]?/g
  //     return reg.exec(cookie)[1]
  //   },
  //   send(){
  //     console.log("get carinfo")
  //     axios.get('http://localhost:8000/cars/carinfo/').
  //     then(res=>{
  //       console.log(res.data)
  //       this.car_list = res.data
  //     }).catch(err=>console.log(err))
  //   },
  //   add(){
  //     let csrf = this.getCookid(document.cookie)
  //     axios.post(
  //       'http://localhost:8000/cars/carinfo/', 
  //       qs.stringify({'name': this.car_name}),
  //     {
  //       headers: {
  //               'Content-Type':'application/x-www-form-urlencoded',
  //               'X-CSRFToken': csrf
  //             }
  // }).
  //     then(res=>{
       
  //       this.car_list = res.data
  //       console.log(this.car_list)
        
  //     }).
  //     catch(err=>console.log(err))
  //     this.send()
  //     this.car_name =''
      
        
  //   }
  // }

}
</script>
