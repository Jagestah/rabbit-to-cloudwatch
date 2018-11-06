import subprocess
import time
p = subprocess.Popen(["ps", "-a"], stdout=subprocess.PIPE)
out, err = p.communicate()
if ('app.py' in str(out)):
    print('App is running')
