<script setup>
  const user = useUserStore()
</script>

<template>
  <nav class="navbar bg-success">
		<div class="container">
      <NuxtLink to="/" class="h2">Snippets</NuxtLink>
      <NuxtLink to="/about">About1</NuxtLink>
      <NuxtLink to="/about">About2</NuxtLink>
      <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#loginModal">
        <span v-if="user.userInfo!=null">{{ user.userInfo.username }}</span>
        <span v-else>Login</span>
      </button>
    </div>
	</nav>
  <LoginDialog id="loginModal"/>
</template>