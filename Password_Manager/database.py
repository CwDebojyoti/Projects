from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import sessionmaker


# Create an engine
engine = create_engine('sqlite:///password_manager.db', echo=True)


# Create a base class for declarative class definitions
Base = declarative_base()



class PasswordManager(Base):
    __tablename__ = 'password'
    id: Mapped[int] = mapped_column(Integer, primary_key= True)
    email: Mapped[str] = mapped_column(String(250), nullable= False)
    platform: Mapped[str] = mapped_column(String(250), unique= True, nullable= False)
    user_password: Mapped[str] = mapped_column(String(250), nullable= False)


# Create all tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
    