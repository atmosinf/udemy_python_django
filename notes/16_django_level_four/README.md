## Screenshots from the lectures<br>

![1](screenshots/1.PNG)<br><br>
![2](screenshots/2.PNG)<br><br>
![3](screenshots/3.PNG)<br><br>
![4](screenshots/4.PNG)<br><br>
![5](screenshots/5.PNG)<br><br>
### Relative URLs with templates
![6](screenshots/6.PNG)<br><br>
![7](screenshots/7.PNG)<br><br>
![8](screenshots/8.PNG)<br><br>
![9](screenshots/9.PNG)<br><br>
![10](screenshots/10.PNG)<br><br>
![11](screenshots/11.PNG)<br><br>
![12](screenshots/12.PNG)<br><br>
![13](screenshots/13.PNG)<br><br>
![14](screenshots/14.PNG)<br><br>
**First set up the project as usual. create a basic_app and a templates folder. set the template directory and add basicapp in settings.py. under templates folder, create a base.html(this will be filled in later), index.html and other.html, and finally a file called relative_url_templates.html which will contain all our relative urls. **<br><br>
![15](screenshots/15.PNG)<br><br>
![16](screenshots/16.PNG)<br><br>
![17](screenshots/17.PNG)<br><br>
![18](screenshots/18.PNG)<br><br>
![19](screenshots/19.PNG)<br><br>
![20](screenshots/20.PNG)<br><br>
**the app_name is used in the template tag (screenshot below).**
![21](screenshots/21.PNG)<br><br>
**NOTE!! The 'basic_app' in the template tag is not from the folder name. It is from the app_name used in urls.py. and similarly, 'other' in the template tag refers to the 'other' in the 'name' specified in urls.py (name='other')**<br><br>
![22](screenshots/22.PNG)<br><br>
![23](screenshots/23.PNG)<br><br>
![24](screenshots/24.PNG)<br><br>
![25](screenshots/25.PNG)<br><br>
**OK, let's move along to show you how you could add something like the admin page as a anchor tax.
We'll say ref.
Percent sign, and then for this, again, you call your URL, and in this case, you're going to call
admin.
Index, so basically what's going on is if you go to settings that pine you're project, you'll notice
that not only is your basic app a application, but also Django that contributes admin and we don't
actually have that open.
But if you wanted to, you could open up the source code or just check out the application admin.
That's something that always gets imported as an install that application.
But inside of that, in its own URL, Stoppie, a file, there is an admin application with an index
named View that it will take you to something.
To note here is that in order for this to work, sometimes you have to make the migration just because
admin wants it that way so we can go ahead and do that.**<br><br>
![26](screenshots/26.PNG)<br><br>
![27](screenshots/27.PNG)<br><br>
![28](screenshots/28.PNG)<br><br>
![29](screenshots/29.PNG)<br><br>
![30](screenshots/30.PNG)<br><br>
**how to go to the index page as an anchor tag**<br><br>
![31](screenshots/31.PNG)<br><br>
![32](screenshots/32.PNG)<br><br>
### URL template inheritance
![33](screenshots/33.PNG)<br><br>
![34](screenshots/34.PNG)<br><br>
![35](screenshots/35.PNG)<br><br>
![36](screenshots/36.PNG)<br><br>
![37](screenshots/37.PNG)<br><br>
![38](screenshots/38.PNG)<br><br>
![39](screenshots/39.PNG)<br><br>
![40](screenshots/40.PNG)<br><br>
![41](screenshots/41.PNG)<br><br>
![42](screenshots/42.PNG)<br><br>
![43](screenshots/43.PNG)<br><br>
![44](screenshots/44.PNG)<br><br>
![45](screenshots/45.PNG)<br><br>
![46](screenshots/46.PNG)<br><br>
![47](screenshots/47.PNG)<br><br>
![48](screenshots/48.PNG)<br><br>
**navbar links work after template tagging**<br><br>
### Template filters and custom filters
![49](screenshots/49.PNG)<br><br>
![50](screenshots/50.PNG)<br><br>
![51](screenshots/51.PNG)<br><br>
![52](screenshots/52.PNG)<br><br>
![53](screenshots/53.PNG)<br><br>
![54](screenshots/54.PNG)<br><br>
![55](screenshots/55.PNG)<br><br>
![56](screenshots/56.PNG)<br><br>
![57](screenshots/57.PNG)<br><br>
![58](screenshots/58.PNG)<br><br>
![59](screenshots/59.PNG)<br><br>
![60](screenshots/60.PNG)<br><br>
![61](screenshots/61.PNG)<br><br>
![62](screenshots/62.PNG)<br><br>
![63](screenshots/63.PNG)<br><br>
![64](screenshots/64.PNG)<br><br>
![65](screenshots/65.PNG)<br><br>
**create a new folder, let's call it templatetags, under the app folder (in this case, under the basic_app folder. not in the project folder). create an empty __init__.py file inside it. this tells python to treat it as a module**<br><br>
![66](screenshots/66.PNG)<br><br>
**So the first one is going to be the string that you call the function when you're using a template tag.
The second one is the function itself.**<br><br>
![67](screenshots/67.PNG)<br><br>
**don't forget to add {% load my_extras %} at the top (lecturer forgot to do that here. check the first screenshot in this section for details)**<br><br>
![68](screenshots/68.PNG)<br><br>
![69](screenshots/69.PNG)<br><br>
**This is a better way to register the custom filter using a decorator**<br><br>
![70](screenshots/70.PNG)<br><br>
**Example of loading the custom filter - {% load my_extras %}. The {% extends %} tag should always come first**<br><br>