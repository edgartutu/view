<template>
    <div>
        <form action="/">
            <input type="text" placeholder="Reg_n0" v-model="reg_no"/><br>
            <input type="password" placeholder="new Password " v-model="oldpass"/><br>
            <input type="password" placeholder=" confirm new Password" v-model="newpass"/>
            <v-btn @click="reset" class="orange">submit</v-btn>
        </form>
    </div>
</template>
<script>
import axios from 'axios'
export default {
   data(){
       return{
           reg_no:"",
           oldpass:"",
           newpass:""
       }
   },
   methods:{
       reset(){
           axios.post('http://127.0.0.1:5000/reset-password',{"reg_no":this.reg_no,"old_pass":this.oldpass,"new_pass":this.newpass}).then(window.location.reload())
       }
   }
}
</script>
<style>
form {
    position: absolute;
    top: 200px;
    display: flex;
    align-items: center;
    justify-content: space-around;
    flex-direction: column;
   
    width: calc(40% );
    height: calc(20% );
    text-align: center;
   
    transition: all .5s ease-in-out;
} 
    input {
      background-color: #eee;
      border: none;
      padding: 20px 50px;
      margin: 6px 0;
      width: calc(100% - 50px);
      border-radius: 50px;
      border-bottom: 1px solid #ddd;
      box-shadow: inset 0 1px 2px rgba(0, 0, 0, .4), 
                        0 -1px 1px #fff, 
                        0 1px 0 #fff;
      overflow: hidden;
    }
      focus {
        outline: none;
        background-color: #fff;
      }

    
  
</style>


