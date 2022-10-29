# Changes to Original Dataset

<!-- The following is to document changes we made to the original dataset: -->

The names of diseases and symptoms will be altered in all four .csv files.

These replacements can be done using Pandas or SQL query.

-> or future tense means replacement in /Data/ .csv's has not happened yet.
"changed to" or past tense means the replacement has been implemented.

Enforcing lower case ensures compatability with web app. It will be trivial to capitalize when served to the dashboard at the beginning of a sentence, using str.upper().

    str = str[0].upper() + str[1:]

Changes to Symptoms:

* Symptom "scurring" -> "scarring"
* Symptom "diarrhoea" -> "diarrhea"
* Symptom "cold_hands_and_feets" -> "cold_hands_and_feet"
* Symptom "swollen_extremeties" -> "swollen_extremities"
* Symptom "foul_smell_ofurine" -> "foul_smell_of_urine"
* Symptom "altered_sensorium" -> "altered mental state"
* Symptom "dischromic_patches" -> "mottling skin"
* Symptom "polyuria" -> "excessive_urination"
* Symptom "burning_micturition" -> "painful_urination"
* Symptom "silver like dusting" -> "blue-gray complexion (argyria)"
* Symptom "pus_filled_pimples" -> "pus-filled_pimples"

* Symptom "toxic_look_(typhos)" needs interpretation
* Symptom "yellow_crust_ooze" probably means "pus"
* Symptom "mucoid_sputum" probably means "clear_phlegm" if it doesn't coincide with "rusty_sputum" and "blood_in_sputum"
* Symptom "rusty_sputum" should also be checked for coincidence with "blood_in_sputum"

* Symptom "fluid_overload" was originally duplicated. The severity weights for the duplicates (4, 6) were averaged together.
* Symptom "prognosis" was removed (not a symptom, does not appear in dataset).

* For all symptoms, replace "_" with whitespace " ".

* In dataset.csv, all symptoms except "itching" are preceded with whitespace " ".

Changes to Diseases:

* "Dimorphic hemorrhoids(piles)" -> "Hemorrhoids"
* "Bronchial Asthma" -> "Bronchial asthma"
* "Common Cold" -> "Common cold"
* "Drug Reaction" -> "Drug reaction"

* "Paralysis (brain hemorrhage)" is probably just "Brain hemorrhage"
* "(vertigo) Paroymsal  Positional Vertigo" -> "Vertigo"?

* Any disease that isn't an acronym (GERD, AIDS) should be lower case.

* Added missing quotation marks to disease descriptions.

* In dataset.csv, some diseases contain a trailing whitespace " ".

Disease precautions also needs some reinterpretation.