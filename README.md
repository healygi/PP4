# Healy's Health

 Healy's Health is a health blog ran by a qualifed nutritionist where users can gain health information and advice. The site will be targeted towards health enthuasits who are interested in reading health articles, people who have health issues and are seeking advice/help on certain issues like gut health. Users can go on this site to educate themselves on their health and engage with fellow health enthuasists. Healys Health will be useful for people who want to take action on their health at home by taking advice from the site and make their meals more nutritious and balanced. 

 This is the live site - https://healyhealth.herokuapp.com/

![responsive](/media/PP4/responsive.png) 

# Features

## Existing Features

- Navigation Bar

   - Featured on every page this is a simple navigation bar. It is fully responsive and includes links to Home, Register and Login. It is identical on each page to allow for easy navigation unless the user logs in then obviously the 'register' link disappears. 
   - If the user is viewing the site a phone or tablet - the navigation becomes a simple burger menu which pops down with the nav links and logo. This allows for easy flow navigation. 
   - The logo 'Healys Health' is also a clickable link to the home page. This allows for easy navigation when the user views the site on a mobile or tablet device. 

  
![nav bar](/media/PP4/nav.png) 

- Home

   - The homepage contains all the current published blog posts, navigation at the top and footer with links to social media at the bottom of the page. Each blog post is aligned using bootstrap cards functionality. 
   - Each blog post is sorted into a card which shows the user an excerpt, the author, an eye-catching image of the post what date and time it was posted and how many comments and likes it has. 
   - The authors name is written in text overlaying the image so the user can see who wrote the article. 

   
![homepage](/media/PP4/Home.png) 

- Footer

   - The footer section includes links to relevant social media sites for Healys Health. The links will open to a new tab to allow easy navigation for the user. 
   - The footer is valuable to the user as it encourages them to keep connected via social media. 
   - The footer sticks to the bottom of the page and is located on every page of this site. 

   
![footer](/media/PP4/footer.png) 

- Register 

   - A user can register by clicking on the register link in the nav bar. 
   - The user is taken to the sign up page where they are instructed to sign up via email and enter their password twice. 
   - Email validation is in place requring an '@' sign and '.com, .co, .ie, etc.'
   - The user is welcomed to Healys Health blog and asked if they have an account already - if so they are provided with a link to sign in instead. 
   - There is a button for the user to submit their form, they are then signed up. 
   - This page will allow the user to get signed up to Healys Health to start their health journey with the community. 

  ![register](/media/PP4/register.png) 

- Login

   - A user can login by clicking on the login link in the nav bar. 
   - The user is taken to the sign in page where they are instructed to sign in via email or social media. If the user does not have an account they can sign up following the provided link. 
   - On the sign-in page the user can sign in using an email address and password. They can select "remember me" if they so wish. 
   - Users can also sign in using Facebook.
   - The user has to enter a valid email containing "@" and a valid password. 
   - I created password validation to require - a miniumum length, a numeric value and avoid common password. 
   - There is a button for the user to submit their form, they are then signed in and alerted that they are signed in. 

  ![login](/media/PP4/sign_in.png) 

- Blog Post

   - When a blog post is selected on the home page, the user is taken to the full blog post article. 
   - The user can read this post. The ability to comment/like the post is limited to logged in users. Thus, the comment form does not display unless the user is logged in. 

![Blog Post](/media/PP4/BlogPost.png) 

- Comment Form 
   
   - A logged in user can comment on the blog post in the comment form. 
   - They can write their comment and hit submit. 
   - The comment is sent to django admin to be verifed by the site owner. 
   - The user is presented with an alert message - 'your comment is awaiting approval.'

![Comment Form](/media/PP4/comment-form.png) 

- Delete

   - A logged in user can delete their comment on the blog post. 
   - A button will appear beside their comment, if clicked they are taken to a page to confirm deletion. 
   - If confirmed the comment will delete.

- Edit Form

   - A logged in user can edit their comment on the blog post. 
   - A button will appear beside their comment, if clicked they are taken to a page with a form. 
   - They can resubmit their comment/edits.
   - The comment is then updated. 

![Buttons](/media/PP4/edit-delete-buttons.png) 

- Admin 

    - The admin (site owner) can access their site administration using the Django administration framework.
    - Here the site owner can validate comment and upload/publish blog posts.


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

  - I would like to implement a contact page so that users can contact the site owner whether on site, phone, email or social media. 
  - The booking system would be implemented on this page. 

- Footer

  - I would like the footer to include location and further contact information. 

# Technologies Used

## Languages

- HTML5 was used to build the front-end website
- CSS was used to style the HTML and add responsiveness
- JavaScript was used with Bootstrap to provide interaction on the front-end
- Bootstrap was used to style the website, add responsiveness and interactivity
- Python was used to code the back end of the project
- PyPI to install the python packages

# Frameworks 

- Django 3.2.14
- Django supporting libraries:
    - allauth for authentication, registration, account management as well as 3rd party (social) account authentication
    - crispy-forms to style the forms
    - summernote as editor
    - gunicorn as the server for Heroku
    - psycopg2as an adaptor for Python and PostgreSQL databases
    - dj-database to parse the database URL from the environment variables in Heroku

# Database

- Heroku Postgres for the production database

# Other Technologies

- Cloudinary was used to host the static files and media
- Gitpod as the IDE
- Git used for version control via the terminal in Gitpod
- GitHub used to store the code in the repository
- Heroku was used as the cloud based platform for deployment
- Fontawesome for icons
- Google images for images
- Lucid for wireframes
- Google Chrome Dev Tools for inspection during development to check reponsiveness and contrast.
- Favicon.io for the favicon
- W3C Markup Validation Service
- W3C CSS Validation Service(Jigsaw) 
- PEP8 Online Checker

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

# Scope

The scope of this project was large at the planning stage. The ultimate goal was to allow logged in users to have full CRUD functionality for all their own content. Time constraints meant this was limited to CRUD functionality for logged in users only for their own comments on blog posts as this was deemed a must-have. More functionality for logged in users will be added in the future. For instance, I would like to add the ability for the user to submit a blog post they have written that is then submitted to be approved by the site owner. 

# Structure

The site consists of 6 pages: Home, Sign-up/Sign-in, Blog Posts (x3 currently). All pages can be viewed by all users. The ability to comment/like posts is limited to logged in users. 

# Epics and User Stories
 - I had 8 Epics:

 1. Epic: Set up admin page for admin to manage blog posts, comments and site users. 
 2. Epic: Enable users to set up an account on the site to have full access to features. 
 3. Epic: Create eye-catching home page. 
 4. Epic: Enable registered users to comment/like/edit/delete posts. 
 5. Epic: Create Blog page for users to read blog posts. 
 6. Epic: Enable registered users to interact with blog posts to enhance UX and engagement with other users.
 7. Epic: Enable users to sign-in/register with Facebook account. 
 8. Epic: Enable users to CRUD own comments.  

 - I had 19 User Stories in total and moved them in accordance with whether they were in progress or completed. Here are my User Stories:

           - As a *user/admin* I want to be able to register an account and *sign up/in* to the website. (must-have/completed) 

           - As a *user/admin* I want to be able to view comments in order to be able to *read/view comments.* (must-have/completed)

           - As a *user/admin* I want to be able to open posts in order to be able to *read/view them* (must-have/completed)

           - As a *user/admin* I want to be able to read excerpts of the posts on the home page to *improve UX design and get a taste of what the article is about* (should-have/completed)

           - As a *user/admin* I want to be able to view posts so that I can see *how many likes a post gets* (must-have/completed)

           - As a *site owner* I want to be able to create drafts of my posts and recieve posts from users so that *I can review, schedule and draft posts before posting.* (must-have/completed)

           - As a *site owner* I want to be able to *like & comment on blog posts including my own so that I can engage with my users/community.* (must-have/completed)

           - As a *site owner*  I want to be able to *give my clients(users) feedback on their session with me and homework/nutrition plan if needed so that there is clear connection and organisation between client & nutritionist.* (could-have/future feature)

           - As a *site owner*  I want to be able to *login & see my schedule & clients so that everything is organised and readable* (could-have/future feature)

           - As a *site owner* I want my *booking system to be adjustable and follow my schedule/diary so that it is organised with accordance to my schedule* (could-have/future feature)

           - As a *site owner*  I want to be able to *receive bookings and make sure there are no double bookings so that I can set up meetings with my users* (could-have/future feature)

           - As a *site owner*  I want to be able to *vet comments before posting so that abusive/poor comments aren't posted.* (must-have/completed)

           - As a *site owner*  I want to be able to *post to my blog so that my users can engage and read my content* (must-have/completed)

           - As a *User* I want the ability to sign in/out so that I can *have access to the full features of the site* (must-have/completed)

           - As a *User* I want the ability to sign in/out via Facebook so that I can *streamline my account* (could-have/completed)

           - As a *User* I want the ability to *book an appointment with a nutritionist so that I can get help & advice with my health issues* (could-have/future feature)

           - As a *User* I want the ability to *read blogs so that I can learn about nutrition & health* (must-have/completed)

           - As a *User* I want the ability to *like posts so that I can engage with others* (should-have/completed)
           
           - As a *User*, I want the ability to *comment and delete and edit posts so that manage my own content* (must-have/completed)

 - I labelled them with MoSCow prioritization so that this allowed me to prioritise certain tasks to implement over less important tasks depending on time and scope. 

# Testing

## Manual Testing:

 - I chose to manually test my project as my app is small and not so complicated. If my project was bigger and if I decide to continue with developing this app further I would consider automated testing as manual testing for a larger project has a high error rate and probably would not suffice by itself. For this project I believe manual testing was all that was needed. 

 - I began my manual testing by checking that my project works according to user stories, this is known as BDD - Behaviour Driven Development where the result is based on an expected outcome. This type of testing bulids from user stories where I would sit in front of my app and test it to see if it behaves as expected. Similar to user story template - AS - I WANT - SO THAT - I created a number of atomic tests by using the template - GIVEN - WHEN - THEN. This template describes the outcome in a testable way. 
 
 ## Atomic Tests
 
 - My tests were written for both the user and admin. They read as follows:

        - AS A *User* I WANT *To be able to click the logout button* SO THAT *I can log out of my account*
        - GIVEN *That a user is logging out* WHEN *The logout button is clicked* THEN *The user will be logged out*

        - AS A *User* I WANT *the ability to like posts* SO THAT *I can engage with other users*
        - GIVEN *That a user is logged in* WHEN *The heart icon is clicked* THEN *The user will have liked the post, the heart will turn red and the number will increase by one*

        - AS A *User* I WANT *the ability to unlike posts* SO THAT *I can unlike a post if I so wish*
        - GIVEN *That a user is logged in and the heart icon is red* WHEN *The heart icon is clicked* THEN *The user will have unliked the post, the heart will turn white and the number will decrease by one*

        - AS A *User/Admin* I WANT *the ability to open posts in order to be able to read/view them* SO THAT *I can engage with other users and inform myself*
        - GIVEN *That a user is on the site* WHEN *a blog post is clicked* THEN *The user will be taken to another page and be able to view/read the full blog post*

        - AS A *User* I WANT *the ability to comment on posts* SO THAT *I can engage with other users and leave my opinion on the article*
        - GIVEN *That a user is logged in* WHEN *the comment box is present the user is able to write a comment and press submit* THEN *The user will have made a comment that needs to be verified before it is posted*

        - AS A *User* I WANT *the ability to edit my comments* SO THAT *I can correct my mistake if needed*
        - GIVEN *That a user is logged in* WHEN *their comment is present the user is able to click on the edit button* THEN *an edit form is displayed and the user can write a new comment replacing their old one and submit*

        - AS A *User* I WANT *the ability to delete my comments* SO THAT *I can delete my comment if needed*
        - GIVEN *That a user is logged in* WHEN *their comment is present the user is able to click on the delete button* THEN *asked to confirm the deletion and submit*

        - AS A *User/Admin* I WANT *the ability to register an account* SO THAT *I can sign up to the website*
        - GIVEN *That a user/admin is able to sign up* WHEN *The sign up button is clicked* THEN *The user will be able to sign up and register an account by filling out the provided form and pressing submit*

        - AS A *User* I WANT *the ability to view comments* SO THAT *I can engage with other users and read their comments*
        - GIVEN *That a user is on the site* WHEN *a blog post is clicked on* THEN *The user will have access to reading other users comments*

        - AS A *Admin* I WANT *the ability to vet comments before they are posted* SO THAT *abusive/poor taste comments aren't posted*
        - GIVEN *That an admin is logged in* WHEN *a user has commented on a post* THEN *The admin will have access to view this comment and decided whether it is or isn't acceptable for publishing and if so can publish or delete the comment*

        - AS A *Admin* I WANT *the ability to create blog posts* SO THAT *I can update my blog and engage with other users*
        - GIVEN *That an admin is logged in* WHEN *they have access to the backend* THEN *The admin will be able to write, publish or save a draft of their blog posts for their site*

        - AS A *User* I WANT *to be able to see the number of likes and comments on each post on the homepage* SO THAT *I can see how many likes and comments there are*
        - GIVEN *That a user is on the sites homepage* WHEN *the user looks at the blog excerpt* THEN *The user will be able to see the number of likes and comments on each post*

 ## Example of running Atomic Test:

 - User Story:

   - AS A *User* I WANT *the ability to like posts* SO THAT *I can engage with other users*

   - GIVEN *That a user is logged in and on the blog post page* WHEN *The heart icon is clicked* THEN *The user will have liked the post, the heart will turn red and the number will increase by one*

 - Testing Steps:

  1. I log into a user account. 
  2. I am on the blog post site.
  3. I click on the heart icon.

 - Expected Result: 

   - The heart turns red, the post is 'liked' by the user and the number of likes increases by one.

 - Actual Result:

   - The heart turns red, the post is 'liked' by the user and the number of likes increases by one.   

- Pass or Fail:
   
   - Atomic test *passes* because expected result matches actual result. 

- I went through each User Story following the template above and accounted for whether the test failed or passed in conjunction with my GIVEN-WHEN-THEN template. If it passed my test was valid and I could move on to the next one. If it failed I had to go back to development and resolve the issue.  

## Other Forms of Testing
 
- I tested if my project worked on different browsers such as - Google Chrome, Safari, Microsoft Edge and Firefox - with different resolutions. 

- I tested if my project was responsive on a number of different devices- mobile, tablets, desktops from 320px to 1201px. I used developer tools to make sure my site works on all device sizes. 

- I sent my deployed link to friends and family to double check that it worked adequately on all different types of screens.

- I tested my site on the website - responsive design checker- which ran my site through a variety of different screen sizes and devices. I inspected each one and was happy with the level of responsivity.

- I tested my site in dev tools lighthouse and was happy with the result:

 ![lighthouse](/media/PP4/lighthouse.png) 

## Validator Testing 

- HTML
   - No errors were returned when passing through the official W3C validator

- CSS
   -  No errors were returned when passing through the official Jigsaw validator

- Python
   - No errors were returned when passing through the PEP8 online check. 

- Javascript 
   - No errors were returned 

   ![html-validator](/media/PP4/validator.png) 

## Unfixed Bugs

- Social media login worked locally but when ran in the deployed app I recieved an error cannot connect url - I only noticed this on final deployment and couldn't fix it due to time constraints. 

## UX Design 

- I implemented UX design when developing my project. I did so by putting myself in the users shoes and designed the site based on their needs. This site is for users interested in health and nutrition - so if I was this user I would want to see excerpts of the blog posts available to read and have the ability to engage with a community who have similar interests. 
- I viewed other nutrition and health websites to gain inspriation on what design fits best for this type of website. 
- I made sure my site was accessible by making sure all text is readable and that there is a right amount of contrast between colours. 
- I selected the colour pallet white and green as I thought it reflected health and nature colours which would be assoicated with nutrition, health and taking care of oneself. These soft colours are warm and inviting but also smart and serious. 
- I made sure my site was simple as a design principle for an ease in terms of user experience. 
- I selected a simple readable, pleasing font to make sure my text was easily and quickly readable. 
- I provided ease of navigation so that the user can go back and forth between the homepage and blog articles and can also easily comment and like posts. 
- I created a favicon icon with the intials of my site 'HH'. I used an eyecatching font and stuck with the pallet of my site green and white. 
- I created a wireframe of my project prior to creating it, this wireframe allowed me to have a simple basis of what I developing and how it should look. 

## Wireframe 

![wireframe](/media/PP4/wireframe.png) 

## Final Project

![final project](/media/PP4/Home.png) 

- As you can see my design basically stayed the same but with a better color pallet and navigation placed beside a nicer designed logo at the top of the page. 
- I also provided excerpts of my blog site, an image to reflect the content of the blog and the name of the author. I thought this action would intrigue the user to click on the article itself to read it further. I also thought it was more professional and visually pleasing than a simple link to a blog post.

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
11. I created a DISABLE_COLLECTSTATIC in my config vars and set it to 1 as my project was empty at this stage of development. I later removed this. 
12. In my settings.py file I added 'cloudinary_storage' and the cloudinary library to my INSTALLED_APPS.
13. After linking Django to Cloundinary, adding my Templates Directory, creating my three directories - media, static and templates, adding a Procfile (web: gunicorn healyshealth.wsgi) and adding my heroku app to ALLOWED_HOSTS in my settings.py file- I was then ready to make my first deployment to Heroku. 
14. In the deployment tab of my app I connected GitHub to my deployment method. 
15. I then connected my app to my GitHub repository and deployed it to my main branch. 
16. I watched the buliding log and when it was complete I selected 'open app' and my app successfully deployed. 
17. I followed continuous deployment throughout my project. 
18. On final deployment I set "DEBUG = False". 

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

  - I used Stack Overflow for issues I was struggling with.

  - I read Bootstrap and Django documentation to aid my process of developing this site. 


- Media:
 
  - The photos within the blog articles where taken from Google images. 


- Acknowledgements:
 
  - I want to thank my mentor for guiding me through the developemt of this project. 

  - I want to thank student support in CI for helping me with issues I was stuggling with.  
