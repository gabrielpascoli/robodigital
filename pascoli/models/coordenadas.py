from models.base import Base
from sqlalchemy import Column, Integer, Float

class Coordenada(Base):
    __tablename__ = 'coordenadas'
    # Atributes:
    id = Column(Integer, primary_key=True)
    posicao_x = Column(Float)
    posicao_y = Column(Float)
    rotacao = Column(Float)
        
    def json_return(self):
        return {"id": self.id,
                "posicao_x": self.posicao_x,
                "posicao_y": self.posicao_y,
                "rotacao": self.rotacao}
        
    def __repr__(self) -> str:
        return f"id: {self.id}, posicao: (x: {self.posicao_x}, y: {self.posicao_y}, rotacao: {self.rotacao})"
    