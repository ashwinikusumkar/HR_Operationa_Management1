// Js code for Accept all agreement

 function disableSubmit() {
  document.getElementById("signup").disabled = true;
 }

  function activateButton(element) {

      if(element.checked) {
        document.getElementById("signup").disabled = false;
       }
       else  {
        document.getElementById("signup").disabled = true;
      }

  }
