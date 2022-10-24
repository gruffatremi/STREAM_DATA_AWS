# STREAM_DATA_AWS
Une fois le node manager élu et configurer il faut :
 - docker-compose-stack.yml qui s'occupe de deployer le stack
 - Dockerfile pour generer les images locale
 * Le code est contenu dans chaque sous dossier de dockerfile pour chaque image
 - 1 Docker de visualisation :  docker run -it -d -p 8080:8080 -v /var/run/docker.sock:/var/run/docker.sock dockersamples/visualizer 
   Docker visualizer
 - 1 Docker pour partager les images local à travers les nodes : docker service create --name registry --publish published=5000,target=5000 registry:2
 - Le script ./deploy (avec paramètres) a effectuer pour le premier lancement et pour update les images (quand on modifie le dockerfile ou les scripts ou autres)
