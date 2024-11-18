<script setup>
  import { useTemplateRef, onMounted } from 'vue'

  // the first argument must match the ref value in the template
  const input = useTemplateRef('my-input')

  onMounted(() => {
    input.value.focus()
    input.value.title = 'My input'
    input.value.defaultValue = 'Template Ref'
    input.value.readOnly = true
  })
</script>

<template>
  <main>
    <h1>10. Template Refs</h1>
    <input ref="my-input"/>
    <p>{{ input }}</p>
  </main>
</template>