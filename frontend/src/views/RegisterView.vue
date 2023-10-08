<template>
	<div class="q-pa-md row justify-center" style="height:80vh; align-items: center;">
		<div class="col-10 col-md-6 col-lg-4">
			<q-form
				@submit="register"
				class="q-gutter-md"
			>
			<div class="row">
				<div class="col-md-6 col-sm-10 col-xs-12">
				<q-input
				filled
				v-model="firstName"
				label="Your First Name *"
				hint="First Name"
				lazy-rules
				:rules="[ val => val && val.length > 0 || 'Please type something']"
				/>
			</div>
			<div class="col-md-6 col-sm-10 col-xs-12">
				<q-input
				filled
				v-model="lastName"
				label="Your Surname *"
				hint="lastName"
				lazy-rules
				:rules="[ val => val && val.length > 0 || 'Please type something']"
				/>
			</div>
			</div>
			<div class="row">
				<div class="col-md-6 col-sm-10 col-xs-12">
					<q-input
				filled
				v-model="username"
				label="Your Username *"
				hint="Enter a Valid Username"
				lazy-rules
				:rules="[ val => val && val.length > 0 || 'Please type something']"
				/>
				
				</div>
				<div class="col-md-6 col-sm-10 col-xs-12">
					<q-input
						filled
						type="email"
						v-model="email"
						label="Your Email *"
						hint="Enter a valid email"
						lazy-rules
						/>
		
				</div>
				
			</div>
			<div class="row">
					<div class="col-md-6 col-sm-10 col-xs-12">
						<q-input
							filled
							type="password"
							v-model="password"
							label="Password *"
							lazy-rules
							:rules="[
								val => val !== null && val !== '' || 'Please type your age',
								]"
							/>
					</div>
					<div class="col-md-6 col-sm-10 col-xs-12">

						<q-input
						filled
						type="password"
						v-model="password1"
						label="Confirm Password *"
						lazy-rules
								:rules="[
									val => val !== null && val !== '' || 'Please type your age',
									]"
						/>
					</div>
				</div>
			<div class="row" style="justify-content: space-between;">

				
				<div class="col-8">
					<q-toggle v-model="accept" label="I accept the license and terms" />
				</div>
				
				<div class="col-4 right">
				<q-btn label="Submit" type="submit" color="primary" class="right"/>
				</div>
			</div>
				
				
			</q-form>
  
		</div>
	  
	</div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import gql from "graphql-tag";
  import { useQuasar } from 'quasar'
  import { useMutation, useApolloClient } from "@vue/apollo-composable";
  import { useAuthStore } from '@/stores/auth';

  const REGISTER_MUTATION = gql`
		mutation registerUser($email: String!, $firstName: String, $lastName: String, $password: String!, $username: String!){
			registerUser(
				email:$email,
				username: $username, 
				password: $password, 
				firstName: $firstName, 
				lastName:$lastName
			){
				success
				user{
					username
					firstName
					lastName
					id
					email
				}
			}
		}`;
  
export default {
  setup() {
	const $q = useQuasar();
    const username = ref('');
	const email = ref("");
	const firstName = ref("");
	const lastName = ref("");
    const password = ref('');
    const { mutate: signupMutation } = useMutation(REGISTER_MUTATION);
	const user = useAuthStore();
	console.log(user.isAuthenticated)
    const register = async () => {
      try {
        const { data } = await signupMutation({
          username: username.value,
		  email: email.value,
		  firstName: firstName.value,
		  lastName: lastName.value,
          password: password.value,
        });
		console.log(data)
        //const token = data.tokenAuth.token;
		$q.notify("Signup Successful")
        // Store the token or redirect the user as needed
      } catch (error) {
		console.log(JSON.stringify(error))
		$q.notify("signup failed")
      }
    };

    return { email,
			firstName,
			lastName,
			username, 
			password,
			register 
			};
  },
};
  </script>  