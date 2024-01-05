# Silk road map quizzes

This repository contains the silk road map quizzes from the Silk Road Seattle project
(made in 2002 by Lance Jenott).

The javascript does not work very well with modern browsers, so I wrote a converter to 
create more modern versions of the quizzes, with a few additional features. 

## repo structure

```
|- old_versions : contains the old html and jpg files
|- new_versions : contains the new html files (manually converted) + the old jpg files
|- new_versions_auto : contains the new html files (converted by the convert.py script)
|- convert.py: script that converts the old versions into new versions, using a template file
|- template.html: template for the new versions. 
|- placenames.html: all place names in the quizzes
|- index.html: the original homepage of the mapquiz project, with links to the new files
```