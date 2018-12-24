from flask import Flask, render_template, request
from optlang import Model, Variable, Constraint, Objective

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/test')
def compute():

   x1 = Variable('x1', lb=0)
x2 = Variable('x2', lb=0)
x3 = Variable('x3', lb=0)
x4 = Variable('x4', lb=0)
x5 = Variable('x5', lb=0)
x6 = Variable('x6', lb=0)
x7 = Variable('x7', lb=0)
x8 = Variable('x8', lb=0)
x9 = Variable('x9', lb=0)

# LOWER BOUND >=
#UPPER BOUND <=

# A constraint is constructed from an expression of variables and a lower and/or upper bound (lb and ub).
# The contraints wiht = sign should be reconstructed to have two new contraints with >= and <=

c1 = Constraint(x1+ x2+ x3+ x4+ x5+ x6+ x7+ x8+ x9,lb= 100 )
c2 = Constraint(0.088*x1+0.44*x2+0.157*x3+ 0*x4 + 0*x5 + 0*x6 + 0.6*x7+0.6*x8 + 0*x9, lb=20.87)
c3 = Constraint(0.04*x1 +0.035*x2 + 0*x3 + 0*x4 + 0*x5 + 0*x6 + 0*x7 + 0*x8 + 0*x9 ,ub= 3.55)
c4 = Constraint(0.02*x1+0.065*x2+0.051*x3 + 0*x4 + 0*x5 + 0*x6 + 0*x7 + 0*x8 + 0*x9 ,ub= 4.09)
c5 = Constraint(0.0001*x1+0.002*x2+0.0014*x3+0.21*x4+0.38*x5 + 0*x6 + 0*x7 + 0*x8 + 0*x9 ,ub= 1.86)
c6 = Constraint(0.0009*x1+0.002*x2+0.0115*x3+0.185*x4+0.015*x5 + + 0*x6 + 0*x7 + 0*x8 + 0*x9 ,lb=0.58 )
c7 = Constraint(0.0025*x1+0.028*x2+0.0059*x3 + 0*x5 + 0*x6 + x7 + 0*x8 + 0*x9,lb= 1.26 )
c8 = Constraint(0.0018*x1+0.0059*x2+0.0042*x3+0*x5 + 0*x6 + 0*x7 + x8 + 0*x9,lb=0.42 )
c9 = Constraint(3432*x1 + 2230*x2 + 1300*x3+ + 0*x4 + 0*x5 + 0*x6 + 0*x7 + 0*x8 + 0*x9,lb= 2826.39)
c10 = Constraint(0*x1 + 0*x2 + 0*x3 + 0*x4 + 0*x5 + x6 + 0*x7 + 0*x8 + 0*x9, ub=0.3)
c11 = Constraint(0*x1 + 0*x2 + 0*x3 + 0*x4 + 0*x5 + 0*x6 + 0*x7 + 0*x8 + x9, ub=0.3)
c12 = Constraint(0.0001*x1+0.002*x2+0.0014*x3+0.21*x4+0.38*x5 + 0*x6 + 0*x7 + 0*x8 + 0*x9 ,lb= 1.86)




# An objective can be formulated
obj = Objective( 58*x1+150*x2+60*x3+15*x4+50*x5+90*x6+700*x7+1300*x8+550*x9
 ,direction='min')

# Variables, constraints and objectives are combined in a Model object, which can subsequently be optimized.
model = Model(name='Simple model')
model.objective = obj
model.add([c1, c2, c3,c4,c5,c6,c7,c8,c9,c10,c11,c12])
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
