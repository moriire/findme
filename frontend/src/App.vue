<script setup>
import { RouterLink, RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'
import LeftSide from './components/LeftSide.vue'
import RightSide from './components/RightSide.vue'
</script>

<template>
  <nav-bar></nav-bar>
  <div class="container-fluid">
    <div class="row">
      <left-side></left-side>
      <right-side></right-side>
     
      <RouterView />
    </div>
  </div>
  
</template>
