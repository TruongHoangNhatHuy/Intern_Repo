<!-- AlertBox.vue -->
<template>
  <div class="alert-box">
    <strong>This is an Error for Demo Purposes</strong>
    <br/>
    <slot />
  </div>
</template>

<style scoped>
.alert-box {
  color: darkgray;
  border: 2px solid red;
  border-radius: 10px;
  padding: 10px;
  margin: 10px;
  background-color: #242424;
}
  
strong {
	color: red;    
}
</style>