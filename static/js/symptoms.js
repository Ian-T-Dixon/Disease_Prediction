function init() {
  // Grab a reference to the symptom list checkbox form
  var selector = d3.select("#symptomList");

  // Use the list of symptoms to populate the list of checkboxes
  d3.json("./static/data/symptoms.json").then((data) => {
    symptomArray = Object.values(data);
    symptomArray.forEach(symptom => {
      selector
        .append("h6")
      selector
        .append("input")
        .property("type", "checkbox")
        .property("className", "symp_box")
        .property("value", "True")
        .property("id", symptom)
        .property("name", symptom)
      selector
        .append("label")
        .property("for", symptom)
        .text(symptom)
    });
  });
};

// Function to clear all checkboxes
// Called when "Clear All" button pressed

// Initialize the dashboard
init();