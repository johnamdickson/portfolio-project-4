
# <img src="static/images/favicon.png"  width="40" height="40">  &nbsp;Emissions Monitoring Tool

Emissions Monitoring Tool is an application for industrial clients to monitor, verify and report any unwanted emissions that do not neccesitate an immediate shutdown to repair. The application allows for user registration, role based permissions, adding new emissions and performing regular checks on those emissions all whilst displaying the data to the user in a design friendly manner.

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
  - [Development Testing](#development-testing)
  - [Testing User Stories](#testing-user-stories)
     - [User Goals](#user-goals)
     - [Site Administrator Goals](#site-administrator-goals)
  - [Validator Testing](#validator-testing)
  - [Bugs / Issues](#bugs--issues)
  - [Unresolved Bugs / Issues](#unresolved-bugs-or-issues)
- [Deployment](#deployment)
  - [Deploying to Heroku](#deploying-to-heroku)
  - [Forking the GitHub Repository](#forking-the-github-repository)
  - [Making a Local Clone](#making-a-local-clone)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)

## UX
### Strategy
The objective of the site is to allow users to review past weather for a location in Ireland or obtain a weather forecast for a geographic location using coordinates.
#### User Stories
- User Goals:
  - 
<br><br>
- Site Administrator Goals:
  - 
<br><br>
- Site Owner Goals:
  - 

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
