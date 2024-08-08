$(document).ready(() => {
  $('#btn_translate').click(() => {
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
  });
});
