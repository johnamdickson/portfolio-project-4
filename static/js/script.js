window.addEventListener('load', function () {
    hideElements()
})

window.addEventListener('resize', function (event) {
    hideElements()
}, true);

// dismiss alerts after 2.5 seconds
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);

// hide elements on screen depending on screen size

function hideElements() {

    let windowWidth = window.innerWidth;

    let hiddenElements = document.getElementsByClassName("hidden-home");

    if (windowWidth <= 767) {
        for (let elements of hiddenElements) {
            elements.style.display = 'none'
        }
    } else {
        for (let elements of hiddenElements) {
            elements.style.display = 'block'
        }
    }
}