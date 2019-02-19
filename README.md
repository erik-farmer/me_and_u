# MeNu

_A meal planning application._

## Working locally

Use the `docker-compose.yml` file to have a clean/local postgres and redis install via `docker-compose up` from the project directory.

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

## Creating Migrations

Credit Two Scoops of Django (6.2.1 Tips for Creating Migrations)

* As soon as a new app or model is created, take that extra minute to create the initial django.db.migrations for that new model. All we do is type python manage.py makemigrations.
* Examine the generated migration code before you run it, especially when complex changes are involved. Also review the SQL that will be used with the sqlmigrate command.
* Use the MIGRATION_MODULES setting to manage writing migrations for third-party apps that don’t have their own django.db.migrations-style migrations.
* Don’t worry about how many migrations are created. If the number of migrations becomes unwieldy, use squashmigrations to bring them to heel.
* Always back up your data before running a migration.

## Model Guidelines

Follow 6.4.4 `When to Use Null and Blank` from TwoScoops when possible.