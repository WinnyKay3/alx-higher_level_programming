// use jQuery to add click event handler to div with id toggle_header
$('#toggle_header').click(function() {
  // toggle the red and green classes of header when div is clicked
  $('header').toggleClass('red green');
});
