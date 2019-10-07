# Flask w Stripe (StripedFlask_v1)

## Feature Goals
- user login, full authentication w password recovery, etc (creates a basic membership site)
- Stripe integration (creates a basic sales site)
- SQL-backed content per user (allows for transaction records)
- deployed to AWS (public access from any device)

## Installation thru Hello World
+ copy this directory, `cd` into it and then...

`brew -v`
+ ([install homebrew if needed](https://docs.brew.sh/Installation))
```
brew update
brew install python3
python3 -m venv StripedFlask_v1
source /bin/activate
pip install -r requirements.txt
python3 app.py
```

+ Demo message displays in browser at [localhost:5000](localhost:5000).


## Dependencies // pip freeze > requirements.txt
+ bcrypt==3.1.7
+ cffi==1.12.3
+ Click==7.0
+ Flask==1.1.1
+ itsdangerous==1.1.0
+ Jinja2==2.10.3
+ MarkupSafe==1.1.1
+ pycparser==2.19
+ six==1.12.0
+ Werkzeug==0.16.0


_______
### [alexanderjacks](https://github.com/alexanderjacks)
### [richard83](https://github.com/Richand83)

###### MIT, 2019