<template>
  <q-layout view="hHh Lpr fFf">
    <q-header elevated class="bg-primary text-white" height-hint="98">
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg">
          </q-avatar>
          FindMe
        </q-toolbar-title>

        <q-btn dense flat round icon="menu" @click="toggleRightDrawer" />
      </q-toolbar>

      <q-tabs align="center">
        <q-route-tab to="/" label="Home" />
        <q-route-tab to="/about" label="My Circle" />
        <q-route-tab to="/about" label="Post" />
        <q-route-tab to="/about" label="Notification" />
        <q-route-tab to="/about" label="Pitch" />
      </q-tabs>
    </q-header>

    <q-drawer v-model="rightDrawerOpen" side="right" behavior="mobile" elevated>
      <!-- drawer content -->
      <q-scroll-area class="fit">
          <q-list>
            <q-item clickable active="menuItem.label === 'Outbox'" v-ripple>
                <q-item-section avatar>
                  <q-icon name="menuItem.icon" />
                </q-item-section>
                <q-item-section>
                  dggdgd
                </q-item-section>
              </q-item>
              <q-separator/>
              <q-item clickable active="menuItem.label === 'Outbox'" v-ripple>
                <q-item-section avatar>
                  <q-icon name="menuItem.icon" />
                </q-item-section>
                <q-item-section>
                  dggdgd
                </q-item-section>
              </q-item>
              <q-separator/>
              <q-item clickable active="menuItem.label === 'Outbox'" v-ripple>
                <q-item-section avatar>
                  <q-icon name="menuItem.icon" />
                </q-item-section>
                <q-item-section>
                  dggdgd
                </q-item-section>
              </q-item>
              <q-separator/>
              <q-item clickable active="menuItem.label === 'Outbox'" v-ripple>
                <q-item-section avatar>
                  <q-icon name="menuItem.icon" />
                </q-item-section>
                <q-item-section>
                  dggdgd
                </q-item-section>
              </q-item>
              <q-separator/>
              <q-item clickable active="menuItem.label === 'Outbox'" v-ripple>
                <q-item-section avatar>
                  <q-icon name="menuItem.icon" />
                </q-item-section>
                <q-item-section>
                  dggdgd
                </q-item-section>
              </q-item>
              <q-separator/>
              <q-item clickable active="menuItem.label === 'Outbox'" v-ripple>
                <q-item-section avatar>
                  <q-icon name="menuItem.icon" />
                </q-item-section>
                <q-item-section>
                  dggdgd
                </q-item-section>
              </q-item>
              <q-separator/>
          </q-list>
        </q-scroll-area>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

  </q-layout>
</template>

<script>
import { ref } from 'vue'

export default {
  setup () {
    const rightDrawerOpen = ref(false)

    return {
      rightDrawerOpen,
      toggleRightDrawer () {
        rightDrawerOpen.value = !rightDrawerOpen.value
      }
    }
  }
}
</script>