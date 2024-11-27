<script setup>
  const route = useRoute();
  const id = route.params.id;
  const { data: snippet, status, refresh } = useFetch(`http://127.0.0.1:8000/snippets/${id}/`);

  const editing = ref(false);
</script>

<template>
  <div class="h-100 m-5 mt-3">
    <h1>Detail</h1>
    <ItemForm v-if="status==`success`" v-model="snippet" :is-readonly="!editing"/>
    <div class="mt-2">
      <button class="btn btn-secondary m-1" @click="$router.back()">Back</button>
      <button v-if="!editing" class="btn btn-primary m-1" @click="editing=true">Edit</button>
      <span v-else>
        <button class="btn btn-primary m-1" @click="editing=false">Cancel edit</button>
        <button class="btn btn-success m-1" @click="editing=false">Submit</button>
      </span>
    </div>
  </div>
</template>