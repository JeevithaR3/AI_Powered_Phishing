document.getElementById('unshorten-btn').addEventListener('click', function() {
  const shortenedUrl = document.getElementById('url-input').value;

  if (shortenedUrl) {
    console.log("Unshortening URL:", shortenedUrl);

    // Send message to background script to start tracking the unshortening process
    chrome.runtime.sendMessage(
      { action: 'unshorten', url: shortenedUrl },
      function(response) {
        if (response.unshortenedUrl) {
          document.getElementById('result').textContent = 'Unshortened URL: ' + response.unshortenedUrl;
        } else {
          document.getElementById('result').textContent = 'Error unshortening URL: ' + response.error;
        }
      }
    );
  } else {
    document.getElementById('result').textContent = 'Please enter a URL';
  }
});
