// var input = document.getElementById("comment");
// input.addEventListener("keyup", function(event) {
//   if (event.keyCode === 13) {
//    event.preventDefault();
//    document.getElementById("submit-comment").click();
//   }
// });

// $(document).ready(function() {
//   $(document).on('submit', '#my-form', function() {
//     // do your things
//     return false;
//    });
// });
document.getElementById('file').onchange = function () {
  var src = URL.createObjectURL(this.files[0])
  document.getElementById('prew').src = src
}
function submitOnEnter(event){
  if(event.which === 13){
      event.target.form.dispatchEvent(new Event("submit", {cancelable: true}));
      event.preventDefault();
  }
}

document.getElementById("comment").addEventListener("keypress", submitOnEnter);

// 
// Get the modal
var modal = document.getElementById("post_nuotrauka");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById("post_nuotrauka");
var modalImg = document.getElementById("post_nuotrauka");
var captionText = document.getElementById("caption");
img.onclick = function(){
  modal.style.display = "block";
  modalImg.src = this.src;
  captionText.innerHTML = this.alt;
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}