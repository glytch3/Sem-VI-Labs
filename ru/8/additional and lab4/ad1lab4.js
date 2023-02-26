const paragraph = document.getElementById("my-paragraph");

paragraph.addEventListener("mouseover", function() {
  paragraph.style.fontSize = "20px";
});

paragraph.addEventListener("mouseout", function() {
  paragraph.style.fontSize = "16px";
});
