<script setup>
  const config = useRuntimeConfig();
  const user = useUserStore()
  const route = useRoute();
  
  const editing = ref(false);
  const submitting = ref(false)
  
  // const snippet = ref(null) // TODO: Cache snippet
  const id = route.params.id;
  const { data: snippet, status, refresh } = await useFetch(`${config.public.serverUrl}/snippets/${id}/`)
  // snippet.value = data.value

  async function handleSubmit() {
    try {
      submitting.value = true
      const { data, status } = await useFetch(`${config.public.serverUrl}/snippets/${id}/`, {
        method: 'patch',
        headers: {
          "Authorization": `Bearer ${user.accessToken}`
        },
        body: JSON.stringify(snippet.value)
      })

      if (status.value=='success') {
        refresh()
        editing.value = false
      } else {
        alert('Failed to edit snippet, try again!')
      }
    } catch (error) {
      console.warn(error)
      alert("Error")
    } finally {
      submitting.value = false
    }
  }

  function handleCancel() {
    refresh()
    editing.value = false
  }

  async function handleDelete() {
    const result = confirm("Do you want to delele this snippet?")
    if (result) {
      const { data, status } = await useFetch(`${config.public.serverUrl}/snippets/${id}/`, {
          method: 'delete',
          headers: {
            "Authorization": `Bearer ${user.accessToken}`
          }
        })
      if (status.value=='success') {
        alert("Snippet deleted!")
        navigateTo('/')
      } else {
        alert('Failed to delete snippet, try again!')
      }
    }
  }
</script>

<template>
  <form class="h-100 w-100 m-3" @submit.prevent="handleSubmit">
    <h1>
      <span v-if="editing">Edit</span>
      <span v-else>Detail</span>
    </h1>
    <ItemForm v-if="status==`success`" v-model="snippet" :is-readonly="!editing||submitting"/>
    <div class="mt-2">
      <button class="btn btn-secondary m-1" type="button" @click="$router.back()">Back</button>
      <span v-if="status=='success' && user.userInfo?.username==snippet.owner">
        <span v-if="!editing">
          <button class="btn btn-primary m-1" type="button" @click="editing=true">Edit</button>
          <button class="btn btn-danger m-1" type="button" @click="handleDelete()">Delete</button>
        </span>
        <span v-else>
          <button class="btn btn-primary m-1" type="reset" @click="handleCancel()" :disabled="submitting">
            Cancel edit
          </button>
          <button class="btn btn-success m-1" type="submit" :disabled="submitting">
            <span v-if="submitting" class="spinner-border" role="status">
              <span class="visually-hidden">Loading...</span>
            </span>
            <span v-else>Submit</span>
          </button>
        </span>
      </span>
    </div>
  </form>
</template>