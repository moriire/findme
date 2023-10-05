<template>
	<div class="q-pa-md row justify-center" style=".max-width: 400px">
		<div class="col-10 col-md-4 col-lg-4">
			<q-form
				@submit="onSubmit"
				@reset="onReset"
				class="q-gutter-md"
			>
				<q-input
				filled
				v-model="name"
				label="Your Full Name *"
				hint="Name and surname"
				lazy-rules
				:rules="[ val => val && val.length > 0 || 'Please type something']"
				/>
				
				<q-input
				filled
				v-model="username"
				label="Your Username *"
				hint="Enter a Valid Username"
				lazy-rules
				:rules="[ val => val && val.length > 0 || 'Please type something']"
				/>
				
				<q-input
				filled
				type="email"
				v-model="email"
				label="Your Email *"
				hint="Enter a valid email"
				lazy-rules
				/>
		
				
				<q-input
				filled
				type="date"
				v-model="dob"
				label="Your DOB *"
				lazy-rules
				:rules="[
					val => val !== null && val !== '' || 'Please type your age',
					val => val > 0 && val < 100 || 'Please type a real age'
				]"
				/>
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
				<q-input
				filled
				type="password"
				v-model="password"
				label="Confirm Password *"
				
				/>
				<q-toggle v-model="accept" label="I accept the license and terms" />
		
				<div>
				<q-btn label="Submit" type="submit" color="primary"/>
				<q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm" />
				</div>
			</q-form>
  
		</div>
	  
	</div>
  </template>
  
  <script>
  import { useQuasar } from 'quasar'
  import { ref } from 'vue'
  
  export default {
	setup () {
	  const $q = useQuasar()
  
	  const name = ref(null)
	  const age = ref(null)
	  const accept = ref(false)
  
	  return {
		name,
		age,
		accept,
  
		onSubmit () {
		  if (accept.value !== true) {
			$q.notify({
			  color: 'red-5',
			  textColor: 'white',
			  icon: 'warning',
			  message: 'You need to accept the license and terms first'
			})
		  }
		  else {
			$q.notify({
			  color: 'green-4',
			  textColor: 'white',
			  icon: 'cloud_done',
			  message: 'Submitted'
			})
		  }
		},
  
		onReset () {
		  name.value = null
		  age.value = null
		  accept.value = false
		}
	  }
	}
  }
  </script>  