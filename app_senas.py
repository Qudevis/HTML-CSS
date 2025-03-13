# from flask import Flask, render_template, request # importuojam flask
# from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__) # pasakome, kad cia bus pagrindinis musu programos failas

# db = SQLAlchemy(app) # kad musu flask (kuris vadinasi app) susiristu su musu duomenu baze, kuri dabar vadinasi db

# # @app.route("/") # endpointas - tai taskas i kuri kreipiasi naudotojai (/ - tiesiog nieko)
# # def home(): 
# #     skaicius = 5
# #     skaicius2 = 9
# #     suma = skaicius + skaicius2
# #     return render_template("index.html", vardai=["Justas","Jonas","Mantas"], slaptas=suma)

# # @app.route("/slaptas/<vardas>") # endpointas - tai taskas i kuri kreipiasi naudotojai (/ - tiesiog nieko)
# # def slaptas(vardas): 
# #     return f" Sveikas {vardas} tu patekai i Labai slapta puslapi"

# # @app.route("/naujas") # endpointas - tai taskas i kuri kreipiasi naudotojai (/ - tiesiog nieko)
# # def naujas_puslapis(): 
# #     return f" Naujas puslapis"

# with app.app_context():
#     db.create_all()

# @app.route("/", methods=['POST','GET'])
# def home():
#     if request.method == 'GET':
#         return render_template("pagrindinis.html")
#     else:    
#         name = request.form['vardas']
#         print(f"Sveikas {name}")
#         return render_template("pagrindinis.html")  

# # @app.route("/", methods=['POST'])
# # def home_post():
# #     name = request.form['vardas']
# #     print(f"Sveikas {name}")
# #     return render_template("pagrindinis.html")  

# # @app.route("/", methods=['GET'])
# # def home():
# #     return render_template("pagrindinis.html")








# # virs funkcijos eta, reiskia dekoratoriu - o dekratorius yra tiesiog kita funkcija, kur ideda aplink funkcija savo logika
# if __name__ == '__main__':
#     app.run(debug=True) # paleidziam flask kad veiktu ir eitu prisijungti