import { defineStore } from 'pinia';

export const useAuthStore = defineStore({
  id: 'auth',
  state: () => ({
    user: null,
    isAuthenticated: false,
  }),
  actions: {
    login(user) {
      // Perform authentication logic here
      this.user = user;
      this.isAuthenticated = true;
    },
    logout() {
      // Perform logout logic here
      this.user = null;
      this.isAuthenticated = false;
    },
  },
});
