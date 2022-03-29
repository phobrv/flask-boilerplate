# I. Environment Installation
## Create new environment
```
conda create --name test python=3.8 -y && conda activate test
```
## install requirements:
```
pip install -r requirements.txt
```
# II. Run
```
python app/create_db.py #create tables
python app/app.py
```