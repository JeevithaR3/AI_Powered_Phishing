// Wait for the DOM to fully load before adding event listeners
document.addEventListener('DOMContentLoaded', function() {
    const checkEmailButton = document.getElementById('checkEmail');
    const emailTextArea = document.getElementById('emailText');
    const predictionText = document.getElementById('prediction');

    // Make sure the button exists
    if (checkEmailButton) {
        checkEmailButton.addEventListener('click', function() {
            const emailText = emailTextArea.value;

            if (emailText.trim() === '') {
                predictionText.textContent = 'Please enter some email text to check.';
                return;
            }

            // Call your backend API here for prediction
            fetch('http://localhost:5000/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email_content: emailText }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.is_phishing) {
                    predictionText.textContent = 'This email is Phishing!';
                } else {
                    predictionText.textContent = 'This email is not Phishing.';
                }
            })
            .catch(error => {
                console.error('Error:', error);
                predictionText.textContent = 'Error checking email. Please try again.';
            });
        });
    }
});
