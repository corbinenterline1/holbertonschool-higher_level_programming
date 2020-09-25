// Adds class red to the HEADER tag when the user clicks on
// DIV#red_header, using jQuery
const $ = window.$;
$('#red_header').click(function () {
$('header').addClass('red');
});
