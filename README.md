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

# 1. Ders Özet

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


# 2. Ders Özet

* Blog app'ini oluşturduk. Modelimizi yazdık.
  1. ./manage.py startapp blog
  2. 'blog' INSTALLED_APP'e ekledi.
  3. ./manage.py makemigrations blog
  4. ./manage.py migrate
  5. ./manage.py migrate --list (Tüm migrate dosyalarını ve durumlarını gösterir.)

* Modelde değişiklik yaptık ve migrate roll back nasıl yapılır gördük.
 1. ./manage.py migrate 0001, ./manage.py migrate zero (0001'e kadar olan yada tamamının aktifliğini kaldırdık.)
 2. Aktifliğini kaldırdığımız migrate dosyalarını sildik.
 3. Tekrar ./manage.py makemigrations blog
 4. ./manage.py migrate blog

* Admin panelini değiştirdik.(Django Suit)
 1. [Django Suit Read Docs](https://django-suit.readthedocs.org/en/develop/)
 2. Kurulum ve yapılması gereken ayarların hepsi yukarıdaki linkte mevcut.

* Views, Urls ve Template kısımlarını yazarak veri tabanından çektiğimiz blog yazılarını sayfada güncelden eskiye sıralı gösterdik.
 1. [Urls](https://docs.djangoproject.com/en/1.9/topics/http/urls/)
 2. [Templates](http://www.djangobook.com/en/2.0/chapter04.html)
 3. [TemplateView](https://docs.djangoproject.com/en/1.9/topics/class-based-views/#simple-usage-in-your-urlconf)

* requirements.txt oluşturmak.
 1. pip freeze (virtualenv'de yada sistemde(hangisi aktifse) kurulu pip paketlerini gösterir.)
 2. pip freeze > requirements.txt (pip paketlerini dosyaya yazar.)
 3. pip install -r requirements.txt  (Dosyada yazılı pip paketlerini kurar.)
 4. [Pip Freeze Read Docs](https://pip.pypa.io/en/stable/reference/pip_freeze/)
