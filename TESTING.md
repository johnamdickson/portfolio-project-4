# Table of Contents
- [User Story Testing](#user-story-testing)
- [Validator Testing](#validator-testing)
  * [HTML](#html)
    + [Fixed Errors](#fixed-errors)
    + [Unfixed Errors](#unfixed-errors)
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

All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/) with the home page checked using address and every other page using page source text input. The results can be found in the table below:

**Page**|**First Pass**|**Warnings/Errors**|**Second Pass<br><sup><sub>(Post Fix)</sub></sup>**|**Screenshot**
:-----:|:-----:|:-----|:-----:|:-----:
 | index| ❌ |<sub>Warning: Consider adding a lang attribute to the html start tag to declare the language of this document. <br>Info: Trailing slash on void elements has no effect and interacts badly with unquoted attribute values. <br> Error: An img element must have an alt attribute, except under certain conditions.<br>Error: Stray end tag div.<br>Error: Stray start tag tr.<br>Error: The aria-labelledby attribute must point to an element in the same document.</sub>| ✅ |Home Page ![html_checker](TESTING-files/index-html-validator.png) 
 | emissions| ❌ |<sub>Error: An img element must have an alt attribute, except under certain conditions.<br>Error: Attribute value missing.<br>Error: End tag div seen, but there were open elements.<br>Error: No space between attributes.<br>Error: Bad value `${checkEmissionUrl}` for attribute href on element a: Illegal character in path segment: { is not allowed. <br> Error: Bad value `${allEmissionsUrl}` for attribute href on element a: Illegal character in path segment: { is not allowed.<br>Error: Stray end tag div.<br>Warning: Section lacks heading. Consider using h2-h6 elements to add identifying headings to all sections, or else use a div element instead for any cases where no heading is needed.<br>Error: The aria-labelledby attribute #must point to an element in the same document.</sub> | ✅|Emissions Page![html_checker](TESTING-files/emissions-html-validator.png) 
 |emission-detail| ❌ | <sub>Error: Element p not allowed as child of element button in this context. (Suppressing further errors from this subtree.) <br> Error: The element h4 must not appear as a descendant of the th element. <br> Error: The element h5 must not appear as a descendant of the th element.<br> Error: Duplicate attribute class.<br>Error: Stray end tag div.<br>Error: The aria-labelledby attribute must point to an element in the same document.<br>Error: Bad value 100% for attribute width on element img: Expected a digit but saw % instead.</sub>| ✅|Emissions Detail Page for FT-4100 ![html_checker](TESTING-files/emission-detail-html-validator.png) 
 |emission-checks | ❌ | <sub>Error: No space between attributes.<br>Warning: Section lacks heading. Consider using h2-h6 elements to add identifying headings to all sections, or else use a div element instead for any cases where no heading is needed.<br> Error: Bad value `${checkEmissionUrl}` for attribute href on element a: Illegal character in path segment: { is not allowed.<br> Error: Bad value `${allEmissionsUrl}` for attribute href on element a: Illegal character in path segment: { is not allowed.<br>Stray end tag div.<br>Error: The aria-labelledby attribute must point to an element in the same document.</sub>| ✅| Emission Checks Page ![html_checker](TESTING-files/emission-checks-html-validator.png) 
 | | | 
 | | | 
 | | | 
