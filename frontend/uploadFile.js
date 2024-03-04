const axios = require('axios');

// Sample data to send in the POST request
const formData = {
  name: 'John Doe',
  email: 'johndoe@example.com'
};

axios.post('http://localhost:3000/upload', formData)
  .then(response => {
    console.log('Upload successful', response.data);
  })
  .catch(error => {
    console.error('Error uploading file', error);
  });
