// script that adds a <li> element to a list when the user clicks DIV#add_item
$('div#add_item').click(function () {
  const element = '<li>Item</li>';
  $('ul.my_list').append(element);
});
