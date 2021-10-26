## Screenshots from the lectures
****<br><br>
![1](screenshots/1.PNG)<br><br>
![2](screenshots/2.PNG)<br><br>
![3](screenshots/3.PNG)<br><br>
![4](screenshots/4.PNG)<br><br>
### Hello World with CBVs
![5](screenshots/5.PNG)<br><br>
![6](screenshots/6.PNG)<br><br>
**#start a project and an app. in settings.py add the app in the INSTALLED_APPS list, add TEMPLATE_DIR. create the templates folder. create index.html and base.html under the templates folder.**<br><br>
![7](screenshots/7.PNG)<br><br>
![8](screenshots/8.PNG)<br><br>
![9](screenshots/9.PNG)<br><br>
**this is a normal function based view. we'll replace this with a class based view**<br><br>
![10](screenshots/10.PNG)<br><br>
**#1. python manage.py migrate 2. python manage.py makemigrations 3. python manage.py migrate 4. python manage.py runserver 8080. check that everything works**<br><br>
![11](screenshots/11.PNG)<br><br>
**replace the function based view with a class based view**<br><br>
![12](screenshots/12.PNG)<br><br>
![13](screenshots/13.PNG)<br><br>
![14](screenshots/14.PNG)<br><br>
### Template views with CBVs
![15](screenshots/15.PNG)<br><br>
![16](screenshots/16.PNG)<br><br>
![17](screenshots/17.PNG)<br><br>
![18](screenshots/18.PNG)<br><br>
![19](screenshots/19.PNG)<br><br>
![20](screenshots/20.PNG)<br><br>
![21](screenshots/21.PNG)<br><br>
![22](screenshots/22.PNG)<br><br>
![23](screenshots/23.PNG)<br><br>
![24](screenshots/24.PNG)<br><br>
### Detail View and List View Part One
![25](screenshots/25.PNG)<br><br>
![26](screenshots/26.PNG)<br><br>
![27](screenshots/27.PNG)<br><br>
![28](screenshots/28.PNG)<br><br>
![29](screenshots/29.PNG)<br><br>
![30](screenshots/30.PNG)<br><br>
![31](screenshots/31.PNG)<br><br>
![32](screenshots/32.PNG)<br><br>
![33](screenshots/33.PNG)<br><br>
![34](screenshots/34.PNG)<br><br>
![35](screenshots/35.PNG)<br><br>
![36](screenshots/36.PNG)<br><br>
![37](screenshots/37.PNG)<br><br>
![38](screenshots/38.PNG)<br><br>
![39](screenshots/39.PNG)<br><br>
**add a few students per school**<br><br>
![40](screenshots/40.PNG)<br><br>
![41](screenshots/41.PNG)<br><br>
**create a templates folder under the app folder, and a subfolder with the app name. this is useful if you want to reuse your app in other projects. create the html files as shown**<br><br>
![42](screenshots/42.PNG)<br><br>
### Detail View and List View Part Two
![43](screenshots/43.PNG)<br><br>
![44](screenshots/44.PNG)<br><br>
**copy everything from base.html and paste to basic_app_base.html**<br><br>
![45](screenshots/45.PNG)<br><br>
![46](screenshots/46.PNG)<br><br>
**but where does the school_list context dictionary come from? it wasn't defined in the view.py file. check below**<br><br>
![47](screenshots/47.PNG)<br><br>
**We don't see any mention of the variable school underscore list.
So again, where does this actually come from?
School underscore list.
Do we have to define this by ourselves with some sort of call to a context dictionary?
And the list view object right here that we inherit from actually is doing the work of creating that
context dictionary and returning it for you.
*In fact, what it does is it takes the model you called, lowercases everything and then adds underscore
list.* So for ListViews, model = models.School would return a context dictionary of 'school_list'. But DetailViews return just the model name in lowercase. So model = models.School would return a context dictionary of 'school'**<br><br>
![48](screenshots/48.PNG)<br><br>
**but if you want to set the context dictionary name manually, set it using the context_object_name attribute**<br><br>
![49](screenshots/49.PNG)<br><br>
![50](screenshots/50.PNG)<br><br>
![51](screenshots/51.PNG)<br><br>
![52](screenshots/52.PNG)<br><br>
![53](screenshots/53.PNG)<br><br>
![54](screenshots/54.PNG)<br><br>
![55](screenshots/55.PNG)<br><br>
![56](screenshots/56.PNG)<br><br>
![57](screenshots/57.PNG)<br><br>
**remember that the student model did not have a primary key. it just had a foreign key which was the school. but django automatically adds an id in the background (serial id, like the first record has id 1, the second 2 and so on)**<br><br>
![58](screenshots/58.PNG)<br><br>
![59](screenshots/59.PNG)<br><br>
**the 'students' in 'school_detail.students.all' comes from the foreign key used in the Student model in models.py. screenshot below**<br><br>
![60](screenshots/60.PNG)<br><br>
![61](screenshots/61.PNG)<br><br>
![62](screenshots/62.PNG)<br><br>
**what's actually happening here? in school_list.html when we click on the school.name, the href is just going to return a single number, the actual number that corresponds to a primary key (pk). this is <pk> in the regex in the urls.py file. so this helps us link to that school's particular detail view. the regex says this - grab the basic_app extension of the domain name / whatever the number happens to be for the pk, and take that in as the SchoolDetailView**<br><br>
![63](screenshots/63.PNG)<br><br>
![64](screenshots/64.PNG)<br><br>
![65](screenshots/65.PNG)<br><br>
### CRUD Views
![66](screenshots/66.PNG)<br><br>
![67](screenshots/67.PNG)<br><br>
![68](screenshots/68.PNG)<br><br>
![69](screenshots/69.PNG)<br><br>
![70](screenshots/70.PNG)<br><br>
![71](screenshots/71.PNG)<br><br>
![72](screenshots/72.PNG)<br><br>
![73](screenshots/73.PNG)<br><br>
![74](screenshots/74.PNG)<br><br>
![75](screenshots/75.PNG)<br><br>
![76](screenshots/76.PNG)<br><br>
**the default name expected by django is the model name in lowercase underscore form. eg: school_form. so let's add that html file**<br><br>
![77](screenshots/77.PNG)<br><br>
**Well, basically what I'm saying is the following I'm going to extend from basic app, have the body
block and the heading of this form page.
That page is going to check if the instance of the primary key exists or not.
If it does not exist, that means this is a new school and we're going to create the school.
Otherwise we're updating a school that currently exists.
And this will make more sense as we actually develop the update view, but hopefully get the basic idea
that I'm checking first.**<br><br>
![78](screenshots/78.PNG)<br><br>
![79](screenshots/79.PNG)<br><br>
![80](screenshots/80.PNG)<br><br>
![80](screenshots/80.PNG)<br><br>
![81](screenshots/81.PNG)<br><br>
![82](screenshots/82.PNG)<br><br>
![83](screenshots/83.PNG)<br><br>
**submit the form again or refresh the page that was in error and click Continue when asked about form resubmission**<br><br>
![84](screenshots/84.PNG)<br><br>
![85](screenshots/85.PNG)<br><br>
**there are 2 because form was submitted twice**<br><br>
![86](screenshots/86.PNG)<br><br>
![87](screenshots/87.PNG)<br><br>
![88](screenshots/88.PNG)<br><br>
![89](screenshots/89.PNG)<br><br>
![90](screenshots/90.PNG)<br><br>
![91](screenshots/91.PNG)<br><br>
![92](screenshots/92.PNG)<br><br>
![93](screenshots/93.PNG)<br><br>
![94](screenshots/94.PNG)<br><br>
**success_url will call reverse underscore lazy.
And passing that, we want to go to the basic app and the list of you, so what this success, your
means is all right, once you successfully deleted a school, I want you to go back to the list page
of the basic app and show all the schools.
And theoretically, once you're done deleting it, that school should no longer be on that list.
The reason we use reverse lazy is that we don't want this evaluated completely when running our .py
file.
We only want it to wait until it's actually called as a success.**<br><br>
![95](screenshots/95.PNG)<br><br>
![96](screenshots/96.PNG)<br><br>
![97](screenshots/97.PNG)<br><br>
**_confirm_delete is the django default url naming. so we'll make a file with that name**<br><br>
![98](screenshots/98.PNG)<br><br>
![99](screenshots/99.PNG)<br><br>
![100](screenshots/100.PNG)<br><br>
