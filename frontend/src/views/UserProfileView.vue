<script>
import gql from "graphql-tag";
import { useQuery } from "@vue/apollo-composable";
import { useRoute } from 'vue-router'

const USER_QUERY = gql`
				query {
					bioByUsername(username: "username"){
						user{
						username
						lastName
						firstName
						isActive
						id
						}
						img
						body
					}
					}`;
export default {
  name: 'UserProfileView',
  setup() {
    const route = useRoute();
	const { result, loading, error  } = useQuery(USER_QUERY, {
  variables: { username: route.params.user_id },
});
console.log(error.networkError);
console.log(JSON.stringify(error))//, null, 2));
/*
    const { result, loading, error } = useQuery(USER_QUERY, {
        variables: {
            username: route.params.user_id
        }
    });*/
	return {
      route,
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

	{{ route.params.user_id }}
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
	  <q-list bordered >
		<q-separator />
		<q-item clickable v-ripple>
			
		  <q-item-section thumbnail >

			<img src="https://cdn.quasar.dev/img/mountains.jpg" class="showcase">
		  </q-item-section>
		  <q-item-section class="align-start">
			<div class="column">
				<h3>
					{{ error }}
				</h3>
				<p>{{ result }}</p>
			</div>
			
		</q-item-section>
		</q-item>
	  </q-list>
	</div>
	</div>
  </template>