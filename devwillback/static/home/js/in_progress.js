document.addEventListener("DOMContentLoaded", function() {
    const progressBar = document.querySelector('.progress');
    const progressPercentage = document.getElementById('progress-percentage');

    let width = 0;
    const interval = setInterval(() => {
        if (width >= 100) {
            clearInterval(interval);
        } else {
            width++;
            progressBar.style.width = width + '%';
            progressPercentage.textContent = width + '%';
        }
    }, 50); // Adjust the speed of the progress bar here
});