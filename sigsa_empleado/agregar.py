from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncpg

Base = sigsa()

class sigsa(Base):
    __tablename__ = 'empleados'

    clave = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True)
    jefe_directivo = Column(String, unique=True, index=True)
    departamento = Column(String, unique=True, index=True)
    fecha_ingreso = Column(String, unique=True, index=True)
    antiguedad = Column(String, unique=True, index=True)



#fffff

DATABASE_URL = "postgres://postgres:Real.1234@localhost/sigsa"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


#ffffff

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from postgres import Session

app = FastAPI()

class empleadocreate(BaseModel):
    clave:str
    nombre: str
    jefedirectivo: str
    departamento: str
    fecha_ingreso :str
    antiguedad: str
    

@app.post("/agregar_usuario")
async def agregar_datos(item: Item):
    query = "INSERT INTO empleados (clave, nombre, jefe_directo, departamento, fecha_ingreso, antigüedad) VALUES ($1, $2) RETURNING id"
    db.add(db_empleado)
    db.commit()
    db.refresh(db_empleado)
    return db_empleado


{
    "clave": "clave de usuario",
    "nombre": "nombre de usuario",
    "jefedirectivo": "jefe",
    "departamento": "departamento de donde es",
    "fecha_ingreso" : "decha de inicio",
    "antiguedad": "cuantos años en la empresa tiene"
    
}


