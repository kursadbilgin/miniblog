# Mini Blog

## LINK

* TEXT EDITOR
  * [Atom](https://atom.io/)
  * [Sublime Text](https://www.sublimetext.com/) 

* IDE
  * [Pycharm](https://www.jetbrains.com/pycharm/download/#section=linux)

* PIP 
  * [Read Docs](https://pip.pypa.io/en/stable/installing/)

* VIRTUALENV
  * [Read Docs](https://virtualenv.pypa.io/en/latest/)

* DJANGO
  * [Source Code](https://github.com/django/django)
  * [Orijinal Document](https://www.djangoproject.com/)
  * [Django Packages](https://www.djangopackages.com/)

# 1. Ders Kısa Özet

* İlk önce pip kurduk. Kurulum PIP linkinde mevcut.
  1. sudo apt-get install python-pip
  2. get-pip.py dosyasını indir. python get-pip.py ile çalıştır.

* Daha Sonra virtualenv kurduk.
  1. pip install virtualenv

* Daha sonra sanal bir alan oluşturduk kendimize  ve bunu aktif ettik.
  1. mkdir Django101
  2. cd Django101
  3. virtualenv -p /usr/bin/python3.4 MiniBlog/env
  4. cd MiniBlog
  5. source env/bin/activate

* Daha sonra Django kurduk ve projemizi oluşturduk.
  1. pip install Django==1.8.12
  2. django-admin startproject miniblog

* Daha sonra settings.py'de ayarlamalar yaptık ve projeyi çalıştırdık.
  1. LANGUAGE_CODE = "tr-TR"
  2. TIME_ZONE = "Europe/Istanbul"
  3. python manage.py runserver 8080, ./manage.py runserver 8080
  4. Tarayıcıdan localhost:8080 adresine giderek sayfamızı görüntüledik.

* Son olarak super kullanıcı oluşturduk ve admin panelini inceledik.
  1. python manage.py createsuperuser, ./manage.py createsuperuser
  2. Tarayıcıdan localhost:8080/admin/ adresine giderek admin panelini inceledik.
