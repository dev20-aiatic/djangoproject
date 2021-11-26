//Text Count

document.addEventListener("DOMContentLoaded", function () {

    document.getElementById('id_message').onkeyup = function () {
        document.getElementById('count').innerHTML = "Carácteres restantes: " + (500 - this.value.length);
    };

});
