## Stats about GitHub Repos


## Developer Setup

Execute the following commands in the root of the project.  This must be done *BEFORE* you open the project in PyCharm:

* `python3 -m venv .env` to create a virtual environment
* `source .env/bin/activate` to activate the virtual environment
* `pip install -r requirements.txt` to install the dependencies
* `pip install -e .` to install the source as an editable package

To tell PyCharm to use `pytest`:

* Open Preferences (CMD-,)
* Goto 'Tools/Python Integrated Tools'
* Change 'Default Test Runner' to 'py.test'
