$(document).ready(() => {
  function fetchTranslation() {
    const languageCode = $('#language_code').val();
    if (languageCode) {
      const endPoint = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}/`;
      $.getJSON(endPoint, (data) => {
        $('#hello').text(data.hello);
      })
      .fail(() => {
        $('#hello').text('Error: Language code not found.');
      });
    }
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress((event) => {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});
