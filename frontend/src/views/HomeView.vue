<script>
import gql from "graphql-tag";
import { useQuery } from "@vue/apollo-composable";

const USERS_QUERY = gql`query {
	allBios {
		body
		user{
			id
        	username
			firstName
			lastName
		}
    }
  }`;
export default {
  name: 'HomeView',
  setup () {
    const { result, loading, error } = useQuery(USERS_QUERY);
    //console.log(result)
	return {
      result,
      loading, 
      error
    }
  }
}
</script>

<template>
<div class="q-pa-md row justify-center">
	<div class="col-lg-8 col-md-10">
{{ result }}
	
	<q-circular-progress
			
			font-size="12px"
			v-if="loading"
			size="50px"
			:thickness="0.22"
			color="teal"
			track-color="grey-3"
			class="q-ma-md"
			>
      loading...
    </q-circular-progress>
	  <q-list bordered v-else>
		<q-separator />
		<q-item clickable v-ripple v-for="user in result.allBios">
			
		  <q-item-section thumbnail >

			<img src="https://cdn.quasar.dev/img/mountains.jpg" class="showcase">
		  </q-item-section>
		  <q-item-section class="align-start">
			<div class="column">
				<h3>
					{{ user.user.username }}
				</h3>
				<p>{{ user.body }}</p>
				<router-link :to="{'name': 'profile', 'params': {'user_id':`${user.user.username}`}}">view</router-link>
			</div>
			
		</q-item-section>
		</q-item>
	  </q-list>
	</div>
	</div>
  </template>
  <style scoped>
  img.showcase{
			width: 150px;
			height: 150px;
		}

		@media only screen and (min-width: 500px) {
		img.showcase{
			width: 800px;
			height: 200px;
		}
	}
	@media only screen and (min-width: 820px) {
		img.showcase{
			width: 300px;
			height: 300px;
		}
	}
</style>