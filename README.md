# BOOK API VERSION 1

## Getting Started

### Installation des Dépendances

#### Python 3.10.2
#### pip 21.3.1 from C:\Users\hp\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)

Suivez les instructions suivantes pour installer l'ancienne version de python sur la plateforme [python docs](https://www.python.org/downloads/windows/#getting-and-installing-the-latest-version-of-python)

#### Dépendances de PIP

Pour installer les dépendances, ouvrez le dossier `/Documentation` et exécuter la commande suivante:

```bash ou powershell ou cmd
pip install -r requirements.txt
or
pip3 install -r requirements.txt
```

Nous passons donc à l'installation de tous les packages se trouvant dans le fichier `requirements.txt`.

##### clé de Dépendances

- [Flask](http://flask.pocoo.org/)  est un petit framework web Python léger, qui fournit des outils et des fonctionnalités utiles qui facilitent la création d’applications web en Python.

- [SQLAlchemy](https://www.sqlalchemy.org/) est un toolkit open source SQL et un mapping objet-relationnel écrit en Python et publié sous licence MIT. SQLAlchemy a opté pour l'utilisation du pattern Data Mapper plutôt que l'active record utilisés par de nombreux autres ORM

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Démarrer le serveur

Pour démarrer le serveur sur Linux ou Mac, executez:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
Pour le démarrer sur Windows, executez:

```bash
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
``` 

## API REFERENCE

Getting starter

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.

## Type d'erreur
Les erreurs sont renvoyées sou forme d'objet au format Json:
{
    "success":False
    "error": 400
    "message":"Ressource non disponible"
}

L'API vous renvoie 4 types d'erreur:
. 400: Bad request ou ressource non disponible
. 500: Internal server error
. 422: Unprocessable
. 404: Not found

## Endpoints
. ## GET/livres

    GENERAL:
        Cet endpoint retourne la liste des objets livres, la valeur du succès et le total des livres. 
    
        
    EXEMPLE: curl https://bookapi-v1.herokuapp.com/livres
```
        {
    "livres": [
        {
      "auteur": "Camara Laye\n", 
      "categorie_id": 2, 
      "date_publication": "Mon, 01 Jun 2009 00:00:00 GMT", 
      "editeur": "Jonathan", 
      "id": 1, 
      "isbn": "new-001\n", 
      "titre": "Enfant Noir \n\n"
    }, 
    {
      "auteur": "Abdou Laleye", 
      "categorie_id": 3, 
      "date_publication": "Sun, 01 Jan 2017 00:00:00 GMT", 
      "editeur": "Damali\n", 
      "id": 2, 
      "isbn": "new-002\n", 
      "titre": "Mon P\u00e8re, Mon Choix\n"
    }, 
    {
      "auteur": "Agatha Christie ", 
      "categorie_id": 5, 
      "date_publication": "Sat, 06 Feb 1999 00:00:00 GMT", 
      "editeur": "Kossi\n", 
      "id": 3, 
      "isbn": "new-003", 
      "titre": "Mort d'une nuit"
    }
  ], 
  "success": true, 
  "total_livres": 3
}
   
```

.##GET/livres(id_liv)
  GENERAL:
  Cet endpoint permet de récupérer les informations d'un livre particulier s'il existe par le biais de l'ID.

    EXEMPLE: https://bookapi-v1.herokuapp.com/books/3
```
   {
    "auteur": "Kossi\n",
    "categorie_id": 5,
    "date_publication": "Sat, 06 Feb 1999 00:00:00 GMT",
    "editeur": "Kossi\n",
    "id": 3,
    "isbn": "new-003",
    "titre": "Mort d'une nuits"
}
```


. ## DELETE/livres (id_liv)

    GENERAL:
        Supprimer un element si l'ID existe. Retourne l'ID du livre supprimé, la valeur du succès et le nouveau total.

        EXEMPLE: curl -X DELETE https://bookapi-v1.herokuapp.com/books/3
```
  
{
    "delete successfully": 3,
    "success": true
}
. ##PATCH/livres(id_liv)
  GENERAL:
  Cet endpoint permet de mettre à jour, le titre, l'auteur, et l'éditeur du livre.
  Il retourne un livre mis à jour.

  EXEMPLE.....Avec Patch
  ``` curl -X PATCH https://bookapi-v1.herokuapp.com/books/1 -H "Content-Type:application/json" -d '{
    "auteur": "Damali\n",
    "categorie_id": 3,
    "date_publication": "Sun, 01 Jan 2017 00:00:00 GMT",
    "editeur": "Damali\n",
    "id": 2,
    "isbn": "new-002\n",
    "titre": "Mon Père, Mon Choix\n"
}
  ```
  ```
    
    ```

. ## GET/categories

    GENERAL:
        Cet endpoint retourne la liste des categories de livres, la valeur du succès et le total des categories disponibles. 
    
        
    EXEMPLE: curl https://bookapi-v1.herokuapp.com/categories

      {
    "Categorie": [
        {
            "id": 3,
            "libelle_categorie": "Conte"
        },
        {
            "id": 4,
            "libelle_categorie": "Harlequin"
        },
        {
            "id": 5,
            "libelle_categorie": "Science"
        },
        {
            "id": 2,
            "libelle_categorie": "Fixions"
        }
    ],
    "success": true,
    "total_categories": 4
}
```

.##GET/categories(id)
  GENERAL:
  Cet endpoint permet de récupérer les informations d'une categorie si elle existe par le biais de l'ID.

    EXEMPLE: https://bookapi-v1.herokuapp.com/categories/3
```
   {
    "id": 3,
    "libelle_categorie": "Conte"
}
```

. ## DELETE/categories (id)

    GENERAL:
        Supprimer un element si l'ID existe. Retourne l'ID da la catégorie supprimé, la valeur du succès et le nouveau total.

        EXEMPLE: curl -X DELETE https://bookapi-v1.herokuapp.com/categories/5
```
    
       {
    "delete successfully": 5,
    "success": true
        }
```

. ##PATCH/categories(id)
  GENERAL:
  Cet endpoint permet de mettre à jour le libelle ou le nom de la categorie.
  Il retourne une nouvelle categorie avec la nouvelle valeur.

  EXEMPLE.....Avec Patch
  ``` curl -X PATCH 'https://bookapi-v1.herokuapp.com/categories/4' -H "Content-Type:application/json" 
  {
    "query": {
        "id": 4,
        "libelle_categorie": "Harlequin"
    },
    "success modify": true
}
  ```
  ```

.##GET/livres/categories(id)
  GENERAL:
  Cet endpoint permet de lister les livres appartenant à une categorie donnée.
  Il renvoie la classe de la categorie et les livres l'appartenant.

    EXEMPLE: https://bookapi-v1.herokuapp.com/categories/4/livres
```
   {
    "Livres": [],
    "success": true,
    "total_livres": 0
}
