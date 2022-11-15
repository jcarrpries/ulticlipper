# The Ultimate Clipper
A web application to help Ultimate teams search through their game footage based on statistics from UltiAnalytics.

## Requirements
- Docker

## Running
The file `dev` is a small shell script used as a task runner. Invoke it with `./dev <command>`. If you get a permission error, run `chmod +x ./dev`.

Available commands are as follows:
- `test`: Run Django unit tests (`deploy/dockerfiles/django-test.dockerfile)
- `itest`: Run puppeteer integration tests. Automatically starts up the CI environment before running tests and tears down the environment after finishing running the tests.
- `env <environment>`: Starts up the environment by envoking the docker compose file `docker-compose-<environment>`. E.g. `./dev env dev`
- `down <environment>`: Tears down the given environment by running `docker compose down`.
- `build-prod`: Builds the docker images used for production deployments and saves them as tar archives. Used in CI.
- `deploy`: Meant to be run on the deployment server. Stops and prunes docker daemon containers and networks, loads the images expected from the continuous delivery system, and runs the images.

## Environments
- `dev`: Runs a NodeJS container that watches for frontend changes and auto-builds, and runs a python container that serves static files and runs the backend and automatically restarts on python changes. Django uses SQLite as a database.
- `ci`: Runs a caddy container with built-in static file serving, and a python container that runs the backend with gunicorn, and a database container that runs PostgreSQL. Containers don't auto-reload upon changes. Django uses Postgres as a database.

More information about Django's configuration between environments can be found in `ulticlipper/settings`.

## Debugging (Django )
Copy `launch_vscode_degugger.json` into `/.vscode` and rename file to `launch.json`

Install the Docker extension in VS Code so that you can run docker compose up
Right click on `docker-compose-debug.yml` and select Compose Up

Navigate to the Run and Debug tab in VS Code 
Select `Django Debug` from the RUN AND DEBUG configuration options
If it doesn't work on the first try wait a few seconds and try again

Set desired break points and away you go!

## Structure
The project is split into a frontend, backend, database, and proxy.
### Deployment
- Production deployment isn't configured yet
- Development setup uses docker compose to run a container for each component
- Frontend container just runs `npm-watch`, watching for changes and live-rebuilding jsx to js and sass to css. You have to refresh the page
- Backend container runs django in development mode, should live-reload most python files.
- Database container runs postgres
- Proxy container runs Caddy, a nice proxy that handles HTTPS automatically (HTTPS isn't set up yet, but should be easy to set up later)

### Frontened
- React components are mainly in `javascript`
- `javascript/app.jsx` has the React router configuration, linking to everything else
- `javascript/nav.jsx` has the navbar
- `javascript/home.jsx` is rendered as the root
- `javascript/search.jsx` has examples of querying the backend API
- `javascript/upload.jsx` has an example for uploading to the API
- Styles are kept in the `styles` directory
- Bulma CSS framework is used, so styles are pretty minimal

### Backend
- Django split the configuration files into the `ulticlipper` directory, and the main backend code into the `backend` directory
- Django REST framework is used to facilitate serializing data to and from JSON so it's easy to work with from the front end
- Django REST framework provides convenient ways to browse the API, check it out at http://localhost/api/clips/
- `backend/views.py` is where code is called to respond to frontend requests.
- `backend/urls.py` is used to add new API routes.
- `backend/models.py` is where models can be configured.

# Technologies Used
## Frontend
- React
- React router
- Bulma
- Sass

## Backend
- Django
- Django REST framework
- PostgreSQL

## Deployment
- Docker / Docker compose
- Caddy
