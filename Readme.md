# WEB API

## Fonctionnement :

Bonjour, voici notre solution de déploiement (et création d'API) avec Flask !  
Vous avez une base de données sql et vous voulez en faire une API ?  
Vous êtes au bon endroit !  

## Prérequis:

Vous avez besoin de **trois VMs**.

```
Nom_VM     | Ip VM       | ISO VM

Api.VM     | 10.110.1.11 | Rocky Linux 9

Mariadb.VM | 10.110.1.12 | Rocky Linux 9

RProxy.VM  | 10.110.1.13 | Rocky Linux 9
```

### Sur chaque vm il vous faut git:
```bash
sudo dnf install git -y  
git clone https://github.com/Echalaye/WebApiInfra.git  
```

## Configuration Mariadb.VM

### A. Installation des packages de base

```bash
sudo bash WebApiInfra/mariadb_install.sh
```

**installation du serveur mariadb**

```bash
sudo mysql_secure_installation
```
**Les paramètres suivants sont recommandés**
```bash
Switch to unix_socket authentication [Y/n] y
Change the root password? [Y/n] y
Remove anonymous users? [Y/n] y
Disallow root login remotely? [Y/n] y
Remove test database and access to it? [Y/n] y
Reload privilege tables now? [Y/n] y
```

**Configuration du serveur**

```bash
sudo mysql -u root -p  
CREATE USER 'flask'@'10.110.1.11' IDENTIFIED BY 'flask';  
CREATE DATABASE PokemonDB;
exit
mysql -u root -p PokemonDB < WebApiInfra/data.sql 
sudo mysql -u root -p  
use PokemonDB;
show TABLES;
```
**Vous devez avoir le résultat suivant**  
```bash
+---------------------+
| Tables_in_PokemonDB |
+---------------------+
| ability             |
| base_stat           |
| move                |
| pokemon             |
| pokemon_ability     |
| pokemon_move        |
| pokemon_type        |
| sqlite_sequence     |
| type                |
+---------------------+
```
```bash
GRANT ALL PRIVILEGES ON PokemonDB.* TO 'flask'@'10.110.1.11';
FLUSH PRIVILEGES;
exit;
```

**Vous avez fini la mise en place de votre serveur Mariadb**

## Configuration RProxy.VM

```bash
sudo bash WebApiInfra/reverseproxy_install.sh
```

## Configuration Api.VM

```bash
sudo bash WebApiInfra/flask_install.sh ; bash WebApiInfra/api_setup.sh
```

## Utilisation

**Pour lancer l'api:**
```bash
source ./env/bin/activate ; python WebApiInfra/app.py
```

Pour accéder à votre api il faut:
Aller sur le lien suivant 10.110.1.13 dans votre navigateur ou avec un curl


