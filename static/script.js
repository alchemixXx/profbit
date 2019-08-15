$('#myForm').submit(function(){
    $('.message').show();
    event.preventDefault(); // if you want to send data only, do not reload page.
});
