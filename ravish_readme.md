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
```