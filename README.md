## API For todo App

- Dependency Management with [Poetry](https://python-poetry.org/)
- run: 

`poetry install`

`poetry run python3 makemigrations`

`poetry run python3 migrate`

`poetry run python3 runserver`

## Documentation via Swagger API

`http://127.0.0.1:8001/api/`

Using: function based views.

TaskList model is linked to Task model via Foreign Key. (Many to One relationship)

