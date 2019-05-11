Swiper
======

项目初始化

```shell
mkdir swiper
cd swiper
virtualenv .venv
source .venv/bin/activate
pip install django==1.11.18 gunicorn gevent redis==2.10.6 celery ipython
django-admin startproject swiper ./
git init
touch .gitignore
git add ./
git commit -m 'first commit'
git remote add origin git@github.com:BJ-1813/swiper.git
git push -u origin master
```
