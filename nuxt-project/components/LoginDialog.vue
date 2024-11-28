<script setup>
  import { useUserStore } from '@/stores/user'
  
  const user = useUserStore()
  const username = ref("")
  const password = ref("")

  const disableLogin = ref(false)
  const loggedin = ref(false)

  function handleBlur() {
    username.value = ""
    password.value = ""
    disableLogin.value = false
  }

  async function login() {
    disableLogin.value = true
    const success = await user.authenticate(username.value, password.value)
    if (success) {
      loggedin.value = true
    } else {
      disableLogin.value = false
    }  
  }
</script>

<template>
  <div class="modal fade" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true" @blur="handleBlur()">
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
            <input class="form-control mb-2" type="text" placeholder="username" v-model="username" :disabled="disableLogin"/>
            <input class="form-control" type="password" placeholder="password" v-model="password" :disabled="disableLogin"/>
          </span>
        </div>
        <div v-if="!loggedin" class="modal-footer">
          <button type="button" class="btn btn-primary" :disabled="disableLogin" @click="login()">
            <span v-if="disableLogin" class="spinner-border" role="status">
              <span class="visually-hidden">Loading...</span>
            </span>
            <span v-else>Login</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>