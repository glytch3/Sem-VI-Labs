function find(){
    let entered = document.getElementById("entry").value;
    document.write("<table> <tr><td>Number</td><td>Square</td><td>Cube</td></tr>")
   for(let i=0;i<=entered;i++)
    {
        document.write("<tr><td>"+i+"</td><td>"+(i*i)+"</td><td>"+(i*i*i)+"</td></tr>")
    }
    document.write("</table>")
}