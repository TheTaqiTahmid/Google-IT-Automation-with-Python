# To check available disk space and cpu usage
import shutil
import psutil
from UPTIOS_week1_exercise import *


# du = shutil.disk_usage("/")
# print(du)
#
# print((du.free/du.total)*100)
#
# cu = psutil.cpu_percent(0.1)
# print(cu)

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = (du.free / du.total) * 100
    return free > 20


def cpu_usage():
    cu = psutil.cpu_percent(1)
    return cu < 75


if not check_disk_usage("/") or not cpu_usage():
    print("ERROR!")
elif check_connectivity() and check_localhost():
     print("Everything looks fine")
else:
    print("Network checks failed")
