<script setup>
  import { ref } from 'vue';

  const name = ref('Vue.js')

  function greet(e) {
    alert(`Greeting ${e.target.value}`)
  }
</script>

<template>
  <main>
    <h1>7. Event Handling</h1>
    <input type="text" placeholder="Type & hit Enter" @keyup.enter="greet" />
    <div/>
    <input type="text" placeholder="Type & hit Alt + Enter" @keydown.alt.enter="greet" />
    <div/>
    <input type="text" placeholder="Type & hit Alt + Ctrl + Enter" @keydown.alt.ctrl.enter="greet" />
    <table>
      <tr>
        <td>Event Modifiers</td>
        <td><pre>
          .stop 
          .prevent
          .self
          .capture
          .once
          .passive
        </pre></td>
      </tr>
      <tr>
        <td>Key Modifiers Aliases</td>
        <td><pre>
          .enter
          .tab
          .delete (both "Delete" and "Backspace" keys)
          .esc
          .space
          .up
          .down
          .left
          .right
        </pre></td>
      </tr>
      <tr>
        <td>System Modifier Keys</td>
        <td><pre>
          .ctrl
          .alt
          .shift
          .meta
        </pre></td>
      </tr>
      <tr>
        <td>Mouse Button Modifiers</td>
        <td><pre>
          .left
          .right
          .middle
        </pre></td>
      </tr>
    </table>
  </main>
</template>