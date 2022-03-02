"""
- Khởi tạo 1 số tham số cho database SQLAlchemy
"""



from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'


# Kết nối Database
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


# Trước khi thực hiện các tác vụ như query hay thay đổi database, cần kết nối database với 1 session
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Khởi tạo lớp Base là lớp cha để các lớp mới đc tạo ra sau kế thừa
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
