FROM node:21-bookworm-slim
WORKDIR /react-app
COPY package.json /react-app
COPY package-lock.json /react-app
RUN npm install
EXPOSE 3000
CMD ["npm", "start"]