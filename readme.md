# Flask w Stripe (StripedFlask_v1)

## Feature Goals
- user login, full authentication w password recovery, etc (creates a basic membership site)
- Stripe integration (creates a basic sales site)
- SQL-backed content per user (allows for transaction records)
- deployed to AWS (public access from any device)

# To Begin
+ copy this directory, `cd` into it and then...

## Full Install on new macOS
`brew -v`
+ ([installs homebrew](https://docs.brew.sh/Installation))
```
brew update
brew install python3
```

## Typical Install
```
python3 -m venv SF
source bin/activate
pip3 install -r requirements.txt
python3 app.py
```
+ Demo message displays in browser at [localhost:5000](localhost:5000).


## Next steps:
###[Stripe API, Authentication](https://stripe.com/docs/api/authentication)
### Deployment pipeline, likely AWS CodePipeline
+[#1](https://docs.aws.amazon.com/cli/latest/reference/deploy/register-on-premises-instance.html)
+[#2](https://stackoverflow.com/questions/54697348/how-do-i-get-the-instance-name-of-a-lightsail-instance)

## Notes:
[aws Lightsail](https://lightsail.aws.amazon.com/ls/webapp/us-west-2/instances/StripedFlask1/connect) app update cmd after `git pull`:
+ sudo service nginx restart
+ did not see expected result w/ this ⬆️, need to understand how to integrate/publish `git pull` changes

[SQL Alchemy for flask](https://stripe.com/docs/api/authentication)


## Project Dependencies
Update dependencies list with `pip freeze > requirements.txt`
+ alembic==1.2.1
+ bcrypt==3.1.7
+ cffi==1.12.3
+ Click==7.0
+ Flask==1.1.1
+ Flask-Bcrypt==0.7.1
+ Flask-Migrate==2.5.2
+ Flask-SQLAlchemy==2.4.1
+ itsdangerous==1.1.0
+ Jinja2==2.10.3
+ Mako==1.1.0
+ MarkupSafe==1.1.1
+ pycparser==2.19
+ python-dateutil==2.8.0
+ python-editor==1.0.4
+ six==1.12.0
+ SQLAlchemy==1.3.10
+ Werkzeug==0.16.0

_______
### [richard83](https://github.com/Richand83)
### [alexanderjacks](https://github.com/alexanderjacks)

###### MIT, 2019
