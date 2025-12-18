docker-compose down -v
docker-compose up --build -d

# MY_SQL Connection Troubleshoot

docker exec -it mysql_db mysql -u root -p

## Check MySQL users

SELECT host, user FROM mysql.user;
SHOW GRANTS FOR 'flaskuser'@'%';

## Grant All Privileges To Flaskuser

GRANT ALL PRIVILEGES ON flask_crud.\* TO 'flaskuser'@'%';
FLUSH PRIVILEGES;
EXIT;

docker restart flask_app

# Test Connection Inside Flask Container

docker exec -it flask_app python
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://flaskuser:flaskpass@db:3306/flask_crud")
engine.connect()

# create a new repository on the command line

echo "# flask_crud_prod" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/mofiz-mizu/flask_crud_prod.git
git push -u origin main

# push an existing repository from the command line

git remote add origin https://github.com/mofiz-mizu/flask_crud_prod.git
git branch -M main
git push -u origin main
