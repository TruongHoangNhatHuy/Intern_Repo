<!-- BlogPost.vue -->
<script setup>
  const props = defineProps(['title'])
  defineEmits(['enlarge-text'])
  // console.log(props.title)
</script>

<template>
  <div class="card">
    <h4>{{ title }}</h4>
    <button @click="$emit('enlarge-text')">Enlarge text</button>
  </div>
</template>

<style scoped>
.card {
  border: 2px, solid, lightgreen;
  border-radius: 10px;
  padding: 10px;
  margin: 10px;
}
</style>