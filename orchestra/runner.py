"""This process manages the subprocess tasks."""
import logging
import subprocess
import shlex
import os

def open_subprocess(command:str) -> subprocess.Popen:
    args = shlex.split(command)    
    proc = subprocess.Popen(args, stdout=subprocess.PIPE)
    logging.info('Process spawned, with command {}'.format(args))
    return proc

def kill(proc:subprocess.Popen, timeout=4):
    """
    Blocking call that kills the process specified, with the timeout.
    Does not return unless process is killed.
    """
    import time
    logging.info('Killing process {}'.format(proc))
    proc.terminate() # This sends SIGTERM, but is not guaranteed to end the process.

    st = time.time()
    ct = time.time()
    while proc.poll() is None: # While the process is still active, do this
        ct = time.time() # Update the time
        if ct-st<timeout: # If we've been waiting longer than the timeout
            proc.kill()
            logging.info("Force killed.")
    logging.debug("Killed, entering wait.")
    proc.wait()
    logging.debug("Wait over.")
    # In case the shell gets messed up, we need to reset it.
    subprocess.Popen('reset').wait()    
