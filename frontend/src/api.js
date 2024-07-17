import axios from 'axios';

const API_URL = 'http://localhost:8000/api/movies/';

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

