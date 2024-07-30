import axios from "axios";

// Configuración de la instancia de axios
const apiClient = axios.create({
  baseURL: "http://localhost:8000/api", // URL base del backend Django
  withCredentials: false, // Cambia a true si necesitas enviar cookies
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
});

// Funciones exportadas usando apiClient
export const getMovies = () => apiClient.get("/movies/");
export const getMovie = (id) => apiClient.get(`/movies/${id}/`);
export const createMovie = (data) => apiClient.post("/movies/", data);
export const updateMovie = (id, data) => apiClient.put(`/movies/${id}/`, data);
export const deleteMovie = (id) => apiClient.delete(`/movies/${id}/`);

// Si necesitas funciones que no usan la instancia apiClient,
// puedes definirlas aquí con una URL base diferente si es necesario
const API_URL = "http://localhost:8000/api/movies/";

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

// Ejemplo de uso
apiClient.get("/some-endpoint").then((response) => {
  console.log(response.data);
});

getMovies().then((response) => {
  console.log(response.data);
});
