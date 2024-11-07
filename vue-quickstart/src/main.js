import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)

app.config.errorHandler = (err) => {
    /* handle error */
}

// Make sure to apply all app configurations before mounting the app!
app.mount('#app')
