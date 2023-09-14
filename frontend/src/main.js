import './assets/lib/animate/animate.min.css'
import './assets/lib/owlcarousel/assets/owl.carousel.min.css'
import './assets/lib/lightbox/css/lightbox.min.css'
import './assets/css/bootstrap.min.css'
import './assets/css/style.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
