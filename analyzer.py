import argparse


def to_text(filepath):
	textfile_path=""
	return textfile_path

def tokenize(textfile_path):
	tokens=[]
	return tokens

def extract_skills(tokens, keywords_file):
	skills=[]
	count=0
	with open(keywords_file) as f:
		for line in f.readlines():
			count=count+1
			if line in tokens:
				skills.append(line)
	return (skills,count)

def main():
	parser = argparse.ArgumentParser(usage="-h for full usage")
	parser.add_argument("cv", help='cv file',required=True)
    parser.add_argument('-k', dest="keywords", help='keywords file',required=True)
    parser.add_argument('-t', dest="threshold", help='acceptance threshold',required=True)
    args = parser.parse_args()
    tempfile=to_text(args.cv)
    tokens=tokenize(tempfile)
    skills, count=extract_skills(tokens,args.keywords)
    for skill in skills:
    	print skill
    verdict="rejected"
    if len(skills)/count > int(args.threshold):
    	verdict="accepted"
    print verdict

if __name__ == '__main__':
	main()
