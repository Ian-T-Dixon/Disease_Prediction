# Changes to Original Dataset

<!-- The following is to document changes we made to the original dataset: -->

Minor changes were made to .csv filenames for clarity. Missing quotation marks were added to disease descriptions. These changes were made manually.

The following replacements were done across all four .csv files using Pandas.

<!-- -> or future tense means replacement in /Data/ .csv's has not happened yet.
"changed to" or past tense means the replacement has been implemented. -->

<!-- Enforcing lower case ensures compatability with web app. It will be trivial to capitalize when served to the dashboard at the beginning of a sentence, using str.upper().

    str = str[0].upper() + str[1:] -->

## Changes to Symptoms

* "scurring" -> "scarring"
* "diarrhoea" -> "diarrhea"
* "cold_hands_and_feets" -> "cold_hands_and_feet"
* "swollen_extremeties" -> "swollen_extremities"
* "foul_smell_ofurine" -> "foul_smell_of_urine"
* "altered_sensorium" -> "altered_mental_state"
* "dischromic_patches" -> "mottling_skin"
* "polyuria" -> "excessive_urination"
* "burning_micturition" -> "painful_urination"
* "silver like dusting" -> "blue-gray_complexion_(argyria)"
* "pus_filled_pimples" -> "pus-filled_pimples"
* "toxic_look_(typhos)" -> "toxic_look_(toxemia)"
* "yellow_crust_ooze" -> "yellow_oozing_scabs"

<!-- line break -->

* "fluid_overload" was originally duplicated. The severity weights for the duplicates (4, 6) were averaged together.
* "prognosis" was removed (not a symptom, does not appear in dataset).

<!-- line break -->

* In dataset.csv, all symptoms except "itching" were preceded with whitespace " ".
* Some symptoms appeared with spaces and underscores, e.g. "dischromic _patches".
* Removed any whitespaces from symptoms, then replaced "_" with " ".

## Changes to Diseases

* "Dimorphic hemorrhoids(piles)" -> "Hemorrhoids"
* "Dimorphic hemmorhoids(piles)" -> "Hemorrhoids"
* "Bronchial Asthma" -> "Bronchial asthma"
* "Common Cold" -> "Common cold"
* "Drug Reaction" -> "Drug reaction"
* "Paralysis (brain hemorrhage)" -> "Brain hemorrhage"
* "(vertigo) Paroymsal  Positional Vertigo" -> "Positional vertigo"
* "Osteoarthristis" -> "Osteoarthritis"
* "Typhoid" -> "Typhoid fever"

<!-- line break -->

* Any preceding or trailing whitespace was stripped from disease names.
* Any disease that isn't an acronym (GERD, AIDS) was made lowercase.

## Changes to Precautions

* "anti itch medicine" -> "anti-itch medicine"
* "antiboitic therapy" -> "antibiotics"
* "apply calamine" -> "apply calamine lotion"
* "avoid abrupt head movment" -> "avoid abrupt head movement"
* "avoid non veg food" -> "avoid non-vegeterian food"
* "avoid sudden change in body" -> "avoid sudden body movements"
* "avoid too many products" -> "avoid too many skincare products"
* "bath twice" -> "bathe twice"
* "check in pulse" -> "check pulse"
* "chew or swallow asprin" -> "chew or swallow aspirin"
* "Consult nearest hospital" -> "consult nearest hospital"
* "consume alovera juice" -> "consume aloe vera juice"
* "dont stand still for long" -> "don't stand still for long"
* "eat fruits and high fiberous food" -> "eat fruits and foods high in fiber"
* "eat high calorie vegitables" -> "eat high-calorie vegetables"
* "follow up" -> "follow up with doctor"
* "keep mosquitos out" -> "keep mosquitos away"
* "salt baths" -> "warm bath with epsom salt"
* "switch to loose cloothing" -> "loosen clothing"
* NaN (4th precaution of "Heart attack") -> "loosen clothing"
* "take otc pain reliver" -> "take OTC pain reliever"
* "take vapour" -> "steam inhalation"
* "use detol or neem in bathing water" -> "use oil of tea tree or peppermint in bathing water"
* "use neem in bathing " -> "use oil of tea tree or peppermint in bathing water"
* "use oinments" -> "use ointments"
* "use poloroid glasses in sun" -> "use polarized glasses in sun"
* "wash hands through" -> "wash hands thoroughly"
* "wash hands with warm soapy water" -> "wash hands thoroughly"
* "wear ppe if possible" -> "wear PPE if possible"