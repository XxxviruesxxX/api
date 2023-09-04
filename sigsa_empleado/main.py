from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncpg

app = FastAPI()

# Configura la conexión a la base de datos
DATABASE_URL = "postgresql://postgres:Real.1234@localhost/sigsa"

@app.on_event("startup")
async def startup_db_client():
    app.state.db = await asyncpg.connect(DATABASE_URL)

@app.on_event("shutdown")
async def shutdown_db_client():
    await app.state.db.close()

# Modelo de datos usando Pydantic
class Empleado(BaseModel):
    clave: str
    nombre: str
    jefe_directo: str
    departamento: str
    fecha_ingreso: str
    antiguedad: str

# Ruta para obtener datos desde la base de datos
@app.get("/obtener_datos")
async def obtener_datos():
    query = "SELECT * FROM empleados"
    result = await app.state.db.fetch(query)
    return result

# Ruta para crear un nuevo elemento en la base de datos
@app.post("/agregar_datos")
async def agregar_datos(empleado: Empleado):
    query = "INSERT INTO empleados (clave, nombre, jefe_directo, departamento, fecha_ingreso, antigüedad) VALUES ($1, $2, $3, $4, $5, $6) RETURNING id"
    values = (
        empleado.clave,
        empleado.nombre,
        empleado.jefe_directo,
        empleado.departamento,
        empleado.fecha_ingreso,
        empleado.antiguedad,
    )
    record_id = await app.state.db.fetchval(query, *values)
    return {"clave": record_id}
