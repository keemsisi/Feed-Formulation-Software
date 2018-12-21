from flask import Flask, render_template, request
from optlang import Model, Variable, Constraint, Objective

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/test')
def compute():

    # All the (symbolic) variables are declared, with a name and optionally a lower and/or upper bound.

    x1 = Variable('x1', lb=0)
    x2 = Variable('x2', lb=0)
    x3 = Variable('x3', lb=0)
    x4 = Variable('x4', lb=0)
    x5 = Variable('x5', lb=0)
    x6 = Variable('x6', lb=0)
    x7 = Variable('x7', lb=0)

    # A constraint is constructed from an expression of variables and a lower and/or upper bound (lb and ub).

    c1 = Constraint(0.08*x1 + 0.01*x2 + 0.1*x3 + 0.11*x4 + 0.1*x5, ub=0.11)
    c2 = Constraint(x1 + x2, ub=55)
    c3 = Constraint(x3 + x4, ub=40)
    c4 = Constraint(x5, ub=22)
    c5 = Constraint(x6, ub=2)
    c6 = Constraint(x7, ub=1)
    c7 = Constraint(x1 + x2 + x3 + x4 + x5 + x6 + x7, ub=100)

    # An objective can be formulated
    obj = Objective(8.5 * x1 + 6 * x2 + 15 * x3 + 13 * x4 + 10 * x5 + 2 *40 + 1 *5 ,direction='min')

    # Variables, constraints and objectives are combined in a Model object, which can subsequently be optimized.
    model = Model(name='Simple model')
    model.objective = obj
    model.add([c1, c2, c3, c4, c5, c6, c7])
    status = model.optimize()

    print("status:", model.status)
    print("objective value:", model.objective.value)
    print("-------------")
    result = model.objective.value

    return render_template('home.html', result = result)

@app.route('/form')
def form():
    return render_template('feed_form.html')

@app.route('/testing', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        request = request.form
        return render_template("result.html", result = result)

app.run()
