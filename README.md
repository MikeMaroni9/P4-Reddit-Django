<h1> Project 4 - Reddit Style Blog</h1>
<h2> mockdd <span style="color:red;">">i</span>t</h2>
<p> Blog type application where a registered user can create a new posts, or comment on already existing one.</p>
<p> Developed using : HTML, CSS, JAVASCRIPT, PYTHON and DJANGO</p>
<br>
<p>Link to the project on Heroku:</p>
<a href="https://project4-django-blog-x-24e6733e46ab.herokuapp.com/">mockdd <span style="color:red;">">i</span>t on Heroku</a>
<br>
<br>
<p>Link to the GITHUB repository:</p>
<a href="https://github.com/MikeMaroni9/P4-Reddit-Django">GITHUB</a>
<br>
<p>Link to the GITHUB USER Stories:</p>
<a href="https://github.com/users/MikeMaroni9/projects/4/views/1">User Stories</a>
<br>
<br>

<h2> The Process of the Web Page</h2>
<p>Reddit style web page with authentication, ability to create posts, delete posts. Leave comments and like the posts.</p>


<p>Upon opening a page, you are greeted with pre-filled reddit style page. All content is taken from the original reddit page, including the comments and chosen randomly without particular agenda</p>
<img src="">


<p>For visitors that are not signed-up and logged in, you are greeted with mockddit logo which acts as a link button to index page, and two buttons on the opposite side. Register and Login</p>
<img src="">

<p>Register, takes you to the sign-up form that asks for username and password input, leaving email - optional.</p>
<img src="">

<p>Login, takes you to login page for prerigistered users and there's also a choice to sign in with google account, connected to Google API on the backend.</p>
<img src="">

<p>If you decide to sign in using goolge account, first you will be taken to the process page to check if you really like to perform this action</p>
<img src="">

<p>And then taken to the google login screen</p>
<img src="">

<p>Upon signing in, you will be returned to the index page. Bootstrap alert message will confirm that you have logged in/logged out. MSG will dissapear after few secons.</p>
<img src="">

<p>While logged in the navigation bar changes. Now you have option to create a New Post of visit your Profile Page.</p>
<img src="">

<p>Profile Page will show your information and also have the ability to edit it. </p>
<img src="">

<p>Editing the profile picture, you have ability to change, username, email, first name and last name. changing password has been turned off.</p>
<img src="">

<p>New Post : You are greeted with a simple form to input Title and Content of your post. Username is asigned automatically for the logged in user. {% if authenticated %} has been added to allow only logged in User to create a new posts. Added is also Bootsrap MSG that can be dismissed, reminding users to be polite and follow the mockddits rules.</p>
<img src="">

<p>Newests POSTS are automatically showed at the top of the page.</p>
<img src="">

<p>Author of the post has the ability to edit or to delete the post. User has to be logged in and user.id has to match author.id</p>
<img src="">

<p>As a signed in user, you can like the post, increasing the like count and add comments</p>
<img src="">

<p>Adding a comment takes you to new comments page, user id and current post is asigned automatically, leaving you with only option to leave a comment.</p>
<img src="">

<p>Maximum posts per page are 6, automatically paginating older post to the next page.</p>
<img src="">

<p></p>
<img src="">

<p></p>
<img src="">

<p></p>
<img src="">




<h2>Tests</h2>
<hr>

<p>Am I responsive Test:</p>
<img src="">

<p>Lighthouse Test:</p>
<img src="">

<p>WRC CSS Validator:</p>
<img src="">

<p>CI Python Linter</p>
<img src="">

<p>Automatic Python Tests with Comments : </p>
<img src="">
<img src="">
<img src="">

<h2>Used Materials / References</h2>
<p>"CI" I Think Therefore I Blog project</p>
<p>"CI" Hello Django project</p>
<p>Auto assigning author to the posts :</p>
<a href="https://www.youtube.com/watch?v=-s7e_Fy6NRU&t=1573s&ab_channel=CoreySchafer">CoreySchafer</a>
<p>Profile Page edits :</p>
<a href="https://www.youtube.com/watch?v=D9Xd6jribFU&ab_channel=MaxGoodridge">Max Goodridge</a>
<p>Google Auth addon:</p>
<a href="https://dev.to/mdrhmn/django-google-authentication-using-django-allauth-18f8">AllAuth</a>



<h2>Deployment<h2>
<p>I have committed all the files and pushed them on to the repository. </p>
<p>Created requirement file for the dependencies used for the project to run:</p>



<a href="https://ibb.co/WnSTp8Z"><img src="https://i.ibb.co/Q9s5jSL/step-1-requirements-file-created.png" alt="step-1-requirements-file-created" border="0"></a>
<p>Made a new heroku app for the Zodiac Version:2.0</p>
<a href="https://ibb.co/sQM6Fpm"><img src="https://i.ibb.co/TRFbHDv/step-2-created-version-2-zodiac-app-on-heroku.png" alt="step-2-created-version-2-zodiac-app-on-heroku" border="0"></a>
<p> Added the necessary CONFIG VAR files, for the GOOGLE API's to work, as well as New PORT</p>
<a href="https://ibb.co/1Tpzvbx"><img src="https://i.ibb.co/KWQK0mH/step-3-config-vars-have-been-added-port-and-cred.png" alt="step-3-config-vars-have-been-added-port-and-cred" border="0"></a>
<p>For the project to work on heroku, added Python and NODE.JS buildpacks to the project</p>
<a href="https://ibb.co/z28w3C5"><img src="https://i.ibb.co/QH8GWhc/step-4-python-and-nodejs-buildpacks-have-been-added.png" alt="step-4-python-and-nodejs-buildpacks-have-been-added" border="0"></a>
<p>Connected GITHUB repo page to the heroku with project designation:</p>
<a href="https://ibb.co/k9L761h"><img src="https://i.ibb.co/KLtPzw9/step-5-connect-the-github-page-and-add-the-project.png" alt="step-5-connect-the-github-page-and-add-the-project" border="0"></a>
<p>Deployed the project on Heroku</p>
<a href="https://ibb.co/hMTr7ZG"><img src="https://i.ibb.co/0Xz1DF0/step-6-deploy-the-project-on-heroku.png" alt="step-6-deploy-the-project-on-heroku" border="0"></a>
<br>
<p>Link to the project:</p>
<a href="https://zodiac-version2-2c53e1995910.herokuapp.com/">Zodiac Project : 2.0</a>





<h2> The Process of the Program</h2>
<p>You are introduced to the program with a simple ASCII artwork and asked to enter your name</ul>
<p>This could be left empty and skipped, in which case system will assign that you wished to remain anonymous.</p>
<a href="https://ibb.co/j5XK4S0"><img src="https://i.ibb.co/H28vgjw/1.png" alt="1" border="0"></a>
<br>
<p>Then you are asked the year you were born in, this data is used to calculate "days alive" and Chinese Horoscope function:</p>
<a href="https://ibb.co/d7VNp98"><img src="https://i.ibb.co/QXTWHBy/2.png" alt="2" border="0"></a>
<p>Then you are asked to enter your month. Used to determining one of two possible Western Horoscope signs:</p>
<a href="https://ibb.co/L17wFNF"><img src="https://i.ibb.co/w4mHkck/3.png" alt="3" border="0"></a>
<p>Finally, the exact date you were born in, to narrow down the correct Horoscope Sign:</p>
<a href="https://ibb.co/VL58WwQ"><img src="https://i.ibb.co/wdj1Ncw/4.png" alt="4" border="0"></a>
<p>Then the functions determine which data to print out and gives you the result:</p>
<a href="https://ibb.co/syrXY4T"><img src="https://i.ibb.co/72F0mD3/5.png" alt="5" border="0"></a>
<p>And the Chinese horoscope part:</p>
<a href="https://ibb.co/0cgVycM"><img src="https://i.ibb.co/Vt7pYtS/6.png" alt="6" border="0"></a>


<h2>Testing and Error Checking<h2>
<p>I have been testing out the program extensively, original functions were developed to print out if the data input was correct and printed out statements if something went wrong, as well as acknowledgement if the functions worked correctly.</p>
<p>Some of these print statements were removed for the better flow of the project, but in case of the wrong input, it still displays what went wrong with the print out statement and asks the user to input the data again.</p>
<p>Correct input of the month is compared with the list of predefined months, that will print out the error if invalid month is included.</p>
<p>Months can be input either way, lower case or all caps, they will be transformed to usable format.</p>
<p>Also the Chinese Horoscope system is working from year 1948-2031, if other years are included. the system will show error notification that the current version works only with this range of years.</p>
<p>Code has been passed through the PEP8 and most of the problems have been fixed. ASCII art is giving errors and few lines of extended code, but both of those are needed</p>
<p>I personally couldn't get this code to break, and I posted the heroku link to on the Slacks #peer-code-review, where nobody found an error with the code as well.</p> 
<a href="https://ibb.co/Rhxq0cL"><img src="https://i.ibb.co/n3HFcjh/peer-review.png" alt="peer-review" border="0"></a>


<h2>Deployment<h2>
<p>I have committed all the files and pushed them on to the repository. </p>
<p>Created requirement file for the dependencies used for the project to run:</p>
<a href="https://ibb.co/WnSTp8Z"><img src="https://i.ibb.co/Q9s5jSL/step-1-requirements-file-created.png" alt="step-1-requirements-file-created" border="0"></a>
<p>Made a new heroku app for the Zodiac Version:2.0</p>
<a href="https://ibb.co/sQM6Fpm"><img src="https://i.ibb.co/TRFbHDv/step-2-created-version-2-zodiac-app-on-heroku.png" alt="step-2-created-version-2-zodiac-app-on-heroku" border="0"></a>
<p> Added the necessary CONFIG VAR files, for the GOOGLE API's to work, as well as New PORT</p>
<a href="https://ibb.co/1Tpzvbx"><img src="https://i.ibb.co/KWQK0mH/step-3-config-vars-have-been-added-port-and-cred.png" alt="step-3-config-vars-have-been-added-port-and-cred" border="0"></a>
<p>For the project to work on heroku, added Python and NODE.JS buildpacks to the project</p>
<a href="https://ibb.co/z28w3C5"><img src="https://i.ibb.co/QH8GWhc/step-4-python-and-nodejs-buildpacks-have-been-added.png" alt="step-4-python-and-nodejs-buildpacks-have-been-added" border="0"></a>
<p>Connected GITHUB repo page to the heroku with project designation:</p>
<a href="https://ibb.co/k9L761h"><img src="https://i.ibb.co/KLtPzw9/step-5-connect-the-github-page-and-add-the-project.png" alt="step-5-connect-the-github-page-and-add-the-project" border="0"></a>
<p>Deployed the project on Heroku</p>
<a href="https://ibb.co/hMTr7ZG"><img src="https://i.ibb.co/0Xz1DF0/step-6-deploy-the-project-on-heroku.png" alt="step-6-deploy-the-project-on-heroku" border="0"></a>
<br>
<p>Link to the project:</p>
<a href="https://zodiac-version2-2c53e1995910.herokuapp.com/">Zodiac Project : 2.0</a>


<h2> Materials Used / References</h2>
<p>ASCII Zodiac Code from: https://ascii.co.uk/art/zodiac</p>
<p>Delay Timer from: https://realpython.com/python-sleep/</p>
<p>Horoscope Information from : https://www.allure.com/story/zodiac-sign-personality-traits-dates</p>
<p>Chinese Horoscope from : https://www.oprahdaily.com/life/a35119928/chinese-zodiac-signs/</p>
<p>Google API integration borrowed from Love-Sandwiches project, GSPREAD web page used for the information : how to call specific lines from google sheets/columns to incorporate it in Python code</p>


<h2> The Persistent Problems </h2>
<p>With the google API integration came the delay, after the input of the year it takes few seconds to retrieve the data from google sheets.</p>
<p> The python code checker doesn't like the ASCII art and throw errors, but I don't think there's anything I can do about that.</p>
<p> Those are only errors that the checker doesn't like, line length and ascii art</p>
<p>I minimized the line length where I could, rest has to stay as is, per functionality of the project</p> 
<p>In version one there were problems with indentation. I have double checked all the code, there are 2 lines between each code section. 4-8-12 indents throughout<p>
<a href="https://ibb.co/ygHpNdV"><img src="https://i.ibb.co/ss8Cgbt/pep8.png" alt="pep8" border="0"></a>
<br>