# Changes to Original Dataset

<!-- The following is to document changes we made to the original dataset: -->

The names of diseases and symptoms will be altered in all four .csv files.

These replacements can be done using Pandas or SQL query.

Changes to Symptoms:

* Symptom "scurring" -> "scarring"
* Symptom "diarrhoea" -> "diarrhea"
* Symptom "cold_hands_and_feets" -> "cold_hands_and_feet"
* Symptom "swollen_extremeties" -> "swollen_extremities"
* Symptom "foul_smell_ofurine" -> "foul_smell_of_urine"
* Symptom "altered_sensorium" -> "altered mental state"
* Symptom "dischromic_patches" -> "mottling skin"
* Symptom "polyuria" -> "excessive_urination"
* Symptom "silver like dusting" -> "blue-gray complexion (argyria)"
* Symptom "pus_filled_pimples" -> "pus-filled_pimples"

* Symptom "toxic_look_(typhos)" needs interpretation
* Symptom "yellow_crust_ooze" probably means "pus"
* Symptom "mucoid_sputum" probably means "clear_phlegm" if it doesn't coincide with "rusty_sputum" and "blood_in_sputum"
* Symptom "rusty_sputum" should also be checked for coincidence with "blood_in_sputum"

* Symptom "fluid_overload" was originally duplicated. The severity weights for the duplicates were averaged together.
* Symptom "prognosis" was removed (not a symptom, does not appear in dataset).

* For all symptoms, replace "_" with whitespace " ".

Changes to Diseases:

* "Dimorphic hemorrhoids(piles)" -> "Hemorrhoids"
* "Bronchial Asthma" -> "Bronchial asthma"
* "Common Cold" -> "Common cold"
* "hepatitis A" -> "Hepatitis A"
* "Drug Reaction" -> "Drug reaction"

* "Paralysis (brain hemorrhage)" is probably just "Brain hemorrhage"
* "(vertigo) Paroymsal  Positional Vertigo" -> "Vertigo"?

* Any disease that isn't an acronym (GERD, AIDS) should be lower case.

* Added missing quotation marks to disease descriptions.

Disease precautions also needs some reinterpretation.