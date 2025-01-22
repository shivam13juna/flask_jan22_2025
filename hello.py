from flask import Flask, request
import pickle

pancakes = Flask(__name__)

#!pip install flask

# git checkout -b pytest

@pancakes.route('/ping', methods=['GET'])
def ping(): # function name doesn't
	return {'message': 'Pinging Model pancakeslication!!'}


@pancakes.route('/hello', methods=['GET'])
def hello():
	return {'message': 'Hello World!!'}

@pancakes.route('/', methods=['GET'])
def home():
    return '''
    <html>
        <head>
            <title>Congratulation on successful CI/CD completion</title>
        </head>
        <body>
            <h1>Congratulation on successful CI/CD completion, Good going guys!!</h1>
            <p>MLOPS Engineer on the rise!!.</p>
        </body>
    </html>
    '''

model_pickle = open("classifier.pkl", "rb")
clf = pickle.load(model_pickle)


@pancakes.route('/predict', methods=['POST'])
def predict():
	loan_req = request.get_json()

	if loan_req['Gender'] == "Male":
		Gender = 0
	else:
		Gender = 1

	if loan_req['Married'] == "Unmarried":
		Married = 0
	else:
		Married = 1

	if loan_req['Credit_History'] == "Unclear Debts":
		Credit_History = 0
	else: 
		Credit_History = 1
	
	ApplicantIncome = loan_req['ApplicantIncome']

	LoanAmount = loan_req['LoanAmount']
	
	result = clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

	if result == 0:
		pred = "Rejected" 
	else:
		pred = "Approved"
	
	return {"loan_approval_status": pred}


#{
#    "Gender": "Male",
#    "Married": "Unamrried",
#    "ApplicantIncome": 50000, 
#    "Credit_History": "Cleared Debts",
#    "LoanAmount": 50

#}


#flask --pancakes hello.py run

#http://127.0.0.1:5000/ping


#gu "Code for  unit-changes done"

#gu() {
#    # First argument as commit message
#    local commit_msg="$1"
#    # Determine branch: use second argument if provided, otherwise use current branch
#    local branch="${2:-$(git rev-parse --abbrev-ref HEAD)}"

#    git add .
#    git commit -m "$commit_msg"
#    git push --set-upstream origin "$branch"
#}