# ipaddr.ca-python
python rewrite of ipaddr.ca

## Requirements:

*	python-virtualenv python-pip uwsgi

## Instructions

	cd /home/ipaddr
	git clone https://github.com/tbaschak/ipaddr.ca-python
	cd ipaddr.ca-python
	virtualenv ipaddrenv
	source ipaddrenv/bin/activate
	pip install flask uwsgi

Afterwards setup this application like any other uwsgi/flask/python application, for a refresher visit [this](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-16-04) handy DigitalOcean Community Tutorial. There is an ini file included for uwsgi and a nginx configuration vhost.


