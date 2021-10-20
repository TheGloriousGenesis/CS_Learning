FROM node:alpine AS build
WORKDIR '/app'
COPY Docker/ExampleNode/package.json .
RUN npm install
COPY Docker/ExampleNode/ .
RUN npm run build


FROM nginx
EXPOSE 80
COPY --from=build /app/build /usr/share/nginx/html
