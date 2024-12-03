<script setup>
  const prop = defineProps({
    title: String,
    content: String,
    description: String,
  })
  
  const emit = defineEmits(['openDetail'])
</script>

<template>
  <div class="btn btn-light card h-100" @click="emit('openDetail')">
    <div class="card-body">
      <h3 class="card-title">{{ title }}</h3>
      <div class="card-text">{{ content }}</div>
      <div class="card-text">{{ description }}</div>
      <!-- <a href="" class="btn btn-success">Edit</a>
      <a href="" class="btn btn-danger" onclick="return confirm('Are you sure?')">Delete</a> -->
    </div>
  </div>
</template>