import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

#install("requests")

#install("bs4")

#install("lxml")

#install("csv")

#install("time")

#install("import urllib.request")

#install("os")

#install("tinydb")

install("django")
