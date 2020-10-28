@ECHO OFF

ECHO Update PIP
python -m pip install --upgrade pip

ECHO Starting requirements download
python -m pip install -r requirements.txt

