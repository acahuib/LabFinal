import axios from "axios";
import apiClient, { getMovies, getMovie } from "./api";

const API_URL = "http://localhost:8000/api/movies/";

const apiClient = axios.create({
  baseURL: "http://localhost:8000/api", // URL base del backend Django
  withCredentials: false, // Cambia a true si necesitas enviar cookies
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
});

export default apiClient;

export const getMovies = () => apiClient.get("/movies/");
export const getMovie = (id) => apiClient.get(`/movies/${id}/`);
export const createMovie = (data) => apiClient.post("/movies/", data);
export const updateMovie = (id, data) => apiClient.put(`/movies/${id}/`, data);
export const deleteMovie = (id) => apiClient.delete(`/movies/${id}/`);

export const api = {
  getMovies() {
    return axios.get(API_URL);
  },
  createMovie(movie) {
    return axios.post(API_URL, movie);
  },
  updateMovie(id, movie) {
    return axios.put(`${API_URL}${id}/`, movie);
  },
  deleteMovie(id) {
    return axios.delete(`${API_URL}${id}/`);
  },
};

apiClient.get("/some-endpoint").then((response) => {
  console.log(response.data);
});

getMovies().then((response) => {
  console.log(response.data);
});
