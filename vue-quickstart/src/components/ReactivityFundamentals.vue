<script setup>
	import { ref, reactive } from 'vue'

	const count = ref(0)
	function increment() {
		count.value++
	}

	const obj = ref({
		nested: { count: 0 },
		arr: ['foo', 'bar']
	})
	function mutateDeeply() {
		obj.value.nested.count++
		obj.value.arr.push('baz')
	}
	function objReset() {
		obj.value = {
			nested: { count: 0 },
			arr: ['foo', 'bar']
		}
	}

	const state = reactive({ count: 0 })
</script>

<template>
	<main>
		<h1>2. Reactivity Fundamentals</h1>
		<!-- Reactive State -->
		<div>
			<button @click="increment">Clicked: {{ count }}</button>
			<button @click="count--">Decrement</button>
			<button @click="count=0">Reset</button>
		</div>
		<!-- Deep Reactivity -->
		<div>
			<button @click="mutateDeeply">Deep Reactivity</button>
			<button @click="objReset">Reset</button>
			<p>obj.value.nested.count = {{ obj.nested.count }}</p>
			<p>obj.value.arr = {{ obj.arr }}</p>
		</div>
		<!-- reactive() -->
		<div>
			<button @click="state.count++">{{ state.count%2 ? 'State.count is odd' : 'State.count is even' }}</button>
			{{ state.count }}
		</div>
	</main>
</template>