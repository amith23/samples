FROM node:14-alpine as build-stage

RUN mkdir -p /app
WORKDIR /app

COPY package.json .
COPY package-lock.json .
RUN npm install

# Set environment variables
ENV NODE_ENV production
ENV PORT 80
ENV CHOKIDAR_USEPOLLING true
ENV REACT_APP_API_HOST http://qwikfoneloadbalancer-316216489.eu-west-2.elb.amazonaws.com
ENV REACT_APP_WS ws://qwikfoneloadbalancer-316216489.eu-west-2.elb.amazonaws.com/graphql
ENV REACT_APP_API_PATH /graphql
ENV REACT_APP_REST_API_PATH /api/v1
ENV REACT_APP_JWT_TOKEN_NAME app-jwt

COPY . .

RUN npm run build

# production-stage
FROM nginx:stable-alpine as production-stage

COPY --from=build-stage /app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx",  "-g", "daemon off;"]
