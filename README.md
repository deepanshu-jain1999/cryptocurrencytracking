# cryptocurrencytracking


sudo apt install redis-server
sudo systemctl status redis-server


To run the task:-
crawl_currency.delay()
It will send task to redis and from redis it will run by celery

Run celery:-
celery -A cryptocurrency worker --loglevel=info
