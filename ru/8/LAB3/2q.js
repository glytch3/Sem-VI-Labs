function print(){
    var tex=document.getElementById("latin").value;
    var res=tex.split(" ");
    var t="";
    for(var i=0; i<res.length; i++){
        var d=res[i][0];
       var s=res[i].substr(1,res[i].length-1);
       t+=s+d+"ay"+" ";
    }
   alert(t);
}