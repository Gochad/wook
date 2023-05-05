# wook
Wook is a simple website made in Django to store and display cooking recipes and notes about cooking. 
If you want to store your data, you can register and login after it.

## Install
1. clone repo: `git clone https://github.com/Gochad/wook <directory>`
2. run `make setup` - to create virtual environment for project
3. run `source env/bin/activate` - to open virtual environment 
4. run `make requirements` - to install requirements in virtual env
5. make database with `make initdb`
6. to run server you can use `make server`, but if you have problem `Error: That port is already in use.` you can use `make porterr` (it close connection on default port and open server on this port)
7. if you're changing some models in models.py files, you can refresh database with `make updatedb`
## Testing

### Running tests

To run tests: `make test`

### Writing tests
Tests for every django app are located in `<app_dir>/tests.py`. You can write them using functions or grouping them into classes.
