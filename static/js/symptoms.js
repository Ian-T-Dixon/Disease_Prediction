function init() {
  // Grab a reference to the symptom list
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
        .property("value", "True")    // defaults to 'on'
        .property("id", symptom)      // symptom
        .property("name", symptom)    // key
      selector
        .append("label")
        .property("for", symptom)     // must match 'id'
        .text(symptom)
    });
  });
};

// Initialize the dashboard
init();

// Function to clear all checkboxes
// Called when "Clear All" button pressed