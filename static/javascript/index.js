window.onload = startInterval;

function startInterval() {
    setInterval("startTime();", 1000);
}

function startTime() {
    var today = new Date();
    let time = ('0' + today.getHours()).slice(-2) + ":"
        + ('0' + today.getMinutes()).slice(-2) + ":"
        + ('0' + today.getSeconds()).slice(-2);
    document.getElementById('time').innerHTML = time;
}