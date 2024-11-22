<script setup lang="ts">
  const prop = defineProps<{
    title: string,
    content: string,
    description: string,
  }>()
  
  const emit = defineEmits<{
    (e: 'openDetail'): void
  }>()
</script>

<template>
  <div class="btn btn-light card h-100" @click="emit('openDetail')">
    <div class="card-body">
      <h3 class="card-title">{{ title }}</h3>
      <p class="card-text">{{ content }}</p>
      <p class="card-text">{{ description }}</p>
      <!-- <a href="" class="btn btn-success">Edit</a>
      <a href="" class="btn btn-danger" onclick="return confirm('Are you sure?')">Delete</a> -->
    </div>
  </div>
</template>