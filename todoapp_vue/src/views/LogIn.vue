<template>
    <div class="col-6 mx-auto">
        <form>
            <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Email address</label>
                <input type="email" v-model="username" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
            </div>
            <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label">Password</label>
                <input type="password" v-model="password" class="form-control" id="exampleInputPassword1">
            </div>
            <button type="submit" @click="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</template>
<script>
export default{
    name:"LogIn",
    data(){
        return {
            username:"",
            password:"",
            errors:[]
        }
    },
    methods:{
        submit(e){
            e.preventDefault()
            if(!this.username){
                this.errors.push("Fill username")
            }
            if(!this.password){
                this.errors.push("Fill password")
            }
            if(this.errors.length==0){
                const requestOptions={
                    method:"POST",
                    headers:{
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        username:this.username,
                        password: this.password
                    })
                }
                fetch("http://localhost:8000/api/token/",requestOptions)
                .then(res=>res.json())
                .then(data=>{
                    console.log(data.access)
                    localStorage.setItem("token",data.access)
                    window.location.href="/"
                })
            }
            else{
                console.log(JSON.stringify(this.errors))
            }
        }
    }
}
</script>