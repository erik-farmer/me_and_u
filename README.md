# Django Boiler Plate

_A sane project starting point as outlined in [Two Scoops of Django](https://www.twoscoopspress.com/)._

## Gettings Started
Run the following to get started:
```commandline
export DJANGO_SETTINGS_MODULE="config.settings.local"
python manage.py runserver
```
and you're off to the races!

### Working on your project
Per the guidelines set in TwoScoops:
  * Static files should be placed in a `static` folder at the project level.
  * Templates should be placed in a `templates` folder at the project level.
  * New app directories should be added at the project level (and added to settings.base.PROJECT_APPS).