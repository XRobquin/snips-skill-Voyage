#/usr/bin/env bash -e

VENV=venv

git reset --hard HEAD

if [ ! -d "$VENV" ]
then

    PYTHON=`which python2`

    if [ ! -f $PYTHON ]
    then
        echo "could not find python"
    fi
    virtualenv -p $PYTHON $VENV

fi

. $VENV/bin/activate

pip install -r requirements.txt

sudo chmod +x /var/lib/snips/skills/snips-skill-Voyage/action-discussion.py
