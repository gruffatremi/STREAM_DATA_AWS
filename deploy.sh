#!/bin/bash
#Deploy new image to Docker
deploy_app () {
   echo $1 $2 $3
   if [[ (( $1 == 1 || $2 == 1 || $3 == 1 )) ]]; then
    cd /home/ubuntu/dockerfile/apiappd/
    docker build --tag 127.0.0.1:5000/api-docker .
   fi
   if [[ (($1 == 2 || $2 == 2 || $3 == 2 )) ]]; then
    echo "tut"
    cd /home/ubuntu/dockerfile/reactive_streamingd/
    docker build --tag 127.0.0.1:5000/reactive-streaming-docker .
   fi
   if [[ (( $1 == 3 || $2 == 3 || $3 == 3 )) ]]; then
    cd /home/ubuntu/dockerfile/mosquittod
    docker build --tag 127.0.0.1:5000/eclipse-mosquitto-docker .
   fi
   cd /home/ubuntu
   docker-compose push
 #  docker stack deploy -c docker-compose-stack.yml STREAM_DATA
   set -o errexit
   set -o nounset

   source /efs/docker-compose-grafana-influxdb/influx2.env

   echo "==> Prepare Configurations"
   sed -e 's/%%INFLUXDB_INIT_ORG%%/'${DOCKER_INFLUXDB_INIT_ORG}'/g' \
       -e 's/%%INFLUXDB_INIT_BUCKET%%/'${DOCKER_INFLUXDB_INIT_BUCKET}'/g' \
       -e 's/%%INFLUXDB_INIT_ADMIN_TOKEN%%/'${DOCKER_INFLUXDB_INIT_ADMIN_TOKEN}'/g' \
       /efs/docker-compose-grafana-influxdb/grafana/etc/provisioning/datasources/datasource.yaml.template \
     > /efs/docker-compose-grafana-influxdb/grafana/etc/provisioning/datasources/datasource.yaml
   docker stack rm STREAM_DATA
   docker stack deploy -c docker-compose-stack.yml STREAM_DATA
}
if [ $# -lt 1 ]
then
echo "Deploiement de l'applicatif pour la premiere fois ou update"
fi
if [ $# -gt 3 ]
then
echo "Maximum 3 arguments attendu (valeur 1 2 ou 3)"
exit 0
fi

deploy_app $1 $2 $3
exit 0
