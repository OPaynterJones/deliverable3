FROM node:20-bookworm-slim
WORKDIR /react-app
COPY package.json /react-app
COPY package-lock.json /react-app
RUN npm install --silent
COPY . /react-app
EXPOSE 3000
CMD ["npm", "start"]