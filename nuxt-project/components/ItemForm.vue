<script setup>
  const model = defineModel()

  const props = defineProps({ 
    isReadonly: Boolean
  })

  const { data: languages, status, refresh } = useFetch(`http://127.0.0.1:8000/languages/`);
</script>

<template>
  <form class="card container m-0">
    <div class="row p-2">
      <label class="col-3">Title</label>
      <input class="col-9" type="text" v-model="model.title" :disabled="isReadonly">
    </div>
    <div class="row p-2">
      <label class="col-3">Language</label>
      <select class="col-9" v-model="model.language" :disabled="isReadonly">
        <option 
          v-if="status==`success`" 
          v-for="item in languages.choice" 
          :key="item[0]" 
          :value="item[0]"
        >{{ item[1] }}</option>
      </select>
    </div>
    <div class="row p-2">
      <label class="col-3">Code</label>
      <textarea class="col-9" rows="9" v-model="model.code" :disabled="isReadonly"/>
    </div>
    <div class="row p-2">
      <label class="col-3">Linenos</label>
      <span class="col-9 form-check form-switch fs-5">
        <input class="form-check-input" type="checkbox" v-model="model.linenos" :disabled="isReadonly">
      </span>
    </div>
  </form>
</template>