<script setup lang="ts">
  const route = useRoute();
  const id = route.params.id;
  const { data: snippet, status, refresh } = useFetch(`http://127.0.0.1:8000/snippets/${id}/`);
</script>

<template>
  <div class="h-100 m-5 mt-3">
    <h1>Detail</h1>
    <ItemForm v-if="status==`success`" v-model="snippet" :is-readonly="true"/>
    <div class="mt-2">
      <button class="btn btn-secondary m-1" @click="$router.back()">Back</button>
      <button class="btn btn-primary m-1" @click="">Edit</button>
    </div>
  </div>
</template>