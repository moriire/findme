<template>
    <div>
      <input type="file" @change="handleFileUpload" accept="image/*" />
      <button @click="uploadImage">Upload Image</button>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import { useMutation } from '@vue/apollo-composable';
  import gql from 'graphql-tag';
  //import UPLOAD_IMAGE_MUTATION from '@/graph/uploadImageMutation.graphql';

  export default {
    setup() {
      const username = ref("");
      const img = ref(null);
      const { mutate } = useMutation(
        //UPLOAD_IMAGE_MUTATION
        gql`
      mutation ($user: ID!, $img: Upload!){
        uploadImage(user:$user, img:$img){
          success
        }
      }
      `);
  
      const handleFileUpload = (event) => {
        img.value = event.target.files[0];
      };
  
      const uploadImage = async () => {
        if (img.value) {
          //console.log(event.target.files);
          //console.log(event.target.files[0]);
          console.log(img.value);
          try {
            const { data } = await mutate({ img: img.value, user:1 });
            console.log('Image uploaded:', data.uploadImage);
            // Handle success or redirect as needed
          } catch (error) {
            console.log('Error uploading image:', JSON.stringify(error));
            // Handle error
          }
        }
      };
  
      return {
        img,
        handleFileUpload,
        uploadImage,
      };
    },
  };
  </script>  