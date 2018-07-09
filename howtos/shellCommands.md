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
