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

 - I documented and implemented all User Stories using the Agile Project Management tool - Kanban Board - on GitHub. 
 - I labelled my User Stories in consolidation with MoSCow prioritization.  
 - I researched and asked friends and family who had an interest in health what they would want from a health blog site. 
 - I asked them to write some User Stories to see if they came up with ones I hadn't thought of. 
 - I kept my site simple to ensure all the functionality ran smoothly and efficiently, keeping continious attention to technical proficiency. 

![kanban board](/media/PP4/kanban_board.png) 

 - I had 17 User Stories and moved them in accordance with whether they were in progress or completed. 
 - After I had labelled them with MoSCow prioritization this allowed me to prioritise certain tasks to implement over less important tasks. 
# Testing
 <!-- JEST SECTION GOES HERE -->


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

  - The icons in the navbar were taken from Font Awesome.



- Media:
 
  - The photos within the blog articles where taken from Google images. 

