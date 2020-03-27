from flask import Flask, render_template

app = Flask(__name__)
application = app

import csv

def convert_to_dict(filename):
    datafile = open("datingdata.csv", newline='')
    my_reader = csv.DictReader(datafile)
    list_of_dicts = list(my_reader)
    datafile.close()
    return list_of_dicts


dating_profiles = convert_to_dict("datingdata.csv")

# create a list of tuples in which the first item is the number
# (Presidency) and the second item is the name (President)
triple_list = []
for d in dating_profiles:
    triple_list.append( (d['list-id'], d['name'], d['indexfor-artist-pic']) )


# first route

@app.route('/')
def index():
   return render_template('index.html', triple=triple_list)
#
#dating_dict["birth-name"]
# dating_dict["birthplace"]
# dating_dict["hobby"]

# second route

@app.route('/date_profile/<num>')
def detail(num):
    dating_dict = dating_profiles[int(num) - 1]
    return render_template('dating_profile.html', dict=dating_dict)
# except:
#     return f"<h1>Invalid profile! Please try again</h1>"






# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
