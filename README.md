<h2> Final Resubmission
<h3>Intro</h3>
<hr>
<p>As I was busy refactoring and upgrading the Project 3, I missed the deadline of the Project 4 submissions so that automatically counted as failed attempt. Then I started working on Project 4 named: 
<br><br>
"mockddit - Reddit style web page with authentication, ability to create posts, delete posts. Leave comments and like the posts." 
<br><br>
Unfortunately this second submission failed, leaving me with the final attempt to pass the Project 4.</p>
<a href="https://drive.google.com/file/d/150gy7Fj_-rUseUz-EINGW9FHZY9u1Ehp/view?usp=drive_link">Evaluation Details</a>
<br>
<br>
<p>Most of the project passed the criteria so I focused only on improving the topics that were hightlighted to me. Without changing the core of the project.</p>
<p>Here's the list of comments with my solutions added underneath. </p>
<hr>
<br>

1) Acceptable use of Agile software developement tools, with scope for improvement with documentation of sprints and milestones

<br>
<br>
The USER STORIES have been update, missing ones added. They have always been in the project but wasn't defined as such. Milestones created for Interations and user stories divided per subject.
<br>
<br>
<a href="https://ibb.co/wzxzVYw"><img src="https://i.ibb.co/Kr3rdmL/1-milestones.png" alt="1-milestones" border="0"></a>
<br>
Acceptance Criteria added to all User Stories.
<br>
<a href="https://ibb.co/0hRJMXj"><img src="https://i.ibb.co/RzkH0Sp/2-Acceptance-Criteria.png" alt="2-Acceptance-Criteria" border="0"></a>

<br>
<br>

2) Some HTML Validation errors seen on :
<br>

   <ul>https://validator.w3.org/nu/?doc=https://project4-django-blog-x-24e6733e46ab.herokuapp.com/</ul>
   <ul>https://validator.w3.org/nu/?doc=https://project4-django-blog-x-24e6733e46ab.herokuapp.com/detail/48</ul>
   <ul>https://validator.w3.org/nu/?doc=https://project4-django-blog-x-24e6733e46ab.herokuapp.com/accounts/signup/</ul>


Fixed most of the validator errors, only left with few. Not really an errors as suggestions how to better write and not use Buttons inside a tags, but if I fix it with span instead then my CSS styling dissapears and I have much bigger issues that I would like to address than to fix those at the moment. If I will have time I will come back to it before handing in the project. But even without the absolutely clean code last time the code went in for a review it passed, so I don't think it's such a crucial part.
<br>
<br>
<br>


3) Listing the posts made by the user on the profile page could have added some depth to this project overall, as would have creating new custom models like a contact model or some category models etc.
<br>
<br>
Listing all posts in the profile menu added with links taking each posts to each own detail view. 
<br>
<a href="https://ibb.co/V2tQLc3"><img src="https://i.ibb.co/D5t81HL/Profile-Page-Update.png" alt="Profile-Page-Update" border="0"></a>
<br>
<br>
Category Selection added when creating a new post.
<br>
<br>
<a href="https://ibb.co/HTLqk0w"><img src="https://i.ibb.co/xqK6Ry9/category-added-for-new-posts.png" alt="category-added-for-new-posts" border="0"></a>
<br>
Category can be seen by each individual post in Index html
<br>
<br>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/LpRbdsh/post-category.png" alt="post-category" border="0"></a>
<br>
<br>
And in post detail view upon opening the post
<br>
<br>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/xzKYNc6/post-category-2.png" alt="post-category-2" border="0"></a>
<br>
<br>
Achieved by adding Post Filter option to the Post models class, with multiple selection filter.
<br>
<br>
<a href="https://ibb.co/x3G4xgN"><img src="https://i.ibb.co/4JMQhSH/newnew.png" alt="newnew" border="0"></a>
<br>
<br>
<br>
Comment section upgraded, comments are now editable and deletable. 
<br>
<br>
<a href="https://ibb.co/ZxgN33d"><img src="https://i.ibb.co/4pSJccW/comments-1.png" alt="comments-1" border="0"></a><br>

<br>
<br>
<a href="https://ibb.co/9wMRybP"><img src="https://i.ibb.co/s5BLsK7/comment-3.png" alt="comment-3" border="0"></a>
<br>
<br>
<a href="https://ibb.co/VwpkqyJ"><img src="https://i.ibb.co/FHqdDvm/comment-2.png" alt="comment-2" border="0"></a>
<br>

LO4 - Create automated tests for a Full-Stack Web application using an MVC framework and related contemporary technologies:

5) 4.1  No  Minimal evidence of testing within the project
6) 4.2  No  Minimal evidence of testing within the project
7) 4.3  No  Minimal evidence of testing within the project

<h2>Testing</h2>
<hr>
I created 3 individual files = test_models.py, test_views.py and test_forms.py that covered most of the testing process and also created test_admin file to fill out the necessary coverage to get it to 100%.
<br> 
<br> 
For testing purposes I have installed the Coverage.py as a tool for measuring code testing coverage of Python program. 
<br>
<br>
<a href="https://ibb.co/kcs4Wqz"><img src="https://i.ibb.co/DKH9Swm/1-install-coverage.png" alt="1-install-coverage" border="0"></a>

I ran the program via the code: 
<br>
<br>
<a href="https://ibb.co/3ydnByx"><img src="https://i.ibb.co/KjhJFjt/2-coverage-test-run.png" alt="2-coverage-test-run" border="0"></a>
<br>

The code ran 22 tests in 13.534 sec and found no errors.
<br>
And after the test has executed I ran the “coverage report” command to see the total coverage of the unit test created. 
<br>

<a href="https://ibb.co/42CPJSq"><img src="https://i.ibb.co/FXcgnYr/3-coverage-report.png" alt="3-coverage-report" border="0"></a>
<br>

All test have comments attached to them explaining what each of the test is testing for.
<br>

A total of 100% was covered. 
<hr>

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

4. There needs to be objective evidence provided for the testing performed here. 
Consider adding six main sections with screenshots to the testing:

<br>
1)Manual testing of each section of the site (such as buttons, links etc)
<br>
<br>
2.Testing site responsiveness using a site like <https://responsivedesignchecker.com/>
<br>
<br>
3.Code validation (CSS/HTML/JS using online tools like https://jigsaw.w3.org/css-validator and JSHint) 
<br>
<br>
4.Testing of all user stories/features 
<br>
<br>
5.Documentation of any bugs encountered and their resolution steps
<br>
<br>
6.Documentation of any open bugs Ideally, test cases should focus on each individual section of every page on the website. Each test case should be specific, objective, step-wise replicable. 
<br>
<br>
Instead of adding a general overview saying that everything works fine, consider documenting tests on each element on the page (ie. buttons, input boxes, navigation links etc) by testing them in their happy flow and also the bad/exception flow, mentioning the expected and the observed results, and drawing a parallel between them. 

Consider using the following format for manual test cases: Expected - Feature is expected to do X when the user does Y Testing - Tested the feature by doing Y Result - The feature did not respond due to A,B,C or Result - The feature acted as normally and it did Y Fix - I did Z to the code because something was missing

All code has been put through https://codebeautify.org/python-formatter-beautifier for general appearance and readability.



<h1> Project 4 - Reddit Style Blog</h1>
<h2> mockddit</h2>
<p> Blog type application where a registered user can create a new posts, or comment on already existing one.</p>
<p> Developed using : HTML, CSS, JAVASCRIPT, PYTHON, BOOTSTRAP and DJANGO</p>
<br>
<p>Link to the project on Heroku: <a href="https://project4-django-blog-x-24e6733e46ab.herokuapp.com/">mockddit on Heroku</a></p>
<br>
<p>Link to the GITHUB repository: <a href="https://github.com/MikeMaroni9/P4-Reddit-Django">GITHUB</a></p>
<br>
<p>Link to the GITHUB USER Stories: <a href="https://github.com/users/MikeMaroni9/projects/6">User Stories</a></p>
<br>
<p>Link to the Milestones : <a href="https://github.com/MikeMaroni9/P4-Reddit-Django/milestones">Milestones</a></p>

<p>These User Stories with acceptance criteria and Milestones should be the correct ones.</p>
<p>This is the second iteration of the project and until now I still used original userstories and milestones from first iteration, now I tried to carry everything over to the current file. It should be up to date and correct but in case I have made an error, here's the original updated list.


<br>
<p>GITHUB USER Stories 1st Iteration: <a href="https://github.com/users/MikeMaroni9/projects/4/views/1">User Stories</a></p>
<br>
<p>Link to the Milestones 1st Iteration: <a href="https://github.com/MikeMaroni9/P4-Reddit-Style-Blog-Django/milestones">Milestones</a></p>
<br>
<br>
<h2> The Process of the Web Page</h2>
<p>Reddit style web page with authentication, ability to create posts, delete posts. Leave comments and like the posts.</p>

<p>Upon opening a page, you are greeted with pre-filled reddit style page. All content is taken from the original reddit page, including the comments and chosen randomly without particular agenda</p>

<a href="https://ibb.co/qdgg0WK"><img src="https://i.ibb.co/rmppbcY/mainpicture1.png" alt="mainpicture1" border="0"></a>

<p>For visitors that are not signed-up and logged in, you are greeted with mockddit logo which acts as a link button to index page, and two buttons on the opposite side. Register and Login</p>

<a href="https://ibb.co/hYwyf1b"><img src="https://i.ibb.co/xFdDH8W/mainpicture2.png" alt="mainpicture2" border="0"></a>

<p>Register, takes you to the sign-up form that asks for username and password input, leaving email - optional.</p>

<a href="https://ibb.co/yXGWmhc"><img src="https://i.ibb.co/f2B4V8z/mainpicture3.png" alt="mainpicture3" border="0"></a>
<p>Login, takes you to login page for prerigistered users and there's also a choice to sign in with google account, connected to Google API on the backend.</p>

<a href="https://ibb.co/hV72CM6"><img src="https://i.ibb.co/7KYrbzf/mainpicture4.png" alt="mainpicture4" border="0"></a>

<p>If you decide to sign in using goolge account, first you will be taken to the process page to check if you really like to perform this action</p>

<a href="https://ibb.co/JpVXDh1"><img src="https://i.ibb.co/HP6m5JS/mainpicture6.png" alt="mainpicture6" border="0"></a>

<p>And then taken to the google login screen</p>
<a href="https://ibb.co/SxMZYGs"><img src="https://i.ibb.co/7zZ0MLY/mainpicture7.png" alt="mainpicture7" border="0"></a>

<p>Upon signing in, you will be returned to the index page. Bootstrap alert message will confirm that you have logged in/logged out. MSG will dissapear after few secons.</p>

<a href="https://ibb.co/tYqg8pr"><img src="https://i.ibb.co/gtSNzZK/mainpicture5msg.png" alt="mainpicture5msg" border="0"></a>

<p>While logged in the navigation bar changes. Now you have option to create a New Post of visit your Profile Page.</p>

<a href="https://ibb.co/FHjpPFg"><img src="https://i.ibb.co/ph9qmSJ/mainpicture8.png" alt="mainpicture8" border="0"></a>

<p>Profile Page will show your information and also have the ability to edit it. </p>

<a href="https://ibb.co/FqW1WXK"><img src="https://i.ibb.co/4gfLf27/mainpicture9.png" alt="mainpicture9" border="0"></a>

<p>Editing the profile picture, you have ability to change, username, email, first name and last name. changing password has been turned off.</p>

<a href="https://ibb.co/c60D2LT"><img src="https://i.ibb.co/m9k6h8z/editprofile.png" alt="editprofile" border="0"></a>


<p>New Post : You are greeted with a simple form to input Title and Content of your post. Username is asigned automatically for the logged in user. {% if authenticated %} has been added to allow only logged in User to create a new posts. Added is also Bootsrap MSG that can be dismissed, reminding users to be polite and follow the mockddits rules.</p>

<a href="https://ibb.co/WW9rSSL"><img src="https://i.ibb.co/QFBWss4/newpost.png" alt="newpost" border="0"></a>

<p>Newests POSTS are automatically showed at the top of the page.</p>

<a href="https://ibb.co/pd9hSxr"><img src="https://i.ibb.co/x6RFND8/mainpicture10.png" alt="mainpicture10" border="0"></a>




<p>Author of the post has the ability to edit or to delete the post. User has to be logged in and user.id has to match author.id</p>

<a href="https://ibb.co/7ggyDPZ"><img src="https://i.ibb.co/s5534nN/mainpicture11.png" alt="mainpicture11" border="0"></a>






<p>As a signed in user, you can like the post, increasing the like count and add comments</p>

<a href="https://ibb.co/NFp8M9q"><img src="https://i.ibb.co/K57MJ2g/mainpicture12.png" alt="mainpicture12" border="0"></a>




<p>Adding a comment takes you to new comments page, user id and current post is asigned automatically, leaving you with only option to leave a comment.</p>

<a href="https://ibb.co/wMYNqsv"><img src="https://i.ibb.co/J5CRTQh/mainpicture13.png" alt="mainpicture13" border="0"></a>



<p>Maximum posts per page are 6, automatically paginating older post to the next page.</p>

<a href="https://ibb.co/vjZcH7z"><img src="https://i.ibb.co/3CBT7Dh/mainpicture14.png" alt="mainpicture14" border="0"></a>

<h2>Tests</h2>
<hr>

<p>Lighthouse Test:</p>

<a href="https://ibb.co/TgtpWHR"><img src="https://i.ibb.co/jrDBJLG/lighthouse.png" alt="lighthouse" border="0"></a>

<p>WRC CSS Validator:</p>

<a href="https://ibb.co/BKTh3g5"><img src="https://i.ibb.co/yBgzP8c/css-validator.png" alt="css-validator" border="0"></a>

<p>CI Python Linter</p>

<a href="https://ibb.co/R04563J"><img src="https://i.ibb.co/BZK16yY/linter1.png" alt="linter1" border="0"></a>
<br>
<a href="https://ibb.co/Fbks6CJ"><img src="https://i.ibb.co/qML0BV9/linter2.png" alt="linter2" border="0"></a>
<br>
<a href="https://ibb.co/nmmQVnp"><img src="https://i.ibb.co/YQQfKyg/linter3.png" alt="linter3" border="0"></a>
<br>
<a href="https://ibb.co/9Y3mrDC"><img src="https://i.ibb.co/zfHW4M0/linter4.png" alt="linter4" border="0"></a>

<p>Automatic Python Tests with Comments : </p>

<a href="https://ibb.co/JsQjprX"><img src="https://i.ibb.co/rws2p5n/mainpicture15.png" alt="mainpicture15" border="0"></a>
<br>
<a href="https://ibb.co/ctrJTk0"><img src="https://i.ibb.co/Gk57Pny/mainpicture16.png" alt="mainpicture16" border="0"></a>
<br>
<a href="https://ibb.co/c15HRkY"><img src="https://i.ibb.co/wRHX8Bc/mainpicture17.png" alt="mainpicture17" border="0"></a>

<h2>Database Construct</h2>

<a href="https://ibb.co/MBk14Jh"><img src="https://i.ibb.co/cYh8Hsv/Posts-and-Comments-database-relationship.png" alt="Posts-and-Comments-database-relationship" border="0"></a>
<hr>

<h2>Used Materials / References</h2>
<hr>
<p>"CI" I Think Therefore I Blog project</p>
<p>"CI" Hello Django project</p>
<p>Auto assigning author to the posts : <a href="https://www.youtube.com/watch?v=-s7e_Fy6NRU&t=1573s&ab_channel=CoreySchafer">CoreySchafer</a></p>

<p>Profile Page edits : <a href="https://www.youtube.com/watch?v=D9Xd6jribFU&ab_channel=MaxGoodridge">Max Goodridge</a></p>

<p>Google Auth addon: <a href="https://dev.to/mdrhmn/django-google-authentication-using-django-allauth-18f8">AllAuth</a></p>

<h2>Deployment<h2>
<p>1.Installing gunicorn server to run Django on heroku</p>

<a href="https://ibb.co/jzBVrqR"><img src="https://i.ibb.co/VxrHqbm/dep1.png" alt="dep1" border="0"></a>
<p>2.Install psycopg2 adapted for PostgreSQL database</p>

<a href="https://ibb.co/FntW6C7"><img src="https://i.ibb.co/7bFzvLy/dep2.png" alt="dep2" border="0"></a>
<p>Creating a Requirements.txt file for necessery dependencies</p>
<a href="https://ibb.co/C50wCpG"><img src="https://i.ibb.co/XZJW0fR/dep3.png" alt="dep3" border="0"></a>

<a href="https://imgbb.com/"><img src="https://i.ibb.co/yPbCD8p/mainpicture18.png" alt="mainpicture18" border="0"></a>
<p>Creatign a new project in Django</p>

<a href="https://ibb.co/nw2yt10"><img src="https://i.ibb.co/p1DT5KP/dep4.png" alt="dep4" border="0"></a>
<p>Creating the blogg app</p>

<a href="https://ibb.co/fxLrq5y"><img src="https://i.ibb.co/bKDNQZC/dep5.png" alt="dep5" border="0"></a>
<p>Linking GitHub repository to Heroku</p>

<a href="https://ibb.co/TLQJrTG"><img src="https://i.ibb.co/Wtr7s3X/dep6.png" alt="dep6" border="0"></a>
<p>Creating a PostgreSQL database</p>

<a href="https://ibb.co/VWJzwyz"><img src="https://i.ibb.co/rGFzdPz/dep7.png" alt="dep7" border="0"></a>
<p>Adjusting env.py and settings.py files</p>
<a href="https://ibb.co/C50wCpG"><img src="https://i.ibb.co/XZJW0fR/dep3.png" alt="dep3" border="0"></a>
<p>Setting Config Vars in Heroku</p>

<a href="https://ibb.co/mv1N5GK"><img src="https://i.ibb.co/M8WBksH/dep8.png" alt="dep8" border="0"></a>
<p>Creating a Procfile</p>

<a href="https://imgbb.com/"><img src="https://i.ibb.co/NZy09sj/dep9.png" alt="dep9" border="0"></a>
<p>Set Debug Mode to False</p>

<a href="https://ibb.co/82YY3t3"><img src="https://i.ibb.co/S0ffTGT/dep11.png" alt="dep11" border="0"></a>
<p>Add - X_FRAME_OPTIONS ='SAMEORIGIN' to settings file.</p>

<a href="https://ibb.co/82YY3t3"><img src="https://i.ibb.co/S0ffTGT/dep11.png" alt="dep11" border="0"></a>
<p>Deploying a project on Heroku</p>

<a href="https://ibb.co/J2rLXHc"><img src="https://i.ibb.co/vmL52kc/dep10.png" alt="dep10" border="0"></a>
<hr>
<h2> The Persistent Problems </h2>
<p>Wanted to include more login functionality, forgot password etc. Couldn't get mail server to work. SendGrid didn't let me access the account. Might be because of the VPN use.</p>
<p>Couldn't figure out how to include more comments functionality, to edit and delete them.</p>
<br>










