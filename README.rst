# aboutme
Light webapp to nicely render http://mtabara.ro/

App Quick Installation Guide for dev-purposes
=====
0. Install python prerequisites if missing::

    apt-get install python-setuptools python-dev build-essential
    sudo easy_install -U virtualenv
    sudo easy_install -U pip


1. Clone the repository::

    git clone git@github.com:MihaiTabara/aboutme.git
    cd aboutme/


2. Create & activate a virtual environment::

    virtualenv sandbox
    echo '*' > sandbox/.gitignore
    echo '*.pyc' >> sandbox/.gitignore
    echo 'instance' >> .gitignore
    . sandbox/bin/activate

3. Install dependencies::

    pip install -r requirements-dev.txt

4. Create a configuration file::

    mkdir -p instance
    echo 'SECRET_KEY = "version-diff project secret key"' >> instance/settings.py
    echo 'WTF_CSRF_ENABLED = True' >> instance/settings.py
    echo 'DEBUG = False' >> instance/settings.py


6. Run a test server(see http://127.0.0.1:5000 afterwards)::

    python manage.py runserver

Classic staging installation
============================
0. Start the webapp through a WSGI server; first add the supervisord conf file::

    cp supervisord.conf.sample sandbox/supervisord.conf

1. Modify the values in the supervisord.conf file to cope with machine reality
   constraints and needs (port, PROJEC_ROOT) after which start the
   supervisord daemon::

    supervisord

2. Proxypass from the webserver (Apache, nginx or whatsoever) the requests to
   the webapp.

Ansible production installation
===============================
0. Setup your new server where you want to deploy this webapp::

    Create an user and add it in the sudoers file.
    Make sure Python >= 2.7 is present

1. Identify your host::

    sed "s/something.com/<your.host.name>/g" devops/hosts.example >> devops/hosts

2. Configure the server and deploy the webapp::

    ansible-playbook site.yml -i hosts --ask-sudo-pass
