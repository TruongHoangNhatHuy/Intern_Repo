<script setup>
  import { ref, computed } from 'vue'

  const isActive = ref(true)
  const hasError = ref(false)

  const classObject = computed(() => ({
    active: isActive.value && !error.value,
    'text-danger': error.value && error.value.type === 'fatal'
  }))

  const activeClass = ref('active')
  const errorClass = ref('text-danger')

  const activeColor = ref('red')
  const fontSize = ref(30)

  const styleObject = reactive({
    color: 'red',
    fontSize: '30px'
  })
</script>

<template>
  <main>
    <h1>4. Class & Style Binding</h1>
    <div 
      class="static"
      :class="{ active: isActive, 'text-danger': hasError }"
      :style="{ color: activeColor, fontSize: fontSize+'px' }"
    >Binding to Objects: {{ `<div class="static active"></div>` }}</div>
    <div 
      :class="classObject" 
      :style="styleObject"
    > Binding to Computed property: {{ `<div class="active"></div>` }}</div>
    <div 
      :class="[activeClass, errorClass]"
      :style="[baseStyles, overridingStyles]"
    >Binding to Arrays: {{ `<div class="active text-danger"></div>` }}</div>
  </main>
</template>