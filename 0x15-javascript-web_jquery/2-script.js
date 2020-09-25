// Make the HEADER tag's text color to red via jQuery
// when the user clicks on that mofo DIV#red_header
const $ = window.$;
$('#red_header').click(function () {
$('header').css('color', '#FF0000');
});
