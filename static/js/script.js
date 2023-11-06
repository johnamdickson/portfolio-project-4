

window.addEventListener('load', function () {
    startCarousel()
    initMap()
})

window.addEventListener("DOMContentLoaded", function () {
    hideElements()
    updateChecksComplete()
    statusFilter()
});

window.addEventListener('resize', function (event) {
    hideElements()
    adjustMapZoom()
}, true);


/**
 * Dismisses alerts after 3.5 seconds using setTimeout function.
 * Improve user experience so that routine alerts are automatically
 * dismissed 
 */
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 4000);

/**
 * Hides elements depending on screen size.
 * For example, on home page titles are hidden to improve responsive
 * design. 
 */
function hideElements() {
    let windowWidth = window.innerWidth;
    let hiddenElements = document.getElementsByClassName("callout-hidden");
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
        let className = check.className
        if (check.innerHTML === "Checks Complete") {
            // solution for fontawesome background from stack overflow:
            // https://stackoverflow.com/questions/26516353/font-awesome-background-color
            check.innerHTML = `<div class="checks-complete-td">
                                <p>
                                    <span class="fa-stack" style="vertical-align: top;">
                                        <i class="fas fa-circle fa-stack-2x"style="color: #FFFFFF;"></i>
                                        <i class="fa-solid fa-circle-check fa-stack-2x fa-inverse" style="color: #00D100;"></i>
                                    </span>
                                </p>
                                <p>Complete</p>
                                </div>`
                                
        } else {
            check.innerHTML = `<div class="checks-complete-td">
                                <p>
                                    <span class="fa-stack" style="vertical-align: top;">
                                        <i class="fas fa-circle fa-stack-2x" style="color: #FFFFFF;"></i>
                                        <i class="fa-solid fa-circle-xmark fa-stack-2x fa-inverse" style="color: #BF181D;"></i>
                                    </span>
                                </p>
                                <p>Outstanding</p>
                                </div>`
        }
        if (className.includes('emission-detail-check_status')) {
            updateChecksCompleteClassName()
        }
    }
    // add a class name to enable css to set flex direction to row.
    function updateChecksCompleteClassName() {
        let checksCompleteTd = document.getElementsByClassName("checks-complete-td");
        for (let check of checksCompleteTd) {
            check.className += " emission-detail-td-row";
        }
    }
}
/**
 * Adds modal to the DOM and updates with JSON data passed in
 * from index html.
 */
const showModal = (data) => {
    let emissionArray = JSON.parse(data);
    // solution to passing django url from javascript from stack overflow:
    // https://stackoverflow.com/questions/37311042/call-django-urls-inside-javascript-on-click-event
    let allEmissionsUrl = document.getElementById('emissionUrl').getAttribute('data-url');
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
                                            <table class="home-modal-table">
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
                                            <a href="/${emissionArray.slug}/" class="btn">Go To Emission Detail Page</a>
                                            <a href="${allEmissionsUrl}" class="btn">Go To All Emissions Page</a>
                                        </div>
                                    </div>
                                </div>
                              `;
    new bootstrap.Modal(modalItem).show();
};

/**
 * Adds modal to the DOM and updates with JSON data passed in
 * from emission.html.
 */
const emissionModal = (data) => {
    let emission = JSON.parse(data)
    const modalItem = document.getElementById('emissionModal');
    document.getElementById('emissionModalTitle').innerText = `Emission: ${emission.title}`;
    document.getElementById('emissionModalBody').innerText = 'Please make a selection from the options below:';
    document.getElementById('emissionDetailUrl').setAttribute('data-url', `{% url 'emission_detail' /${emission.slug}/ %}`)
    // set hidden input href attribute to slug of the emission passed into this function.
    document.getElementById('emission-detail-a').setAttribute('href' , `/${emission.slug}/`)
    new bootstrap.Modal(modalItem).show();

}

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

/**
 * Function to filter emissions table for open/closed
 * status. Default selection is open only with toggle
 * switch position determining filter.
 */
function statusFilter() {
    let closedRows = document.getElementsByClassName("closed-row");
    let filterText = document.getElementById("column-filter")
    // verify closed rows exist to prevent console errors
    if (closedRows.length !== 0 ) {
        // initially hide closed emissions.
        for (let row of closedRows) {
            row.style.display = 'none';
        }
        let filterSwitch = document.getElementById('flexSwitchCheckChecked');
        filterSwitch.addEventListener('change', function() {
            // solution to accessing bootstrap switch status from stack overflow:
            // https://stackoverflow.com/questions/65229118/how-to-check-switch-bootstrap-5-with-plain-javascript
            if (this.checked) {
                for (let row of closedRows) {
                    row.style.display = 'none';
                    filterText.innerText = 'Showing Open Emissions';
                }
            } else if (!this.checked){
                for (let row of closedRows) {
                    row.style.display = 'table-row';
                    filterText.innerText = 'Showing Open & Closed Emissions';
                }
            }
          });
    }
}
/**
 * Arrow function to present a confirm dialogue using the 
 * event source element inner text to determine text
 * to display. Defensive design in event of closing or 
 * deleting an emission.
 */
const confirmAction = (event) => {
    // how to get the event source from stack overflow:
    // https://stackoverflow.com/questions/10428562/how-to-get-javascript-event-source-element
    let eventSourceText = event.srcElement.innerText
    // switch the event source text to determine the text for the confirmation prompt.
    switch(eventSourceText) {
        case 'Close Emission':
            confirmText = 'Are you sure you want to close the emission?'
            break;
        case 'Delete Emission':
            confirmText = 'Are you sure you want to delete the emission? This action cannot be reversed'
            break;
        default:
          break;
      }
      if(!confirm(confirmText)) {
        event.preventDefault();
    }

}
/**
 * go back function activated by a button where the window is not 
 * represented in the nav bar items.
 */
function goBack() {
    window.location.replace(document.referrer);
}

const buttonDisabled = (event, closed) => {
    let eventSourceText = event.srcElement.innerText
    console.log(eventSourceText)
    console.log(closed)
    if (closed && eventSourceText === 'Close Emission') {
        alertText = `<p>This emission is already closed.</p>`
    }
    else{
    switch(eventSourceText) {
        case 'Close Emission':
            alertText = `<p>You do not have the necessary permissions to <strong>close</strong> an emission.\n Please contact your system administrator.</p>`
            break;
        case 'Delete Emission':
            alertText = `<p>You do not have the necessary permissions to <strong>delete</strong> an emission.\n Please contact your system administrator.</p>`
            break;
        case 'Add New Emission':
            alertText = `<p>You do not have the necessary permissions to <strong>add</strong> an emission.\n Please contact your system administrator.</p>`
            break;
        default:
          break;
      }
    }
      let alert = document.getElementById('alert-col')
      alert.innerHTML = `
      <div class="alert alert-warning alert-dismissible fade show shadow-lg shadow-primary" id="msg" role="alert">
      <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Warning or Error:">
      <use xlink:href="#exclamation-triangle-fill"/>
      </svg>
      ${alertText}
      <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
  </div>
      `
      setTimeout(function () {
        let messages = document.getElementById('msg');
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 4000);
}



// code for map implementation from google map documentation:
// https://developers.google.com/maps/documentation/javascript

let map;

async function initMap() {
  // The location of factory. In this instance I used an abandoned fish factory in Westport to demonstrate
  // functionaility of feature.   
  const position = { lat: 53.80185, lng: -9.55734 };
  // Request needed libraries.
  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");


  // The map, centered at factory
  map = new Map(document.getElementById("map"), {
    center: position,
      zoom: 19,
      heading: 22,
      tilt: 0,
      mapTypeId: 'satellite',
      mapId: "90f87356969d889c",
    });
// call add marker function and pass in detail taken from emission detail page.
    addMarker(latitude, longitude, markerTitle, imageUrl)
}
// function for adding marker once map has initialised. Taking arguments from 
// emission constants declared in emission detail html.
async function addMarker(latitude, longitude, title, url) {
    const { AdvancedMarkerElement, PinElement } = await google.maps.importLibrary("marker");
    const { Map, InfoWindow } = await google.maps.importLibrary("maps");

    const icon = document.createElement("div");
    icon.classList.add('glyph-icon')
    icon.innerHTML = '<i class="fa-solid fa-droplet"></i>';
    const faPin = new PinElement({
        glyph: icon,
        glyphColor: "#fafafa",
        background: "#dc3123",
        borderColor: "#fafafa",
      });
    const marker = new AdvancedMarkerElement({
        map: map,
        position: {lat: parseFloat(latitude), lng: parseFloat(longitude)},
        title: title,
        content: faPin.element,
      });
    
    const infoWindow = new InfoWindow();
    marker.addListener("gmp-click", function() {
    // const { target } = domEvent;
    infoWindow.close();
    infoWindow.setContent(marker.title + "<br><img width='200' src=" + url + ">");
    infoWindow.open(marker.map, marker);
    });
    marker.setMap(map)
}

/**
 * Adjust zoom of the map depending on screen size. 
 * Called on page load and when the window is resized.
 */
function adjustMapZoom(){
    if (window.innerWidth < 768) {
            map.setZoom(17.8)
       }
       else if ((window.innerWidth < 1200)) {
            map.setZoom(18.5)
       }
        else {
            map.setZoom(19)
        }
}