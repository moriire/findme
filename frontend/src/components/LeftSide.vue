<template>
  <div class="col-lg-5">
        {{  data }}
  </div>
</template>
<script setup>
import axios from "axios";
import { onMounted, ref, computed } from "vue";
const data = ref({})
const errors = ref({})
const getAll = async () =>{
  try{
    const response = await axios.get("http://127.0.0.1:8000/api/main/1/")
    data.value = response.data
    console.log(response)
  } catch(error){
    console.log(error.response.data.detail)
  }
}
onMounted(
  ()=>{
    getAll()
  }
)
</script>