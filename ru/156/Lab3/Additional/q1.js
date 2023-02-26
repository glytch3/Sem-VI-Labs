
let customerArray = [];
function calculateCharges() {
  let hours = document.getElementById("hours").value;
  let charge;
  if (hours <= 3) {
    charge = 2.00;
  } else {
    charge = 2.00 + (hours - 3) * 0.50;
  }
  let result = document.getElementById("result");
  result.innerHTML = "The parking charge is Rs. " + charge.toFixed(2);
  customerArray.push({ hours: hours, charge: charge });
  displayCustomerList();
}
function displayCustomerList() {
  let customerList = document.getElementById("customerList");
  customerList.innerHTML = "";
  customerArray.forEach(function(customer) {
    let item = document.createElement("li");
    item.innerHTML = "Hours parked: " + customer.hours + ", Charge: Rs. " + customer.charge.toFixed(2);
    customerList.appendChild(item);
  });
}
