echo POSTGRES_HOST=$POSTGRES_HOST >> .env
echo POSTGRES_PORT=$POSTGRES_PORT >> .env
echo POSTGRES_DB=$POSTGRES_DB >> .env
echo POSTGRES_USER=$POSTGRES_USER >> .env
echo POSTGRES_PASSWORD=$POSTGRES_PASSWORD >> .env
echo DATABASE_URL=postgres://django:django@db:5432/blue_light_db >> .env
echo REDIS_URL=$REDIS_URL >> .env
echo EMAIL_HOST=$EMAIL_HOST >> .env
echo EMAIL_USE_TLS=$EMAIL_USE_TLS >> .env
echo EMAIL_PORT=$EMAIL_PORT >> .env
echo EMAIL_HOST_USER=$EMAIL_HOST_USER >> .env
echo EMAIL_HOST_PASSWORD=$EMAIL_HOST_PASSWORD >> .env
echo EMAIL_SENDER=$EMAIL_SENDER >> .env
echo API_ROOT_URL=$API_ROOT_URL >> .env
echo WEB_ROOT_URL=$WEB_ROOT_URL >> .env
echo JWT_SECRET_KEY="$JWT_SECRET_KEY" >> .env
echo DJANGO_SUPERUSER_EMAIL=$DJANGO_SUPERUSER_EMAIL >> .env
echo DJANGO_SUPERUSER_PASSWORD=$DJANGO_SUPERUSER_PASSWORD >> .env
echo API_HOSTNAME=$API_HOSTNAME >> .env
echo WEB_HOSTNAME=$WEB_HOSTNAME >> .env