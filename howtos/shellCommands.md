## Bash life saver commands  

### Screen related commands
*This section captures frequently used commands by me for linux screen program*
* Start screen with new escape character (say Cntrl+W) (Dont use Cntrl+M) 
```sh
screen -e'^Ww'
```

* Resize window after Screen sticks it to some weird size 
```sh
$ export TERM=xterm
$ stty rows 58 cols 190
```

### Admin related commands
* Make passwordless ssh login (from a@host1 to a@host2)
On host1, generate ssh key and then add the key to host2 using 
```sh
$ ssh key-gen
$ ssh-copy-id a@host2
```
