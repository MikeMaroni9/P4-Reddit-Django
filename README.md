<h1> Project 4 - Reddit Style Blog</h1>
<h2> mockdd <span style="color:red;">">i</span>t</h2>
<p> Blog type application where a registered user can create a new posts, or comment on already existing one.</p>
<p> Developed using : HTML, CSS, JAVASCRIPT, PYTHON, BOOTSTRAP and DJANGO</p>
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
<a href="https://ibb.co/0cgVycM"><img src="https://i.ibb.co/Vt7pYtS/6.png" alt="6" border="0"></a>
<a href="https://ibb.co/1JsMnZB"><img src="https://i.ibb.co/1JsMnZB/mainpicture1.png" alt="mainpicture1" border="0" /></a>


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
<img src="../P4-Reddit-Django/media/dep11.png">

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
<p>1.Installing gunicorn server to run Django on heroku</p>
<img src="">
<p>2.Install psycopg2 adapted for PostgreSQL database</p>
<img src="">
<p>Creating a Requirements.txt file for necessery dependencies</p>
<img src="">
<p>Creatign a new project in Django</p>
<img src="">
<p>Creating the blogg app</p>
<img src="">
<p>Linking GitHub repository to Heroku</p>
<img src="">
<p>Creating a PostgreSQL database</p>
<img src="">
<p>Adjusting env.py and settings.py files</p>
<img src="">
<p>Setting Config Vars in Heroku</p>
<img src="">
<p>Creating a Procfile</p>
<img src="">
<p>Set Debug Mode to False</p>
<img src="">
<p>Add - X_FRAME_OPTIONS ='SAMEORIGIN' to settings file.</p>
<img src="">
<p>Deploying a project on Heroku</p>
<img src="">
<p>I have committed all the files and pushed them on to the repository. </p>
<p>Created requirement file for the dependencies used for the project to run:</p>




<h2> The Persistent Problems </h2>
<p>Wanted to include more login functionality, forgot password etc. Couldn't get mail server to work. SendGrid didn't let me access the account. Might be because of the VPN use.</p>
<p>Couldn't figure out how to include more comments functionality, to edit and delete them.</p>
<br>