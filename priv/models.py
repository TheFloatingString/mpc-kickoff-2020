from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID

from uuid import uuid4

import os
import datetime 

engine = create_engine(os.environ["DATABASE_URL"], echo=True)

meta = MetaData()
Base = declarative_base()

class Entry(Base):
	__tablename__ = "entries"

	id = Column(Integer, primary_key=True)
	uuid = Column(UUID(as_uuid=True), default=uuid4)
	title = Column(String)
	body = Column(String)
	date_created = Column(DateTime)
	date_modified = Column(DateTime)

	def create_entry(self, title, body):
		self.title=title
		self.body=body
		self.date_created = datetime.datetime.now()
		self.date_modified = datetime.datetime.now()

if __name__ == '__main__':
	Base.metadata.create_all(engine)