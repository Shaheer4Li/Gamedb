import os as os
from flask import Flask,render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from wtforms import *

#watchmedo auto-restart --directory=./ --pattern="*.py" --ignore-patterns="*\\.venv\\*" --recursive -- .\.venv\Scripts\python.exe app.py


basdir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite:///" + os.path.join(basdir, "database.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False
app.config["SECRET_KEY"]="mysecret"

class AddForm(FlaskForm):
    Title = StringField("Title",validators= [DataRequired()])
    cover = StringField("cover Image URL")
    genre = SelectField("Genre",choices=[
            ('action', 'Action'),
            ('adventure', 'Adventure'),
            ('rpg', 'Role-Playing (RPG)'),
            ('fps', 'First-Person Shooter (FPS)'),
            ('strategy', 'Strategy'),
            ('simulation', 'Simulation'),
            ('sports', 'Sports'),
            ('racing', 'Racing'),
            ('puzzle', 'Puzzle'),
            ('survival', 'Survival / Horror'),
            ('platformer', 'Platformer'),
            ('sandbox', 'Sandbox / Open World'),
            ('casual', 'Casual')
        ],
        validators=[DataRequired(message="Please pick a genre.")]
    )
    platform = SelectField("platform",choices=[('pc','PC'),('ps','PS'),('x','Xbox')],
        validators=[DataRequired(message="Please pick a genre.")])
    status = SelectField(
    "Status",
    choices=[
        ('completed', 'Completed'),
        ('playing', 'Playing'),
        ('starting', 'Starting')
    ],
    validators=[DataRequired(message="Please pick a status.")]
)

    description = TextAreaField("Description/review")

    submit = SubmitField("Add Game")



db = SQLAlchemy(app)

class games(db.Model):
    __tablename__ ="game"
    id = db.Column(db.Integer,primary_key=True)
    title =db.Column(db.Text)
    cover =db.Column(db.Text)
    genre =db.Column(db.Text)
    status =db.Column(db.Text)
    platform =db.Column(db.Text)
    description=db.Column(db.Text)

    def __init__(self,title,cover,genre,status,platform,description):
        self.cover=cover
        self.title=title
        self.genre=genre
        self.status=status
        self.platform=platform
        self.description=description
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/collection")
def collection():
    gama = games.query.all()
    return render_template("collection.html",gama=gama)
@app.route("/add",methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        cover= form.cover.data
        title= form.Title.data.title()
        genre= form.genre.data.title()
        status= form.status.data.title()
        platform= form.platform.data.title()
        description= form.description.data

        new_game=games(title=title,cover=cover,genre=genre,status=status,platform=platform,description=description)
        
        db.session.add(new_game)
        db.session.commit()
        return redirect(url_for('collection'))
    return render_template("add.html",form=form)
@app.route("/game/<int:game_id>")
def game_details(game_id):
    game = games.query.get_or_404(game_id)
    return render_template("details.html", game=game)

@app.route("/edit-game/<int:game_id>", methods=["GET", "POST"])
def edit(game_id):
    game = games.query.get_or_404(game_id)
    form = AddForm(obj=game)
    if form.validate_on_submit():
        game.title = form.Title.data
        game.cover = form.cover.data
        game.genre = form.genre.data
        game.platform = form.platform.data
        game.description = form.description.data
        db.session.commit()
        return redirect(url_for("game_details", game_id=game.id))
    return render_template("edit.html", form=form, game=game)
@app.route("/dele/<int:game_id>", methods=['GET',"POST"])
def delete(game_id):
    game = games.query.get_or_404(game_id)
    try:
        db.session.delete(game)
        db.session.commit()
        flash("Game Deleted successfully")
    except Exception as e:
        db.session.rollback()
        flash("There was an error deleting that game.")
    return redirect(url_for('collection'))
@app.route("/statistics")
def staic():
     total_games = games.query.count()
     completed = games.query.filter_by(status="Completed").count()
     play = games.query.filter_by(status="Playing").count()
     start = games.query.filter_by(status="Starting").count()

     gernres = db.session.query(games.genre,db.func.count(games.id)).group_by(games.genre).all()
     platform = db.session.query(games.platform,db.func.count(games.id)).group_by(games.platform).all()
     return render_template("statistics.html",total=total_games,completed=completed,play=play,start=start,gernres=gernres,platform=platform)


if __name__ =="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

