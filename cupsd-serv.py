import os
import subprocess

def run(*cmd):
    """Run a command without running a shell"""
    return subprocess.call(cmd)

#

def get_state():
    s = get_profile("System.Service.setState")
    if s:
        state = s["state"]
    else:
        state = "on"
    
    return state

#

def info():
    state = get_state()
    return "local\n" + state + "\nCUPS"

def start():
    run("/sbin/start-stop-daemon", "--start", "-q", "--exec", "/usr/sbin/cupsd")

def stop():
    run("/sbin/start-stop-daemon", "--stop", "-q", "--exec", "/usr/sbin/cupsd")

def ready():
    s = get_state()
    if s == "on":
        start()

def setState(state=None):
    if state == "on":
        start()
    elif state == "off":
        stop()
    else:
        fail("Unknown state '%s'" % state)
