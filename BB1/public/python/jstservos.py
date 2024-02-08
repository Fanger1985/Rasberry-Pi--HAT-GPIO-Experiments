const express = require('express');
const { spawn, exec } = require('child_process');
const app = express();
const port = 3000;

let servoProcess = null;

app.use(express.static('public'));

app.get('/start-servo', (req, res) => {
    if (servoProcess === null) {
        servoProcess = spawn('python', ['jstservo.py']);
        res.send('Servo movement started');
    } else {
        res.send('Servo is already moving');
    }
});

app.get('/stop-servo', (req, res) => {
    if (servoProcess !== null) {
        exec('pkill -f jstservo.py'); // Adjust the script name accordingly
        servoProcess = null;
        res.send('Servo movement stopped');
    } else {
        res.send('Servo was not moving');
    }
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});

// Cleanup for server shutdown
process.on('SIGINT', () => {
    if (servoProcess !== null) {
        exec('pkill -f jstservo.py'); // Ensure the Python script is terminated
    }
    console.log('Shutting down server...');
    process.exit();
});
