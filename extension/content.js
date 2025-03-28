// content.js - Detects shortened URLs and sends them to background.js for unshortening

const links = document.querySelectorAll('a');

links.forEach(link => {
    const url = link.href;
    if (isShortened(url)) { // Check if it's a shortened URL
        chrome.runtime.sendMessage(
            { action: "unshortenUrl", url: url },
            (response) => {
                // Replace the href of the link with the unshortened URL
                if (response && response.unshortenedUrl) {
                    link.href = response.unshortenedUrl;
                }
            }
        );
    }
});

// Simple check for shortened URLs (this can be expanded)
function isShortened(url) {
    return url.includes('bit.ly') || url.includes('goo.gl'); // Add other shortening services as needed
}
