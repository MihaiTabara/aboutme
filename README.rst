# aboutme
light webapp to nicely render http://mtabara.ro/

Ansible production installation
===============================
0. Setup your new server where you want to deploy this webapp::

    Create an user and add it in the sudoers file.
    Make sure Python >= 2.7 is present

1. Identify your host::

    sed "s/something.com/<your.host.name>/g" devops/hosts.example >> devops/hosts

2. Configure the server and deploy the webapp::

    cd devops/
    ansible-playbook site.yml -i hosts --ask-sudo-pass
