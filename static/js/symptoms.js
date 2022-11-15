function init() {
  // Grab a reference to the symtpom list
  var selector = d3.select("#symptomList");

  // Use the list of symptoms to populate the list of checkboxes
  d3.json("./static/data/symptoms.json").then((data) => {
    var symptomNames = data.ID;
    symptomArray = Object.values(symptomNames);

    

    symptomArray.forEach(symptom => {
      selector
        .append("h6")
      selector
        .append("input")
        .property("type", "checkbox")
        .property("value", symptom)
        .property("id", symptom);
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
  for (var i = 0; i < checkboxes.length; i++) {
    var checkbox = checkboxes[i];
    if (checkbox.checked) {
      outputArray.push(1);
  }
    else {
      outputArray.push(0);
    }
  }
  console.log(outputArray);
}