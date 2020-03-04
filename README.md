# PandaValley

## Pre-requisite

1. Clone the project from github

```shell script
git clone "https://github.com/unsw-cse-comp3900-9900/capstone-project-pentapanda"
```

2. Create a virtual python environment

```shell script
python -m venv env
```

> Or using Pycharm: Settings->Project->Project Interpreter
>> Project Interpreter->Add->New Virtual Environment

3. Install python requirements in Terminal below in Pycharm

```shell script
brew install mysql-client
pip3 install -r requirements.txt
```

4. Configure the database

[Download MySQL community server](https://dev.mysql.com/downloads/mysql/)

> Set your password to be admin123

```shell script
# back to your project root directory
python manage.py makemigrations
python manage.py migrate
```

5. Build frontend project

```shell script
cd ui
npm install
npm run build
# npm run dev - on debugging purpose
```

> Or click the start button in `ui/package.json`
