import { createApp, provide, h } from 'vue';
import { createPinia } from 'pinia';
import { ApolloClient, createHttpLink, InMemoryCache } from '@apollo/client/core'
import { DefaultApolloClient } from '@vue/apollo-composable'

import { Quasar, Notify } from 'quasar'
import App from './App.vue'
import router from './router'
import '@quasar/extras/material-icons/material-icons.css'
import 'quasar/src/css/index.sass'

const httpLink = createHttpLink({
    uri: "http://127.0.0.1:8000/graphql"
})

const cache = new InMemoryCache()

const apolloClient = new ApolloClient({
    link: httpLink,
    cache: cache,
})
const app = createApp(App);
app.provide(DefaultApolloClient, apolloClient);

app.use(createPinia())
app.use(Quasar, {
  plugins: {
    Notify
  },
  config: {
    //notify: /* look at QuasarConfOptions from the API card */
  }
})
app.use(router)
app.mount('#app')