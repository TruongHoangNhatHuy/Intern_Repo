<script setup>
const config = useRuntimeConfig()
const user = useUserStore()

const snippet = ref({
  title: "",
  code: "",
  linenos: false,
  language: "",
  style: "vs"
});
const submitting = ref(false)

async function postSnippet() {
  try {
    submitting.value = true
    // const { data, status, error } = await useFetch('https://dummyapi.online/api/todos')
    const { data, status } = await useFetch(`${config.public.serverUrl}/snippets/`, {
      method: 'post',
      headers: {
        "Authorization": `Bearer ${user.accessToken}`
      },
      body: JSON.stringify(snippet.value)
    })

    if (status.value=='success') {
      alert('Snippet added!')
      navigateTo('/')
    } else {
      alert('Failed to add snippet, try again!')
    }
  } catch (error) {
    console.warn(error)
    alert("Error")
  } finally {
    submitting.value = false
  }
}
</script>

<template>
  <form class="h-100 w-100 m-3" @submit.prevent="postSnippet">
    <h1>Add</h1>
    <ItemForm v-model="snippet" :is-readonly="false" />
    <div class="mt-2">
      <button class="btn btn-secondary m-1" @click="$router.back()">Back</button>
      <button class="btn btn-success m-1" type="submit" :disabled="submitting">
        <span v-if="submitting" class="spinner-border" role="status">
          <span class="visually-hidden">Loading...</span>
        </span>
        <span v-else>Submit</span>
      </button>
    </div>
  </form>
</template>