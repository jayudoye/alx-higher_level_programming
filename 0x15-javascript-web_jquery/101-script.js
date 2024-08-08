$(document).ready(() => {
  $('#add_item').click(() => {
    $('<li>Item</li>').appendTo('.my_list');
  });

  $('#remove_item').click(() => {
    $('.my_list li:last-child').remove();
  });

  $('#clear_list').click(() => {
    $('.my_list').empty();
  });
});
