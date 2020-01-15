from app import db
from app.models import User, Task

Task.query.delete()
User.query.delete()

user = User(username = "Sandy")
db.session.add(user)
db.session.commit()

user2 = User(username = "John")
db.session.add(user2)
db.session.commit()

users = user.query.all()
print(users)

user = users[1]
print(user.id, user.username)
user = User.query.get(1)
print(user.id, user.username)

task1 = Task(title = "Learn Python",
            description = "Learn Flask today",
            done=True,
            user = user)


task2 = Task(title = "Read Metro",
            description = "Find out the news today",
            done=False,
            user = user) 

db.session.add(task1)
db.session.add(task2)   
db.session.commit()

tasks = Task.query.all()
# print(tasks)

task_user = Task.query.get(1).user
# print(task_user.username)
