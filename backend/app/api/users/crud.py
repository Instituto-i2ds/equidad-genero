from sqlalchemy.orm import Session
from .schemas import UserCreate, UserUpdate, User
from .models import Usuario, Empresa, Empleado, Pais, Region

def get_user(db: Session, user_id: int):
    return db.query(Usuario).filter(Usuario.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Usuario).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    db_user = Usuario(
        nombre=user.nombre,
        apellido=user.apellido,
        email=user.email,
        password=user.password  # Note: You should hash the password before saving it
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = get_user(db, user_id)
    if db_user is None:
        return None
    
    update_data = user.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)
    
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user is None:
        return None
    
    db.delete(db_user)
    db.commit()
    return db_user

# Additional functions to handle relationships
# def get_user_empresas(db: Session, user_id: int, skip: int = 0, limit: int = 100):
#     return db.query(Empresa).filter(Empresa.user_id == user_id).offset(skip).limit(limit).all()

# def create_user_empresa(db: Session, empresa: EmpresaCreate, user_id: int):
#     db_empresa = Empresa(**empresa.dict(), user_id=user_id)
#     db.add(db_empresa)
#     db.commit()
#     db.refresh(db_empresa)
#     return db_empresa
