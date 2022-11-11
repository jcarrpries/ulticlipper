# Build react app
FROM node:lts-alpine3.15 as nodebuild
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package.json ./
COPY package-lock.json ./
RUN npm install
COPY javascript ./javascript
COPY styles ./styles
RUN npm run build:prod

# Run caddy
FROM caddy:2.6.1-alpine
WORKDIR /app
COPY --from=nodebuild /app/static /static
COPY ./static/index.html /static
