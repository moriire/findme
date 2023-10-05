<template>
	<div class="q-pa-md row justify-center align-center" style=".max-width: 400px">
		<div class="col-10 col-md-4 col-lg-4">
		
			<q-form
				class="q-gutter-md"
				@submit.prevent="login()"
			>
				<q-input
				v-model="username"
				label="Your Username *"
				hint="Enter a Valid Username"
				lazy-rules
				:rules="[ val => val && val.length > 0 || 'Please type something']"
				/>
			
				<q-input
				filled
				type="password"
				v-model="password"
				label="Your Password *"
				lazy-rules
				:rules="[ val => val && val.length > 0 || 'Please type something']"				
				/>
				<div>
				<q-btn label="Login" type="submit" color="primary" class="center"/>
				</div>
			</q-form>
			
		</div>
	</div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import gql from "graphql-tag";
  import { useMutation, useApolloClient } from "@vue/apollo-composable";
  import { useAuthStore } from '@/stores/auth';

  const LOGIN_MUTATION = gql`
			mutation tokenAuth($username: String!, $password: String!){
				tokenAuth(username: $username, password: $password){
					payload
					token
					refreshExpiresIn
				}
			}`;

export default {
  setup() {
    const username = ref('');
    const password = ref('');
    const { mutate: loginMutation } = useMutation(LOGIN_MUTATION);
	const user = useAuthStore();
	console.log(user.isAuthenticated)
    const login = async () => {
      try {
        const { data } = await loginMutation({
          username: username.value,
          password: password.value,
        });
		console.log(data.tokenAuth.token)
        const token = data.tokenAuth.token;
        // Store the token or redirect the user as needed
      } catch (error) {
        alert('Login failed:');
      }
    };

    return { username, password, login };
  },
};
  </script>  