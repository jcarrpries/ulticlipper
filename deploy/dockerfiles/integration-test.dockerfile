FROM node:lts-alpine3.15
WORKDIR /app

RUN apk add chromium
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true \
    PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser

ENV PATH /app/node_modules/.bin:$PATH
COPY package.json ./
COPY package-lock.json ./
RUN npm install
RUN npm install puppeteer jest-puppeteer expect-puppeteer
RUN addgroup -S pptruser && adduser -S -G pptruser pptruser \
    && mkdir -p /home/pptruser/Downloads /app \
    && chown -R pptruser:pptruser /home/pptruser \
    && chown -R pptruser:pptruser /app

# Run everything after as non-privileged user.
USER pptruser

COPY javascript ./javascript
COPY styles ./styles
COPY javascript/integration_tests/jest-puppeteer.config.js /app/jest-puppeteer.config.js

CMD npm test
