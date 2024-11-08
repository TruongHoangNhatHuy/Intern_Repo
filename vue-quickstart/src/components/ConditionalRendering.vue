<script setup>
  import { ref, computed } from 'vue'

  const awesomeNum = ref(3)
  const awesome = computed(() => {
    if (awesomeNum.value<1) awesomeNum.value = 3
    if (awesomeNum.value>3) awesomeNum.value = 1
    return awesomeNum.value
  })

  const show = ref(true)
</script>

<template>
  <main>
    <h1>5. Conditional Rendering</h1>

    <div class="row">
      <button @click="awesomeNum--">Toggle</button>
      <h2 v-if="awesome==3">Vue is awesome!</h2>
      <h2 v-else-if="awesome==2">Vue is great!</h2>
      <h2 v-else>Oh no 😢</h2>
    </div>
    <div class="row">
      <button @click="show = !show">{{ show ? "Show" : "Hide" }}</button>
      <h2 v-show="!show">Now you see me</h2>
      <h2 v-show="show">Now you don't</h2>
    </div>
  </main>
</template>

<style scoped>
.row { 
  display: flex;
  justify-content: space-around;
  padding-top: 10px;
}
</style>