<template>
  <div class="col-md-6 mx-auto">
    <div class="form-group d-flex">
      <input type="text" class="form-control" v-model="name" placeholder="Enter a task...">
      <button class="btn btn-success" @click="createTask">Create</button>
    </div>
    
    <ul class="list-group list-group-flush mt-4">
      <li @click="updateTask(task.uid,task.isCompleted)" class="list-group-item d-flex justify-content-between align-items-center" v-for="task in tasks" :key="task.uid">
        <strike v-if="task.isCompleted">{{task.name}}</strike>
        <div v-else>{{task.name}}</div>
        <span class="badge bg-primary rounded-pill">{{task.created_at}}</span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  data(){
    return{
      name:"",
      tasks:[]
    }
  },
  created(){
    this.getTasks()
  },
  methods:{
    createTask(){
      let token = localStorage.getItem("token")
      const requestOptions={
        method:"POST",
        headers:{
            "Content-Type": "application/json",
            "Authorization": "Bearer "+token
        },
        body: JSON.stringify({
            name:this.name
        })
    }
      fetch("http://localhost:8000/api/tasks/",requestOptions)
      .then(res=>res.json())
      .then(data=>{
        console.log(data)
        //let task = `<li class="list-group-item d-flex justify-content-between align-items-center">${data.name}<span class="badge bg-primary rounded-pill">${data.created_at}</span></li>`
        this.getTasks()
      })
    this.name=""
    },
    getTasks(){
      let token = localStorage.getItem("token")
      const requestOptions={
        method:"GET",
        headers:{
            "Content-Type": "application/json",
            "Authorization": "Bearer "+token
        },
    }
      fetch("http://localhost:8000/api/tasks/",requestOptions)
      .then(res=>res.json())
      .then(data=>{
        this.tasks = data.data
      })
    },
    updateTask(uid,isCompleted){
      let token = localStorage.getItem("token")
      const requestOptions={
        method:"PATCH",
        headers:{
            "Content-Type": "application/json",
            "Authorization": "Bearer "+token
        },
        body: JSON.stringify({
            uid:uid,
            isCompleted: !isCompleted
        })
    }
      fetch("http://localhost:8000/api/tasks/",requestOptions)
      .then(res=>res.json())
      .then(data=>{
        console.log(data)
        this.getTasks()
        //let task = `<li class="list-group-item d-flex justify-content-between align-items-center">${data.name}<span class="badge bg-primary rounded-pill">${data.created_at}</span></li>`
        
      })
    }
  }
}
</script>
