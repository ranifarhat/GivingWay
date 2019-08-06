from model import Base, Student

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///students.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_challenger(name, lastn, ch_num, vid):
	"""
	Add a student to the database, given
	their name, year, and whether they have
	finished the lab.
	"""
	ch_object = Student(
		name=name,
		year=year,
		finished_lab=finished_lab)
	session.add(student_object)
	session.commit()