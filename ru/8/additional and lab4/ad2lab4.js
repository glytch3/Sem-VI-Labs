document.addEventListener('click', function(event) {
    let message = "A click event was triggered.";
  
    if (event.shiftKey) {
      message += " You held Shift during the click event.";
    }
  
    if (event.ctrlKey) {
      message += " The element that triggered the event was " + event.target.tagName;
    }
  
    alert(message);
  });
  