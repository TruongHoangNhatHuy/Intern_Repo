<script setup>
  import { ref } from 'vue';

  const books = ref([
    'Vue 2 - Advanced Guide',
    'Vue 3 - Basic Guide',
    'Vue 4 - The Mystery'
  ])

  function addBook() {
    const book = document.getElementById('text-newBook').value
    books.value.push(book)
  }
</script>

<template>
  <main>
    <h1>6. List Rendering</h1>
    <input type="text" id="text-newBook" placeholder="New Book">
    <button @click="addBook">Add</button>
    <ul v-for="(book, index) in books">
      <li :key="index">{{ book }}</li>
    </ul>
  </main>
</template>