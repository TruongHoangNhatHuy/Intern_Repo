	<script setup>
		import { reactive, computed } from 'vue'

		const author = reactive({
			firstName: 'John',
			lastName: 'Doe',
			books: [
				'Vue 2 - Advanced Guide',
				'Vue 3 - Basic Guide',
				'Vue 4 - The Mystery'
			]
		})
		// Computed Properties:
		const hasPublishedBooks = computed(() => {
			return author.books.length > 0 ? 'Yes' : 'No'
		})
		// Writable Computed
		const fullName = computed({
			get() { // getter
				return author.firstName + ' ' + author.lastName
			},
			set(newValue) { // setter
				[author.firstName, author.lastName] = newValue.split(' ')
			}
		})
		function changeName() {
			const firstName = document.getElementById("text-firstName").value
			const lastName = document.getElementById("text-lastName").value
			fullName.value = firstName + " " + lastName
		}
	</script>

	<template>
		<main>
			<h1>3. Computed Properties</h1>
			<p>{{ fullName }} has published books: {{ hasPublishedBooks }}</p>
			<p>Change Name: 
				<input type="text" id="text-firstName" placeholder="first name" :value="author.firstName">
				<input type="text" id="text-lastName" placeholder="last name" :value="author.lastName">
				<button @click="changeName">Change</button>
			</p>
		</main>
	</template>