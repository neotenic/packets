from collections import defaultdict
import sys
import json
import os

# os.chdir("db")

rounds = defaultdict(list)


for line in sys.stdin:
	q = json.loads(line)
	year = "Unknown"
	if 'year' in q:
		year = q['year']
	path = q['type'] + '/' + str(year) + "/" + q['tournament']
	# try:
	# 	os.makedirs(path)
	# except OSError:
	# 	pass
	if 'num' not in q:
		q['num'] = len(rounds[path + "/" + q['round']]) + 1

	if 'answer' not in q:
		continue

	rounds[path + "/" + q['round']].append(q)

	# print q['round'].split(".")[0].split("-")[0].strip().replace("_", " ")
	# rou = path + '/' + 

	# with open("test.txt", "a") as myfile:
	# 	myfile.write("appended text")

def ser(obj):
	return "\n".join([unicode(key) + ": "   + unicode(obj[key]) for key in obj])

def squi(q):
	keys = ["num", "category", "difficulty", "fixed", "seen", "answer"]

	return "\n".join([unicode(key) + ": "   + unicode(q[key]) for key in keys if key in q]) + "\n\n" + q['question']


for rou in rounds:
	# print rou
	questions = sorted(rounds[rou], key=lambda q: int(q['num']))
	print len(questions), rou
	hed = questions[0]

	# header = {
	# 	'tournament': hed['tournament'],
	# 	'round': hed['round']
	# }

	headerkeys = ['tournament', 'round', 'year', 'date']

	roundname = hed['round'].split(".")[0] + ".txt"
	if hed['type'] == 'jeopardy':
		path = hed['type'] + '/' + str(hed['year'])
		roundname = hed['date'] + ".txt"
	elif 'year' in hed:
		# header['year'] = hed['year']
		path = hed['type'] + '/' + str(hed['year']) + "/" + hed['tournament']
	else:
		path = hed['type'] + "/" + hed['tournament']

	try:
		os.makedirs(path)
	except OSError:
		pass

	with open(path + "/" + roundname, "w") as f:
		# f.write(("\n----\n".join([squi(q) for q in questions])).encode('utf-8'))
		f.write("####\n" + "\n".join([unicode(key) + ": " + unicode(hed[key]) for key in headerkeys if key in hed]) + "\n####\n\n")
		f.write(("\n\n----\n".join([squi(q) for q in questions])).encode('utf-8'))



