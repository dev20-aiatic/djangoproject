
//Alert Messages' FadeOut

window.setTimeout(function() {
    $(".alert-dismissible").fadeTo(500, 0).slideUp(500, function(){
        $(this).remove();
    });
}, 5000);

//Navbar
document.addEventListener("DOMContentLoaded", function(){
  // add padding top to show content behind navbar
  navbar_height = document.querySelector('.navbar').offsetHeight;
  document.body.style.paddingTop = navbar_height + 'px';
});


//Loading button
$(document).ready(function(){
$("#loginbutton").click(function(){
var r= $('<i class="fa fa-spinner fa-spin"></i>');
$("#loginbutton").html(r);
$("#loginbutton").append(" Iniciando sesión...");
$("#loginbutton").attr("disabled", true);

}, 3000);
});




//Picture Uploader
$("#profileImage").click(function(e) {
    $("#imageUpload").click();
});

function fasterPreview( uploader ) {
    if ( uploader.files && uploader.files[0] ){
          $('#profileImage').attr('src',
             window.URL.createObjectURL(uploader.files[0]) );
    }
}

$("#imageUpload").change(function(){
    fasterPreview( this );
});


$(document).on("change", "#id_profile_picture", function () {
  const triggerInput = this;
  const currentImg = $(this).closest(".pic-holder").find(".pic").attr("src");
  const holder = $(this).closest(".pic-holder");
  const wrapper = $(this).closest(".profile_picture_wrapper");
  $(wrapper).find('[role="alert"]').remove();
  const files = !!this.files ? this.files : [];
  if (!files.length || !window.FileReader) {
    return;
  }
  if (/^image/.test(files[0].type)) {
    // only image file
    const reader = new FileReader(); // instance of the FileReader
    reader.readAsDataURL(files[0]); // read the local file
      reader.onloadend = function () {
      $(holder).addClass("uploadInProgress");
      $(holder).find(".pic").attr("src", this.result);
      $(holder).append(
        '<div class="upload-loader"><div class="spinner-border text-primary" role="status"><span class="sr-only">Loading...</span></div></div>'
      );
      setTimeout(() => {
        $(holder).removeClass("uploadInProgress");
        $(holder).find(".upload-loader").remove();
        $(wrapper).append('<div class="snackbar show" role="alert"><i class="fa fa-check-circle text-success"></i> Imagen cargada correctamente</div>');
          setTimeout(() => {
            $(wrapper).find('[role="alert"]').remove();
          }, 3000);
      }, 1500);
    };
  } else {
    $(wrapper).append(
      '<div class="snackbar show" role="alert"><i class="fa fa-times-circle text-danger"></i> ¡Sólo se permiten archivos de imagen! </div>'
    );
    setTimeout(() => {
      $(wrapper).find('[role="alert"]').remove();
    }, 3000);
  }
});


