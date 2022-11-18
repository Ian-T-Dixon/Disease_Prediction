function init() {
  // Grab a reference to the symtpom list
  var selector = d3.select("#symptomList");

  // Use the list of symptoms to populate the list of checkboxes
  d3.json("../static/data/symptoms.json").then((data) => {
    var symptomNames = data.ID;
    symptomArray = Object.values(symptomNames);

    symptomArray.forEach(symptom => {
      selector
        .append("h6")
      selector
        .append("input")
        .property("type", "checkbox")
        .property("value", symptom)
        .property("id", symptom)
        .property("name", "symptom")
      selector
        .append("label")
        .property("for", symptom)
        .text(symptom)
    });
  });
};



// Initialize the dashboard
init();

// Create the output array from SymptomList
function createSymptomArray() {
  var checkboxes = document.getElementById("symptomList");
  var outputArray = []
  var outputDict = {}
  
  // Loop through checkboxes and create a dictionary with true/false values.
  for (var i = 0; i < checkboxes.length; i++) {
    var checkbox = checkboxes[i];
    if (checkbox.checked) {
      outputDict[checkbox.value] = true
  }
    else {
      outputDict[checkbox.value] = false
    }
  }
    delete outputDict.Submit
    console.log(outputDict)
// sends json filetype to flask
    fetch('/predict', {
      headers : {
          'Content-Type' : 'application/json'
      },
      method : 'POST',
      body : JSON.stringify(outputDict)
  })
  .then(function (response){

      if(response.ok) {
          response.json()
          .then(function(response) {
              console.log(response);
          });
      }
      else {
          throw Error('Something went wrong');
      }
  })
  .catch(function(error) {
      console.log(error);
  });
}
  //// working code for creating an array with true/flse values.  
  // for (var i = 0; i < checkboxes.length; i++) {
  //   var checkbox = checkboxes[i];
  //   if (checkbox.checked) {
  //     outputArray.push(true);
  // }
  //   else {
  //     outputArray.push(false);
  //   }
  // }
  // for (var g = 0; g < outputArray.length; g++) {
  //   var symptom = outputArray[g];
  //   outputDict[symptom] = g
  // }
// console.log(outputArray)
