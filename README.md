<h4>Kjør disse i rekkefølge</h4>

**pip install Django==2.1.5**

> I tutorialen bruker han Django version 2.0.7, men for å unngå error kan man oppgradere til 2.1.5

**Activate virtual environment**
<br>

> (root) : source bin/activate

**Run these two in order (If you make changes to the database, call these two in order)**

##

> (src) : python manage.py makemigrations<br>
> (src) : python manage.py migrate

##

**Starts server**
<br>

> (src) : python manage.py runserver

**Creates a superuser / admin user (Log in)**

> (src) : python manage.py createsuperuser

<h4>Andre commands og stuff</h4>

**Opens python shell with django setting and stuff (Remember to activate virtual env first!)**
<br>

> (src) : _python manage.py shell_

**If you try to add a field to database that doesn't exist is the previous**
**fields and try to makemigration, press 1, and set the value. This will be the value in all previous fields**

Was 2.0.7

**Deactivate virtual environment** _Doesnt work?_
<br>

> (root) : source bin/deactivate

**Hooks up database with django project / settings**
<br>

> (src) : python manage.py migrate

**Creates a new App**
<br>

> (src) : python manage.py startapp _App_Name_

**Python shell example**

> -_from products.models import Product_<br> - _Product.objects.all()_<br> - _<QuerySet [<Product: Product object (1)>]_<br> - _Product.objects.create(title = "asdf", description = "asdf", price = "1234", summary = "asdf")_<br> - _obj = Product.objects.get(id = 1)_<br> - _dir(obj)_
