import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
});

// Attach customer id from localStorage to every request
api.interceptors.request.use((config) => {
  const customerId = localStorage.getItem("customerId");
  if (customerId) {
    config.headers = config.headers || {};
    config.headers["X-Customer-Id"] = customerId;
  }
  return config;
});

// Persist customer id returned by the server
api.interceptors.response.use((response) => {
  const cid = response.headers["x-customer-id"] || response.headers["X-Customer-Id"];
  if (cid) localStorage.setItem("customerId", cid);
  return response;
});

export default api;
