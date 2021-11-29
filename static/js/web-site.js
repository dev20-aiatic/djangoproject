//Text Count

document.addEventListener("DOMContentLoaded", function () {

    document.getElementById('id_message').onkeyup = function () {
        document.getElementById('count').innerHTML = "Carácteres restantes: " + (500 - this.value.length);
    };

});


//Loading button
$(document).ready(function(){
$("#loadingbutton").click(function(){
var r= $('<i class="fa fa-spinner fa-spin"></i>');
$("#loadingbutton").html(r);
$("#loadingbutton").append("Enviando...");
$("#loadingbutton").attr("disabled", true);


setTimeout(function(){
$("#loadingbutton").attr("disabled", false);
$("#loadingbutton").html('Enviado');

}, 3000);


});
});


$('.toast').toast('show');