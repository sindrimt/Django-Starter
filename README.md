**Activate virtual environment**
<br>
source bin/activate

**Deactivate virtual environment** _Doesnt work?_
<br>
source bin/deactivate

**Starts server**
<br>
python manage.py runserver

**Hooks up database with django project / settings**
<br>
(src) : python manage.py migrate

**Creates a superuser / admin user**
python manage.py createsuperuser

**Every time models.py is changed, run these two in order**

##

python manage.py makemigrations<br>
python manage.py migrate

##

**Opens python shell with django setting and stuff (Remember to activate virtual env first!)**
<br>
_python manage.py shell_

**Python shell example**

_from products.models import Product_
_Product.objects.all()_
_<QuerySet [<Product: Product object (1)>]>_
_Product.objects.create(title = "new procudt 2", description = "another one", price = "2323", summary = "SJSJSJS")_

**If you try to add a field to database that doesn't exist is the previous**
**fields and try to makemigration, press 1, and set the value. This will be the value in all previous fields**

Was 2.0.7
