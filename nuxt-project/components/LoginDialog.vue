<script setup>
  import { useUserStore } from '@/stores/user'
  
  const user = useUserStore()
  const username = ref("")
  const password = ref("")

  const disableLogin = ref(false)
  const retry = ref(false)
  const loggedin = computed(() => user.userInfo!=null)

  function handleBlur() {
    username.value = ""
    password.value = ""
    disableLogin.value = false
    retry.value = false
  }

  async function login() {
    disableLogin.value = true
    const success = await user.authenticate(username.value, password.value)
    if (success) {
      // logged in
    } else {
      retry.value = true
      disableLogin.value = false
    }  
  }
</script>

<template>
  <div class="modal fade" tabindex="-1" @blur="handleBlur()">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">
            <span v-if="loggedin">You have logged in!</span>
            <span v-else>Login</span>
          </h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <span v-if="loggedin">Welcome <b>{{ user.userInfo.username }}</b></span>
          <span v-else>
            <div v-if="retry" class="text-danger mb-2"><b>Username or password incorrect!</b></div>
            <input class="form-control mb-2" type="text" placeholder="username" v-model="username" :disabled="disableLogin"/>
            <input class="form-control" type="password" placeholder="password" v-model="password" :disabled="disableLogin"/>
          </span>
        </div>
        <div class="modal-footer">
          <span v-if="loggedin">
            <button type="button" class="btn btn-primary">
              Logout
            </button>
          </span>
          <span v-else>
            <button type="button" class="btn btn-primary" :disabled="disableLogin" @click="login()">
              <span v-if="disableLogin" class="spinner-border" role="status">
                <span class="visually-hidden">Loading...</span>
              </span>
              <span v-else>Login</span>
            </button>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>