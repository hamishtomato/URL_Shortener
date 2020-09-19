# url_shortener Serive

## API Swagger
https://hamish-url-shortener.herokuapp.com/docs#/

## Deploying to Heroku

### Step 1
Install Heroku CLI<br>
[Download](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

### Step 2
- Register Heroku account<br> 
[Register Here](https://dashboard.heroku.com/)<br>

- Login

```cmd
heroku login
```

### Step 3
- Create app <heroku app_name><br>
```cmd
heroku create {heroku app_name}
```
- Create app on dashboard [Heroku application](https://dashboard.heroku.com/new?org=personal-apps)
![alt tag](http://i.imgur.com/8KVzbfD.jpg)


### Step4
- Deploy Paranuara on Heroku
```cmd
heroku git:remote -a {heroku app_name}
```
```cmd
heroku buildpacks:set heroku/python
```
```cmd
git push heroku master
```
