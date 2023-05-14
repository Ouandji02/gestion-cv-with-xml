# Projet de gestion de CV avec XML

```
    Il était question pour nous de gérer les CV en créant à base des informations reçues un fichier XML qui sera par la suite tester à notre schéma XML. S'il est valide alors on transformera le fichier XML à l'aide d'un fichier XSLT qui nous retournera un fichier HTML ou ODT. 

```

## Installation

Pour faire fonctionner le projet en local, il suffit de


1.Clonez le projet sur 

    ```
    https://github.com/Ouandji02/gestion-cv-with-xml

    ```
### Pour l'api

1.Exécuter la commandes suivante : 

    ```
    cd gestion-cv-with-xml/api

    ```

2.Ensuite activez l'environnement en tapant 

    ```
    python3 venv venv

    ```

3.Installer les packages nécéssaires 

    ```
    pip install -r requirements.txt

    ```
4.Lancez l'environnement en tapant 

si vous êtes sur linux

    ```
    ./venv/bin/activate

    ```
si vous êtes sur windows

    ```
    ./venv/Scripts/activate

    ```
5.Lancer le projet 

    ```
    flask run

    ```

### Pour le front

1.Exécuter la commandes suivante : 

    ```
    cd gestion-cv-with-xml/gestion_cv

    ```

2.Installer les packages nécéssaires 

    ```
    npm install 

    ```
3.Lancer le projet 

    ```
    npm start

    ```
 ## Pour voir le projet

 Si le projet est demarré avec Live Server, visiter le lien (Côté front):

    ```
        http://localhost:5173
    ```

Cote API

    ```
        http://localhost:5000

    ```
## Licence

Ce projet n'est sous aucune licence.

## Credit

    1. lxml
    2. flask
    3. odfpy
    4. flask_cors
    5. axios
    6. react-syntax-highlighter

## Auteurs

Ce projet est le fruit du groupe 12 du cours d'intergiciel (Univ DSCHANG)

1. OUANDJI DJANANG THIERRY ARMEL
2. NGUEWOUO MBAKOP MANICK
3. NKEMENYI Hema Serena
4. SOPJIO KOUGANG ROCHNEL FABRICE



