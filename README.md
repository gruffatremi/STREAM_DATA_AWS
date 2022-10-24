# STREAM_DATA_AWS

ansible-playbook -i inv.yml install_swarm.yml Commande pour :

  - Installer docker sur tous les noeuds
  - Demarrer le service docker
  - Mount /efs sur tout les noeuds pour les volumes de docker
  - init un swarm manager
  - join les worker au noeud
Ansible code branch


Le code se trouve dans install_swarm.yml


L'inventaire : inv.yml


- Les tâches sont effectuées dans roles/docker/tasks/main.yml et roles/swarm/tasks/main.yml

- Les vars sont dans roles/docker/vars/main.yml et roles/swarm/vars/main.yml

- Les paramètres par défaut sont dans roles/docker/defaults/main.yml et roles/swarm/defaults/main.yml
