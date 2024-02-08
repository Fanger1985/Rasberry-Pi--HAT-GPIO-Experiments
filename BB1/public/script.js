document.getElementById('fan-toggle').addEventListener('click', () => {
    fetch('/toggle-fan').catch(console.error);
});

document.getElementById('led-toggle').addEventListener('click', () => {
    fetch('/toggle-led').catch(console.error);
});

const logEvent = (event) => {
    const logDiv = document.getElementById('log');
    logDiv.innerHTML += `<p>${event}</p>`;
    logDiv.scrollTop = logDiv.scrollHeight; // Scroll to bottom
};

// Simulating joystick and button #17 events, replace with actual event listeners
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowUp') logEvent('Joystick Up');
    if (e.key === 'ArrowDown') logEvent('Joystick Down');
    if (e.key === 'ArrowLeft') logEvent('Joystick Left');
    if (e.key === 'ArrowRight') logEvent('Joystick Right');
    if (e.key === 'Enter') logEvent('Button #17 Pressed');
});
// Add these functions to your existing JavaScript file

// Function to simulate changing pin status
const togglePinStatus = (pin) => {
    const statusElement = document.getElementById(`${pin}-status`);
    statusElement.textContent = statusElement.textContent === 'Off' ? 'On' : 'Off';
}

// Call this function in your existing event listeners for fan and LED toggle buttons
document.getElementById('fan-toggle').addEventListener('click', () => {
    fetch('/toggle-fan')
        .then(() => togglePinStatus('fan'))
        .catch(console.error);
});

document.getElementById('led-toggle').addEventListener('click', () => {
    fetch('/toggle-led')
        .then(() => togglePinStatus('led'))
        .catch(console.error);
});

// Simulate button #17 press
document.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        const statusElement = document.getElementById('button17-status');
        statusElement.textContent = 'Pressed';
        setTimeout(() => { statusElement.textContent = 'Not Pressed'; }, 1000); // Reset after 1 sec
    }
});
document.getElementById('dotstar-toggle').addEventListener('click', () => {
    fetch('/toggle-dotstar').catch(console.error); // You'll need to add this endpoint to your server
    // Assuming toggling DotStar affects both data and clock pins
    togglePinStatus('dotstar-data');
    togglePinStatus('dotstar-clock');
});

document.getElementById('backlight-toggle').addEventListener('click', () => {
    fetch('/toggle-backlight').catch(console.error); // Add this endpoint too
    togglePinStatus('backlight');
});

// Update the logEvent function to include joystick movements
document.addEventListener('keydown', (e) => {
    // Existing code for arrow keys and Enter
    if (e.key === ' ') {  // Assuming spacebar for joystick select
        logEvent('Joystick Select Pressed');
        togglePinStatus('joystick-select');
    }
});

// Extend this to include more detailed logging and status updates for each joystick direction and button press