Create environment

```bash
  517  conda create -n wineq python=3.8 -y
  518  conda activate wineq
```

Create requirements.txt

```bash
  519  touch requirements.txt
```

Add entries to requirements.txt
```
dvc
dvc[gdrive]
scikit-learn
pandas
pytest
tox
flake8
flask
gunicorn
mlflow
```

Install libraries using requirements.txt

```bash
  520  pip install -r requirements.txt
```

Create template.py

```bash
  523  touch template.py
```

Write the code to create files and directory structure and execute template.py

```bash
  524  python template.py
```

Copy winequality.csv to data_given folder then git and dvc init and push

```bash
  528  git init
  529  dvc init
  530  dvc add data_given/.gitignore
  531  dvc add data_given/winequality.csv
  532  git add .
  533  git commit -m "First Commit"
  534  git branch -M main
  535  git remote add origin https://github.com/ravisharma1702/mlops_simple_demo.git
  536  git branch -M main
  537  git push -u origin main
```

```
Update params.yaml

git add . && git commit -m "added params.yaml"
git push -u origin main
```

```
create get_data.py
create load_data.py
```

```
Update dvc.yaml

stages :
  load_data :
    cmd : python src/load_data.py --config=params.yaml
    deps :
      - src/get_data.py
      - src/lead_data.py
      - data_given/winequality.csv
    outs:
      - data/raw/winequality.csv
```

```
Below will run the load_data.py and create the target csv file in the raw folder

dvc repro

git add . && git commit -m "added params.yaml"
git push -u origin main
```

Update dvc.yaml

```
  split_data :
    cmd : python src/split_data.py --config=params.yaml
    deps :
      - src/split_data.py
      - data/raw/winequality.csv
    outs :
      - data/processed/train_winequality.csv
      - data/processed/test_winequality.csv
```

Create split_data.py, write code and execute pipeline
```
  562  touch src/split_data.py
  563  dvc repro
```

Commit new code
```
  565  git add . && git commit -m "Added split_data.py to prepare test and train data"
  566  git push -u origin main
```

Update dvc.yaml
```
  train_and_evaluate :
    cmd : python src/train_and_evaluate.py  --config=params.yaml
    deps :
      - data/processed/train_winequality.csv
      - data/processed/test_winequality.csv
      - src/train_and_evaluate.py
    params :
      - estimators.ElasticNet.params.alpha
      - estimators.ElasticNet.params.l1_ratio
    metrics :
      - report/scores.json :
          cache : false
      - report/params.json :
          cache : false
    outs :
      - saved_models/model.joblib
```

Create train_and_evaluate.py, write code and execute pipeline
```
  570  touch src/train_and_evaluate.py
  574  dvc repro
```

Commit new code
```
  565  git add . && git commit -m "Added train_and_evaluate.py to tarin and evaluare the model"
  566  git push -u origin main
```

Add code to generate reports and tracker
```
  584  mkdir report
  585  touch report/params.json
  586  touch report/scores.json
  587  dvc repro
  593  git add . && git commit -m "Updated train_and_evaluate to generate reports and add tracker"
  594  git push -u origin main

Above "dvc repro" command will generate the scores. Update the alpha and l1_scores in params.yaml and reexecute "dvc repro" command then execute below commands to see the difference in results:
  590  dvc params diff
  591  dvc metrics show
  592  dvc metrics diff
  593  git add . && git commit -m "Updated alpha and l1_ratio params and reran the model"
  594  git push -u origin main
```

Configuring and running tests
```
  596  touch tox.ini - write content
  597  mkdir tests
  598  touch tests/conftest.py tests/test_config.py
  599  touch tests/__init__.py
  600  pytest -v
  602  tox
```

Preparing distribution
```
  603  touch setup.py - write the setup code
  604  pip install -e .
  606  freeze
  607  pip freeze
  608  python setup.py sdist bdist_wheel
  593  git add . && git commit -m "Added Test Setup and Created Distribution"
  594  git push -u origin main
```

Update test_config.py to add new test case
```python
class NotInRange(Exception) :
    def __init__(self, message="Value not in given range - by Oracle India") :
        self.message = message
        super().__init__(self.message)

def test_generic1() :
    a=50
    with pytest.raises(NotInRange) :
        if a not in range(10,20) :
            raise NotInRange
```

Run pytest to test the changes
```bash
pytest -v
```

Linting using flake8 - Update tox.ini
```ini
commands =
    #Stop the build if there are python syntax errors or undefined names
    flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

    #Exit zero treats all errors as warnings. The GitHub editor is 127 characters wide
    flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

    pytest -v
```

Run tox command
```bash
tox
```

Create Prediction Webapp
```bash
  638  mkdir prediction_service
  639  mkdir -p prediction_service/model
  640  mkdir webapp
  641  touch app.py
  642  touch prediction_service/__init__.py
  643  touch prediction_service/prediction.py
  644  mkdir -p webapp/static/script
  646  mkdir -p webapp/static/css
  645  touch webapp/static/css/main.css
  647  touch webapp/static/script/index.js
  651  mkdir webapp/templates
  652  touch webapp/templates/index.html
  654  touch webapp/templates/404.html
  655  touch webapp/templates/base.html
```


ML Flow
```
202  pip install -r requirements.txt
  203  mlflow
  204  mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 0.0.0.0 -p 1234

  git add . && git commit -m "ML Flow Added" && git push -u origin main
  205  history
```

Log Production Model

Write the code for log_production_model.py
Update dvc.yaml to add log_production_model stage
Bash commands:
```bash
  dvc repro
  mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 0.0.0.0 -p 1234
  git add . && git commit -m "Added log_production_model.py module" && git push -u origin main
```