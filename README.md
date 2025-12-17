# ansible-apache-molecule-testinfra
# Proof of Concept Ansible - Apache2 avec Molecule et Testinfra

## Description

Ce projet est un Proof of Concept (PoC) démontrant l'utilisation de Molecule avec Testinfra pour tester automatiquement un rôle Ansible qui installe et configure Apache2.

## Objectifs

- Installer Apache2 sur un conteneur Docker Ubuntu 22.04
- Configurer un VirtualHost personnalisé
- Valider automatiquement l'installation avec 7 tests Testinfra

## Prérequis

- Python 3.8+
- Docker
- Git

## Installation
```bash
# Cloner le projet
git clone https://github.com/VOTRE_USERNAME/ansible-apache-molecule-testinfra.git
cd ansible-apache-molecule-testinfra

# Créer l'environnement virtuel
python3 -m venv ../venv
source ../venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Installer la collection Docker
ansible-galaxy collection install community.docker
```

## Exécution des tests
```bash
# Test complet
molecule test

# Ou étape par étape
molecule create
molecule converge
molecule verify
molecule destroy
```

## Tests Testinfra

Le projet inclut 7 tests automatisés :

1. Vérification de l'installation du paquet Apache2
2. Vérification que le service est démarré
3. Vérification que le service est activé au boot
4. Vérification de l'existence du fichier de configuration
5. Vérification des permissions du fichier (root:root, 0644)
6. Vérification du contenu du fichier de configuration
7. Vérification qu'Apache écoute sur le port 80

## 📁 Structure du projet
```
apache_role/
├── ansible.cfg
├── files/
│   └── custom-site.conf
├── handlers/
│   └── main.yml
├── meta/
│   └── main.yml
├── molecule/
│   └── default/
│       ├── converge.yml
│       ├── create.yml
│       ├── destroy.yml
│       ├── molecule.yml
│       └── tests/
│           └── test_default.py
├── tasks/
│   └── main.yml
└── README.md
```

## Projet réalisé dans le cadre
Cours : Automatisation 
École : Haute École de Namur-Liège-Luxembourg  
Date : Décembre 2025

## Licence
MIT
