"""
Test Cases for Counter Web Service

Create a service that can keep a track of multiple counters
- API must be RESTful - see the status.py file. Following these guidelines, you can make assumptions about
how to call the web service and assert what it should return.
- The endpoint should be called /counters
- When creating a counter, you must specify the name in the path.
- Duplicate names must return a conflict error code.
- The service must be able to update a counter by name.
- The service must be able to read the counter
"""
from unittest import TestCase
from flask import Flask

# HTTP status codes
HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_204_NO_CONTENT = 204
HTTP_404_NOT_FOUND = 404
HTTP_405_METHOD_NOT_ALLOWED = 405
HTTP_409_CONFLICT = 409

app = Flask(__name__)

COUNTERS = {}

# We will use the app decorator and create a route called /counters.
# specify the variable in route <name>
# let Flask know that the only methods allowed to call
# this function are "POST".
@app.route('/counters/<name>', methods=['POST'])
def create_counter(name):
    """Create a counter"""
    app.logger.info(f"Request to create counter: {name}")
    global COUNTERS
    if name in COUNTERS:
        return {"Message":f"Counter {name} already exists"}, HTTP_409_CONFLICT
    COUNTERS[name] = 0
    return {name: COUNTERS[name]}, HTTP_201_CREATED

@app.route('/counters/<name>', methods=['PUT'])
def update_counter(name):
    """Update a counter"""
    app.logger.info(f"Request to update counter: {name}")
    global COUNTERS
    if name not in COUNTERS:
        return {"Message": f"Counter {name} does not exist"}, HTTP_404_NOT_FOUND
    COUNTERS[name] += 1
    return {name: COUNTERS[name]}, HTTP_200_OK

@app.route('/counters/<name>', methods=['GET'])
def read_counter(name):
    """Read a counter"""
    app.logger.info(f"Request to read counter: {name}")
    global COUNTERS
    if name not in COUNTERS:
        return {"Message": f"Counter {name} does not exist"}, HTTP_404_NOT_FOUND
    return {name: COUNTERS[name]}, HTTP_200_OK

class CounterTest(TestCase):
    """Counter tests"""

    def setUp(self):
        self.client = app.test_client()


    def test_create_a_counter(self):
        """It should create a counter"""
        client = app.test_client()
        result = client.post('/counters/foo')
        self.assertEqual(result.status_code, HTTP_201_CREATED)

    def test_duplicate_a_counter(self):
        """It should return an error for duplicates"""
        result = self.client.post('/counters/bar')
        self.assertEqual(result.status_code, HTTP_201_CREATED)
        result = self.client.post('/counters/bar')
        self.assertEqual(result.status_code, HTTP_409_CONFLICT)

    def test_update_a_counter(self):
        """It should update a counter"""
        result = self.client.post('/counters/tester')  # POST request for creation
        self.assertEqual(result.status_code, HTTP_201_CREATED)

        initial_value = COUNTERS['tester']
        self.assertEqual(initial_value, 0)  # check for proper creation

        result = self.client.put('/counters/tester')  # PUT request for update
        self.assertEqual(result.status_code, HTTP_200_OK)

        updated_value = COUNTERS['tester']
        self.assertEqual(updated_value, initial_value + 1)  # check for proper update

    def test_read_a_counter(self):
        """It should read a counter"""
        result = self.client.post('/counters/baz')  # POST request for creation
        self.assertEqual(result.status_code, HTTP_201_CREATED)

        result = self.client.get('/counters/baz')  # GET request for read
        self.assertEqual(result.status_code, HTTP_200_OK)

        data = result.get_json()
        self.assertEqual(data['baz'], 0)  # check for correct value
