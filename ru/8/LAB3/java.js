var size = 25;
var increasing = true;

function handleText(){
var text = document.getElementById("text")
if(size >= 50 || size <= 0){
if(increasing) {
 increasing = false 
  text.innerHTML = "TEXT-SHRINKING"
text.style.color="blue" }
 else{
 increasing = true
 text.innerHTML = "TEXT-GROWING"
 text.style.color="red"} } 
  if(increasing)
  size+=0.1;
  else
  size-=0.1;
 text.style.fontSize = size;}
setInterval(handleText,100)