from typing import List
from sqlalchemy import Column, ForeignKey, String, Integer, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()


def generate_uuid():
    return str(uuid.uuid4())


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(String(36), primary_key=True, default=generate_uuid)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    empresas = relationship("Empresa", back_populates="usuario")


class Empresa(Base):
    __tablename__ = 'empresas'

    id = Column(String(36), primary_key=True, default=generate_uuid)
    nombre = Column(String(255), nullable=False)
    user_id = Column(String(36), ForeignKey('usuarios.id'), nullable=False)
    pais_id = Column(String(36), ForeignKey('paises.id'), nullable=False)
    region_id = Column(String(36), ForeignKey('regiones.id'), nullable=False)

    usuario = relationship("Usuario", back_populates="empresas")
    pais = relationship("Pais", back_populates="empresas")
    region = relationship("Region", back_populates="empresas")
    empleados = relationship("Empleado", back_populates="empresa")


class Empleado(Base):
    __tablename__ = 'empleados'

    id = Column(String(36), primary_key=True, default=generate_uuid)
    salario = Column(Numeric(precision=10, scale=2), nullable=False)
    genero = Column(String(10), nullable=False)
    area = Column(String(100), nullable=False)
    cargo = Column(String(100), nullable=False)
    edad = Column(Integer, nullable=False)
    anos_empresa = Column(Integer, nullable=False)
    empresa_id = Column(String(36), ForeignKey('empresas.id'), nullable=False)
    pais_id = Column(String(36), ForeignKey('paises.id'), nullable=False)
    region_id = Column(String(36), ForeignKey('regiones.id'), nullable=False)

    empresa = relationship("Empresa", back_populates="empleados")
    pais = relationship("Pais", back_populates="empleados")
    region = relationship("Region", back_populates="empleados")


class Pais(Base):
    __tablename__ = 'paises'

    id = Column(String(36), primary_key=True, default=generate_uuid)
    nombre = Column(String(100), nullable=False)
    abreviacion = Column(String(10), nullable=False)

    empresas = relationship("Empresa", back_populates="pais")
    empleados = relationship("Empleado", back_populates="pais")
    regiones = relationship("Region", back_populates="pais")


class Region(Base):
    __tablename__ = 'regiones'

    id = Column(String(36), primary_key=True, default=generate_uuid)
    nombre = Column(String(100), nullable=False)
    abreviacion = Column(String(10), nullable=False)
    pais_id = Column(String(36), ForeignKey('paises.id'), nullable=False)

    pais = relationship("Pais", back_populates="regiones")
    empresas = relationship("Empresa", back_populates="region")
    empleados = relationship("Empleado", back_populates="region")
