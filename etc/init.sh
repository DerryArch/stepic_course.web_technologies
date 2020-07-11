sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/shit.conf
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn_wsgi.conf /etc/gunicorn.d/shit
sudo gunicorn -c /home/box/web/etc/gunicorn.conf hello:wsgi_application
sudo gunicorn -c /home/box/web/etc/gunicorn-django.conf --bind 0.0.0.0:8000 --workers=2 --timeout=15 --access-logfile acc.log --error-logfile err.log ask.wsgi:application & sudo python3 manage.py runserver 0:8000
