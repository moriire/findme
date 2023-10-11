import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegisterView from '../views/RegisterView.vue'
import LoginView from '../views/LoginView.vue'
import ProfileView from '../views/ProfileView.vue'
import EditProfileView from "../views/EditProfileView.vue"
import UserProfileView from "@/views/UserProfileView.vue"
import { useAuthStore } from '@/stores/auth';
import UploadView from "@/views/UploadView.vue";
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      //meta: { requiresAuth: true },
    },
    {
      path: '/me',
      name: 'myProfile',
      component: ProfileView,
      //meta: { requiresAuth: true },
    },
    {
      path: '/upload',
      name: 'image-upload',
      component: UploadView,
      //meta: { requiresAuth: true },
    },
    {
      path: '/:user_id/profile',
      name: 'profile',
      component: UserProfileView,
      //meta: { requiresAuth: true },
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },
    {
      path: '/:user_id/edit',
      name: 'edit-profile',
      component: EditProfileView,
      meta: { requiresAuth: true },
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !useAuthStore().isAuthenticated) {
    next('/login');
  } else {
    next();
  }
});
