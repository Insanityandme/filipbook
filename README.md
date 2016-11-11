# Commands for working with this project
**Start postgres server:**
`postgres -D /usr/local/var/postgres/`
`createdb name_of_db`

### Local
`python manage.py runserver --settings=config.settings.local` 

### Staging
`change requirements.txt to requirements/staging.txt`

`change manage.py to include config.settings.staging`

`git push staging master`

### Production
`change requirements.txt to include requirements/production.txt`

`change manage.py to include config.settings.production`

`git push heroku master`

### push database to heroku
`heroku pg:reset DATABASE_URL --app filipbook-staging/filipbook`

`heroku pg:push mysite_db DATABASE_URL --app filipbook-staging/filipbook`

https://devcenter.heroku.com/articles/heroku-postgresql#pg-push-and-pg-pull


### How to fix .gitignore not working as you'd like
**First commit any outstanding code changes,** and then, run this command:

`git rm -r --cached .`

`git add .`

`git commit -m ".gitignore is now working"`

### How to work with postcss in your local dev env
`gulp watch` (will watch for changes in gulp-assets)

# links and resources
* https://console.aws.amazon.com/s3/ (where I host my media files)
* filipbook-staging.herokuapp.com
* filipbook.herokuapp.com
* filipbook.com
