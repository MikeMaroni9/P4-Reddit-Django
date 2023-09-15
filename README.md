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
<a href="https://ibb.co/1JsMnZB"><img src="https://i.ibb.co/1JsMnZB/mainpicture1.png" alt="mainpicture1" border="0" /></a>


<p>For visitors that are not signed-up and logged in, you are greeted with mockddit logo which acts as a link button to index page, and two buttons on the opposite side. Register and Login</p>
<a href="https://ibb.co/NjVBh1h"><img src="https://i.ibb.co/NjVBh1h/mainpicture2.png" alt="mainpicture2" border="0" /></a>

<p>Register, takes you to the sign-up form that asks for username and password input, leaving email - optional.</p>
<a href="https://ibb.co/rFgyG1Z"><img src="https://i.ibb.co/rFgyG1Z/mainpicture3.png" alt="mainpicture3" border="0" /></a>

<p>Login, takes you to login page for prerigistered users and there's also a choice to sign in with google account, connected to Google API on the backend.</p>
<a href="https://ibb.co/mJywvxy"><img src="https://i.ibb.co/mJywvxy/mainpicture4.png" alt="mainpicture4" border="0" /></a>

<p>If you decide to sign in using goolge account, first you will be taken to the process page to check if you really like to perform this action</p>
<a href="https://ibb.co/Kr2wssp"><img src="https://i.ibb.co/Kr2wssp/mainpicture6.png" alt="mainpicture6" border="0" /></a>

<p>And then taken to the google login screen</p>
<a href="https://ibb.co/PNdcJwY"><img src="https://i.ibb.co/PNdcJwY/mainpicture7.png" alt="mainpicture7" border="0" /></a>

<p>Upon signing in, you will be returned to the index page. Bootstrap alert message will confirm that you have logged in/logged out. MSG will dissapear after few secons.</p>
<a href="https://ibb.co/SmvYtmv"><img src="https://i.ibb.co/SmvYtmv/mainpicture5msg.png" alt="mainpicture5msg" border="0" /></a>

<p>While logged in the navigation bar changes. Now you have option to create a New Post of visit your Profile Page.</p>
<a href="https://ibb.co/T4dfNt7"><img src="https://i.ibb.co/T4dfNt7/mainpicture8.png" alt="mainpicture8" border="0" /></a>

<p>Profile Page will show your information and also have the ability to edit it. </p>
<a href="https://ibb.co/6RXCG9v"><img src="https://i.ibb.co/6RXCG9v/mainpicture9.png" alt="mainpicture9" border="0" /></a>

<p>Editing the profile picture, you have ability to change, username, email, first name and last name. changing password has been turned off.</p>
<a href="https://ibb.co/X2Y9v1y"><img src="https://i.ibb.co/X2Y9v1y/editprofile.png" alt="editprofile" border="0"></a>

<p>New Post : You are greeted with a simple form to input Title and Content of your post. Username is asigned automatically for the logged in user. {% if authenticated %} has been added to allow only logged in User to create a new posts. Added is also Bootsrap MSG that can be dismissed, reminding users to be polite and follow the mockddits rules.</p>
<a href="https://ibb.co/fk8sqr7"><img src="https://i.ibb.co/fk8sqr7/newpost.png" alt="newpost" border="0"></a>

<p>Newests POSTS are automatically showed at the top of the page.</p>
<a href="https://ibb.co/Kxx00t6"><img src="https://i.ibb.co/Kxx00t6/mainpicture10.png" alt="mainpicture10" border="0" /></a>

<p>Author of the post has the ability to edit or to delete the post. User has to be logged in and user.id has to match author.id</p>
<a href="https://ibb.co/3mxQgRy"><img src="https://i.ibb.co/3mxQgRy/mainpicture11.png" alt="mainpicture11" border="0" /></a>

<p>As a signed in user, you can like the post, increasing the like count and add comments</p>
<a href="https://ibb.co/56cWNcL"><img src="https://i.ibb.co/56cWNcL/mainpicture12.png" alt="mainpicture12" border="0" /></a>

<p>Adding a comment takes you to new comments page, user id and current post is asigned automatically, leaving you with only option to leave a comment.</p>
<a href="https://ibb.co/bHjCs39"><img src="https://i.ibb.co/bHjCs39/mainpicture13.png" alt="mainpicture13" border="0" /></a>

<p>Maximum posts per page are 6, automatically paginating older post to the next page.</p>
<a href="https://ibb.co/MSrKpcx"><img src="https://i.ibb.co/MSrKpcx/mainpicture14.png" alt="mainpicture14" border="0" /></a>

<h2>Tests</h2>
<hr>

<p>Am I responsive Test:</p>
!!!!!!!!!!!!!!!! HAVE TO ADD

<p>Lighthouse Test:</p>
<a href="https://ibb.co/T1C5tg4"><img src="https://i.ibb.co/T1C5tg4/lighthouse.png" alt="lighthouse" border="0" /></a>

<p>WRC CSS Validator:</p>
<a href="https://ibb.co/rmrxXx7"><img src="https://i.ibb.co/rmrxXx7/css-validator.png" alt="css-validator" border="0" /></a>

<p>CI Python Linter</p>
<a href="https://ibb.co/4ZvGvvC"><img src="https://i.ibb.co/4ZvGvvC/linter1.png" alt="linter1" border="0" /></a>
<a href="https://ibb.co/G7SC7m7"><img src="https://i.ibb.co/G7SC7m7/linter2.png" alt="linter2" border="0" /></a>
<a href="https://ibb.co/5r4ZqDB"><img src="https://i.ibb.co/5r4ZqDB/linter3.png" alt="linter3" border="0" /></a>
<a href="https://ibb.co/Zcp6d96"><img src="https://i.ibb.co/Zcp6d96/linter4.png" alt="linter4" border="0" /></a>

<p>Automatic Python Tests with Comments : </p>
<a href="https://ibb.co/SNbpmxx"><img src="https://i.ibb.co/SNbpmxx/mainpicture15.png" alt="mainpicture15" border="0" /></a>
<a href="https://ibb.co/zbNDqd0"><img src="https://i.ibb.co/zbNDqd0/mainpicture16.png" alt="mainpicture16" border="0" /></a>
<a href="https://ibb.co/YDCHDLX"><img src="https://i.ibb.co/YDCHDLX/mainpicture17.png" alt="mainpicture17" border="0" /></a>


<h2>Used Materials / References</h2>
<p>"CI" I Think Therefore I Blog project</p>
<p>"CI" Hello Django project</p>
<p>Auto assigning author to the posts : <a href="https://www.youtube.com/watch?v=-s7e_Fy6NRU&t=1573s&ab_channel=CoreySchafer">CoreySchafer</a></p>

<p>Profile Page edits : <a href="https://www.youtube.com/watch?v=D9Xd6jribFU&ab_channel=MaxGoodridge">Max Goodridge</a></p>

<p>Google Auth addon: <a href="https://dev.to/mdrhmn/django-google-authentication-using-django-allauth-18f8">AllAuth</a></p>




<h2>Deployment<h2>
<p>1.Installing gunicorn server to run Django on heroku</p>
<a href="https://ibb.co/Z8FVtm5"><img src="https://i.ibb.co/Z8FVtm5/dep1.png" alt="dep1" border="0" /></a>
<p>2.Install psycopg2 adapted for PostgreSQL database</p>
<a href="https://ibb.co/TqdQZd6"><img src="https://i.ibb.co/TqdQZd6/dep2.png" alt="dep2" border="0" /></a>
<p>Creating a Requirements.txt file for necessery dependencies</p>
<a href="https://ibb.co/8zTn72y"><img src="https://i.ibb.co/8zTn72y/mainpicture18.png" alt="mainpicture18" border="0" /></a>
<p>Creatign a new project in Django</p>
<a href="https://ibb.co/VVMd79Y"><img src="https://i.ibb.co/VVMd79Y/dep4.png" alt="dep4" border="0" /></a>
<p>Creating the blogg app</p>
<a href="https://ibb.co/h7wXvLr"><img src="https://i.ibb.co/h7wXvLr/dep5.png" alt="dep5" border="0" /></a>
<p>Linking GitHub repository to Heroku</p>
<a href="https://ibb.co/3Y9qzHd"><img src="https://i.ibb.co/3Y9qzHd/dep6.png" alt="dep6" border="0" /></a>
<p>Creating a PostgreSQL database</p>
<a href="https://ibb.co/3kp0ZjK"><img src="https://i.ibb.co/3kp0ZjK/dep7.png" alt="dep7" border="0" /></a>
<p>Adjusting env.py and settings.py files</p>
<p>Setting Config Vars in Heroku</p>
<a href="https://ibb.co/4MmGjNw"><img src="https://i.ibb.co/4MmGjNw/dep8.png" alt="dep8" border="0" /></a>
<p>Creating a Procfile</p>
<a href="https://ibb.co/wzQ5B9J"><img src="https://i.ibb.co/wzQ5B9J/dep9.png" alt="dep9" border="0" /></a>
<p>Set Debug Mode to False</p>
<a href="https://ibb.co/bmWZc4Q"><img src="https://i.ibb.co/bmWZc4Q/dep11.png" alt="dep11" border="0" /></a>
<p>Add - X_FRAME_OPTIONS ='SAMEORIGIN' to settings file.</p>
<a href="https://ibb.co/bmWZc4Q"><img src="https://i.ibb.co/bmWZc4Q/dep11.png" alt="dep11" border="0" /></a>
<p>Deploying a project on Heroku</p>
<a href="https://ibb.co/Kj8gPW1"><img src="https://i.ibb.co/Kj8gPW1/dep10.png" alt="dep10" border="0" /></a>
<p>I have committed all the files and pushed them on to the repository. </p>
<p>Created requirement file for the dependencies used for the project to run:</p>
<hr>
<h2> The Persistent Problems </h2>
<p>Wanted to include more login functionality, forgot password etc. Couldn't get mail server to work. SendGrid didn't let me access the account. Might be because of the VPN use.</p>
<p>Couldn't figure out how to include more comments functionality, to edit and delete them.</p>
<br>