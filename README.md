# GOYA

Goya es una aplicacion utilizada para el contro de inventarios de productos y de salida a traves de ordenes

# Deploy en Produccion
## 1. Preparacion del entorno en Gcloud

A. debe ingresar a la consola de GCLOUD y dirigirse a la [pagina de proyectos](https://console.cloud.google.com/projectselector2/home/dashboard?hl=es-419&_ga=2.57351530.1519666507.1603669465-840240528.1584889811) y crear un nuevo proyecto.

B. Luego de esto debe activar  [Cloud SQL Admin API](https://console.cloud.google.com/flows/enableapi?apiid=sqladmin.googleapis.com&hl=es-419&_ga=2.265369295.1519666507.1603669465-840240528.1584889811) una ves activado puede iniciar el SDK de Gcloud.

[Instalacion de SDK](https://cloud.google.com/sdk/docs/install?hl=es-419)

## 2. Configuracion entorno local

A. se inicia sescion por medio de la terminal ingresando el siguiente comando

```bash
gcloud auth application-default login
```

B. luego de esto debemos configurar el [proxy de Cloud SQL](https://cloud.google.com/sql/docs/mysql/sql-proxy?hl=es-419) para hacer pruebas locales y con el cliente ya instalado debe ingresar el siguiente comando para abilitar conexiones por mediod del proxi.

```bash
gcloud services enable sqladmin
```

## 3. Instalacion del proxy SQL

A. En este caso el ambiente de desarrollo es debian por lo que se utilizara wget para obtener el ejecutable 

```bash 
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
```

se le otorga permisos de ejcucion 

```bash
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
```

## 4. Creacion de una instancia de Cloud SQL

A. primero debemos ingresar a la consola de [gcloud SQL  para MySQL](https://cloud.google.com/sql/docs/mysql/create-instance?hl=es-419) y crear la intancia

***debe de asegurarse de crear una instancia de segunda generacion***

B. una vez ya creada su intancia puede ejecutar el comando siguiente sustitullendo el nombre que le dio al momento de que se creo la misma

```bash
gcloud sql instances describe [NOMBRE_DE_LA_INSTANCIA]
```
no debe cerrar la ventana con el script ya que este nos proporcionara los datos de conexion que utilizaremos para configurar el archivo settings.py

## 5. Iniciar instancia de Cloud SQL 
A. debe ingresar en la terminal el siguiente comando cambiando el nombre de la instancia por el nombre de conexion otorgando por el comando anterior
```bash
./cloud_sql_proxy -instances="[NOMBRE_DE_LA_CONEXION_A_SU_INSTANCIA]"=tcp:3306
```
esto mostrar un mensaje que espera nuevas conexiones por lo que dejaremos esta terminal en espera y debera estar activa al momento que se realizen las pruebas locales y las migraciones

##6. Configuracion de la conexion a BD
A. primero abriremos el archivo settings.py ubicado en *./Goya/settings.py* y cambiaremos la configuracion de base de datos por 

```python
import pymysql  # noqa: 402
pymysql.version_info = (1, 4, 6, 'final', 0)  # change mysqlclient version
pymysql.install_as_MySQLdb()

# [START db_setup]
if os.getenv('GAE_APPLICATION', None):
    # Running on production App Engine, so connect to Google Cloud SQL using
    # the unix socket at /cloudsql/<your-cloudsql-connection string>
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/[YOUR-CONNECTION-NAME]',
            'USER': '[YOUR-USERNAME]',
            'PASSWORD': '[YOUR-PASSWORD]',
            'NAME': '[YOUR-DATABASE]',
        }
    }
else:
    # Running locally so connect to either a local MySQL instance or connect to
    # Cloud SQL via the proxy. To start the proxy via command line:
    #
    #     $ cloud_sql_proxy -instances=[INSTANCE_CONNECTION_NAME]=tcp:3306
    #
    # See https://cloud.google.com/sql/docs/mysql-connect-proxy
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'NAME': '[YOUR-DATABASE]',
            'USER': '[YOUR-USERNAME]',
            'PASSWORD': '[YOUR-PASSWORD]',
        }
    }
# [END db_setup]
```

se sustitullen los datos por los obtenidos en el paso 4 y guardamos el archivo

## 6. Migraciones

A. ahora tenemos que ejecutar nuestro entorno virtual configurado en la seccion de PREREQUISITOS y ejecitar el siguiente coando para poder crear los archivos de mitraciones

```bash
python manage.py makemigrations
```
B. luego de esto se realizaran las migraciones
```bash
python manage.py migrate
```
si las migraciones no se realzian se debe realizar de forma manual la migracion de cada uno ejecutando el siguiente codigo sustitullendo por el nombre de modulo
```bash
python manage.py makemigrations [NOMBRE_DEL_MODULO]
```

## 7. Creacion de super usuario de la aplicacion
A. se procedera a crea un usuario para poder acceder tanto al modulo administrativo como a nuestra aplicacion.

Para esto se ejecuta el siguiente comando y se configura el usuario con los datos solicitados.

```bash
python manage.py createsuperuser
```
B. Comprobamos el estado del usuario con levantando el servidor y dirigiendonos a la ruta *http://localhost:8000/admin*
```bash
python manage.py runserver
```
## 8. Preparacion para el deploy
A. antes de hacer deplon en gcloud debemos crear dos archivos sin lo cuales ngnix mostrara un error 502 o 500.

Empesamos creando el archivo main.py en la raiz de nuestro proyecto 

```python 
from <modulo_raiz>.wsgi import application

# App Engine by default looks for a main.py file at the root of the app
# directory with a WSGI-compatible object called app.
# This file imports the WSGI-compatible object of your Django app,
# application from mysite/wsgi.py and renames it app so it is discoverable by
# App Engine without additional configuration.
# Alternatively, you can add a custom entrypoint field in your app.yaml:
# entrypoint: gunicorn -b :$PORT mysite.wsgi
app = application
```
B. luego el archivo app.yaml donde se le indicara que version de python se utilizara en este caso la version 3.8 de la siguiente manera
```python 

# [START django_app]
runtime: python38

handlers:
# This configures Google App Engine to serve the files in the app's static
# directory.
- url: /static
  static_dir: static/

# This handler routes all requests not caught above to your main app. It is
# required when static routes are defined, but can be omitted (along with
# the entire handlers section) when there are no static files defined.
- url: /.*
  script: auto
# [END django_app]
```
C. por ultimo creamos el archivo con el nombre de requirements.txt con las dependencias que utilizara nuestro proyecto con el comando 

```bash
pip freeze > requirements.txt
```

## 10 Deploy 

para poder realizar nuestro deploy usamos el siguiente comando y esperamos a que nos muestre el mensaje de concluido
```bash
gcloud app deploy
```
para ver los resultados podemos ingresar https://PROJECT_ID.REGION_ID.r.appspot.com y sustituimos con los datos de nuestra aplicacion o ejecutando en nuestra consola
```bash
gcloud browse
```
pip3 install -r requirements.txt
pip3 install djangorestframework 
pip3 install markdown
pip3 install django-filter    
python3  manage.py migrate 
pip3 install psycopg2-binary   

 pip freeze 
python3 manage.py createsuperuser
 pip3 frezze    
python3 manage.py runserver    
 psql postgres 

BCS

IONOS

Batrescs.com

https://login.ionos.com/

BAT-bcs$19!

USUARIO admin@bcs-media.com

PASS Batres@2019

heroku login
git:remote -a goyasistem
git branch
git merge oala/create/update master
heroku run python manage.py createsuperuser
heroku run python manage.py collectstatic
git add .
git commit -m “Update"
git push heroku master:master
