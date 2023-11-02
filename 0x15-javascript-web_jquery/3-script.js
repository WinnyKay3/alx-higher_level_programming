// User jQuery to add a click event handler to the div with id red_header
$('#red_header').click(function() {
  // add the red class to the header when the div is clicked
  $('header').clickClass('red');
});
