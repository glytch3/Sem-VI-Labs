function find(){
    let entered = document.getElementById("entry").value;
    let areaval = entered.substr(1,3)
    let phoneval = entered.substr(5,12)
    let area = document.getElementById("area")
    let phone = document.getElementById("phone")
    area.textContent = areaval;
    phone.textContent = phoneval;
}