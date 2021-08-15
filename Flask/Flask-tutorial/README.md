### Flask tutorial
## Found at [Flask official site](https://flask.palletsprojects.com/en/2.0.x/tutorial/)

## Running:
# Windows
``` powershell
python3 -m venv venv
. venv/Scripts/activate
pip3 install -r requirements.txt
$env:FLASK_APP='flaskr'
$env:FLASK_ENV='development'
```

Then go to http://127.0.0.1:5000/

# Linux
``` shell
python3 -m venv venv
. venv/activate
pip3 install -r requirements.txt
export FLASK_APP='flaskr'
export FLASK_ENV='development'
```

Then go to http://127.0.0.1:5000/
