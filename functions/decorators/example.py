class Employee:

    @staticmethod
    def add():
        pass

    @classmethod
    def create():
        pass

    @property
    def salary():
        pass

#@staticmethod
#@classmethod
#@property #are decorators, but they're being used inside OOP.

# Also, frameworks like Flask use decorators:
@app.route("/login")
def login():
    pass

# And FastAPI:
@app.get("/employees")
def get_employees():
    pass