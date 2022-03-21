# Inspire Python Take Home

### Hello Future Inspire Coworkers! 

Here is my completed assignment. I created _two separate versions_:

- 1st Version: Bottle-Py 
  -  Original Assignment
  -  All Exams Passed
  -  Utlized `Bottle-SQLAlchemy` to better manipulate the data
  -  Created a `models.py` file to create structure and organization
 
- 2nd Version: Flask & GraphQL
  - Created REST API endpoint
  - Created GraphQL queries and mutations
  - Utilized `unittest` from python 
  - Used Flask's `blueprints` and application factory structure to make the API scalable and organized


I first completed the assignment as instructed using _Bottle microframework_. Bottle is actually pretty similar to _Flask_, but I had to get my bearings a bit and read the documentation on Bottle. I wanted to demonstrate that I could take the time and learn a different technology to solve a problem. 

Once I completed it, I wanted to solve the same problem by using technologies I am more familiar with. I did this to demonstrate how I could build a more complex and scalable version of the same API. The _Flask_ version has the same REST API endpoints as the _Bottle_ version. It also has similar functionality written in GraphQL. In the GraphQL version you can additionally __sort by birthdate ascending or descending__ in the `wombats` query. I created separate `unittest`s for both the REST API and GraphQL endpoints, but you _only have to run the test command once_. 


### Setting Up the Flask Environment

1. Make sure you are in the __FlaskVersion__ directory
2. You'll want to set up a `venv` in the way suggested in your assignment
3. Once the environment is created, you can --> `pip install -r requirements.txt`
4. In the command line on your terminal you'll want to enter the following:
   - `export FLASK_APP=app.py`
   - `export FLASK_DEBUG=1` _Only need this line if you plan to run the server, not for running the tests_
   - `flask test` _This will run the tests_
   - `flask run` _You can run this after the tests if you want to activate the flask server_
   - You can head to `http://localhost:5000/wombats` and you should see some JSON with the first three users
   - If you go to `http://localhost:5000/graphql` you will see the GraphiQL window to make some _queries_ and _mutations_
   - In the GraphQL version, by default the `wombats` are sorted by birthday in a _descending_ order.


I hope you enjoy looking at my code. I am looking forward to meeting all of you and join the team. 

Have a great week!
