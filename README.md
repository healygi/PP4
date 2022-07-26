<!-- ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png) -->

# Healys Health

Healys Health is a health blog where users can gain health information and advice. The site will be targeted towards health enthuasits who are interested in reading health articles, people who have health issues and are seeking advice/help on certain issues like gut health. Users can go on this site to educate themselves on their health and engage with fellow health enthuasists. Healys Health will be useful for people who want to take action on their health at home by taking advice from the site and make their meals more nutritious and balanced. 
------
------

# Features

## Existing Features

- Navigation Bar

   - Featured on every page this is a simple navigation bar. It is fully responsive and includes links to Home, Register and Login. It is identical on each page to allow for easy navigation unless the user logs in then obviously the 'register' link disappears. 
   - If the user is viewing the site a phone or tablet - the navigation becomes a simple burger menu which pops down with the nav links and logo. This allows for easy flow navigation. 
   - The logo 'Healys Health' is also a clickable link to the home page. This allows for easy navigation when the user views the site on a mobile or tablet device. 

   <!-- INCLUDE IMAGE OF NAVIAGTION BAR HERE - BURGER AND NO BURGER -->

- Blog Posts

   - The homepage contains all the current published blog posts, navigation at the top and footer with links to social media at the bottom of the page. Each blog post is aligned using bootstrap cards functionality. 
   - Each blog post is sorted into a card which shows the user an excerpt, the author, an eye-catching image of the post what date and time it was posted and how many comments and likes it has. 
   - The authors name is written in text overlaying the image so the user can see who wrote the article. 

   <!-- INCLUDE IMAGE OF HOME PAGE BLOGS AND NAV BAR AND FOOTER -->

- The Footer

   - The footer section includes links to relevant social media sites for Healys Health. The links will open to a new tab to allow easy navigation for the user. 
   - The footer is valuable to the user as it encourages them to keep connected via social media. 
   - The footer sticks to the bottom of the page and is located on every page of this site. 

- Register 

- Login

- Admin 

   <!-- IMAGE OF FOOTER AND SOCIAL MEDIA LINKS --> 



We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
