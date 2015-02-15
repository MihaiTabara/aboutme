from functools import wraps
from fabric.api import *
from fabric.contrib.files import exists


env['aboutme'] = {
    'staging': {
        'host_string': 'mtabara@evo',
        'aboutme_repo':     '/var/local/aboutme-staging',
        'aboutme_sandbox':  '/var/local/aboutme-staging/sandbox',
        'supervisor_process': 'aboutme-staging',

    },
}

env['aboutme_default_target'] = 'staging'


def choose_target(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        name = kwargs.pop('target', None)
        if name is None and 'aboutme_target' not in env:
            name = env['aboutme_default_target']

        if name is None:
            target_env = {}
        else:
            target_env = env['aboutme'][name]
            target_env['aboutme_target'] = name

        with settings(**target_env):
            return func(*args, **kwargs)

    return wrapper


@task
@choose_target
def install():
    if not exists("%(aboutme_repo)s/.git" % env):
        run("git init '%(aboutme_repo)s'" % env)

    local("git push -f '%(host_string)s:%(aboutme_repo)s' HEAD:incoming" % env)
    with cd(env['aboutme_repo']):
        run("git reset incoming --hard")

    if not exists(env['aboutme_sandbox']):
        run("virtualenv -p /opt/python/bin/python2.7 --no-site-packages '%(aboutme_sandbox)s'" % env)
        run("echo '*' > '%(aboutme_sandbox)s/.gitignore'" % env)

    run("%(aboutme_sandbox)s/bin/pip install "
        "-r %(aboutme_repo)s/requirements.txt"
        % env)


def supervisor(root, command):
    run('%s/sandbox/bin/supervisorctl %s' %
        (root, command))


@task
@choose_target
def restart():
    supervisor(env['aboutme_repo'], "restart %s" % env['supervisor_process'])


@task
@choose_target
def status():
    supervisor(env['aboutme_repo'], "status")
