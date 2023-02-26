var fontSize = 5;
var inc = 5;
var color = "red";
var text = "TEXT-GROWING";
var f=0;

function modify(color, size, text)
{
    document.getElementById("LAB3Q1a").style.color = color;
    document.getElementById("LAB3Q1a").textContent = text;
    document.getElementById("LAB3Q1a").style.fontSize = size;
}

function update(){
    modify(color, fontSize.toString()+"pt", text);
    if(f==1)
    {
        color = "blue";
        text = "TEXT-SHRINKING";
        fontSize -= inc;
    }
    else if(f==0)
    {
        color = "red";
        text = "TEXT-GROWING";
        fontSize += inc;
    }
    if(fontSize == 50)
    {
        f=1;
    }
    else if(fontSize == 5)
    {
        f=0;
    }
}

setInterval(update, 100);
