<script setup>
  const rawHtml = "<span style='color: red'>This should be red.</span>"
  var dynamicId = 100
  var isDisabled = true

  const objectOfAttrs = {
    id: 'container',
    class: 'wrapper',
    style: 'background-color:green'
  }
</script>

<template>
  <main>
    <h1>1. Template Syntax</h1>
    <!-- Text Interpolation & Raw HTML -->
    <p>Using text interpolation: {{ rawHtml }}</p>
    <p>Using v-html directive: <span v-html="rawHtml"></span></p>
    <!-- Attribute Bindings -->
    <div :id="`div-${dynamicId}`">Dynamic Id: {{ dynamicId }}</div>
    <!-- Boolean Attributes -->
    <button :disabled="isDisabled">Boolean Attributes</button>
    <!-- Dynamically Binding Multiple Attributes -->
    <div v-bind="objectOfAttrs">Dynamically Binding Multiple Attributes</div>
    <h2>Full directive syntax visuallize:
      <img :src="`https://vuejs.org/assets/directive.DtZKvoAo.png`" width="100%">
    </h2>
  </main>
</template>

<style scoped>

</style>