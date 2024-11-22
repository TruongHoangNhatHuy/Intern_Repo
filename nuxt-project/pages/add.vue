<script setup>
  const snippet = ref({
    title: "",
    code: "",
    linenos: false,
    language: "",
    style: "vs"
  });

  function postSnippet() {
    const body = JSON.stringify(snippet.value)
    alert(body)
    // const { data, status } = useFetch(`http://127.0.0.1:8000/snippets/`, {method:'POST'});
  }
</script>

<template>
  <div class="h-100 m-5 mt-3">
    <h1>Add</h1>
    <ItemForm v-model="snippet" :is-readonly="false"/>
    <div class="mt-2">
      <button class="btn btn-secondary m-1" @click="$router.back()">Back</button>
      <button class="btn btn-primary m-1" @click="postSnippet">Submit</button>
    </div>
  </div>
</template>