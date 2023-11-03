## eCommerceAPI

### ENG
After cloning this repo run command: `pip install -r requirements.txt`.
Run migrations: `python manage.py migrate`.

To access [Django administration panel](http://localhost:8000/admin) you first need to create
a superuser for yourself.
Run `python manage.py createsuperuser` and fill the form with username, email and password.

Then run `python manage.py runserver`.

Visit [Django administration panel](http://localhost:8000/admin) and log in.
As default your role will be set to "Customer" you can change it in admin panel.

Add some product categories using admin panel.

Now you can visit http://localhost:8000/api/products/ to display a list of all products. If your role is set to "Seller", you can add new products, as well as modify information about a single product or delete it.

Set your role to "Customer" and place a new order by visiting http://localhost:8000/api/orders/.

If your role is set to "Seller", you can visit http://localhost:8000/api/products-stats/ to view statistics for the most frequently ordered products.

### PL
Po sklonowaniu tego repozytorium uruchom polecenie: `pip install -r requirements.txt`. \
Następnie wykonaj migracje: `python manage.py migrate`. 

Aby uzyskać dostęp do [panelu administracyjnego Django](http://localhost:8000/admin), najpierw musisz stworzyć konto super użytkownika.
Uruchom polecenie `python manage.py createsuperuser` i wypełnij formularz, podając nazwę użytkownika, email i hasło.

Następnie uruchom polecenie `python manage.py runserver`.

Odwiedź panel administracyjny Django i zaloguj się.
Domyślnie Twoja rola zostanie ustawiona na "Klient", ale możesz ją zmienić w panelu administracyjnym.

Dodaj kilka kategorii produktów za pomocą panelu administracyjnego.

Teraz możesz odwiedzić `http://localhost:8000/api/products/`, żeby wyświetlić listę wszystkich produktów. Jeśli twoja rola ustawiona jest na "Sprzedawca" możesz dodawać nowe produkty, a także modyfikować informacje o pojedynczym produkcie lub usunąć go.

Ustaw rolę na "Klient" i złóż nowe zamówienie odwiedzając `http://localhost:8000/api/orders/`.

Jeśli twoja rola ustawiona jest na "Sprzedawca" możesz odwiedzić `http://localhost:8000/api/products-stats/` i wyświetlić statystyki najczęściej zamawianych produktów.

### URLs
http://localhost:8000/admin/ \
http://localhost:8000/api/products/ \
http://localhost:8000/api/products/{product_id}/ \
http://localhost:8000/api/orders/ \
http://localhost:8000/api/products-stats/ 