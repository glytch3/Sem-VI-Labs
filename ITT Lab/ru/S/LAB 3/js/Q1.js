var size=5;
f=0;
var t1="Text-Growing";
var t2="Text-Shrinking";
function f1()
{
    if(size==50)
    {
        f=1;
        document.getElementById("text").innerHTML=t2;
    }
    else if(size==5)
    {
        f=0;
        document.getElementById("text").innerHTML=t1;
    }
    if(f==0)
    {
        document.getElementById("text").setAttribute("style","font-size:"+size+"pt; color:red;");
        size+=5;  
    }
    else if(f==1)
    {
        document.getElementById("text").setAttribute("style","font-size:"+size+"pt; color:blue;");
        size-=5;
    }
    setTimeout(f1,100);
}