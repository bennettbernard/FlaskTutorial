from flaskblog import app


# to set up database in terminal
""" 
'python' 'from flaskblog import db' (name of database) 
'db.create_all()'
'from flaskblog import User, Post'
user1 = User(username='Corey', email='c@demo.com', password='password')
db.session.add(user1)
user2 = User(username='John', email='j@demo.com', password='password')
db.session.add(user2)
db.session.commit()
"""
#example querys
"""
User.query.all()
User.query.first()
User.query.filter_by(username='Corey').first()

"""

if __name__ == '__main__':
    app.run(debug=True)