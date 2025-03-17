import React, { useState, useEffect } from 'react';
import { Container, TextField, Button, Grid, Card, CardMedia, CardContent, Typography } from '@mui/material';
import { searchVideos, getVideos } from './services/api';

function App() {
  const [query, setQuery] = useState('');
  const [videos, setVideos] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchVideos();
  }, []);

  const fetchVideos = async () => {
    try {
      const data = await getVideos();
      setVideos(data);
    } catch (error) {
      setError('Error fetching videos');
      console.error('Error fetching videos:', error);
    }
  };

  const handleSearch = async (e) => {
    e.preventDefault();
    if (!query.trim()) return;
    
    setLoading(true);
    setError(null);
    
    try {
      const response = await searchVideos(query);
      if (response.data && response.data.videos) {
        setVideos(response.data.videos);
        setQuery('');
      }
    } catch (error) {
      setError('Error searching videos. Please try again.');
      console.error('Error searching videos:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      <form onSubmit={handleSearch} style={{ marginBottom: 24 }}>
        <Grid container spacing={2}>
          <Grid item xs={10}>
            <TextField
              fullWidth
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Enter search query"
              disabled={loading}
              error={!!error}
              helperText={error}
            />
          </Grid>
          <Grid item xs={2}>
            <Button
              fullWidth
              variant="contained"
              type="submit"
              disabled={loading || !query.trim()}
            >
              {loading ? 'Searching...' : 'Search'}
            </Button>
          </Grid>
        </Grid>
      </form>

      {loading && (
        <Typography align="center" sx={{ my: 4 }}>
          Searching for videos... Please wait...
        </Typography>
      )}

      <Grid container spacing={3}>
        {videos.map((video) => (
          <Grid item xs={12} sm={6} md={4} key={video.id}>
            <Card>
              {video.thumbnail && (
                <CardMedia
                  component="img"
                  height="140"
                  image={video.thumbnail}
                  alt={video.title}
                />
              )}
              <CardContent>
                <Typography gutterBottom variant="h6" component="div">
                  {video.title}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  Channel: {video.channel_name}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  Views: {video.views}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  Posted: {video.time_posted}
                </Typography>
                <Button
                  href={video.video_url}
                  target="_blank"
                  rel="noopener noreferrer"
                  variant="contained"
                  size="small"
                  sx={{ mt: 1 }}
                >
                  Watch Video
                </Button>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Container>
  );
}

export default App;
