TheFanger 

this server.js is supposed to be an attempt at remote controlling my gpo pins on my rasberry pi 4
this picontrol.html is meant to be ran on the py to control its own gpio pins 
there is a clientpicontrol.html file that will be existing as well 







const express = require('express');
const { Gpio } = require('pigpio'); // Make sure you've got pigpio installed
const app = express();
const port = 3000; // Change this to whatever port you want to use

// Initialize the fan on GPIO 4 as an output
const fan = new Gpio(4, { mode: Gpio.OUTPUT });

// Placeholder function to simulate toggling DotStar LEDs
const toggleDotStar = () => {
    // Your logic to toggle DotStar LEDs goes here
    // This will depend on how you've set up control for the DotStar LEDs
    console.log('DotStar LEDs toggled');
};

// Serve static files from 'public' directory (where your frontend code lives)
app.use(express.static('public'));

// Endpoint to turn the fan on
app.get('/fan/on', (req, res) => {
    fan.digitalWrite(1); // Sets fan GPIO to high
    res.send('Fan turned on');
});

// Endpoint to turn the fan off
app.get('/fan/off', (req, res) => {
    fan.digitalWrite(0); // Sets fan GPIO to low
    res.send('Fan turned off');
});

// Endpoint to toggle DotStar LEDs
app.get('/toggle-dotstar', (req, res) => {
    toggleDotStar(); // Call your DotStar toggle function
    res.send('DotStar LEDs toggled');
});

// Start the server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});

// Graceful shutdown
process.on('SIGINT', () => {
    fan.digitalWrite(0); // Turn fan off
    fan.unexport(); // Unexport GPIO to free resources
    console.log('Server shutting down');
    process.exit();
});
