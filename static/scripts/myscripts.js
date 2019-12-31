$(document).ready(function() {
    $('#list').on('click', function() {
        console.log("List")
        $('#products .item').addClass('list-group-item');
    });
    $('#grid').on('click', function() {
        console.log("grid")
        $('#products .item').removeClass('list-group-item');
        $('#products .item').addClass('grid-group-item');
    });
});