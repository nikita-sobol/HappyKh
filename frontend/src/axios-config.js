/* eslint-disable no-param-reassign */
import axios from 'axios';
import store from './store';

const HOST = 'http://127.0.0.1:8000';

export const axiosInstanceAuth = axios.create({
  baseURL: HOST,
});

axiosInstanceAuth.interceptors.request.use(
  (config) => {
    const token = store.getters.getToken;
    if (token) {
      config.headers.Authorization = `Token ${token}`;
    }
    return config;
  },
  error => Promise.reject(error),
);

export const axiosInstance = axios.create({
  baseURL: HOST,
});

