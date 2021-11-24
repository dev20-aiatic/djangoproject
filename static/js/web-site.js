
//Alert Messages' FadeOut

window.setTimeout(function() {
    $(".alert-dismissible").fadeTo(500, 0).slideUp(500, function(){
        $(this).remove();
    });
}, 5000);



//Message Count

document.addEventListener("DOMContentLoaded", function() {

document.getElementById('msg').onkeyup = function () {
document.getElementById('count').innerHTML = "Carácteres restantes: " + (500 - this.value.length);
};

});