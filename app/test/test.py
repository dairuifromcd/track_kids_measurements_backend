from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

# Connect to the database
engine = create_engine("sqlite:///example.db", echo=False)
Base = declarative_base()
    
# Define models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    posts = relationship("Post", back_populates="user")

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="posts")

# Create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert data
alice = User(name="Alice", age=25)
session.add(alice)
session.commit()

post1 = Post(title="Alice's first post", user=alice)
session.add(post1)
session.commit()

# Query data
all_users = session.query(User).all()
print(all_users)

all_posts = session.query(Post).all()
print(all_posts)

# Close session
session.close()
