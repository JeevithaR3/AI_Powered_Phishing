// proxy-server.js
const express = require('express');
const fetch = require('node-fetch');
const cors = require('cors');
const bodyParser = require('body-parser');

// Initialize the Express app
const app = express();

// Middleware to handle CORS
app.use(cors());

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Unshorten URL Endpoint
app.post('/unshorten', async (req, res) => {
  const { url } = req.body;

  try {
    // Send a HEAD request to follow redirects
    const response = await fetch(url, { method: 'HEAD', redirect: 'follow' });
    const unshortenedUrl = response.url;

    // Respond with the final unshortened URL
    res.json({ long_url: unshortenedUrl });
  } catch (error) {
    // Handle errors and send a response
    res.status(500).json({ error: 'Error unshortening URL' });
  }
});

// Start the server
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Proxy server is running on http://localhost:${PORT}`);
});
