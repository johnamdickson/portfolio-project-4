
# <img src="static/images/favicon.png"  width="40" height="40">  &nbsp;Emissions Monitoring Tool

Emissions Monitoring Tool is an application for industrial clients to monitor, verify and report any unwanted emissions that do not neccesitate an immediate shutdown to repair. .

This application is showcasing Full Stack Frameworks for Project Portfolio 4 and can be accessed by following this [link.](https://emissions-monitoring-tool-99fd7318f662.herokuapp.com/)

![Responsive Mockup Screenshot](README-files/am-i-responsive.png)

## Contents
<a name="contents"></a>

- [UX](#ux)
  - [Strategy](#strategy)
    - [User Stories](#user-stories)
  - [Scope](#scope)
    - [Essential Content](#essential-content)
    - [Optional Content](#optional-content)
  - [Structure](#structure)
  - [Skeleton](#structure)
    - [Wireframes](#wireframes)
  - [Surface(Design)](#surface-design)
    - [Colour Scheme](#colour-scheme)
    - [Imagery](#imagery)
    - [Favicon](#favicon)
    - [Typography](#typography)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Deploying to Heroku](#deploying-to-heroku)
  - [Forking the GitHub Repository](#forking-the-github-repository)
  - [Making a Local Clone](#making-a-local-clone)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)

## UX
### Strategy
The objective of the site is to allow user registration, role based permissions, adding new emissions and performing regular checks on those emissions all whilst displaying the data to the user in an engaging and responsive manner.

#### Agile Methodology

The Agile Project Management approach was used in this project. Eleven epics were completed each with their own varying number of user stories. Over the course of the project, fifteen sprints were completed, selecting user stories based on a timebox value of no more than 8 per sprint. The epics, user stories and also bugs were all categorised using the Github Project Kanban board feature, which can be found [here.](https://github.com/users/johnamdickson/projects/2/views/1)

#### User Stories

The user stories were collated into eleven epics. Each user story was assigned to either the user, site admin, super user or site owner. The user stories were broken down into tasks and acceptance criteria which can be reviewed by clicking on the linked epics and user stories below.

- [Project Setup Epic](https://github.com/johnamdickson/portfolio-project-4/issues/1)
    - [As a **Site Admin** I can **deploy the project early** so that **fault finding through to deployment commences at the start of build**](https://github.com/johnamdickson/portfolio-project-4/issues/2)
    - [As a **Site Owner** I can **review wireframes** so that **site layout can be provisionally agreed**](https://github.com/johnamdickson/portfolio-project-4/issues/3)
    - [As a **Site Admin** I can **confirm that the SQL database is functional** so that **the connection to project and corresponding models is assured**](https://github.com/johnamdickson/portfolio-project-4/issues/4)

- [Basic Site Navigation Epic](https://github.com/johnamdickson/portfolio-project-4/issues/7)
    - [As a **User** I can **navigate the website** so that **I am able to access different pages with ease.**](https://github.com/johnamdickson/portfolio-project-4/issues/8)
    - [As a **User** I can **create a new account** so that **I am able to access the monitoring tool.**](https://github.com/johnamdickson/portfolio-project-4/issues/9)
    - [As a **User** I can **effortlessly sign in and sign out of my account** so that **my access to the account is secure.**](https://github.com/johnamdickson/portfolio-project-4/issues/10)

- [Site Administration Epic](https://github.com/johnamdickson/portfolio-project-4/issues/11)
    - [As a **Site Admin** I can **create, read, update and delete emissions on the provided Django panel** so that **the monitoring tool is current and reflective of emissions status**](https://github.com/johnamdickson/portfolio-project-4/issues/12)
    - [As a **Site Admin** I can **verify that emissions are locked for editing to non-superusers** so that **the monitoring tool content is locked for auditing purposes**](https://github.com/johnamdickson/portfolio-project-4/issues/13)
    - [As a **Site Admin** I can **allow certain users  to create of emissions on a linked page** so that **the monitoring tool is current and reflective of emissions status**](https://github.com/johnamdickson/portfolio-project-4/issues/14)

- [Create Home Page Epic](https://github.com/johnamdickson/portfolio-project-4/issues/15)

    - [As a **User** I can **access a summary of emissions from the back-end with a designed front-end** so that **the home page contains a useful summary of all open emissions.**](https://github.com/johnamdickson/portfolio-project-4/issues/16)
    - [As a **User** I can **view images of the emissions** so that **any ambiguity around the emission location is reduced**](https://github.com/johnamdickson/portfolio-project-4/issues/17)
    - [As a **Site Admin** I can **design the home page to match site styling** so that **the user experience is a positive and informative one**](https://github.com/johnamdickson/portfolio-project-4/issues/18)
    - [As a **Site Admin** I can **implement a map API** so that **maps showing emission location can be made available to the user.**](https://github.com/johnamdickson/portfolio-project-4/issues/22)
    - [As a **User** I can **select individual emissions** so that **I can drill down into further details**](https://github.com/johnamdickson/portfolio-project-4/issues/23)

- [Emissions Display and Interaction Epic](https://github.com/johnamdickson/portfolio-project-4/issues/19)
    - [As a **User** I can **see a list of emissions** so that **I have an overview of the facility.**](https://github.com/johnamdickson/portfolio-project-4/issues/20)
    - [As a **User** I can **filter the emissions list** so that **I can view only ones that are open.**](https://github.com/johnamdickson/portfolio-project-4/issues/21)
    - [As a **Site Admin** I can **implement a map API** so that **maps showing emission location can be made available to the user.**](https://github.com/johnamdickson/portfolio-project-4/issues/22)
    - [As a **User** I can **see a list of emissions** so that **I have an overview of the facility.**](https://github.com/johnamdickson/portfolio-project-4/issues/20)
    - [As a **Site Admin or authorised user** I can **close emissions on the emissions page** so that **the process of completing emissions once they are repaired is straight forward**](https://github.com/johnamdickson/portfolio-project-4/issues/25)
    - [As a **Site Admin** I can **delete emissions from the database on the emissions page** so that **erroneous emissions can be removed**](https://github.com/johnamdickson/portfolio-project-4/issues/26)
    - [As an **Authorised User** I can **create emissions from the emissions page** so that **new emissions can be recorded in the system**](https://github.com/johnamdickson/portfolio-project-4/issues/27)

- [Emission Checks Display and Interaction Epic](https://github.com/johnamdickson/portfolio-project-4/issues/24)

    - [As a **User** I can **easily create and complete emissions checks** so that **one of my duties as an operator can be fulfilled.**](https://github.com/johnamdickson/portfolio-project-4/issues/35)
    - [As a **Site Owner** I can **view the latest emissions checks on an emissions detail page** so that **I can verify checks are being completed at a glance for that particular emission**](https://github.com/johnamdickson/portfolio-project-4/issues/36)
    - [As a **Super User** I can **delete emissions checks** so that **erroneous emission checks can be removed from the system.**](https://github.com/johnamdickson/portfolio-project-4/issues/37)
    - [As a **Super User** I can **verify that emissions are locked for editing to non-superusers** so that **the monitoring tool content is locked for auditing purposes**](https://github.com/johnamdickson/portfolio-project-4/issues/38)
    - [As a **User and Site Admin** I can **see all emissions checks for my facility on one page** so that **I can readily access all of the the emission check history.**](https://github.com/johnamdickson/portfolio-project-4/issues/39)
    - [As a **User** I can **edit emissions checks** so that **any errors I have made can be corrected.**](https://github.com/johnamdickson/portfolio-project-4/issues/45)
    - [As a **Site Admin** I can **update emission check due dates automatically** so that **they do not have to be manually updated by users**](https://github.com/johnamdickson/portfolio-project-4/issues/46)
    - [As a **User** I can **filter checks that are open or open/closed** so that **checks on open emissions are prioritised for the user**](https://github.com/johnamdickson/portfolio-project-4/issues/66)

- [Emission Detail Page and Interaction Epic](https://github.com/johnamdickson/portfolio-project-4/issues/28)

    - [As a **User** I can **view all emission details on one page** so that **I can see all of the information that exists for it.**](https://github.com/johnamdickson/portfolio-project-4/issues/29)
    - [As a **User** I can **view the emission location on a map** so that **I can visualise the emissions location**](https://github.com/johnamdickson/portfolio-project-4/issues/30)
    - [As a **Site Owner** I can **verify permissions to close and delete emissions** so that   **they are not moved to an undesirable position in error.**](https://github.com/johnamdickson/portfolio-project-4/issues/31)
    - [As a **Site Admin and User** I can **view the relevant emission detail based on status** so that **only pertinent information is visible**](https://github.com/johnamdickson/portfolio-project-4/issues/32)

- [Maps API Epic](https://github.com/johnamdickson/portfolio-project-4/issues/33)

    - [As a **Site Admin** I can **implement a map API** so that **maps showing emission location can be made available to the user.**](https://github.com/johnamdickson/portfolio-project-4/issues/22)
    - [As a **User** I can **view the emission location on a map** so that **I can visualise the emissions location**](https://github.com/johnamdickson/portfolio-project-4/issues/30)
    - [As a **User** I can **see all of the emissions on a map** so that **their location is immediately obvious and given context with the users location.**](https://github.com/johnamdickson/portfolio-project-4/issues/34)
    - [As a **User** I can **select the emission location using a map and pin** so that **I do not need to work out the latitude and longitude manually**](https://github.com/johnamdickson/portfolio-project-4/issues/70)

- [Managing HTTP Status Codes Epic](https://github.com/johnamdickson/portfolio-project-4/issues/51)
    - [As a **Site Admin** I can **ensure users are informed of client error responses (400,403 and 404) in an informative and design friendly manner** so that **they can be made aware of the issue whilst maintaining the site aesthetic**](https://github.com/johnamdickson/portfolio-project-4/issues/53)
    - [As a **Site Admin** I can **ensure users are informed of the server error response (500) in an informative and design friendly manner** so that **they can be made aware of the issue whilst maintaining the site aesthetic**](https://github.com/johnamdickson/portfolio-project-4/issues/54)

- [Fine Tuning User Experience and Site Admin Epic](https://github.com/johnamdickson/portfolio-project-4/issues/55)
    - [As a **User** I can **scroll to the bottom of overflowing emissions tables** so that **I have a better experience of using the tables and I can visualise that there is overflow content.**](https://github.com/johnamdickson/portfolio-project-4/issues/56)
    - [As a **Site Admin** I can **provide a confirm prompt that fits with site styling** so that **users experience a fluent and seamless styling in all aspects of the site**](https://github.com/johnamdickson/portfolio-project-4/issues/57)
    - [As a **User** I can **exit form without submission using a cancel / go back button in the window as opposed to browser back button** so that **I can navigate from the site at point of use instead of using browser control.**](https://github.com/johnamdickson/portfolio-project-4/issues/58)
    - [As a **User** I can **traverse the site using commonly styled buttons** so that **the navigation experience is consistent and intuitive**](https://github.com/johnamdickson/portfolio-project-4/issues/60)
    - [As a **Site Admin** I can **condense all form htmls into a template for extension** so that **DRY principle can be adhered to.**](https://github.com/johnamdickson/portfolio-project-4/issues/61)
    - [As a **User** I can **log onto the monitoring tool with single sign on** so that **logging is a simple and secure process using a familiar log in**](https://github.com/johnamdickson/portfolio-project-4/issues/63)
    - [As a **Site Admin** I can **check a users log in status** so that **those not logged in are only able to access the home page**](https://github.com/johnamdickson/portfolio-project-4/issues/64)
    - [As a **Site Admin** I can **ensure that the add emission form contains the correct inputs** so that **unnecessary fields are removed.**](https://github.com/johnamdickson/portfolio-project-4/issues/64)

- [Testing and Documentation Epic](https://github.com/johnamdickson/portfolio-project-4/issues/72)
    - [As a **Site Admin** I can **complete manual testing** so that **all aspects of the project will be tested.**](https://github.com/johnamdickson/portfolio-project-4/issues/74)
    - [As a **Site Owner** I can **review well commented and annotated code** so that **purpose and scope of code is known now and into the future**](https://github.com/johnamdickson/portfolio-project-4/issues/82)
    - [As a **Site Owner** I can **access the project README** so that **all of the necessary information for the tool is available on project completion**](https://github.com/johnamdickson/portfolio-project-4/issues/75)


### Scope
#### Essential Content
 -  
#### Optional Content
- 
### Structure
- The structure of the database was defined and mapped out on a [database schema](views/README-files/flowchart.png). This helped define the required data interactions to develop a usuable product.
- The front end
- The database
### Skeleton
#### Wireframes
- The project wireframe can be found [here.](README-files/pp4-wireframes.pdf)
### Surface (Design)
#### Colour Scheme
- 

![Colour Pallett](views/README-files/color-pallette.png)
#### Imagery
- Images
- Icons
<img src="views/images/title-icon-bolt.png"  width="200" height="200"> <img src="views/images/title-icon-sun.png"  width="200" height="200">

#### Favicon
- .
#### Typography
- .<br><br>
<a href="#contents">BACK TO CONTENTS 🔼</a>

## Features 

### Existing Features

- __Insert Features Here__ 
  - Text<br><br>


### Features Left to Implement
- .

<a href="#contents">BACK TO CONTENTS 🔼</a>

## Technologies Used

### Languages Used
- **Python**: used extensively during project.
- **Markdown**: Used exclusively for README.
- **HTML5**: minor use when adding additional elements to the web page.
- **CSS3**: minor use when applying styling to app view.<br>

### Frameworks, Libraries & Programs Used
- **datetime**: from the standard library, used to perform operations on date and time objects and strings.
- **os**: from the standard library used to access system method to clear terminal screen at appropriate points whilst the program is running.
- **Gitpod** cloud based IDE used for majority of the project.
- **Git** used for version control.
- **GitHub** as cloud repository for Git version control.

- **Credentials**: imported from google.oauth.serivice_account to enable access to Google Sheets.

<br><a href="#contents">BACK TO CONTENTS 🔼</a>
## Testing 


<a href="#contents">BACK TO CONTENTS 🔼</a>

## Deployment

### Deploying to Heroku
* This site was deployed by completing the following steps:

1. Log in to [Heroku](https://id.heroku.com) or create an account.
2. On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New App.
3. You must enter a unique app name.
4. Next select your region.
5. Click on the Create App button
6. The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars.
7. Click Reveal Config Vars and enter the following:
    - Add port into the Key box and 8000 into the Value box and click the Add button.
    - Enter CREDS into the next available Key box and the Google credentials into the corresponding Value box.
    - Enter API_KEY into the next available Key box and the Open Weather API key into the corresponding Value box.
8. Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes.
9. Repeat step 8 to add node.js. o Note: The Buildpacks must be in the correct order. If not click and drag them to move into the correct order.
10. Scroll to the top of the page and choose the Deploy tab.
11. Select Github as the deployment method.
12. Confirm you want to connect to GitHub.
13. Search for the repository name and click the connect button.
14. Scroll to the bottom of the deploy page and select the preferred deployment type.
15. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository.](https://github.com/johnamdickson/portfolio-project-3)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository.](https://github.com/johnamdickson/portfolio-project-3)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.<br><br>
<a href="#contents">BACK TO CONTENTS 🔼</a>
## Credits 
### Content 
NOTE: Specific links are included within the Python, HTML, CSS  files. The list below summarises content credits in general.
- Stack Overflow, W3 Docs and other online resources were a massive help for Python, HTML or CSS code that enabled some of the functionality I was looking for.
- This [website](https://www.scaler.com/topics/multiline-comment-in-python/) gave guidance for making multi-line comments where using `“””` is recommended for docstrings and using `#` for comments.

- Thanks to my tutor Graham for his advice during the mentoring sessions.

### Media
- Google Fonts.
- All gifs were generated on [ezgif.com.](https://ezgif.com/video-to-gif)


- The colour names were sourced from [Name That Color.](https://chir.ag/projects/name-that-color/)
- The site colour scheme pallete was generated using the palette creation tool in [Color Hex.](https://www.color-hex.com/) 
- The title icons were from [Favicon](https://favicon.io/) which in turn sourced them from [Twemoji.](https://twemoji.twitter.com/)

<br><br>
<a href="#contents">BACK TO CONTENTS 🔼</a>
