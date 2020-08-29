Commandes docker


Pour vérifier l'état de la machine Docker nous exécutons la commande :
docker-machine status
**
Les commandes Docker permettent de gérer les conteneurs de manière basique.

- docker build : Construire une nouvelle image à partir du code source dans le PATH
- docker commit : Créer une nouvelle image à partir des changements d’un conteneur
- docker images : Lister des images
- docker ps : Liste de conteneurs
- docker pull : Récupérer une image ou un repository à partir du Docker HUB
- docker rm : Supprimer une ou plusieurs conteneurs
- docker rmi : Supprimer une ou plusieurs images
- docker start : Lancer un ou plusieurs conteneurs arrêtés
- docker run : Exécuter une commande dans un nouveau conteneur
- docker stop : Arrêtez un conteneur en cours d’exécution



Voici quelques commandes utiles dans la gestion des images et des containers. 

- Lister les images téléchargées
  
  docker images
- Supprimer une image
  
  docker rmi {nom de l'image}:{version}
- Lister les containers actifs
  
  docker ps
- Lister tous les containers
  
  docker ps -a
- Lancer un container
  
  docker start {nom de votre container}
Attention ! Il ne faut pas confondre docker run et docker start. Le run crée un container à partir d'une image et l’exécute. Le start exécute un container DÉJÀ existant. 

- Se connecter à un container
  
  docker exec -ti {nom de votre container} /bin/bash
Arrêter un container

	docker kill {nom de votre container}

Supprimer un container

	docker rm {nom de votre container}