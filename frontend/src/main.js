import { createApp, provide, h } from 'vue';
import { createPinia } from 'pinia';

import { ApolloClient, createHttpLink, InMemoryCache } from '@apollo/client/core'
import { DefaultApolloClient } from '@vue/apollo-composable'

import App from './App.vue'
import router from './router'
import { Quasar } from 'quasar'
// Import icon libraries
import '@quasar/extras/material-icons/material-icons.css'

// Import Quasar css
import 'quasar/src/css/index.sass'

const httpLink = createHttpLink({
    uri: "http://127.0.0.1:8000/graphql"
})

const cache = new InMemoryCache()

const apolloClient = new ApolloClient({
    link: httpLink,
    cache,
})



const app = createApp({
    setup () {
    provide(DefaultApolloClient, apolloClient)
  },
  render: () => h(App),
})

app.use(createPinia())
app.use(Quasar, {
  plugins: {}, // import Quasar plugins and add here
})
app.use(router)
app.mount('#app')