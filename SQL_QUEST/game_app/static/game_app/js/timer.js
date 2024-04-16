// timer.js

// Initialize variables
var startTime;
var timerInterval;

// Function to start the timer
function startTimer() {
    startTime = new Date().getTime();
    timerInterval = setInterval(updateTimer, 1000);
}

// Function to stop the timer
function stopTimer() {
    clearInterval(timerInterval);
}

// Function to update the timer display
function updateTimer() {
    var currentTime = new Date().getTime();
    var elapsedTime = currentTime - startTime;
    var minutes = Math.floor(elapsedTime / (1000 * 60));
    var seconds = Math.floor((elapsedTime % (1000 * 60)) / 1000);
    document.getElementById("timer").innerText = "Time: " + formatTime(minutes) + ":" + formatTime(seconds);
}

// Function to format time with leading zeros
function formatTime(time) {
    return time < 10 ? "0" + time : time;
}

// Start the timer when the page loads
window.onload = function() {
    startTimer();
};
