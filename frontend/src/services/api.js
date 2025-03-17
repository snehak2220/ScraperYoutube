import axios from 'axios';

const API_URL = 'http://localhost:8000';  // Remove /api prefix

const axiosInstance = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    },
    withCredentials: false
});

export const searchVideos = async (query) => {
    try {
        const response = await axiosInstance.post('/scrape/', { 
            query: query,
            csrfmiddlewaretoken: document.querySelector('[name=csrfmiddlewaretoken]')?.value 
        });
        if (response.data && response.data.videos) {
            return response.data;
        }
        throw new Error(response.data?.error || 'Failed to fetch videos');
    } catch (error) {
        if (error.response?.status === 500) {
            throw new Error('Server error. Please try again later.');
        }
        throw error;
    }
};

export const getVideos = async () => {
    try {
        const response = await axiosInstance.get('/videos/');
        return response.data;
    } catch (error) {
        if (error.response?.status === 500) {
            throw new Error('Server error while fetching videos.');
        }
        throw error;
    }
};