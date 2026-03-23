from flask.helpers import url_for
import pandas as pd
from flask import Flask,render_template,request,session
from werkzeug.utils import redirect
import csv,json
from flask_sqlalchemy import SQLAlchemy
from werkzeug.wrappers import ResponseStream
app=Flask(__name__)
app.secret_key = 'une_cle_secrete_longue_et_unique'  # Définit la clé secrète
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://admin:Momo-38780@database-1.c3uyuw6ukqdq.eu-north-1.rds.amazonaws.com/database_quizz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
class User(db.Model):
    __tablename__ = 'users'  # Nom de la table dans la base de données
    
    id = db.Column(db.Integer, primary_key=True)  # Clé primaire
    age = db.Column(db.String(50), nullable=False)  # Âge de l'utilisateur
    nationalite = db.Column(db.String(100), nullable=False)  # Nationalité de l'utilisateur
    name=db.Column(db.String(100),nullable=False)
    livres_lus = db.Column(db.String(50), nullable=True)  # Nombre de livres lus
    actualite = db.Column(db.String(50), nullable=True)  # Fréquence d'actualités
    type_etudes=db.Column(db.String(50),nullable=False)
    interests = db.Column(db.String(200), nullable=True)  # Centres d'intérêt
    pays = db.Column(db.String(50), nullable=True)  # Nombre de pays visités
    telerealite = db.Column(db.String(50), nullable=True)  # Regarde-t-il de la télé-réalité ?
    diplome = db.Column(db.String(100), nullable=True)  # Dernier diplôme obtenu
    etude = db.Column(db.String(100), nullable=True)  # Études hors de la France ?
    reseaux = db.Column(db.String(50), nullable=True)  # Temps passé sur les réseaux sociaux
    cinema = db.Column(db.String(50), nullable=True)  # Fréquence des sorties au cinéma
    auto_evaluation = db.Column(db.String(100), nullable=True)  # Auto-évaluation de l'utilisateur
    reponses = db.relationship('Reponse', backref='user', lazy=True)
class Reponse(db.Model):
    __tablename__="reponses"

    id=db.Column(db.Integer,db.ForeignKey('users.id' ),primary_key=True) 
    question1 = db.Column(db.String(255))
    question2 = db.Column(db.String(255))
    question3 = db.Column(db.String(255))
    question4 = db.Column(db.String(255))
    question5 = db.Column(db.String(255))
    question6 = db.Column(db.String(255))
    question7 = db.Column(db.String(255))
    question8 = db.Column(db.String(255))
    question9 = db.Column(db.String(255))
    question10 = db.Column(db.String(255))
    question11 = db.Column(db.String(255))
    question12 = db.Column(db.String(255))
    question13 = db.Column(db.String(255))
    question14 = db.Column(db.String(255))
    question15 = db.Column(db.String(255))
    question16 = db.Column(db.String(255))
    question17 = db.Column(db.String(255))
    question18 = db.Column(db.String(255))
    question19 = db.Column(db.String(255))
    question20 = db.Column(db.String(255))
    score=db.Column(db.String(255))
with app.app_context():
    db.create_all()
@app.route('/')
#Fonction d'acceuil
def home():
    return """
    <html>
    <head>
        <title>🔥 Quiz de l’Axoulou 🔥</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                text-align: center;
                background-color: #121212;
                color: white;
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 600px;
                margin: 100px auto;
                background: #1e1e1e;
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0px 0px 15px rgba(255, 255, 255, 0.2);
            }
            h1 {
                font-size: 28px;
                color: #facc15;
            }
            p {
                font-size: 18px;
            }
            .start-btn {
                display: inline-block;
                padding: 12px 25px;
                font-size: 20px;
                font-weight: bold;
                color: black;
                background: #facc15;
                text-decoration: none;
                border-radius: 8px;
                transition: 0.3s;
            }
            .start-btn:hover {
                background: #f59e0b;
            }
            .gif {
                width: 70%;
                border-radius: 10px;
                margin-bottom: 15px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <img src="/static/image/bienvenue.gif" class="gif" alt="Axel en mode giga intello">
            <h1>Bienvenue dans le Quiz de l’Axoulou !</h1>
            <p>Prêt à montrer que t’as le cerveau bien affûté ? 🔥</p>
            <a class="start-btn" href="/form">💡 Commencer le Quiz 💡</a>
        </div>
    </body>
    </html>
    """



#Fonction formulaire 
@app.route('/form',methods=['GET','POST'])
def user_info():
    if request.method=='POST':
        #recupere les donne envoyer par le formulaire
        age=request.form['age']
        nationalite=request.form['nationalite']
        name=request.form['name']
        livres_lus=request.form['livres']
        actualite=request.form['actualite']
        type_etudes=request.form['type_etudes']
        interests=",".join(request.form.getlist('interests[]'))
        pays=request.form['pays']
        telerealite=request.form['telerealite']
        
        diplome=request.form['diplome']
        etude=request.form['etude']
        reseaux=request.form['reseaux']
        cinema=request.form['cinema']
      
        auto_evaluation=request.form['auto_evaluation']
        newuser=User(
            age= age,
            nationalite= nationalite,
            name=name,
            livres_lus= livres_lus,
            actualite= actualite,
            interests=interests,
            type_etudes=type_etudes,
            pays= pays,
            telerealite= telerealite,
            diplome= diplome,
            etude= etude,
            reseaux= reseaux,
            cinema= cinema,
            auto_evaluation= auto_evaluation
        )
        db.session.add(newuser)
        db.session.commit()
        print(newuser.id)
        #session['user_info']=user_info
        #print(user_info)          
        return redirect(url_for('quizz',id=newuser.id))
    return render_template('form.html')# Affiche le formulaire

@app.route('/quizz/<int:id>',methods=['GET','POST'])
def quizz(id):
    print('quiz ',id)
    if request.method=="POST":
        nb_question=20    #Nombre de question dans le quizz
        answers={}
        for question in range(1,nb_question+1):
            key=f'question{question}'
            if key in request.form:
                answers[key]=request.form[key]  
            
        #print(request.form['question1'])    
        score=sum(1 for answer  in answers.values() if answer=='correct')
        answers["score"]=score
        newreponse=Reponse(id=id,**answers)
        db.session.add(newreponse)
        db.session.commit()
        session['info']=score
        return redirect(url_for('submit_quizz'))
     # Quand l'utilisateur envoi ses reponses
      
    return render_template('quizz.html',id=id)

@app.route('/submit_quizz',methods=['GET','POST'])
def submit_quizz():
    score=session['info']
    nb_question=20
    print(request.form)
    
    print(score)
    
    
    #print("le score est :",score )
    #user_info=session.get('user_info',{})
    #user_info.update(answers)
    #print(user_info)
    #save_to_csv(user_info,nb_question)
    return render_template("result.html", score=score, total=nb_question)

def save_to_csv(user_info,nb_question):
    try:
        with open('all_data_quizz.csv','a',newline='') as csvfile: #'a' : Permet d'ajouter des données au fichier existant. et newline='' : Cela empêche Python d'ajouter des lignes vides supplémentaires entre les enregistrements dans le fichier CSV
            fieldnames=[v for v in list(user_info.keys())]# Ajouter toutes les questions comme colonnes
            writer=csv.DictWriter(csvfile,fieldnames=fieldnames) #C'est une classe fournie par le module csv pour écrire des données sous forme de dictionnaire dans un fichier CSV.

            # Si c'est la première ligne, ajouter les en-têtes
            print(user_info )
            csvfile.seek(0,2)  #seek(offset, whence)offset=0 : Pas de déplacement supplémentairewhence=2 : Déplace le curseur à la fin du fichier.
            if csvfile.tell()==0: # Retourne la position actuelle du curseur dans le fichier.
                writer.writeheader()
            writer.writerow(user_info)  # Ajouter la ligne avec toutes les informations
            print(f"Données sauvegardées dans {csvfile}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde dans le fichier CSV : {e}")
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)



