
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$-*c5gei%cikbqw&1eqj$7_%c3npk^^7xp#_x(8oc$zy(j3wus'



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_clone_db',
        'USER': 'root',
        'PASSWORD': 'Open_sesame!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}