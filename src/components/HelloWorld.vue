<script setup>

</script>

<template>
  <div class="row">
    <div class="col-md-8">
      <table  class="table">
        <thead>
          <tr>
            <td>car name</td>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in car_list" :key="item.id">
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
    <div class="col-md-4">
     
          <input type="text" v-model="car_name">
          <button type="button" @click="add()">submit</button>
  
    </div>
    {{ car_name }}
  </div>
</template>
<script>
import axios from 'axios'
import qs from 'qs'
export default {
  name: 'carinfo',
  data(){
    return {
        car_list:[],
        car_name: ''
    }
  },
  mounted(){
    this.send()
  },
  methods:{
    getCookid(cookie){
    let reg = /csrftoken=([\w]+)[;]?/g
      return reg.exec(cookie)[1]
    },
    send(){
      console.log("get carinfo")
      axios.get('http://localhost:8000/cars/carinfo/').
      then(res=>{
        console.log(res.data)
        this.car_list = res.data
      }).catch(err=>console.log(err))
    },
    add(){
      let csrf = this.getCookid(document.cookie)
      axios.post(
        'http://localhost:8000/cars/carinfo/', 
        qs.stringify({'name': this.car_name}),
      {
        headers: {
                'Content-Type':'application/x-www-form-urlencoded',
                'X-CSRFToken': csrf
              }
  }).
      then(res=>{
       
        this.car_list = res.data
        console.log(this.car_list)
        
      }).
      catch(err=>console.log(err))
      this.send()
      this.car_name =''
      
        
    }
  }

}
</script>
