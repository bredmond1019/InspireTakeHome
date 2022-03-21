from bottle import Bottle, run, response, request, HTTPResponse, error
from bottle_sqlalchemy import SQLAlchemyPlugin

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Wombat, Base

from datetime import date, datetime
import json

engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)
create_session = sessionmaker(bind=engine)
session = create_session()

app = Bottle()
app.install(SQLAlchemyPlugin(engine, create_session=create_session))


@app.route("/")
def index():
    response.content_type = 'text/plain'
    return "Inspire Candidate Exercise"


@app.route('/wombats', method=['GET'])
def get_wombats(db):

    wombats = session.query(Wombat).all()

    data = [wombat.to_dict() for wombat in wombats]

    print({"wombats": data})
    response.content_type = 'application/json'
    return json.dumps({"wombats": data})


@app.route('/wombats', method=['POST'])
def post_wombats(db):
    print(request)
    data = request.forms

    if 'name' not in data:
        return HTTPResponse(status=400, body="Missing parameter: name")

    if 'dob' not in data:
        return HTTPResponse(status=400, body="Missing parameter: dob")

    dto = datetime.strptime(data["dob"], '%Y-%m-%d').date()

    new_wombat = Wombat(name=data["name"], dob=dto)
    session.add(new_wombat)
    session.commit()

    response.content_type = 'application/json'
    return json.dumps(new_wombat.to_dict())


@app.error(405)
def error405(error):
    return "Method Not Allowed"


if __name__ == '__main__':

    session.add_all([
        Wombat("Alice", date(1865, 11, 26)),
        Wombat("Queen", date(1951, 7, 26)),
        Wombat("Johnny", date(2010, 3, 5))
    ])
    session.commit()

    app.run(host='localhost', port=8080, reloader=True, debug=True)
