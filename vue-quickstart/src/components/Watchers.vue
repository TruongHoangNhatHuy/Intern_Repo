<script setup>
  import { ref, watch, watchEffect } from 'vue'

  const question = ref('')
  const answer = ref('')
  const loading = ref(false)
  
  const todoId = ref(1)
  const todoData = ref(null)

  watch(question, async (newQuestion, oldQuestion, onCleanup) => {
    if (newQuestion.includes('?')) {
      loading.value = true
      answer.value = 'Thinking...'
      try {
        const res = await fetch('https://yesno.wtf/api')
        answer.value = (await res.json()).answer
      } catch (error) {
        answer.value = 'Error! Could not reach the API. ' + error
      } finally {
        loading.value = false
      }
    } else {
      answer.value = 'Questions usually contain a question mark. ;-)'
      loading.value = false
    }
    onCleanup(() => {
      // cleanup logic
    })
  },
  { // watch options
    immediate: true, // execute immediately when mounted
    once: false // execute once time only
  })

  // track the callback's reactive dependencies automatically
  watchEffect(async (onCleanup) => {
    const response = await fetch(
      `https://jsonplaceholder.typicode.com/todos/${todoId.value}`
    )
    todoData.value = await response.json()
    onCleanup(() => {
      // cleanup logic
    })
  })
</script>

<template>
  <main>
    <h1>9. Watchers</h1>
    <div>
      <h2>a) watch</h2>
      <p>
        Ask a yes/no question:
        <input v-model="question" :disabled="loading" />
      </p>
      <p>{{ answer }}</p>
    </div>
    <div>
      <h2>b) watchEffect</h2>
      <button @click="todoId=todoId+1">Next to do</button>
      <p>To do: {{ todoData }}</p>
    </div>
  </main>
</template>