import os
from flask import Flask, jsonify, redirect, render_template, request, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()

app=Flask(__name__)#creer une instance de l'application
motdepasse=os.getenv('mdp')

app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:root@localhost:5432/mabase"
#connexion a la base de données
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db=SQLAlchemy(app)#creer une instance de Dase de données
#migrate =Migrate(app,db)
#migrate = Migrate(app, db)


class Categorie(db.Model):
    __tablename__='categories'
    id_cat=db.Column(db.Integer,primary_key=True)
    libelle_categorie=db.Column(db.String(100),nullable=False)
    cat = db.relationship('Livre',backref='categories',lazy=True)

    def _init_(self,libelle_categorie) :
         self.libelle_categorie=libelle_categorie
         
    def insert(self):
        db.session.add(self)
        db.session.commit()
  
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
        'id': self.id_cat,
        'libelle_categorie': self.libelle_categorie,
        }

class Livre(db.Model):
    __tablename__='livres'
    id_liv=db.Column(db.Integer, primary_key=True)
    isbn=db.Column(db.String(100),nullable=False)
    titre=db.Column(db.String(100),nullable=False)
    date_publication=db.Column(db.Date(),nullable=False)
    auteur=db.Column(db.String(100),nullable=False)
    editeur=db.Column(db.String(100),nullable=False)
    categorie_id=db.Column(db.Integer,db.ForeignKey('categories.id_cat'),nullable=False)
    
    def __init__(self,isbn,titre,date_publication,auteur,editeur,categorie_id):
        self.isbn=isbn
        self.titre=titre
        self.date_publication=date_publication
        self.auteur=auteur
        self.editeur=editeur
        self.categorie_id=categorie_id
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
  
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
        'id': self.id_liv,
        'isbn':self.isbn,
        'titre':self.titre,
        'date_publication':self.date_publication,
        'auteur':self.auteur,
        'editeur':self.editeur,
        'categorie_id': self.categorie_id,
        }



db.create_all()

def paginate(request):
    items = [item.format() for item in request]
    return items
# Afficher toutes less categories
@app.route('/categories')
def get_categories():
    categories = Categorie.query.all()
    categories = paginate(categories)
    return jsonify({
        'success': True,
        'Categorie': categories,
        'total_categories': len(categories)
    })

#Afficher tous les livres
@app.route('/livres')
def get_livres():
    livres= Livre.query.all()
    livres= paginate(livres)
    return jsonify({
        'success':True,
        'Livres':livres,
        'total_livres': len(livres)
    })
#Rechercher une categorie par son id 
@app.route('/categories/<int:id>')
def get_categorie(id):
    categorie = Categorie.query.get(id)
    if categorie is None:
        abort(404)
    else:
        return categorie.format()
#Rechercher un livre par son id 
@app.route('/livres/<int:id>')
def get_livre(id):
    livre = Livre.query.get(id)
    if livre is None:
        abort(404)
    else:
        return livre.format()
#Supprimer une categorie
@app.route('/categories/<int:id>',methods=['DELETE'])
def delete_categorie(id):
    categorie = Categorie.query.get(id)
    categorie.delete()
    return jsonify({
        'success': True,
        'delete successfully': id,
    })
#Supprimer un livre 
@app.route('/livres/<int:id>',methods=['DELETE'])
def delete_livres(id):
    livre =Livre.query.get(id)
    livre.delete()
    return jsonify({
        'success': True,
        'delete successfully': id,
    })
#Modifier les informations d'une categorie
@app.route('/categories/<int:id>',methods=['PATCH'])
def update_categorie(id):
    data = request.get_json()
    query = Categorie.query.get(id)
    if 'libelle_categorie' in data:
        query.libelle_categorie = data['libelle_categorie']
    query.update()
    return jsonify({
        'success modify': True,
        'query': query.format(),
    })
#Modifier les informations d'un livre 
@app.route('/livres/<int:id_liv>',methods=['PATCH'] )
def update_livres(id_liv):
    data = request.get_json()
    query = Livre.query.get(id_liv)
    if 'titre' in data and 'date_publication' in data and 'auteur' in data and 'editeur' in data and 'categorie_id' in data:
        query.titre = data['titre']
        query.date_publication = data['date_publication']
        query.auteur = data['auteur']
        query.auteur = data['editeur']
        query.categorie_id = data['categorie_id']
    query.update()
    return jsonify({
        'success modify': True,
        'livre': query.format(),
    })

# Lister la liste des livres d'une catégorie
@app.route('/categories/<int:id>/livres')
def get_livre_from_categorie(id):
    books=Livre.query.filter(Livre.categorie_id==id)
    books= paginate(books)
    return jsonify({
        'success':True,
        'Livres':books,
        'total_livres': len(books)
    })