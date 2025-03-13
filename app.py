from flask import Flask, render_template, request # importuojam flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__) # pasakome, kad cia bus pagrindinis musu programos failas
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Justas:Code2024.@localhost/darbine'
db : SQLAlchemy = SQLAlchemy(app) # kad musu flask (kuris vadinasi app) susiristu su musu duomenu baze, kuri dabar vadinasi db
migrate = Migrate(app,db)



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return self.name

def create_user(name):
    db.session.add(User(name=name))
    db.session.commit()

@app.route("/test", methods=['POST','GET'])
def test():
    return render_template('index.html')

@app.route("/", methods=['POST','GET'])
def home():
    if request.method == 'GET':
        return render_template("pagrindinis.html")
    else:    
        name = request.form['vardas']
        create_user(name)
        return render_template("pagrindinis.html")  

@app.route("/users", methods=["GET"])
def get_users():
    stmt = db.select(User)
    users = db.session.execute(stmt).scalars().all()
    return "\n".join([f"{u.id}: {u.name}" for u in users])

# virs funkcijos eta, reiskia dekoratoriu - o dekratorius yra tiesiog kita funkcija, kur ideda aplink funkcija savo logika
if __name__ == '__main__':

    app.run(debug=True) # paleidziam flask kad veiktu ir eitu prisijungti