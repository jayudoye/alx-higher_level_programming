$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  method: 'GET',
  success: (data) => {
    $('#character').text(data.name);
  },
  error: (error) => {
    console.error('Error fetching data:', error);
  }
});
