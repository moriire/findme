import { ref, computed, reactive } from 'vue'
import { defineStore } from 'pinia'
import axios from "axios"
export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const data = reactive({email: '', first_name: '', last_name: '', username: ''})
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  };

  function getProfile() {
    axios.get("localhost:8000/api/user/").then(u=>[
      console.log(u.data)
    ]).catch(err=>{
      console.error(err)
    })
  }

  return { count, doubleCount, increment, getProfile }
})
