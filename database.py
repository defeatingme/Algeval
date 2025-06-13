from sqlalchemy import create_engine, Column, String, Integer, Float, Text, Boolean, TIMESTAMP, ForeignKey, LargeBinary, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import SQLAlchemyError
import datetime


# SQLAlchemy Database Connection Details
DB_NAME = "algeval"
DB_USER = "postgres"
DB_PASSWORD = "ashascugpt4o"
DB_HOST = "localhost"
DB_PORT = "5432"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()
database_func = func


# Define the Instructor table
class Instructor(Base):
    __tablename__ = 'Instructor'
    
    instructor_name = Column(String(255), primary_key=True)
    email = Column(Text)
    department = Column(Text)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)


# Define the Sessions table
class Sessions(Base):
    __tablename__ = 'Sessions'
    
    session_id = Column(String(255), primary_key=True)
    session_name = Column(String(255), nullable=True)
    instructor_name = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    
    instructor = relationship("Instructor", backref="sessions", uselist=False)
    instructor_name = Column(String(255), ForeignKey('Instructor.instructor_name', ondelete="CASCADE"))


# Define the AnswerKey table
class AnswerKey(Base):
    __tablename__ = 'AnswerKey'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(String(255), nullable=False)
    sol_weight = Column(Integer, nullable=False)
    fa_weight = Column(Integer, nullable=False)
    ak_latex = Column(Text, nullable=False)
    ak_file = Column(LargeBinary, nullable=True)
    steps_count = Column(Integer, nullable=True)
    problem = Column(Text, nullable=True)
    asm_steps = Column(Integer, nullable=True)
    asm_latex = Column(Text, nullable=True)
    asm_choice = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    
    session = relationship("Sessions", backref="answer_keys")
    session_id = Column(String(255), ForeignKey('Sessions.session_id', ondelete="CASCADE"))


# Define the StudentHAS table
class StudentHAS(Base):
    __tablename__ = 'StudentHAS'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(Text, nullable=True)  # NEW COLUMN
    answer_key_id = Column(Integer, nullable=False)
    has_name = Column(Text)
    has_latex = Column(Text, nullable=False)
    result = Column(Text, nullable=False)
    sol_fraction = Column(Text, nullable=True)
    sol_grade = Column(Integer, nullable=True)
    fa_grade = Column(Integer, nullable=True)
    overall_grade = Column(Integer, nullable=True)
    used_asm = Column(Boolean, default=False, nullable=False)
    has_file = Column(LargeBinary, nullable=True)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    
    session = relationship("Sessions", backref="student_has")  # Link to Sessions table
    answer_key = relationship("AnswerKey", backref="student_has")
    session_id = Column(Text, ForeignKey('Sessions.session_id', ondelete="CASCADE"))  # NEW COLUMN
    answer_key_id = Column(Integer, ForeignKey('AnswerKey.id', ondelete="CASCADE"))

def setup_tables():
    #Check if tables exist before creating
    try:
        # Create all tables
        Base.metadata.create_all(engine)
        print("All tables set up successfully.")
    except SQLAlchemyError as e:
        print(f"Database Setup Error: {e}")

# Call the setup_tables function to create the tables
if __name__ == "__main__":
    setup_tables()

