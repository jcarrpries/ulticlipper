# The Ultimate Clipper
A web application to help Ultimate teams search through their game footage based on statistics from UltiAnalytics.

## Requirements
- Docker

## Running
Run with the following command to view the output from all containers:
```
docker compose -f docker-compose-dev.yml up --build; docker compose -f docker-compose-dev.yml down --volumes
```
The reason the command is split in two is to ensure the resources get cleaned up at the end (mainly the Postgres container data volume). To quit, do `ctrl+C` twice. If you get an error on startup after starting multiple times, run
```
docker compose -f docker-compose-dev.yml down --volumes
```
This should ensure all old resources are cleaned up so things can start fresh.

Visit http://localhost to view the site once all the containers are running.

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
- Django's admin interface can be viewed at http://localhost/admin, the username and password are configured in `Dockerfile-dev-django` and `docker-compose-dev.yml` respectively, and are `admin` and `asdf`.
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
