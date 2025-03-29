chrome.runtime.onInstalled.addListener(() => {
  console.log("URL Unshortener Extension Installed");
});

chrome.webRequest.onCompleted.addListener(
  function(details) {
    const redirectedUrl = details.url;
    console.log("Redirected URL: ", redirectedUrl);

    // Send the final URL back to the popup script
    chrome.storage.local.set({ 'unshortenedUrl': redirectedUrl });
  },
  { urls: ["http://*/*", "https://*/*"] },
  ["responseHeaders"]
);

// Listen for messages from popup.js
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'unshorten') {
    chrome.storage.local.get('unshortenedUrl', function(result) {
      sendResponse({ unshortenedUrl: result.unshortenedUrl || 'Error unshortening the URL' });
    });
    return true;  // Keep the response open for asynchronous response
  }
});
