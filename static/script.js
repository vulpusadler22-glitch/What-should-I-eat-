// Function to pick a random meal from the server
function pickMeal() {
    // Fetch data from Python backend
    fetch('/pick-meal')
        .then(response => response.json())  // Convert response to JSON
        .then(data => {
            // Get the display area
            const mealDisplay = document.getElementById('mealDisplay');
            
            // Update the display with image and meal name
          mealDisplay.innerHTML = `
          <img src="/static/${data.image}" alt="${data.name}" class="meal-image">
          <h2>${data.name}</h2>
          `;
            
            // Show the "Try Again" button
            document.getElementById('tryAgainBtn').style.display = 'inline-block';
        })
        .catch(error => console.error('Error:', error));
}