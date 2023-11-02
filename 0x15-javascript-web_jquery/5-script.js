// use jquery to add a click event handler to div with id add item
$('DIV#add_item').click(function() {
  // append the new item to the ul with class 'my_list'
  $('ul.my_list').append('<li>Item</li>');
});
