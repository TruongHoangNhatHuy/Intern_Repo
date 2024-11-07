<script setup>
  import { computed, ref } from 'vue'
  import HelloWorld from './components/HelloWorld.vue'
  // import TheWelcome from './components/TheWelcome.vue'
  import TemplateSyntax from './components/TemplateSyntax.vue'
  import ReactivityFundamentals from './components/ReactivityFundamentals.vue'
  import ComputedProperties from './components/ComputedProperties.vue'
  import ClassStyleBindings from './components/ClassStyleBindings.vue'

  const totalPage = 4
  const page = ref(1)
  const pageNum = computed(() => {
    if (page.value<1) page.value = 1
    if (page.value>totalPage) page.value = totalPage
    return page.value
  })
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="100" height="100" />

    <div class="wrapper">
      <HelloWorld msg="Vue Quickstart" />
      <div>
        <button @click="page--">Prev</button>
        {{ page }}
        <button @click="page++">Next</button>
      </div>
    </div>
  </header>

  <main>
    <!-- <TheWelcome /> -->
    <TemplateSyntax v-show="pageNum==1"/>
    <ReactivityFundamentals v-show="pageNum==2"/>
    <ComputedProperties v-show="pageNum==3"/>
    <ClassStyleBindings v-show="pageNum==4"/>
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
