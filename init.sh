#Start Nginx
sudo ln -sf $(pwd)/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo unlink /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

#Start Gunicorn
gunicorn -c etc/schedule.py --pythonpath $(pwd)/schedule schedule.wsgi:application
