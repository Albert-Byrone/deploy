
# RelationShips = link different Models(tables)
# ForeignKey
# relationships
# backref
# ORM
# Define the models

# One to Many Relationship -- one record is related to many record from a different table
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(40))
#     email = db.Column(db.String(140))
#     posts = db.relationship("Post", backref="author")
#
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(40))
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


# One to One Relationship -- one record is related to one record from a different table

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(40))
#     email = db.Column(db.String(140))
#
#     profile = db.relationship("Profile", backref="author", uselist=False)
#
# class Profile(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     bio = db.Column(db.String(40))
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


# Many to Many Relationship -- record in one  table can bo related to multiple records from another table

# A student can be enrolled in multiple courses
# A course can have multiple students

# association table
# enrollments = db.Table('enrollments',
#             db.Column("student_id", db.Integer, db.ForeignKey("student.id"), primary_key=True),
#             db.Column("course_id", db.Integer, db.ForeignKey("course.id"), primary_key=True)
# )
#
# class Student(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(40))
#
#     courses = db.relationship("Course", secondary=enrollments, backref=db.backref("students", lazy=True))
#
#
# class Course(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(40))



# Albert     =======> Waiter(API) =====> Cooks
# Albert     <======= Waiter(API) <===== Cooks


# Request     =======> (API) =====> Resource(Server)

# Response     <======= Waiter(API)    Response  <===== Resource(Server)
@app.route('/')
def home():
return "<p>Hello, World!</p>"

@app.route('/api')
def consume_api():
# Make a GET request to the API endpoint
response = requests.get("https://fakestoreapi.com/products")

    if response.status_code == 200:
        data = response.json() # Parse the response to JSON
        return jsonify(data)
    else:
        return jsonify({ "error": "Failed to fetch the product"}), response.status_code

with app.app_context():
db.create_all()



JWT(JSON Web Token) = a small package of information(token)