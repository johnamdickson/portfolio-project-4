window.addEventListener('load', function () {
    hideElements()
    startCarousel()
})

window.addEventListener("DOMContentLoaded", function () {
    updateChecksComplete()

});

window.addEventListener('resize', function (event) {
    hideElements()
}, true);

/**
 * Dismisses alerts after 2.5 seconds using setTimeout function.
 * Improve user experience so that routine alerts are automatically
 * dismissed 
 */
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);

/**
 * Hides elements depending on screen size.
 * For example, on home page titles are hidden to improve responsive
 * design. 
 */
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

/**
 * Adds a fontawseome icon to home page html depending on element text.
 * For checks complete a checkmark icon with green background
 * is returned else a red x mark icon.
 */
function updateChecksComplete() {
    let checkStatus = document.getElementsByClassName("check_status")
    for (let check of checkStatus) {
        console.log(check.innerHTML)
        if (check.innerHTML === "Checks Complete") {
            console.log("checks completed")
            // solution for fontawesome background from stack overflow:
            // https://stackoverflow.com/questions/26516353/font-awesome-background-color
            check.innerHTML = `<p>
                                    <span class="fa-stack" style="vertical-align: top;">
                                        <i class="fas fa-circle fa-stack-2x";"></i>
                                        <i class="fa-solid fa-circle-check fa-stack-2x fa-inverse" style="color: #00D100;"></i>
                                    </span>
                                </p>
                                <p>Complete</p>`
        } else {
            check.innerHTML = `<p>
                                    <span class="fa-stack" style="vertical-align: top;">
                                        <i class="fas fa-circle fa-stack-2x" ></i>
                                        <i class="fa-solid fa-circle-xmark fa-stack-2x fa-inverse" style="color: #BF181D;"></i>
                                    </span>
                                </p>
                                <p>Outstanding</p>`
        }
    }
}

// function showModal(emissionList){
//     let removeSquareBrackets = emissionList.slice(1, -1)
//     let emissionArray = removeSquareBrackets.split(",")
//     console.log('called', typeof emissions)
//         for (let emission of emissionArray){
//             console.log(emission)
//         }
const showModal = (data) => {
    console.log(data, 'here is');
    let emissionArray = JSON.parse(data);
    // solution to passing django url from javascript from stack overflow:
    // https://stackoverflow.com/questions/37311042/call-django-urls-inside-javascript-on-click-event
    let allEmissionsUrl = document.getElementById('emissionUrl').getAttribute('data-url');
    let createdDateArray = emissionArray.created.split(" ")
    const modalItem = document.getElementById('emissionModalCenter');
    modalItem.innerHTML = ` <div class="modal-dialog modal-dialog-centered" role="document">
                                    <div class="modal-content">
                                        <div class="modal-header">
                                            <h4 class="modal-title" id="exampleModalLongTitle">${emissionArray.title}</h4>
                                            <button type="button" class="btn-close" data-dismiss="modal" aria-label="Close">
                                            </button>
                                        </div>
                                            <tr>
                                                <img class="modal-img" src="${emissionArray.imageUrl}">
                                            </tr>
                                            <table>
                                                <tr>
                                                    <td>
                                                        <h5>Type:</h5>
                                                    </td>
                                                    <td>
                                                        <p>${emissionArray.type}</p>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td>
                                                        <h5>Date Registered:</h5>
                                                    </td>
                                                    <td>
                                                        <p>${createdDateArray[0]}</p>
                                                    </td>
                                                </tr>                                                
                                                <tr>
                                                <td>
                                                    <h5>Description:</h5>
                                                </td>
                                                <td>
                                                    <p class="check_status">${emissionArray.description}</p>
                                                </td>
                                                </tr>
                                                <tr>
                                                    <td>
                                                        <h5>Location:</h5>
                                                    </td>
                                                    <td>
                                                        <p class="check_status">${emissionArray.location}</p>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td>
                                                        <h5>Emission Status:</h5>
                                                    </td>
                                                    <td>
                                                        <p class="check_status">${emissionArray.status}</p>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td>
                                                        <h5>Checks Status:</h5>
                                                    </td>
                                                    <td>
                                                        <p class="check_status">${emissionArray.checkComplete}</p>
                                                    </td>
                                                </tr>                                               
                                                <tr>
                                                    <td>
                                                        <h5>Current Check Due:</h5>
                                                    </td>
                                                    <td>
                                                        <p class="check_status">${emissionArray.currentCheck}</p>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td>
                                                        <h5>Last Checked:</h5>
                                                    </td>
                                                    <td>
                                                        <p class="check_status">${emissionArray.lastCheck}</p>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td>
                                                        <h5>Next Check Due:</h5>
                                                    </td>
                                                    <td>
                                                        <p class="check_status">${emissionArray.nextCheck}</p>
                                                    </td>
                                                </tr>                                                   
                                            </table>
                                        <div class="modal-footer">
                                            <a href="" class="btn">Submit ${emissionArray.title} Emission Check</a>
                                            <a href="${allEmissionsUrl}" class="btn">Go To All Emissions</a>
                                        </div>
                                    </div>
                                </div>
                              `;

    new bootstrap.Modal(modalItem).show();
};


// functionality below for carousel from:
// https://www.codeply.com/p/0CWffz76Q9

function startCarousel() {
    let items = document.querySelectorAll('.carousel .carousel-item')

    items.forEach((el) => {
        const minPerSlide = 3
        let next = el.nextElementSibling
        for (var i = 1; i < minPerSlide; i++) {
            if (!next) {
                // wrap carousel by using first child
                next = items[0]
            }
            let cloneChild = next.cloneNode(true)
            el.appendChild(cloneChild.children[0])
            next = next.nextElementSibling
        }
    })
}