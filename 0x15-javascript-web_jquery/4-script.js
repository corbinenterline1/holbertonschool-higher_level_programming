// toggle_header must have a red or green class, toggled by user clicky
const $ = window.$;
$('#toggle_header').click(function () {
$('header').toggleClass('green red');
});
