<script setup>
  import { useUserStore } from '@/stores/user'
  
  const user = useUserStore()
  const username = ref("")
  const password = ref("")

  const loading = ref(false)
  const retry = ref(false)
  const loggedin = computed(() => user.userInfo!=null)

  function handleBlur() {
    username.value = ""
    password.value = ""
    loading.value = false
    retry.value = false
  }

  async function login() {
    loading.value = true
    const success = await user.authenticate(username.value, password.value)
    if (success) {
      retry.value = false
    } else {
      retry.value = true
    }  
    loading.value = false
  }

  async function logout() {
    loading.value = true
    const success = await user.revokeAuth()
    if (success) {
      retry.value = false
    } else {
      retry.value = true
    } 
    loading.value = false
  }
</script>

<template>
  <div class="modal fade" tabindex="-1" @blur="handleBlur()">
    <div class="modal-dialog">
      <!-- not log in -->
      <div class="modal-content" v-if="!loggedin">
        <form @submit.prevent="login()">
          <div class="modal-header">
            <h5 class="modal-title">Login</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <input class="form-control mb-2" type="text" placeholder="username" v-model="username" required :disabled="loading"/>
            <input class="form-control" type="password" placeholder="password" v-model="password" required :disabled="loading"/>
          </div>
          <div class="modal-footer">
            <div v-if="retry" class="text-danger mb-2"><b>Username or password incorrect!</b></div>
            <button type="submit" class="btn btn-primary" :disabled="loading">
              <span v-if="loading" class="spinner-border" role="status">
                <span class="visually-hidden">Loading...</span>
              </span>
              <span v-else>Login</span>
            </button>
          </div>
        </form>
      </div>
      <!-- logged in -->
      <div class="modal-content" v-else>
        <div class="modal-header">
          <h5 class="modal-title">You have logged in!</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <span>Welcome <b>{{ user.userInfo.username }}</b></span>
        </div>
        <div class="modal-footer">
          <div v-if="retry" class="text-danger mb-2"><b>Failed to logout, try again!</b></div>
          <button type="button" class="btn btn-primary" :disabled="loading" @click="logout()">
            <span v-if="loading" class="spinner-border" role="status">
              <span class="visually-hidden">Loading...</span>
            </span>
            <span v-else>Logout</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>