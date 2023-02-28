var size = 30;
var increasing = true;

function handleText()
{
    var text = document.getElementById("text")
    if(size >= 50 || size <= 5)
    {
        if(increasing)
        {
            increasing = false
            document.getElementById("text").style.color = "blue";
            text.innerHTML = "TEXT SHRINKING"
        }
        else
        {
            increasing = true
            document.getElementById("text").style.color = "blue";
            text.innerHTML = "TEXT GROWING"
        }
            
    }
    if(increasing)
        size+=1;
    else
        size-=1;
    
    text.style.fontSize = size; 
}
setInterval(handleText,100)