from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///religion_data.db'
db = SQLAlchemy(app)

class Religion(db.Model):
  __tablename__ = 'religions2'
  __table_args__ = {
    'autoload': True,
    'autoload_with': db.engine
  }
  Religion_in_which_raised = db.Column(db.String, primary_key=True)

@app.route("/")
def hello():
  return "This is a website for religions!"
  # schools = School.query.all()
  # return render_template("list.html", religions=religions)

@app.route("/religions/")
def list():
   religions = Religion.query.all()
  return render_template("list.html", religions=religion)
#   religions = Religion.query.all()
#   return render_template("list.html", schools=schools)

@app.route("/religions/cool-fun-high-school")
def show(Religion_in_which_raised):
  religion = Religion.query.filter_by(Religion_in_which_raised=Religion_in_which_raised).first()
  return render_template("show.html", religion=religion)

# @app.route("/schools/<dbn>/")
# def school(dbn):
#   school = School.query.filter_by(dbn=dbn).first()
#   return render_template("show.html", school=school)

# @app.route("/search")
# def search():
#   name = request.args.get('query')
#   schools = School.query.filter(School.school_name.contains(name)).all()
#   return render_template("list.html", schools=schools)


# If this is running from the command line
# do something
if __name__ == '__main__':
  app.run(debug=True)
