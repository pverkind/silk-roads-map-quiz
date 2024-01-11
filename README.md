# Silk road map quizzes

This repository contains the silk road map quizzes from the Silk Road Seattle project
(made in 2002 by Lance Jenott).

The javascript does not work very well with modern browsers, so I wrote a converter (convert.py) to 
create more modern versions of the quizzes, with a few additional features:
* feedback that includes the number of skipped places
* a "show" button that shows the location of a place and then skips to the next place
* a dropdown menu from which you can select the quiz you want to take
* when the student has successfully finished an exercise, an encoded string is shown
  that contains the name of the exercise, the mistakes s/he made, and 
  the time s/he finished the exercise (to be used as proof that the exercise was successfully finished)

## repo structure

```
|- old_versions/ : contains the old html and jpg files
|- img/ : contains the map image files
|- map_data/ : contains a json file for each map, including the path to the map image,
|              the title of the exercise, and the coordinates of the features to be identified
|- convert.py: script that converts the old versions into new versions, using a template file (map-quiz.html)
|- map-quiz.html: the main map quiz file, from which one can take any of the map quizzes 
|                 (this file also doubles as the template for the new versions of the map quiz files)
|- file_list.json : a list of all json files in the map_data folder (used to create the dropdown menu)
|- index.html: the updated homepage of the original mapquiz project, with links to the new html files
|- placenames.html: all place names in the quizzes
```
In addition, the root folder contains a html file for each map quiz (cities.html, countries.html, etc.)