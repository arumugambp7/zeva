
function m_over(x) {
  x.style.opacity="0.8";
  x.style.cursor="pointer";  
  x.style.border="15px solid pink";
  // x.style.borderRadius="100%";
   
}

function m_out(x) {
  x.style.opacity="1";
  x.style.border="none";   
}

// Get the modal
var modal = document.getElementById("myModal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById("myImg");
var modalImg = document.getElementById("img01");

img.onclick = function(){
  modal.style.display = "block";
  modalImg.src = this.src;

}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}




