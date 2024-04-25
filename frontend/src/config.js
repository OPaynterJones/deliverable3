export const backendUrl =
  process.env.REACT_APP_BACKEND_URL_AND_PORT ||
  `http://${window.location.hostname}:5000`;
