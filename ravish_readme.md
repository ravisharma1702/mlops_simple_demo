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