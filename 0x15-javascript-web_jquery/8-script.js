$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  method: 'GET',
  success: (data) => {
    const movies = data.results;
    const $list = $('#list_movies');

    movies.forEach((movie) => {
      const $li = $('<li></li>').text(movie.title);
      $list.append($li);
    });
  },
  error: (error) => {
    console.error('Error fetching data:', error);
  }
});
