# This is kitchen

The most important aspect of a professional kitchen is discipline. 
This Django project is designed to optimize the functioning 
of this complex mechanism, facilitating communication between chefs and management.

### 🌐 Project deployed  to Render: 
### [This is kitchen website](https://this-is-kitchen.onrender.com)

### 🗝 For testing:
login:`BillyJ`

password: `1qazcde3`

### 💾 Installing using GIT
```shell
  git clone https://github.com/Anatolii-Poznyak/this_is_kitchen
  cd this_is_kitchen
  python -m venv venv
```
- Requirement : Python 3

### 💻 Linux/macOS:
```shell
  source venv/bin/activate
  pip install -r requirements.txt
  export SECRET_KEY=<your_secret_key>
  export DJANGO_DEBUG=True
```
- or set DEBUG and SECRET_KEY right in settings.py (bad practice btw) 
### 🖥 Windows:
```shell
  venv\Scripts\activate
  pip install -r requirements.txt
  set SECRET_KEY=<your_secret_key>
  set DJANGO_DEBUG=True
```

### 👆 After setting .env variables:
```shell
  python manage.py migrate
  python manage.py runserver
```

### 🧾 Features

* Admin panel, easy to customize
* Firm Django Authentication functions
* Access to all manage systems from the web
* Nice and bright

### 📺 Demo ![demo.png](demo.png)
