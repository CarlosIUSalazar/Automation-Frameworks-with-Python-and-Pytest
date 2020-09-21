#This is a place to put fixtures.  Anything in this directory or below has access to these fixtures
#reference to ARGPARSE concept and website in my notes
from pytest import fixture

from config import Config   #Config is the class we made in config.py

def pytest_addoption(parser): #parser is part of the internals of pytest, its not somerhing we made
    parser.addoption("--env", action="store", default="dev",help="Environment to run test agains")    #we may want to pass the browser name, or head list

@fixture(scope='session')
def env(request):  #request is part of pytest, we didnt' implement it.  it holds imformation that come in the CLI
    return request.config.getoption("--env")  #run a fixure that says anytime soemone uses the fixutre env, means go get me the envinrmet for this one.  Ill return you something that was on the request. I'll get the --env

@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg
    