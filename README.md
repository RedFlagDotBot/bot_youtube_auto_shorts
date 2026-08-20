# Bot YouTube Auto Shorts

Bot Python permettant d’automatiser une partie du processus de récupération de clips Twitch et de publication vers YouTube sous forme de Shorts.

Ce projet a été réalisé dans un objectif d’apprentissage autour de l’automatisation, de l’API YouTube, de l’authentification OAuth et de la structuration d’un projet Python simple.

## Objectifs du projet

- Automatiser certaines tâches répétitives liées à la publication de contenus courts.
- Comprendre le fonctionnement de l’authentification OAuth avec Google et YouTube.
- Manipuler des fichiers de configuration locaux.
- Structurer un projet Python simple.
- Documenter les étapes nécessaires pour adapter le script à son propre environnement.

## Fichiers principaux

- `Script_Principal.py` : script principal du projet.
- `script_token_OAuth.py` : script lié à la génération ou au renouvellement du token OAuth.
- `twitch_channels.txt` : fichier permettant de lister les chaînes Twitch utilisées par le projet.
- `client_secret.example.json` : exemple de fichier de configuration OAuth, sans véritable secret.
- `token.example.json` : exemple de fichier de token, sans véritable jeton d’accès.

## Gestion des identifiants et secrets

Ce dépôt ne contient aucun identifiant réel, aucun secret OAuth réel et aucun token exploitable.

Les fichiers fournis sont uniquement des exemples anonymisés :

- `client_secret.example.json`
- `token.example.json`

Pour exécuter le projet localement, il faut copier ces fichiers d’exemple puis les renommer :

```bash
cp client_secret.example.json client_secret.json
cp token.example.json token.json
```

Ensuite, il faut remplacer les valeurs d’exemple par vos propres informations locales obtenues depuis votre console Google Cloud.

Les vrais fichiers suivants ne doivent jamais être publiés sur GitHub :

- `client_secret.json`
- `token.json`
- `credentials.json`
- `.env`

Ils doivent rester uniquement sur la machine locale.

## Exemple de configuration OAuth

Les valeurs comme `YOUR_CLIENT_ID_HERE`, `YOUR_PROJECT_ID_HERE` ou `YOUR_CLIENT_SECRET_HERE` sont des placeholders. Elles doivent être remplacées localement avec vos propres informations.

Exemple de fichier `client_secret.example.json` :

```json
{
  "installed": {
    "client_id": "YOUR_CLIENT_ID_HERE",
    "project_id": "YOUR_PROJECT_ID_HERE",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_secret": "YOUR_CLIENT_SECRET_HERE",
    "redirect_uris": ["http://localhost"]
  }
}
```

Exemple de fichier `token.example.json` :

```json
{
  "token": "YOUR_ACCESS_TOKEN_HERE",
  "refresh_token": "YOUR_REFRESH_TOKEN_HERE",
  "token_uri": "https://oauth2.googleapis.com/token",
  "client_id": "YOUR_CLIENT_ID_HERE",
  "client_secret": "YOUR_CLIENT_SECRET_HERE",
  "scopes": ["YOUR_SCOPES_HERE"]
}
```

## Bonnes pratiques de sécurité

Pour éviter toute exposition accidentelle d’identifiants :

- ne jamais publier de véritables tokens ;
- ne jamais publier de véritables secrets OAuth ;
- utiliser des fichiers `.example` pour documenter la configuration ;
- ignorer les vrais fichiers sensibles avec `.gitignore` ;
- régénérer les identifiants en cas de doute ;
- limiter les droits accordés aux applications OAuth ;
- éviter de publier des fichiers générés automatiquement contenant des accès personnels.

## Installation

Cloner le dépôt :

```bash
git clone https://github.com/RedFlagDotBot/bot_youtube_auto_shorts.git
cd bot_youtube_auto_shorts
```

Installer les dépendances Python nécessaires selon les imports utilisés dans les scripts.

Créer les fichiers locaux de configuration :

```bash
cp client_secret.example.json client_secret.json
cp token.example.json token.json
```

Modifier ensuite les fichiers locaux `client_secret.json` et `token.json` avec vos propres valeurs.

## Utilisation

Le fonctionnement exact dépend de la configuration locale, des accès API Google/YouTube et des paramètres utilisés dans les scripts.

Avant toute utilisation, vérifier :

- que les identifiants OAuth sont valides ;
- que les droits accordés à l’application sont strictement nécessaires ;
- que les fichiers sensibles sont bien ignorés par Git ;
- que les chemins et paramètres utilisés dans les scripts correspondent à votre environnement.

## Limites

Ce projet est un projet personnel d’apprentissage.

Il n’est pas destiné à être utilisé tel quel en production sans :

- revue de sécurité ;
- gestion robuste des erreurs ;
- journalisation propre ;
- contrôle précis des droits OAuth ;
- gestion sécurisée des secrets ;
- documentation complète des dépendances.

## Avertissement

Ce dépôt est fourni à titre éducatif.

Aucun fichier de secret réel ne doit être publié dans ce dépôt. Les fichiers `.example` servent uniquement à montrer la structure attendue des fichiers de configuration.
