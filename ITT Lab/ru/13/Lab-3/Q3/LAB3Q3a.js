var phone = document.getElementById("LAB3Q3a").value;
function get()
{
    var phoneno=document.getElementById("LAB3Q3a").value;
    var a=phoneno.split(" ");
    var areacode = a[0].substring(1,a[0].length-1);
    var phon = a[1]+a[2];
    document.getElementById("area-code").value = areacode;
    document.getElementById("phone-no").value = phon;
}