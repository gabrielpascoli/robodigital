# Para o servidor: usamos flask!
from flask import Flask, render_template, request, redirect, jsonify

# Imports para o banco de dados: usamos o SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models.base import Base
from models.coordenadas import Coordenada

# Criando o banco de dados e um acesso a ele
engine = create_engine('sqlite:///robot.db')
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

app = Flask(__name__)

@app.route('/')
def index():
    session = Session()
    result = session.query(Coordenada).order_by(Coordenada.id.desc()).all()
    
    return render_template('index.html', coordenadas=result)

@app.get('/get_posicao')
def get_posicao():
    try:
        session = Session()
        coord_atual = session.query(Coordenada).order_by(Coordenada.id.desc()).limit(1).one()
        return jsonify(coord_atual.json_return())
    except Exception as err:
        print("Error" + str(err))
        return str(err)
    
    

@app.post('/post_posicao')
def post_posicao():
    try:
        x = request.form['x']
        y = request.form['y']
        rot = request.form['r']
        
        session = Session()
        
        coord = Coordenada(posicao_x = x,
                           posicao_y = y,
                           rotacao = rot)        
        session.add(coord)
        session.commit()
        
        return redirect('/')
    except Exception as err:
        print("Errozao" + str(err))
        return str(err)
    


if __name__ == '__main__':
    app.run(debug=True)
