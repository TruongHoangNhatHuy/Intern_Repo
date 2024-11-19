<script setup>
  import { ref } from 'vue';

  const info = ref({})

  function onSubmit() {
    alert(JSON.stringify(info.value))
  }
</script>

<template>
  <main>
    <h1>8. Form Input Bindings</h1>
    <form @submit.prevent="onSubmit">
      <input v-model.lazy.trim="info.fullname" placeholder="Full name"/>
      <p>Gender:
        <input type="radio" id="male" value=true v-model="info.isMale" />
        <label for="male">Male </label>
        <input type="radio" id="female" value=false v-model="info.isMale" />
        <label for="female">Female</label>
      </p>
      <p>Job:
        <select v-model="info.job">
          <option value="" disabled>--Choose--</option>
          <option value="student">Student</option>
          <option value="teacher">Teacher</option>
        </select>
      </p>
      <button type="submit">Submit</button>
      <button type="reset" @click="info={}">Reset</button>
    </form>
  </main>
</template>