
window.addEventListener('load', function () {
    startCarousel();
    errorCountdown();
    scrollButtons();

    // add event listener to each go back button that on click runs the code to 
    // return to previous page.
    let goBackButton = this.document.querySelectorAll('.go-back-btn');
    for (let button of goBackButton) {
        button.addEventListener("click", function(){
            window.location.replace(document.referrer);
        });
    }
    // add event listener to each button requiring a confirm action which calls that 
    // function from button click.
    let confirmActionButton = document.querySelectorAll('.confirm-action');
    for (let button of confirmActionButton) {
        button.addEventListener("click", confirmAction);
    }
    // add event listener to checks search input which calls the filter checks function
    // on key up
    let searchChecks = document.querySelector('#emission-check-search');
    if (searchChecks){
        searchChecks.addEventListener("keyup", filterChecks);
    }
    
});

window.addEventListener("DOMContentLoaded", function () {
    hideElements();
    updateChecksComplete();
    statusFilter();
    updateStatus();
});

window.addEventListener('resize', function (event) {
    hideElements();
    adjustMapZoom();
    updateStatus();
}, true);



// change to set interval to allow running more than once:
// https://stackoverflow.com/questions/70436333/settimeout-runs-only-once-then-not-working
setInterval(function () {
/**
 * Dismisses alerts after 4 seconds using setTimeout function.
 * Improve user experience so that routine alerts are automatically
 * dismissed 
 */
    if (document.getElementById('msg')) {
        let messages = document.getElementById('msg');
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }
}, 4000);
// set interval same for form message error alert
setInterval(function () {
    if (document.getElementById('form-msg')) {
        let messages = document.getElementById('form-msg');
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }
}, 4000);

function hideElements() {
/**
 * Hides elements depending on screen size.
 * On home page titles are hidden to improve responsive
 * design. On pages with tables, some columns/cells are hidden
 * or cells column/row span is altered.
 */
    let windowWidth = window.innerWidth;
    let descriptionCells = document.getElementsByClassName("description-cell");
    let hiddenCells = document.getElementsByClassName("hidden-col");
    let hiddenElements = document.getElementsByClassName("callout-hidden");
    let closeOutComments = document.getElementsByClassName('close-out-comments');
    let imageCells = document.getElementsByClassName('image-cell');
    for (let cell of hiddenCells) {
        if (windowWidth <= 982) {
            cell.style.display = 'none';
        } else if (windowWidth > 982){
            cell.style.display = 'table-cell';
            }
    }
    for (let cell of descriptionCells) {
        if (windowWidth <= 982) {
            cell.setAttribute('colspan', '4');
        }
        else if (windowWidth >982){
            cell.setAttribute('colspan', '3');
        }
    }
    for (let cell of imageCells) {
        if (windowWidth <= 982) {
            cell.setAttribute('rowspan', '2');
        }
        else if (windowWidth >982){
            cell.setAttribute('rowspan', '4');
        }
    }
    if (closeOutComments) {
        for(let cell of closeOutComments) {
            if (windowWidth <= 982) {
                cell.setAttribute('colspan', '1');
            }
            else if (windowWidth >982){
                cell.setAttribute('colspan', '2');
            }
        }
    }
    if (windowWidth <= 767) {
        for (let elements of hiddenElements) {
            elements.style.display = 'none';
        }

    } else {
        for (let elements of hiddenElements) {
            elements.style.display = 'block';
        }
    }
}

function updateChecksComplete() {
/**
 * Adds a fontawseome icon to home page html depending on element text.
 * For checks complete a checkmark icon with green background
 * is returned else a red x mark icon.
 */
    let checkStatus = document.getElementsByClassName("check_status");

    for (let check of checkStatus) {
        let className = check.className;
        if (check.innerText.includes("Checks Complete")) {
            // solution for fontawesome background from stack overflow:
            // https://stackoverflow.com/questions/26516353/font-awesome-background-color
            check.innerHTML = `<div class="checks-complete-td">
                                <p>
                                    <span class="fa-stack" style="vertical-align: top;">
                                        <i class="fas fa-circle fa-stack-2x"style="color: #FFFFFF;"></i>
                                        <i class="fa-solid fa-circle-check fa-stack-2x fa-inverse" style="color: #00D100;"></i>
                                    </span>
                                </p>
                                <p>Checks Complete</p>
                                </div>`;
                                
        } else if (check.innerText.includes("Outstanding")){
            check.innerHTML = `<div class="checks-complete-td">
                                <p>
                                    <span class="fa-stack" style="vertical-align: top;">
                                        <i class="fas fa-circle fa-stack-2x" style="color: #36454F;"></i>
                                        <i class="fa-solid fa-circle-xmark fa-stack-2x fa-inverse" style="color: #FFA500;"></i>
                                    </span>
                                </p>
                                <p>Checks Outstanding</p>
                                </div>`;
        } else if (check.innerText.includes("No Check")){
            check.innerHTML = `<div class="checks-complete-td">
            <p>
                <span class="fa-stack" style="vertical-align: top;">
                    <i class="fas fa-circle fa-stack-2x" style="color: #FFFFFF;"></i>
                    <i class="fa-solid fa-circle-exclamation fa-stack-2x fa-inverse" style="color: #BF181D;"></i>
                </span>
            </p>
            <p>No Checks \nCompleted Yet</p>
            </div>`;
        }
        if (className.includes('emission-detail-check_status')) {
            updateChecksCompleteClassName();
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
/**
 * Applies color formatting to status cells with green for open and red 
 * for closed.
 */
    if (document.getElementsByClassName('status-cell')) {
        let statusCells = document.getElementsByClassName('status-cell');
        for(let status of statusCells) {
            status.style.color = ('white');
            if (status.innerText.includes('Open')) {
                status.style.backgroundColor = ('green');
            } else if (status.innerText.includes('Closed')){
                status.style.backgroundColor = ('red');
            }
        }
    }
}

const showModal = (data) => {
/**
 * Adds modal to the DOM and updates with JSON data passed in
 * from index html.
 */
    let emissionArray = JSON.parse(data);
    // solution to passing django url from javascript from stack overflow:
    // https://stackoverflow.com/questions/37311042/call-django-urls-inside-javascript-on-click-event
    let allEmissionsUrl = document.getElementById('emissionUrl').getAttribute('data-url');
    // let checkEmissionUrl = document.getElementById('emissionCheckUrl').getAttribute('data-url');
    const modalItem = document.getElementById('emissionModalCenter');
    modalItem.innerHTML = ` <div class="modal-dialog modal-dialog-centered" role="document">
                                    <div class="modal-content">
                                        <div class="modal-header">
                                            <h4 class="modal-title" id="emissionModalLongTitle">${emissionArray.title}</h4>
                                            <button type="button" class="btn-close" data-dismiss="modal" aria-label="Close">
                                            </button>
                                        </div>
                                                <img class="modal-img" src="${emissionArray.imageUrl}">
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


const emissionModal = (data, page, checkId, user, superuser) => {
/**
 * Adds modal to the DOM and updates with JSON data passed in
 * from emissions.html or emission-checks.html.
 */

// delcare constants from JSON, checkId
    const checkIdInt = parseInt(checkId);
    const parsedData = JSON.parse(data);
    const date = new Date(parsedData.date_checked);
    const time = date.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" })
    // working with Javascript date options with support from this tutorial:
    // https://www.influxdata.com/blog/how-get-convert-format-javascript-date-timestamp/#:~:text=Once%20you%20have%20a%20Date,the%20hour%2C%20and%20so%20on.
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    const formattedDate = date.toLocaleDateString('en-GB', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
//  delcare constants for modal iteself, title and body and assign detail as innerText to title and body.
    const modalItem = document.getElementById('emissionModal');
    let modalTitle = document.getElementById('emissionModalTitle');
    modalTitle.innerText = `Emission: ${parsedData.title}`;
     // check if the page is emission-check and add formatted check date to the modal body.
    let modalBody = document.getElementById('emissionModalBody');
    if (page === 'emission-check') {
        modalBody.innerHTML = `${parsedData.title} Emission Check completed<br>
                                on <strong>${formattedDate}</strong> at <strong>${time}</strong>
                                <br>Please make a selection from the options below:`;
    }
    else {
        modalBody.innerText = 'Please make a selection from the options below:';
    }
   
// get submit check button and assign inner HTML with emission title and icon
    let submitEmissionCheckButton = document.getElementById('emission-check-a');
    if (submitEmissionCheckButton) {
        submitEmissionCheckButton.innerHTML = `<p>Submit a Check for\n${parsedData.title}</p><i class="fa-solid fa-clipboard-list"></i>`;
    }
// get emission detail button (only in emission.html hence logic to check) and assign href for accessing emission
// detail with innerHTML set as per submit check above.
    let emissionDetailButton = document.getElementById('emission-detail-a');
    if (emissionDetailButton) {
        emissionDetailButton.setAttribute('href' ,  `/${parsedData.slug}/`);
        emissionDetailButton.innerHTML = `<p>Go to Emission Detail Page for\n${parsedData.title}</p><i class="fa-solid fa-circle-info"></i>`;
    }
// get emission check edit button (only in emission-checks.html hence logic to check) and assign href for accessing emission
// detail with innerHTML set as per submit check above.
    let emissionCheckEditButton = document.getElementById('emission-edit-a');
    if (emissionCheckEditButton) {
        emissionCheckEditButton.innerHTML = `<p>Edit ${parsedData.title} Emission Check</p><i class="fa-solid fa-pen-to-square"></i>`;
    }
    let emissionCheckDeleteButton = document.getElementById('emission-check-delete-a');
    if (emissionCheckDeleteButton) {
        emissionCheckDeleteButton.addEventListener("click", confirmAction);
        emissionCheckDeleteButton.setAttribute ('href', `/delete-check/${parsedData.slug}/${checkIdInt}`);
        emissionCheckDeleteButton.innerHTML = `<p>Delete ${parsedData.title} Check</p><i class="fa-solid fa-trash-can"></i>`;
    }

        // select buttons for emission detail page.
        if (page === 'emission' && parsedData.status === 'Closed'){
                // set hidden input href attribute to slug of the emission passed into this function.
                submitEmissionCheckButton.setAttribute('href' , '#');
                submitEmissionCheckButton.onclick = emissionClosedFunction;
                // add btn-unavailable class when the emission is closed.
                submitEmissionCheckButton.classList.add('btn-unavailable');
          } else if (page === 'emission' && parsedData.status === 'Open'){
                // set hidden input href attribute to slug of the emission passed into this function.
                submitEmissionCheckButton.setAttribute('href' , `/add-check/${parsedData.slug}/`);
        } 
        // select add check button for emission-check page based on emission status
        if (page === 'emission-check' && parsedData.emission_status === 'Closed'){
            submitEmissionCheckButton.setAttribute('href' , '#');
            submitEmissionCheckButton.onclick = emissionClosedFunction;
            submitEmissionCheckButton.classList.add('btn-unavailable');   
        } else if (page === 'emission-check' && parsedData.emission_status === 'Open'){
            submitEmissionCheckButton.setAttribute('href' , `/add-check/${parsedData.slug}/`);
        }

        // select edit check button for emission check page based on emission status being closed.
        if (page =='emission-check' && parsedData.emission_status == 'Closed') {
            emissionCheckEditButton.setAttribute('href', `#`);
            emissionCheckEditButton.classList.add('btn-unavailable');
            emissionCheckEditButton.onclick = emissionClosedFunction;
        // select edit check button for emission check page based on checked by and less than 24 hours parameters.
        } else if (page === 'emission-check' && parsedData.check_less_than_24 && (parsedData.checked_by === user || superuser === 'True') && parsedData.emission_status == 'Open') {
            emissionCheckEditButton.setAttribute('href', `/edit-check/${parsedData.slug}/${checkIdInt}`);
         // select edit check button for emission check page based on more than 24 hours parameters but allowing superuser to complete action.
        } else if (page === 'emission-check' && !parsedData.check_less_than_24 && superuser === 'True' && parsedData.emission_status == 'Open') {
            emissionCheckEditButton.setAttribute('href', `/edit-check/${parsedData.slug}/${checkIdInt}`);
        } 
         // select edit check button for emission check page for all other conditions.
        else if (page === 'emission-check') {
            emissionCheckEditButton.setAttribute('href', `#`);
            emissionCheckEditButton.classList.add('btn-unavailable');
            emissionCheckEditButton.onclick = emissionClosedFunction;
            }
        

// create instance of bootstrap modal and instantiate.
    let emissionModal = new bootstrap.Modal(modalItem);
    emissionModal.show();

// helper function
    function emissionClosedFunction(event) {
        const eventText = event.srcElement.innerText;
        emissionModal.hide();
        if (eventText.includes('Emission Check') && parsedData.emission_status === 'Closed'){
            buttonDisabled('edit', true);
        } 
        else if (eventText.includes('Emission Check') && !parsedData.check_less_than_24) {
            buttonDisabled('edit', false);
        } 
        else if (eventText.includes('Emission Check') && parsedData.checked_by !== user) {
            buttonDisabled('edit_not_user', false);
        }
        else {
            buttonDisabled('submit', true);
        }
    }
};

// functionality below for carousel from:
// https://www.codeply.com/p/0CWffz76Q9

function startCarousel() {
    let items = document.querySelectorAll('.carousel .carousel-item');
    items.forEach((el) => {
        const minPerSlide = 3;
        let next = el.nextElementSibling;
        for (var i = 1; i < minPerSlide; i++) {
            if (!next) {
                // wrap carousel by using first child
                next = items[0];
            }
            let cloneChild = next.cloneNode(true);
            el.appendChild(cloneChild.children[0]);
            next = next.nextElementSibling;
        }
    });
}

/**
 * Function to filter emissions table for open/closed
 * status. Default selection is open only with toggle
 * switch position determining filter.
 */
function statusFilter() {
    let closedRows = document.getElementsByClassName("closed-row");
    let filterText = document.getElementById("column-filter");
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

const confirmAction = (event) => {
/**
 * Arrow function to present a confirm dialogue using the 
 * event source element inner text or class list to determine text
 * to display. Defensive design in event of closing,editing or 
 * deleting an emission.
 */
    // how to get the event source from stack overflow:
    // https://stackoverflow.com/questions/10428562/how-to-get-javascript-event-source-element
    let eventSourceText = event.srcElement.innerText;
    let confirmText;
    // use of value to access text area text solution from stack overflow:
    //  https://stackoverflow.com/questions/16013899/javascript-get-contents-of-textarea-textcontent-vs-innerhtml-vs-innertext
    // switch the event source text to determine the text for the confirmation prompt.
    if (eventSourceText === "Close Emission") {
        confirmText = 'Are you sure you want to close the emission?';
    } else if (eventSourceText === 'Delete Emission') {
        confirmText = 'Are you sure you want to delete the emission? This action cannot be reversed';
    } else if (eventSourceText === 'Edit Check') {
        let editCommentText = document.getElementById('editComments').value;
        confirmText = `Please confirm you are happy with the edit comments: \n
                        ${editCommentText}`;
    } else if (eventSourceText.includes('Delete') && eventSourceText.includes('Check')) {
        confirmText = 'Are you sure you want to delete the check? This action cannot be reversed';
    }
    if(!confirm(confirmText)) {
        event.preventDefault();
    }
};

function goHome() {
/**
 * go home function activated by a button used in HTTP status code
 * pages.
 */
    document.location.href="/";
}

const buttonDisabled = (type, closed) => {
/**
 * Function to read event text and determine appropriate response
 * in the alert col by adjusting the inner html.
 */
    let alert = document.getElementById('alert-col');
    let alertText;
    if (closed && type === 'close') {
        alertText = `<p>This emission is already closed.</p>`;
    } else if (closed && type === 'submit') {
        alertText = `<p>This emission is closed so no further checks are required.</p>`;
    } else if (closed && type === 'edit') {
        alertText = `<p>This emission is closed so no further edits are allowed.</p>`;
    }
      
    else{
    // switch button type argument to determine what text the alert should show to user.
    switch(type) {
        case 'close':
            alertText = `<p>You do not have the necessary permissions to <strong>close</strong> an emission.\n Please contact your system administrator.</p>`;
            break;
        case 'delete':
            alertText = `<p>You do not have the necessary permissions to <strong>delete</strong> an emission/check.\n Please contact your system administrator.</p>`;
            break;
        case 'edit':
            alertText = `<p>A check can only be <strong>edited</strong> for <strong>up to 24 hours</strong> after submission.</p>`;
            break;
        case 'edit_not_user':
            alertText = `<p>Only the user who <strong>created</strong> this emission or a superuser can <strong>edit</strong> it.</p>`;
            break;
        case 'add':
            alertText = `<p>You do not have the necessary permissions to <strong>add</strong> an emission.\n Please contact your system administrator.</p>`;
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
      `;
};


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
        addMarker();
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
    const { InfoWindow } = await google.maps.importLibrary("maps");

    const icon = document.createElement("div");
    icon.classList.add('glyph-icon');
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
    marker.content.classList.add('drop');
    const markerContentParent = marker.content.parentElement;
    markerContentParent.classList.add('grow');

    const infoWindow = new InfoWindow();

    marker.addListener("click", function() {
        infoWindow.close();
        infoWindow.setContent(`<div class="marker-title"><h5>${marker.title}</h5></div>` + "<img width='200' src=" + url + ">");
        infoWindow.open(marker.map, marker);
      });

    marker.setMap(map);
}

initMap();

function adjustMapZoom(){
/**
 * Adjust zoom of the map depending on screen size. 
 * Called on page load and when the window is resized.
 */

    if (document.getElementById("map")){
        if (window.innerWidth < 768) {
            map.setZoom(17.8);
    }
    else if ((window.innerWidth < 1200)) {
            map.setZoom(18.5);
    }
        else {
            map.setZoom(19);
        }
    }
}

// solution to filtering table from Stack Overflow:
// https://stackoverflow.com/questions/51187477/how-to-filter-a-html-table-using-simple-javascript

const filterChecks = () => {
/**
 * Funciton to dynamically filter checks table based 
 * upon text input into search filed.
 */
    const columns = [
      { name: 'Emission', index: 0, isFilter: true },
      { name: 'Comments', index: 1, isFilter: false },
      { name: 'Check Status', index: 2, isFilter: false },
      { name: 'Checked By', index: 3, isFilter: true },
    ];
    const filterColumns = columns.filter(c => c.isFilter).map(c => c.index);
    const trs = document.querySelectorAll(`#emission-checks-table tr:not(.header)`);
    const filter = document.querySelector('#emission-check-search').value;
    const regex = new RegExp((filter), 'i');
    const isFoundInTds = td => regex.test(td.innerHTML);
    const isFound = childrenArr => childrenArr.some(isFoundInTds);
    const setTrStyleDisplay = ({ style, children }) => {
      style.display = isFound([
        ...filterColumns.map(c => children[c]) // <-- filter Columns
      ]) ? '' : 'none';
    };
    
    trs.forEach(setTrStyleDisplay);
  };

const errorCountdown = () => {
/**
 * Function to countdown and display back to user for status code error
 * pages. Solution from codepen:
 * https://codepen.io/joshua-golub/pen/LYYKrKg
 */
    let timeLeft = 10;
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
    function countdown() {
        timeLeft--;
        document.getElementById("error-timer").innerText = String( timeLeft );
        if (timeLeft > 0) {
            setTimeout(countdown, 1000);
        } else {
            goHome();
        }
    }
    if (document.getElementById("error-timer")){
        setTimeout(countdown, 1000);
    }
  };
    

    // use of jquery to utilise smooth animated scrolling in tables
    // https://stackoverflow.com/questions/1144805/scroll-to-the-top-of-the-page-using-javascript


function scrollButtons() {
/**
 * Function to allow for user to scroll to top or 
 * bottom of table using up/down chevron buttons.
 * Buttons opacity changes depending if they are 
 * maxed out at the particular position. 
 */
    
    const tables = document.getElementsByClassName('table-fixed-head');
    let table = tables[0];
    // assign css to elements using jquery:
    // https://www.codecademy.com/learn/learn-jquery/modules/learn-jquery-style-methods/cheatsheet
    $('#to-top').css({
        opacity: 0.5
    });
    $("#to-bottom").on('click', function() {

        $(table).animate({ scrollTop: table.scrollHeight}, "slow");
    });

    $("#to-top").on('click', function() {
        $(table).animate({ scrollTop: 0}, "slow");

    });
    // scroll function from jquery docs:
    // https://api.jquery.com/scroll/
    $(table).on('scroll', function(){
        let tableHeight = (table.scrollHeight) - (table.clientHeight);
        // dealing with fractional part of scrollTop function
        if (Math.round($(table).scrollTop()) >= tableHeight) {
            $('#to-top').css({
                opacity: 0.9
            });
            $('#to-bottom').css({
                opacity: 0.5
            });
        } else if ($(table).scrollTop() === 0) {
            $('#to-top').css({
                opacity: 0.5
            });
            $('#to-bottom').css({
                opacity: 0.9
            });
        } else {
            $('#to-top').css({
                opacity: 0.9
            });
            $('#to-bottom').css({
                opacity: 0.9
            });
        }
    });
}

// solution to console error from stack overflow:
// https://stackoverflow.com/questions/66349868/jest-unit-testing-module-export-error-in-browser-console
var module = module || {};
if (module) {module.exports = errorCountdown;}