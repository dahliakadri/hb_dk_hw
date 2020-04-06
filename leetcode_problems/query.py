from model import db, Movie
from flask_sqlalchemy import SQLAlchemy
from server import app
connect_to_db(app)

def q1():
    """Return the movie with the id 2."""

    return Movie.query.filter(Movie.movie_id == "tt0026898").one()



def q3():
    """Return all animals that were born after 2015.

    Do NOT include animals without birth years.
    """

    return Movie.query.filter(Movie.year_made > 2015).all()


print(q3())
print(q1())


if __name__ == "__main__":
    # Can run this module interactively,to work with the database directly.
	from model import db, Movie
	from flask_sqlalchemy import SQLAlchemy
	from server import app
	connect_to_db(app)
	print("Connected to DB.")

# def q4():
#     """Return the humans with first names that start with 'J'."""

#     return Human.query.filter(Human.fname.like('J%')).all()


# def q4():
#     """Return all animals whose species is 'fish' OR 'rabbit'."""

#     return Animal.query.filter(Animal.animal_species.in_(['fish', 'rabbit'])).all()


# def q5():
#     """Return all humans whose email addresses do NOT contain 'gmail'."""

#     return Human.query.filter(db.not_(Human.email.like('%gmail%'))).all()