#!/usr/bin/python3
import argparse
import threading
import sys
import ftplib
from io import StringIO
import os
import time
from termcolor import colored as color

def ftp_spray_thread(target):
  global alive, vuln, files
  try:
     ftp = ftplib.FTP(target, timeout=5)
     ftp.login()
     filees = StringIO()
     ftp.retrlines('LIST', filees.write)
     files.append(filees.getvalue())
     ftp.quit()
     print(color(target, 'green'))
     vuln.append(target)
  except:
     print(color(target, 'red'))
     pass
  alive -= 1

def ftp_spray(targets):
  global alive, vuln, files
  vuln = []
  files = []
  allowed_threads = 40
  alive = 0
  for target in targets:
      target = target.strip()
      while alive >= allowed_threads:
             time.sleep(0.5)
      threading.Thread(target=ftp_spray_thread, args=(target,)).start()
      alive += 1
  while alive != 0:
     time.sleep(0.5)
  return vuln
def main(args):
  valid_methods = ['pipe', 'file']
  if args.method not in valid_methods:
       print("Invalid method!")
       sys.exit(1)
  if args.method == 'file' and args.file == None: 
       print("File not specified with -f <file>")
       sys.exit(1)
  if args.method == 'file':
       if not os.path.isfile(args.file):
            print("File not found!")
            sys.exit(1)
       ftp_spray(open(args.file).readlines())
  elif args.method == 'pipe':
       ftp_spray(sys.stdin)
  print(color(f"{'_' * 20}SCAN DONE!{'_' * 20}", 'green'))
  for count,ftp_vuln in enumerate(vuln):
       print(ftp_vuln)
       print(files[count] + "\n" * 3)
if __name__ == "__main__":
  args = argparse.ArgumentParser()
  args.add_argument('-m', '--method', help='Method to get targets with pipe,file.', required=True)
  args.add_argument('-f', '--file', help='File of ips to scan (used with -m file).')
  arguments = args.parse_args()
  main(arguments)

