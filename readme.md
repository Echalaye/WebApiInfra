# WEB API

## Fonctionnement :

## Prérequis:

vous avez besoin de **deux machines**.

Nom_Machine     | Ip machine  | ISO machine

Api.machine     | 10.110.1.11 | Rocky Linux 9

Mariadb.machine | 10.110.1.15 | Rocky Linux 9

## Configuration Mariadb.machine

### A. Instalation des packages de base

```
sudo dnf update -y

sudo dnf install git -y

git clone https://github.com/Echalaye/WebApiInfra.git
```

### B. mise en place mariadb-server

```
sudo dnf install mariadb-server -y

sudo systemctl enable mariadb

sudo systemctl start mariadb
```

**faite la commande suivante pour vérifié que votre service mariadb tourne bien**

```
sudo systemctl status mariadb
```
**résultat attendus**
```
Active: active (running) since Tue 2022-11-15 11:29:56 CET; 12s ago
```

**installation du serveur mariadb**

```
sudo mysql_secure_installation
```
**je vous recommande d'avoir l'installation suivante**
```
Switch to unix_socket authentication [Y/n] y
Change the root password? [Y/n] y
Remove anonymous users? [Y/n] y
Disallow root login remotely? [Y/n] y
Remove test database and access to it? [Y/n] y
Reload privilege tables now? [Y/n] y
```

**configuration du serveur**

```
sudo mysql -u root -p

CREATE USER 'django'@'10.110.1.11' IDENTIFIED BY 'VOTRE_MOT_DE_PASSE';

CREATE DATABASE IF NOT EXISTS pokemonDB CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

sudo mysqldump -u root pokemonDB < WebApiInfra/data.sql

GRANT ALL PRIVILEGES ON nextcloud.* TO 'nextcloud'@'10.102.1.11';
