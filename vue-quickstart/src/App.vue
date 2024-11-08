<script setup>
  import { computed, ref } from 'vue'
  import HelloWorld from './components/HelloWorld.vue'
  // import TheWelcome from './components/TheWelcome.vue'
  import TemplateSyntax from './components/TemplateSyntax.vue'
  import ReactivityFundamentals from './components/ReactivityFundamentals.vue'
  import ComputedProperties from './components/ComputedProperties.vue'
  import ClassStyleBindings from './components/ClassStyleBindings.vue'
  import ConditionalRendering from './components/ConditionalRendering.vue'
  import ListRendering from './components/ListRendering.vue'
  import EventHandling from './components/EventHandling.vue'
  import FormInputBindings from './components/FormInputBindings.vue'

  const pages = ref([
    TemplateSyntax,
    ReactivityFundamentals,
    ComputedProperties,
    ClassStyleBindings,
    ConditionalRendering,
    ListRendering,
    EventHandling,
    FormInputBindings,
  ])

  const pageCur = ref(1)
  const pageNum = computed(() => {
    if (pageCur.value<1) pageCur.value = pages.value.length
    if (pageCur.value>pages.value.length) pageCur.value = 1
    return pageCur.value
  })
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="100" height="100" />

    <div class="wrapper">
      <HelloWorld msg="Vue Quickstart" />
      <div>
        <button @click="pageCur--">Prev</button>
        <select :value="pageNum" @change="pageCur=$event.target.value">
          <option v-for="index in pages.length" :value="index">{{ index }}</option>
        </select>
        <button @click="pageCur++">Next</button>
      </div>
    </div>
  </header>

  <main>
    <div v-for="(child, index) in pages" :key="index">
      <component :is="child" v-show="pageNum==index+1"/>
      <!-- <TheWelcome /> -->
    </div>
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

main {
  margin-top: 10px;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
