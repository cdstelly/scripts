$ sudo vim /etc/sysctl.conf

# append
vm.max_map_count=262144
$ sudo sysctl -p 




#change storage dir of containers
$ sudo vim /etc/default/docker
DOCKER_OPTS="--dns 8.8.8.8 --dns 8.8.4.4 -g /mnt/containers"
$ sudo systemctl restart docker



# bash exec shortcut
function e()  {
        docker exec -it $1 /bin/sh
}
