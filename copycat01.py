#!/usr/bin/env python3
#imports
import shutil  #automates copying files and directories
import os  # gets info about operating system

def main():
    #move into directory
    os.chdir("/home/student/mycode/")

    #copy source to destination
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    #copy directory to directory
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()
