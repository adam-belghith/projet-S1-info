# projet-S1-info


# ASSISTANT CLIMATIQUE

# 1 Introduction

Le projet a pour objectif d’aider à gérer l’aération et les différences climatiques entre l’intérieur et l’extérieur en général (si il fait froid dehors par rapport à l’intérieur par exemple)

# 2 Schéma général du projet

- Capteur d’humidité, de température, de CO2
- Enregistrement des données pour afficher un historique (voir type de base de donnée à utiliser)
  - Base de données de séries chronologiques pour les données des capteurs (car les données n'ont pas besoin d'une base de donnée relationnelle, et que ce sera plus optimisé) : À déterminer
  - BDD SQL pour le reste : Postgresql
- Notifications via ntfy, et interface pour paramétrer les seuils d’alertes et voir l’historique
  - Serveur web et backend sur raspberry pi
  - Reverse proxy sur un autre serveur avec une ip fixe qui fait le pont entre l’extérieur et le raspberry pi
- Accès aux données météo depuis internet ou accès aux données de l’extérieur depuis d’autres capteurs
- Moteur pour simuler ouverture fenêtre (à remplacer pour un usage réel par une connexion à une fenêtre connecté ou à un volet)

![](https://nextcloud.nuage-libre.fr/apps/text/image?documentId=3252&sessionId=1918&sessionToken=pFZnC7hDgcsKoTtgOEyIBBkGWd%2FbVW7QTsKcqQlWb0Ltej2hXjZ4IV1%2Fzt1xxZPf&shareToken=axtaRwpiJ5PP8Hc&imageFileName=schema%20%282%29.svg)

Les tracés qui passent par internet signifient qu'on passe par internet

# 

3 Scénarios d’usage

## Information

- Informer sur la différence de température et le vent et, selon les critères de l’utilisateur/utilisatrice, dire quelle est la tenue adaptée en fonction du temps passé dehors.
- Envoyer une notification quand il faudrait aérer (seuil de CO2 et d’humidité paramétrables)
- Indiquer si les conditions sont bonnes pour faire lever du pain (ou de la brioche, des pains chocolat …)
- Envoyer une notification si ce n’est pas la nuit et qu’il faudrait aérer pour la température
- Afficher l’historique des données et les données actuelles

## Action automatisé

- Ouvrir la fenêtre automatiquement la nuit si il fait plus chaud à l’intérieur, et que la température intérieur est trop élevé (pour l’été)
- Ouvrir la fenêtre en envoyant une notification si la concentration de CO2 est critique (valeur paramétrable)
- Une aération automatique pour gérer l’humidité pendant une absence prolongée (aération lorsque l’humidité extérieur n’est pas élevée)

# 4 Fonctionnalités


| n° | Nom                                   | Description                                                                       | Sur quoi la fonction agit                                                      | Importance |
| --- | ------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ---------- |
| 0   | Paramétrer                           | L’utilisateur paramètre le programme                                            | base de données interface                                                     | 2          |
| 1   | Lecture données                      | Récolter les données des capteurs                                               | base de données , capteurs, Rasberry pi                                       | 1          |
| 2   | Se connecter avec un mot de passe     | L’utilisateur entre un couple identifiant - mot de passe                         | base de données interface                                                     | 2          |
| 3   | Commander l’ouverture de la fenêtre | Contrôler l’aération                                                           | base de données capteurs, moteur                                              | 2          |
| 4   | Notifier                              | Envoyer une notification si nécessaire                                           | base de données capteurs, base de données interface, téléphone utilisateur | 2          |
| 5   | Afficher informations                 | L’interface pour avoir des informations                                          | base de données capteurs, base de données interface                          | 1          |
| 6   | Récupérer les données              | Communiquer avec une API météo pour pouvoir afficher les prévision sur le site | basse de données, interface                                                   | 3          |

# 5 Planning prévisionnel


|         | S10 (17/10) | S11 (24/11) | S12 (01/12) | S13 (08/12)           | S14 (15/12)                                   |
| ------- | ----------- | ----------- | ----------- | --------------------- | --------------------------------------------- |
| Adam    | F1, F0      | F1, F0      | F4, F6      | Rapport et soutenance | Temps pour rattraper le retard avant le 19/12 |
| Lucas   | F1, F3      | F5, F2      | F4, F6      | Rapport et soutenance | Temps pour rattraper le retard avant le 19/12 |
| Mathieu | F5          | F5, F2      | F4, F6      | Rapport et soutenance | Temps pour rattraper le retard avant le 19/12 |
