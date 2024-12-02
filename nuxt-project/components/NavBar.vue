<script setup>
  const user = useUserStore()
</script>

<template>
  <nav class="navbar fixed-top bg-success">
		<div class="container">
      <NuxtLink to="/" class="h2 text-decoration-none">Snippets</NuxtLink>
      <NuxtLink to="/about" class="text-black text-decoration-none">About1</NuxtLink>
      <NuxtLink to="/about" class="text-black text-decoration-none">About2</NuxtLink>
      <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#loginModal">
        <span v-if="user.userInfo!=null">{{ user.userInfo.username }}</span>
        <span v-else>Login</span>
      </button>
    </div>
	</nav>
  <LoginDialog id="loginModal"/>
</template>