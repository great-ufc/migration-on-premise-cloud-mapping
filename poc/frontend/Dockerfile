FROM node:16-bullseye AS builder

RUN curl -f https://get.pnpm.io/v6.16.js | node - add --global pnpm@7
RUN pnpm config set store-dir .pnpm-store

COPY ./frontend ./frontend

WORKDIR /frontend

RUN pnpm install 
RUN ls
RUN pnpm run build

FROM nginx:alpine AS production-build

COPY ./frontend/nginx.conf /etc/nginx/nginx.conf

RUN rm -rf /usr/share/nginx/html/*

COPY --from=builder /frontend/dist /usr/share/nginx/html/nested-app

EXPOSE 3000

ENTRYPOINT ["nginx", "-g", "daemon off;"]