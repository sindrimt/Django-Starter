**Activate virtual environment**
source bin/activate

**Deactivate virtual environment** _Doesnt work?_
source bin/deactivate

**Starts server**
python manage.py runserver

**Hooks up database with django project / settings**
(src) : python manage.py migrate

**Creates a superuser / admin user**
python manage.py createsuperuser

**Every time models.py is changed, run these two in order**

##

python manage.py makemigrations
python manage.py migrate

##

**Opens python shell with django setting and stuff (Remember to activate virtual env first!)**
python manage.py shell

**Python shell example**

> > > from products.models import Product
> > > Product.objects.all()
> > > <QuerySet [<Product: Product object (1)>]>
> > > Product.objects.create(title = "new procudt 2", description = "another one", price = "2323", summary = "SJSJSJS")

// If you try to add a field to database that doesn't exist is the previous
// fields and try to makemigration, press 1, and set the value. This will be the value in all previous fields

Was 2.0.7
