
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

function myFunction(x) {
  x.classList.toggle("fa-thumbs-down");
  x.preventDefault();
}