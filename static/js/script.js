
window.addEventListener('load', function () {
    startCarousel()
    errorCountdown()
})

window.addEventListener("DOMContentLoaded", function () {
    hideElements()
    updateChecksComplete()
    statusFilter()
    updateStatus()
});

window.addEventListener('resize', function (event) {
    hideElements()
    adjustMapZoom()
    updateStatus()
}, true);


/**
 * Dismisses alerts after 4 seconds using setTimeout function.
 * Improve user experience so that routine alerts are automatically
 * dismissed 
 */
setTimeout(function () {
    if (document.getElementById('msg')) {
        let messages = document.getElementById('msg');
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }
}, 4000);

/**
 * Hides elements depending on screen size.
 * For example, on home page titles are hidden to improve responsive
 * design. 
 */
function hideElements() {
    let windowWidth = window.innerWidth;
    let descriptionCells = document.getElementsByClassName("description-cell")
    let hiddenCells = document.getElementsByClassName("hidden-col")
    let hiddenElements = document.getElementsByClassName("callout-hidden");
    for (let cell of hiddenCells) {
        if (windowWidth <= 982) {
            cell.style.display = 'none'
        } else if (windowWidth > 982){
            cell.style.display = 'table-cell'
            }
    }
    for (let cell of descriptionCells) {
        if (windowWidth <= 982) {
            cell.setAttribute('colspan', '2')
        }
        else if (windowWidth >982){
            cell.setAttribute('colspan', '3')
        }
    }
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

function updateStatus() {
    if (document.getElementsByClassName('status-cell')) {
        let statusCells = document.getElementsByClassName('status-cell');
        for(let status of statusCells) {
            if (status.innerText === 'Open') {
                status.style.backgroundColor = ('green');
                status.style.color = ('white');
            } else if (status.innerText === 'Closed'){
                status.style.backgroundColor = ('red');
                status.style.color = ('white');
            }
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
    // let checkEmissionUrl = document.getElementById('emissionCheckUrl').getAttribute('data-url');
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
                                            <a href= "add-check/${emissionArray.slug}/" class="btn">Submit ${emissionArray.title} Emission Check<i class="fa-solid fa-clipboard-list"></i>
                                            </a>
                                            <a href="/${emissionArray.slug}/" class="btn">Go To Emission Detail Page<i class="fa-solid fa-circle-info"></i></a>
                                            <a href="${allEmissionsUrl}" class="btn">Go To All Emissions Page<i class="fa-solid fa-table-list"></i></a>
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
const emissionModal = (data, page, checkId, user, superuser) => {
    const checkIdInt = parseInt(checkId)
    const parsedData = JSON.parse(data)
    console.log(parsedData.status)
    console.log(page)
    const modalItem = document.getElementById('emissionModal');
    document.getElementById('emissionModalTitle').innerText = `Emission: ${parsedData.title}`;
    document.getElementById('emissionModalBody').innerText = 'Please make a selection from the options below:';
    let checkButton = document.getElementById('emission-check-a')
    checkButton.innerHTML = `Submit a Check for\n${parsedData.title}<i class="fa-solid fa-clipboard-list"></i>`

    let emissionDetail = document.getElementById('emission-detail-a')
    if (emissionDetail) {
        emissionDetail.setAttribute('href' ,  `/${parsedData.slug}/`)
        emissionDetail.innerHTML = `Go to Emission Detail Page for\n${parsedData.title}<i class="fa-solid fa-circle-info"></i>`
    }
    let emissionEdit = document.getElementById('emission-edit-a')
    if (emissionEdit) {
        
    }

        // select buttons for emission detail page.
        if (page === 'emission' && parsedData.status === 'Closed'){
                // set hidden input href attribute to slug of the emission passed into this function.
                console.log('closed')
                checkButton.setAttribute('href' , '#')
                checkButton.onclick = emissionClosedFunction
                // add btn-unavailable class when the emission is closed.
                checkButton.classList.add('btn-unavailable')
          } else if (page === 'emission' && parsedData.status === 'Open'){
                // set hidden input href attribute to slug of the emission passed into this function.
                checkButton.setAttribute('href' , `/add-check/${parsedData.slug}/`)
        // select add check button for emission-check page based on emission status
        } else if (page === 'emission-check' && parsedData.emission_status === 'Closed'){
            checkButton.setAttribute('href' , '#')
            checkButton.onclick = emissionClosedFunction
            checkButton.classList.add('btn-unavailable')    
        } else if (page === 'emission-check' && parsedData.emission_status === 'Open'){
            checkButton.setAttribute('href' , `/add-check/${parsedData.slug}/`)
        }
        // select edit check button for emission check page based on checked by and less than 24 hours parameters.
        if (page === 'emission-check' && parsedData.check_less_than_24 && (parsedData.checked_by === user || superuser === 'True') && parsedData.emission_status == 'Open') {
            emissionEdit.setAttribute('href', `/edit-check/${parsedData.slug}/${checkIdInt}`)
        } else if (page === 'emission-check'){
            emissionEdit.setAttribute('href', `#`)
            emissionEdit.classList.add('btn-unavailable')
            emissionEdit.onclick = emissionClosedFunction
        }

    let emissionModal = new bootstrap.Modal(modalItem);
    emissionModal.show();

    function emissionClosedFunction(event) {
        console.log(parsedData.emission_status)
        eventText = event.srcElement.innerText
        emissionModal.hide()
        if (eventText === 'Edit Emission Check' && parsedData.emission_status === 'Closed'){
            
            buttonDisabled('edit', true)
        } 
        else if (eventText === 'Edit Emission Check' && parsedData.checked_by !== user) {
            // emissionModal.hide()
            buttonDisabled('edit_not_user', false)
        }
        else if (eventText === 'Edit Emission Check') {
            
            // emissionModal.hide()
            buttonDisabled('edit', false)
        } 
        else {
            // emissionModal.hide()
            buttonDisabled('submit', true)
        }
    }
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
                    updateStatus();
                }
            }
          });
    }
    
}
/**
 * Arrow function to present a confirm dialogue using the 
 * event source element inner text or class list to determine text
 * to display. Defensive design in event of closing or 
 * deleting an emission.
 */
const confirmAction = (event) => {
    // how to get the event source from stack overflow:
    // https://stackoverflow.com/questions/10428562/how-to-get-javascript-event-source-element
    let eventSourceText = event.srcElement.innerText;
    // use of value to access text area text solution from stack overflow:
    //  https://stackoverflow.com/questions/16013899/javascript-get-contents-of-textarea-textcontent-vs-innerhtml-vs-innertext
    // switch the event source text to determine the text for the confirmation prompt.

    if (eventSourceText === "Close Emission") {
        confirmText = 'Are you sure you want to close the emission?'
    } else if (eventSourceText === 'Delete Emission') {
        confirmText = 'Are you sure you want to delete the emission? This action cannot be reversed'
    } else if (eventSourceText === 'Edit Check') {
        let editCommentText = document.getElementById('editComments').value;
        confirmText = `Please confirm you are happy with the edit comments: \n
                        ${editCommentText}`
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
/**
 * go home function activated by a button used in HTTP status code
 * pages.
 */
function goHome() {
    document.location.href="/";
}
/**
 * Function to read event text and determine appropriate response
 * in the alert col by adjusting the inner html.
 */
const buttonDisabled = (type, closed) => {
    let alert = document.getElementById('alert-col')
    if (closed && type === 'close') {
        alertText = `<p>This emission is already closed.</p>`
    } else if (closed && type === 'submit') {
        alertText = `<p>This emission is closed so no further checks are required.</p>`
    } else if (closed && type === 'edit') {
        alertText = `<p>This emission is closed so no further edits are allowed.</p>`
    }

    else{
    switch(type) {
        case 'close':
            alertText = `<p>You do not have the necessary permissions to <strong>close</strong> an emission.\n Please contact your system administrator.</p>`
            break;
        case 'delete':
            alertText = `<p>You do not have the necessary permissions to <strong>delete</strong> an emission/check.\n Please contact your system administrator.</p>`
            break;
        case 'edit':
            alertText = `<p>A check can only be <strong>edited</strong> for <strong>up to 24 hours</strong> after submission.</p>`
            break;
        case 'edit_not_user':
            alertText = `<p>Only the user who <strong>created</strong> this emission or a superuser can <strong>edit</strong> it.</p>`
            break;
        case 'add':
            alertText = `<p>You do not have the necessary permissions to <strong>add</strong> an emission.\n Please contact your system administrator.</p>`
            break;
        default:
          break;
      }
    }
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
        if (document.getElementById('msg')){
            let messages = document.getElementById('msg');
            let alert = new bootstrap.Alert(messages);
            alert.close();
        }
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
  if (document.getElementById("map")){
    map = new Map(document.getElementById("map"), {
        center: position,
          zoom: 19,
          heading: 22,
          tilt: 0,
          mapTypeId: 'satellite',
          mapId: "90f87356969d889c",
        });
    // call add marker function.
        addMarker()
  }
}

// function for adding marker once map has initialised. Taking arguments from 
// emission constants declared in emission detail html.
async function addMarker() {
    // obtain data from constants declared in HTML containing Django variables:
    // https://www.django-antipatterns.com/antipattern/rendering-into-javascript.html
    const lat = JSON.parse(document.getElementById('latitudeJson').textContent);
    const lng = JSON.parse(document.getElementById('longitudeJson').textContent);
    const title = JSON.parse(document.getElementById('titleJson').textContent);
    const url = JSON.parse(document.getElementById('imageUrlJson').textContent);

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
        position: {lat: parseFloat(lat), lng: parseFloat(lng)},
        title: title,
        content: faPin.element,
      });
    //   add drop class for css animation
    marker.content.classList.add('drop')
    const markerContentParent = marker.content.parentElement
    markerContentParent.classList.add('grow')

    const infoWindow = new InfoWindow();

    marker.addListener("click", function() {
        infoWindow.close();
        infoWindow.setContent(`<div class="marker-title"><h5>${marker.title}</h5></div>` + "<img width='200' src=" + url + ">");
        infoWindow.open(marker.map, marker);
      });

    marker.setMap(map)
}

initMap()
/**
 * Adjust zoom of the map depending on screen size. 
 * Called on page load and when the window is resized.
 */
function adjustMapZoom(){
if (document.getElementById("map")){
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
}

// solution to filtering table from Stack Overflow:
// https://stackoverflow.com/questions/51187477/how-to-filter-a-html-table-using-simple-javascript

const filterChecks = () => {
    const columns = [
      { name: 'Emission', index: 0, isFilter: true },
      { name: 'Comments', index: 1, isFilter: false },
      { name: 'Check Status', index: 2, isFilter: false },
      { name: 'Checked By', index: 3, isFilter: true },
    ]
    const filterColumns = columns.filter(c => c.isFilter).map(c => c.index)
    const trs = document.querySelectorAll(`#emission-checks-table tr:not(.header)`)
    const filter = document.querySelector('#emission-check-search').value
    const regex = new RegExp((filter), 'i')
    const isFoundInTds = td => regex.test(td.innerHTML)
    const isFound = childrenArr => childrenArr.some(isFoundInTds)
    const setTrStyleDisplay = ({ style, children }) => {
      style.display = isFound([
        ...filterColumns.map(c => children[c]) // <-- filter Columns
      ]) ? '' : 'none'
    }
    
    trs.forEach(setTrStyleDisplay)
  }

/**
 * Function to countdown and display back to user for status code error
 * pages. Solution from codepen:
 * https://codepen.io/joshua-golub/pen/LYYKrKg
 */
const errorCountdown = () => {
    let timeLeft = 10
    // check if the error-code is 400 or 500 assign 60 to timeLeft based on 
    // fact that errors are not related to wrong page or forbidden so a 10 second
    // timer to go back to home page would be excessive.
    if (document.getElementById("error-heading")) {
        timeLeft = 60;
        document.getElementById("error-timer").innerText = '60';
    }
    else {
        timeLeft = 10;
    }

    if (document.getElementById("error-timer")){
        function countdown() {
            timeLeft--;
            document.getElementById("error-timer").innerText = String( timeLeft );
            if (timeLeft > 0) {
                setTimeout(countdown, 1000);
            } else {
                goHome()
            }
        };
        setTimeout(countdown, 1000);
    }

  }