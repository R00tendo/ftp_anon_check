# ftp_anon_check
Checks massives amount of ips for ftp anonymous login and display the results of "ls" for every vulnerable machine. 

You can adjust the amount of threads by changing line 31

Modes:
 * Pipe:     With this mode you can pipe ips from example scans
 * File:     You provide a list of ips (-f \<file>)

Help page:
```
usage: ftp_anon_check [-h] -m METHOD [-f FILE]

optional arguments:
  -h, --help            show this help message and exit
  -m METHOD, --method METHOD
                        Method to get targets with pipe,file.
  -f FILE, --file FILE  File of ips to scan (used with -m file).

```

<br></br>
All of these are russian ftp servers btw...

<img src="https://user-images.githubusercontent.com/72181445/173401509-c58e7fb0-5e94-4801-8a42-4b56af963c1a.png" width=200 heigth=1000></img>
