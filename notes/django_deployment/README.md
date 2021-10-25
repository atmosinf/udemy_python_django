## Screenshots from the lectures<br>

![1](screenshots/1.PNG)<br><br>
![2](screenshots/2.PNG)<br><br>
![3](screenshots/3.PNG)<br><br>
![4](screenshots/4.PNG)<br><br>
[Deploying to Python Anywhere](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/)<br>
[Deploying to Heroku](https://devcenter.heroku.com/articles/deploying-python)<br>
[Deploying to AWS](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-local-django-app-to-a-vps)<br>
[Deploying to VPS with Digital Ocean](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html)<br><br>
![5](screenshots/5.PNG)<br><br>
![6](screenshots/6.PNG)<br><br>
### Setting up github
![7](screenshots/7.PNG)<br><br>
![8](screenshots/8.PNG)<br><br>
![9](screenshots/9.PNG)<br><br>
![10](screenshots/10.PNG)<br><br>
![11](screenshots/11.PNG)<br><br>
### Deployment walkthrough on Python Anywhere
![12](screenshots/12.PNG)<br><br>
![13](screenshots/13.PNG)<br><br>
**create a new account on python anywhere**<br><br>
![14](screenshots/14.PNG)<br><br>
![15](screenshots/15.PNG)<br><br>
**make a virtual environment using the command shown above. python anywhere does not have conda**<br><br>
![16](screenshots/16.PNG)<br><br>
**Find the version of django you used and install it in python anywhere**<br><br>
![17](screenshots/17.PNG)<br><br>
![18](screenshots/18.PNG)<br><br>
**verify that django is installed**<br><br>
![19](screenshots/19.PNG)<br><br>
![20](screenshots/20.PNG)<br><br>
![21](screenshots/21.PNG)<br><br>
**go to the project root folder and migrate**<br><br>
![22](screenshots/22.PNG)<br><br>
![23](screenshots/23.PNG)<br><br>
![24](screenshots/24.PNG)<br><br>
![25](screenshots/25.PNG)<br><br>
![26](screenshots/26.PNG)<br><br>
![27](screenshots/27.PNG)<br><br>
![28](screenshots/28.PNG)<br><br>
![29](screenshots/29.PNG)<br><br>
**find the path to project root**<br><br>
![30](screenshots/30.PNG)<br><br>
**paste it under Code in the Web tab**<br><br>
![31](screenshots/31.PNG)<br><br>
![32](screenshots/32.PNG)<br><br>
**delete the hello world code (lines 13 - 47 in this case)**<br><br>
![33](screenshots/33.PNG)<br><br>
![34](screenshots/34.PNG)<br><br>
**now save and go to the link (below) to check if there are no gateway errors**<br><br>
![35](screenshots/35.PNG)<br><br>
![36](screenshots/36.PNG)<br><br>
![37](screenshots/37.PNG)<br><br>
**admin page looks weird. we need to go to Web, Static files and put in the path for the admin static file, as well as our own static file**<br><br>
![38](screenshots/38.PNG)<br><br>
![39](screenshots/39.PNG)<br><br>
**we'll fill in the admin static path. our own static path will be filled in later**<br><br>
![40](screenshots/40.PNG)<br><br>
![41](screenshots/41.PNG)<br><br>
![42](screenshots/42.PNG)<br><br>
![43](screenshots/43.PNG)<br><br>
![44](screenshots/44.PNG)<br><br>
![45](screenshots/45.PNG)<br><br>
**add allowed host and save**<br><br>
![46](screenshots/46.PNG)<br><br>
![47](screenshots/47.PNG)<br><br>
**we can see that the admin static file is now linked**<br><br>
![48](screenshots/48.PNG)<br><br>
**we're still in debug mode. let's change that**<br><br>
![49](screenshots/49.PNG)<br><br>
![50](screenshots/50.PNG)<br><br>
**now add the path to your own static folder if you have one**<br><br>
