function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#symptomList");

  // Use the list of sample names to populate the select options
  d3.json("./static/data/symptoms.json").then((data) => {
    var symptomNames = data.ID;
    // console.log(symptomNames);

    Array.from(symptomNames).forEach((symptom) => {
      console.log(symptom)
      selector
      .append("option")
      .text(symptom)
      .property("value", symptom);
  });
  })
};

// Initialize the dashboard
init();
