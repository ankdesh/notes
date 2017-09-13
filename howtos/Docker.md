## Docker Usage 
### Personal Docker commands
*This section captures frequently used commands by me for copy paste*
* Run ubuntu container first time 
```sh
docker run -it -d ubuntu
```

### Generic Docker commands 
*This section captures frequently used generic docker commands*
* Create container, run image (If image not available, it downloads from docker hub). -it makes it interactive and -d (stands for detached) makes the container stand running.
```sh
docker run -it -d <image_name>
```
* Execute interactive bash on detached container
```sh
docker exec -it <container_id> bash
```
