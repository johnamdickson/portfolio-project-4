# Table of Contents
- [User Story Testing](#user-story-testing)
- [Validator Testing](#validator-testing)
  * [HTML](#html)
  * [CSS](#css)
  * [Javascript](#javascript)
  * [Python](#python)
  * [Lighthouse](#lighthouse)
- [Browser Testing](#browser-testing)
- [Device Testing](#device-testing)
- [Automated Testing](#automated-testing)
- [Manual Testing](#manual-testing)
- [Bugs](#bugs)
  * [Fixed Bugs](#fixed-bugs)

  * [Unfixed bugs:](#unfixed-bugs-)


## Validator Testing

### HTML

All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/) with the home page checked using address and every other page using page source text input. The text input was obtained by navaigating to the page to test and then right clicking on the window. From the menu, the view page source option was selected which opened a new tab containing the DOM for the page. The test was then performed by copying and pasting the code into the text input field in the validator.

Results for all HTML pages can be found in the table below:

**Page**|**First Pass**|**Warnings/Errors**|**Second Pass<br><sup><sub>(Post Fix)</sub></sup>**|**Screenshot**
:-----:|:-----:|:-----|:-----:|:-----:
 | index| ❌ |<sub>Warning: Consider adding a lang attribute to the html start tag to declare the language of this document. <br>Info: Trailing slash on void elements has no effect and interacts badly with unquoted attribute values. <br> Error: An img element must have an alt attribute, except under certain conditions.<br>Error: Stray end tag div.<br>Error: Stray start tag tr.<br>Error: The aria-labelledby attribute must point to an element in the same document.</sub>| ✅ |![html_checker](TESTING-files/html-validator/index.png) 
 | emissions| ❌ |<sub>Error: An img element must have an alt attribute, except under certain conditions.<br>Error: Attribute value missing.<br>Error: End tag div seen, but there were open elements.<br>Error: No space between attributes.<br>Error: Bad value `${checkEmissionUrl}` for attribute href on element a: Illegal character in path segment: { is not allowed. <br> Error: Bad value `${allEmissionsUrl}` for attribute href on element a: Illegal character in path segment: { is not allowed.<br>Error: Stray end tag div.<br>Warning: Section lacks heading. Consider using h2-h6 elements to add identifying headings to all sections, or else use a div element instead for any cases where no heading is needed.<br>Error: The aria-labelledby attribute #must point to an element in the same document.</sub> | ✅|![html_checker](TESTING-files/html-validator/emissions.png) 
 |emission-detail| ❌ | <sub>Error: Element p not allowed as child of element button in this context. (Suppressing further errors from this subtree.) <br> Error: The element h4 must not appear as a descendant of the th element. <br> Error: The element h5 must not appear as a descendant of the th element.<br> Error: Duplicate attribute class.<br>Error: Stray end tag div.<br>Error: The aria-labelledby attribute must point to an element in the same document.<br>Error: Bad value 100% for attribute width on element img: Expected a digit but saw % instead.</sub>| ✅|![html_checker](TESTING-files/html-validator/emission-detail.png) 
 |emission-checks | ❌ | <sub>Error: No space between attributes.<br>Warning: Section lacks heading. Consider using h2-h6 elements to add identifying headings to all sections, or else use a div element instead for any cases where no heading is needed.<br> Error: Bad value `${checkEmissionUrl}` for attribute href on element a: Illegal character in path segment: { is not allowed.<br> Error: Bad value `${allEmissionsUrl}` for attribute href on element a: Illegal character in path segment: { is not allowed.<br>Stray end tag div.<br>Error: The aria-labelledby attribute must point to an element in the same document.</sub>| ✅| ![html_checker](TESTING-files/html-validator/emission-checks.png) 
 | login | ❌ |<sub>Error: Stray end tag div.<br> Error: Element p not allowed as child of element button in this context. (Suppressing further errors from this subtree.)<br> Error: Bad value for attribute action on element form: Must be non-empty.<br>Error: End tag main seen, but there were open elements.<br>Error: Unclosed element div.</sub> | ✅ |![html_checker](TESTING-files/html-validator/login.png) 
 | logout|❌  | <sub>Error: End tag main seen, but there were open elements.<br>Error: Unclosed element div.</sub>|✅ |![html_checker](TESTING-files/html-validator/logout.png) 
 | signup| ❌| <sub>Error: Stray end tag div.<br>Error: Duplicate ID help-text.<br>Error: End tag main seen, but there were open elements.<br>Error: Unclosed element div.</sub>|✅ |![html_checker](TESTING-files/html-validator/signup.png) 
 | add-emission| ❌| <sub>Error: Bad value for attribute action on element form: Must be non-empty.<br>Error: End tag main seen, but there were open elements.<br>Error: Unclosed element div.<br>Error: Stray end tag a.</sub>|✅ |![html_checker](TESTING-files/html-validator/add-emission.png) 
 | add-check| ❌| <sub>Error: Bad value for attribute action on element form: Must be non-empty.<br> Error: End tag main seen, but there were open elements.<br>Error: Unclosed element div.</sub>|✅ |![html_checker](TESTING-files/html-validator/add-check.png) 
 | close-emission| ✅| N/A| N/A | ![html_checker](TESTING-files/html-validator/close-emission.png) 
   | edit-check| ✅| N/A| N/A | ![html_checker](TESTING-files/html-validator/edit-check.png)  
  | 400 error| ✅| N/A| N/A | ![html_checker](TESTING-files/html-validator/400.png)
  | 403 error| ✅| N/A| N/A | ![html_checker](TESTING-files/html-validator/403.png) 
  | 404 error| ✅| N/A| N/A | ![html_checker](TESTING-files/html-validator/404.png) 
  | 500 error| ✅| N/A| N/A | ![html_checker](TESTING-files/html-validator/500.png) 

### CSS

The site was run through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/). There were 220 warnings assoiated with Bootstrap CSS and 6 in static CSS file associated with webkit code. These warnings are unavoidable in the validator because they are vendor extensions. However looking at feedback given to other students on Slack who had a similar issue, it appears to be safe to ignore these warnings. 

The warnings and errors that are detailed in the table below reflect problems within the static CSS file and were duly corrected.

**First Pass**|**Errors**|**Warnings**|**Second Pass<br><sup><sub>(Post Fix)</sub></sup>**|**Screenshot**
:-----:|:-----|:-----|:-----:|:-----:
| ❌|Property opaity doesn't exist. The closest matching property name is opacity : 0 <br>Property size doesn't exist. The closest matching property name is resize : 50px<br>Property size doesn't exist. The closest matching property name is resize : 50px|.go-back-btn	Same color for background-color and color<br> .go-back-button Same color for background-color and border-color|✅|![css_checker](TESTING-files/css-validator/css-validator.png) 
