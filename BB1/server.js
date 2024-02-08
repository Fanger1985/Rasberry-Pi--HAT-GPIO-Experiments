const express = require('express');
const { Gpio } = require('onoff');
const app = express();
const port = 3000;
const path = require('path');

// GPIO setup - adjust pins based on your hardware setup and BrainCraft HAT
const fan = new Gpio(4, 'out'); // Example pin for the fan
const led = new Gpio(17, 'out'); // Adjust for a free GPIO pin
const dotstarData = new Gpio(23, 'out'); // Data pin for DotStar LEDs
const dotstarClock = new Gpio(24, 'out'); // Clock pin for DotStar LEDs
const backlight = new Gpio(18, 'out'); // Adjust for the backlight control pin
// Feel free to add more GPIO controls as needed

app.use(express.static('public')); // Serve static files from 'public' directory

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Toggle endpoints
app.get('/toggle-fan', (req, res) => {
    fan.writeSync(fan.readSync() ^ 1);
    res.send('Toggled fan');
});

app.get('/toggle-led', (req, res) => {
    led.writeSync(led.readSync() ^ 1);
    res.send('Toggled LED');
});

app.get('/toggle-dotstar', (req, res) => {
    // Assuming toggling DotStar involves both data and clock pins
    dotstarData.writeSync(dotstarData.readSync() ^ 1);
    dotstarClock.writeSync(dotstarClock.readSync() ^ 1);
    res.send('Toggled DotStar LEDs');
});

app.get('/toggle-backlight', (req, res) => {
    backlight.writeSync(backlight.readSync() ^ 1);
    res.send('Toggled Display Backlight');
});

// Status endpoints
app.get('/status', (req, res) => {
    res.json({
        fan: fan.readSync() === 1 ? 'On' : 'Off',
        led: led.readSync() === 1 ? 'On' : 'Off',
        dotstarData: dotstarData.readSync() === 1 ? 'On' : 'Off',
        dotstarClock: dotstarClock.readSync() === 1 ? 'On' : 'Off',
        backlight: backlight.readSync() === 1 ? 'On' : 'Off',
        // Add more statuses as needed
    });
});

// Start server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});

// Graceful shutdown for cleaning up GPIOs
process.on('SIGINT', () => {
    fan.unexport();
    led.unexport();
    dotstarData.unexport();
    dotstarClock.unexport();
    backlight.unexport();
    // Add more GPIO cleanup as needed

    console.log('Shutting down server...');
    process.exit();
});
