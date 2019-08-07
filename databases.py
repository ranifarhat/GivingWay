from model import Base, Challenger

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
	ch_object = Challenger(
		name=name,
		lastn=lastn,
		ch_num=ch_num,
		vid=vid)
	session.add(ch_object)
	session.commit()

def query_all():
	"""
	Print all the students in the database.
	"""
	challengers = session.query(Challenger).all()
	return challengers

def delete_all():
	session.query(Challenger).delete()
	session.commit()

def get_last():
	last = session.query(Challenger).order_by(Challenger.ch_id.desc()).first()
	return last