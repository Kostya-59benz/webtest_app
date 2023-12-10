$(document).ready(function(){
  $('.dropdown-item').click(function(){
    var selectedOption = $(this).text();
    $('#dropdownMenuButton').text(selectedOption);
    // Здесь можно добавить код для выполнения определенных действий при выборе опции
  });
});
