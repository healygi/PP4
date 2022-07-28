<!-- ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png) -->

# Healys Health

 Healys Health is a health blog ran by a qualifed nutritionist where users can gain health information and advice. The site will be targeted towards health enthuasits who are interested in reading health articles, people who have health issues and are seeking advice/help on certain issues like gut health. Users can go on this site to educate themselves on their health and engage with fellow health enthuasists. Healys Health will be useful for people who want to take action on their health at home by taking advice from the site and make their meals more nutritious and balanced. 

# Features

## Existing Features

- Navigation Bar

   - Featured on every page this is a simple navigation bar. It is fully responsive and includes links to Home, Register and Login. It is identical on each page to allow for easy navigation unless the user logs in then obviously the 'register' link disappears. 
   - If the user is viewing the site a phone or tablet - the navigation becomes a simple burger menu which pops down with the nav links and logo. This allows for easy flow navigation. 
   - The logo 'Healys Health' is also a clickable link to the home page. This allows for easy navigation when the user views the site on a mobile or tablet device. 

   <!-- INCLUDE IMAGE OF NAVIAGTION BAR HERE - BURGER AND NO BURGER -->

- Home

   - The homepage contains all the current published blog posts, navigation at the top and footer with links to social media at the bottom of the page. Each blog post is aligned using bootstrap cards functionality. 
   - Each blog post is sorted into a card which shows the user an excerpt, the author, an eye-catching image of the post what date and time it was posted and how many comments and likes it has. 
   - The authors name is written in text overlaying the image so the user can see who wrote the article. 

   <!-- INCLUDE IMAGE OF HOME PAGE BLOGS AND NAV BAR AND FOOTER -->

- Footer

   - The footer section includes links to relevant social media sites for Healys Health. The links will open to a new tab to allow easy navigation for the user. 
   - The footer is valuable to the user as it encourages them to keep connected via social media. 
   - The footer sticks to the bottom of the page and is located on every page of this site. 

   <!-- IMAGE OF FOOTER AND SOCIAL MEDIA LINKS --> 

- Register 

   - A user can register by clicking on the register link in the nav bar. 
   - The user is taken to the sign up page where they are instructed to sign up via email and enter their password twice. The user is welcomed to Healys Health blog and asked if they have an account already - if so they are provided with a link to sign in instead. 
   - There is a button for the user to submit their form, they are then signed up. 
   - This page will allow the user to get signed up to Healys Health to start their health journey with the community. 

   <!-- IMAGE OF REGISTRATION PAGE --> 

- Login

   - A user can login by clicking on the login link in the nav bar. 
   - The user is taken to the sign in page where they are instructed to sign in via email or social media. If the user does not have an account they can sign up following the provided link. 
   - On the sign-in page the user can sign in using an email address and password. They can select "remember me" if they so wish. 
   - Users can also sign in using social media accounts such as Facebook, Twitter or sign in via Google.
   - The user has to enter a valid email containing "@" and a valid password that isnt too common or too short. <!-- MAY HAVE TO BE MORE CLEAR HERE ON RESTRICTIONS OF PASSWORDS/EMAIL -->
   - There is a button for the user to submit their form, they are then signed in. 

   <!-- IMAGE OF LOGIN PAGE --> 

- Admin 

    - The admin (site owner) can access their site administration using the Django administration framework.
    - Here the site owner can validate comment and post blog posts. The site owner has access to the email addresses that have signed up, the names of the users of the site and the social media applications attached to the site. 

   <!-- IMAGE OF ADMIN PAGE--> 

## Features Left to Implement

I would like my blog site to be a page within a larger website. The project I wanted to create was too far out of scope for my PP4. I would like to implent the following to create a larger functioning website for a nutritional therapist. 

- Booking System

  - I would like to implement a booking system so that the users of the site could book in a session with the site owner (aka a nutritionist). 
  - I would like to implement the ability for the site owner to provide the user with feedback and homework after a one to one session. 

- Testimonials

  - I would like to create a review page so the user can leave testimonials on their experience and journey with Healys Health. 
  - I would like the user to be able to review their experience with the nutritionist and if they would recommend. 

- About 

  - I would like to create an about page to inform users about the nutritionist - her education, experience and qualifications in the sector of health and nutritional therapy. 

- Contact 

  - I would like like to implement a contact page so that users can contact the site owner whether on site, phone, email or social media. 
  - The booking system would be implemented on this page. 

- Footer

  - I would like the footer to include location and contact information. 

# Agile Development Methology:

 - I documented and implemented all User Stories using the Agile Project Management tools on GitHub. 
 - I created a basic kanban board in the projects section of my git-hub repository.
 - Here I created User Stories using the CI template - AS A - I WANT - SO THAT. 
 - I linked them with my project and moved them into the to do section of my kanban board.
 - I labelled my User Stories in accordance with MoSCow prioritization.  
 - I researched and asked friends and family who had an interest in health what they would want from a health blog site. 
 - I asked them to write some User Stories to see if they came up with ones I hadn't thought of. 
 - I kept my site simple to ensure all the functionality ran smoothly and efficiently, keeping continious attention to technical proficiency. 
 - To start, I chose between one - three 'Must Have' user stories and moved them into the 'in progress' board and continued from there, starting with the 'must have' stories first with some others that over-lapped moving on to the 'should have' and then 'could have' depending on my time frame and scope. 

![kanban board](/media/PP4/kanban_board.png) 

 - I had 17 User Stories in total and moved them in accordance with whether they were in progress or completed. 
 - After I had labelled them with MoSCow prioritization this allowed me to prioritise certain tasks to implement over less important tasks. 

# Testing

## Manual Testing:

 - I chose to manually test my project as my app is small and not so complicated. If my project was bigger and if I decide to continue with developing this app further I consider automated testing as manual testing for a larger project has a high error rate and probably would not suffice by itself. For this project I believe manual testing was all that was needed. 

 - I began my manual testing by checking that my project works according to user stories, this is known as BDD - Behaviour Driven Development where the result is based on an expected outcome. This type of testing bulids from user stories where I would sit in front of my app and test it to see if it behaves as expected. Similar to user story template - AS - I WANT - SO THAT - I created a number of atomic tests by using the template - GIVEN - WHEN - THEN. This template describes the outcome in a testable way. My tests were written as follows:

        - AS A *User* I WANT *To be able to click the logout button* SO THAT *I can log out of my account*
        - GIVEN *That a user is logged in* WHEN *The logout button is clicked* THEN *The user will be logged out and returned to the login screen*

        - AS A *User* I WANT *the ability to like posts* SO THAT *I can engage with other users*
        - GIVEN *That a user is logged in* WHEN *The heart icon is clicked* THEN *The user will have liked the post, the heart will turn red and the number will increase by one*

        - AS A *User/Admin* I WANT *the ability to open posts in order to be able to read/view them* SO THAT *I can engage with other users and inform myself*
        - GIVEN *That a user is on the site* WHEN *a blog post is clicked* THEN *The user will be taken to another page and be able to view/read the full blog post*

        - AS A *User* I WANT *the ability to comment on posts* SO THAT *I can engage with other users and leave my opinion on the article*
        - GIVEN *That a user is logged in* WHEN *the comment box is present the user is able to write a comment and press submit* THEN *The user will have made a comment that needs to be verified before it is posted*

        - AS A *User/Admin* I WANT *the ability to register an account* SO THAT *I can sign up to the website*
        - GIVEN *That a user/admin is able to sign up* WHEN *The sign up button is clicked* THEN *The user will be able to sign up and register an account by filling out the provided form and pressing submit*

        - AS A *User* I WANT *the ability to view comments* SO THAT *I can engage with other users and read their comments*
        - GIVEN *That a user is logged in* WHEN *a blog post is clicked on* THEN *The user will have access to reading other users comments*

        - AS A *Admin* I WANT *the ability to vet comments before they are posted* SO THAT *abusive/poor taste comments aren't posted*
        - GIVEN *That an admin is logged in* WHEN *a user has commented on a post* THEN *The admin will have access to view this comment and decided whether it is or isn't acceptable for publishing and if so can publish or delete the comment*

        - AS A *Admin* I WANT *the ability to create blog posts* SO THAT *I can update my blog and engage with other users*
        - GIVEN *That an admin is logged in* WHEN *they have access to the backend* THEN *The admin will be able to write, publish or save a draft of their blog posts for their site*

        - AS A *User* I WANT *to be able to see the number of likes and comments on each post on the homepage* SO THAT *I can see how many likes and comments there are*
        - GIVEN *That a user is on the sites homepage* WHEN *the user looks at the blog excerpt* THEN *The user will be able to see the number of likes and comments on each post*

 - I tested if my project worked on different browsers such as - Google Chrome, Safari, Microsoft Edge and Firefox - with different resolutions. 

 - I tested if my project was responsive on a number of different devices- mobile, tablets, desktops from 320px to 1201px. I used developer tools to make sure my site works on all device sizes. 

 - I sent my deployed link to friends and family to double check that it worked adequately on all different types of screens.

 - I tested my site on the website - responsive design checker- which ran my site through a variety of different screen sizes and devices. I inspected each one and was happy with the level of responsivity.

## Validator Testing 

- HTML
   - No errors were returned when passing through the official W3C validator

- CSS
   -  No errors were returned when passing through the official Jigsaw validator

- Python
   - No errors were returned when passing through the official PEP8 validator

- Javascript 
   - No errors were returned when passing through the official BeautifyTools validator

## Unfixed Bugs

- There are no buys unfixed. 

## UX Design 

- I implemented UX design when developing my project. I did so by putting myself in the users shoes and designed the site based on their needs. This site is for users interested in health and nutrition - so if I was this user I would want to see experts of the blog posts available to read and have the ability to engage with a community who have similar interest. 
- I made sure my site was accessible by making sure all text is readable and that there is a right amount of contrast between colours. 
- I made sure my site was simple as a design principle for a ease in terms of user experience. 
- I selected a simple readable, pleasing font to make sure my text was easily and quickly readable. 
- I provided ease of navigation so that the user can go back and forth between the homepage and blog articles and can also easily comment and like posts. 
- I created a wireframe of my project prior to creating it, this wireframe allowed me to have a simple basis of what I developing and how it should look. 

## Wireframe 

![wireframe](/media/PP4/wireframe.png) 

## Final Project

![final project](/media/PP4/final_project.png) 

# Deployment 

 When creating my project the first step I took was managing deployment as it is best practise to deploy early. I took the following steps to begin my deployment:

1. I installed Django and the supporting libraries.
2. I created a new blank Django project and app.
3. I set my project to use Cloudinary (where my images would be stored) and PostgreSQL (relational database management system). 
4. I created a new app in my Heroku account - named 'HealysHealth', location - 'Europe.'
5. I added PostgreSQL as my database in the Resources tab of my app. 
6. I copied the DATABASE_URL from my Config Vars and added it to my env.py file to link my database_url with my Heroku app.
7. I created my SECRET_KEY in my environ.py file to encrypt session cookies and added this to my Heroku app config vars.
8. I then imported dj_database_url, os and added my SECRET_KEY and DATABASES to my settings.py file.
9. I migrated my files. 
10. I created a Cloudinary account to store my images- I linked this URL to my env.py file and my Heroku app config vars.
11. I created a DISABLE_COLLECTSTATIC in my config vars and set it to 1 as my project was empty at this stage of development. 
12. In my settings.py file I added 'cloudinary_storage' and the cloudinary library to my INSTALLED_APPS.
13. After linking Django to Cloundinary, adding my Templates Directory, creating my three directories - media, static and templates, adding a Procfile (web: gunicorn healyshealth.wsgi) and adding my heroku app to ALLOWED_HOSTS in my settings.py file- I was then ready to make my first deployment to Heroku. 
14. In the deployment tab of my app I connected GitHub to my deployment method. 
15. I then connected my app to my GitHub repository and deployed it to my main branch. 
16. I watched the buliding log and when it was complete I selected 'open app' and my app successfully deployed. 
17. I followed continuous deployment throughout my project. 
18. FINAL DEPLOYMENT INFO GOES HERE 

# Credits

- Content:

  - The text for my blog articles were taken from the following nutrition articles:
  - "The importance of Good Nutrition": 
  https://www.activehealth.sg/read/nutrition/what-is-good-nutrition-and-why-is-it-important
  - "How fermented foods can help!":
   https://www.heartfoundation.org.nz/about-us/news/blogs/fermented-foods-the-latest-trend
  - "Why your microbiome matters!":
   https://www.mydr.com.au/nutrition-weight/why-your-gut-microbiome-should-matter-to-you/#:~:text=Unfavourable%20changes%20to%20the%20microbiome,has%20occurred%20over%20past%20decades.

  - Instuctions on how to implement a blog site using Django were taken from the Code Institutes 'I think therefore I blog" walkthrough. 

  - Information on how to implement manual testing were taken from the Code Institutes 'Introduction to software testing.' 

  - The icons in the navbar were taken from Font Awesome.



- Media:
 
  - The photos within the blog articles where taken from Google images. 