function parsePhone() {
    const phoneInput = document.getElementById('phone');
    const areaCodeInput = document.getElementById('areaCode');
    const phoneNumberInput = document.getElementById('phoneNumber');
    
    const components = phoneInput.value.split(/[\(\)\-]/);
  
    const areaCode = components[1];
    const phoneNumber = components[2] + components[3];
  
    areaCodeInput.value = areaCode;
    phoneNumberInput.value = phoneNumber;
  }
  