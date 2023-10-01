
FROM node:18-alpine as build
WORKDIR frontend/
COPY ./package*.json package.json

RUN yarn install
COPY . .
RUN yarn build


FROM nginx
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /frontend/dist /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]
