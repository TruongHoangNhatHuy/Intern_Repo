<script setup>
  const model = defineModel()

  const props = defineProps({ 
    isReadonly: Boolean
  })

  const config = useRuntimeConfig();

  const { data: languages, status, refresh } = useFetch(`${config.public.serverUrl}/languages/`);
</script>

<template>
  <div class="card container mw-100 m-1">
    <div class="row p-2">
      <label class="col-3">Title</label>
      <input class="col-9" type="text" required v-model="model.title" :disabled="isReadonly">
    </div>
    <div class="row p-2">
      <label class="col-3">Language</label>
      <select class="col-9" required v-model="model.language" :disabled="isReadonly">
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
      <textarea class="col-9" required rows="9" v-model="model.code" :disabled="isReadonly"/>
    </div>
    <div class="row p-2">
      <label class="col-3">Linenos</label>
      <span class="col-9 form-check form-switch fs-5">
        <input class="form-check-input" type="checkbox" v-model="model.linenos" :disabled="isReadonly">
      </span>
    </div>
  </div>
</template>