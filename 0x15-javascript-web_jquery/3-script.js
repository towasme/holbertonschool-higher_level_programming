// script that adds the class red to the HTML tag
$('#red_header').click(function () {
  $('header').add().addClass('red').css({ color: '#FF0000' });
});
