var startTime;
var timerInterval;

function startTimer() {
    startTime = new Date().getTime();
    timerInterval = setInterval(updateTimer, 1000);
}

function stopTimer() {
    clearInterval(timerInterval);
}

function updateTimer() {
    var currentTime = new Date().getTime();
    var elapsedTime = Math.floor((currentTime - startTime) / 1000); // Calculate elapsed time in seconds
    var minutes = Math.floor(elapsedTime / 60);
    var seconds = elapsedTime % 60;
    document.getElementById("timer").innerText = "Time: " + formatTime(minutes) + ":" + formatTime(seconds);
}

function formatTime(time) {
    return time < 10 ? "0" + time : time;
}

window.onload = function() {
    startTimer();
};
