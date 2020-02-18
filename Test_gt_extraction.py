import pickle
import json

# read from the pickle file
with open('annotation_test.pkl', 'rb') as f:
    annot = pickle.load(f, encoding='latin1')

# write the ground truth values for openness trait to a text file
with open('openesss.txt', 'w') as f:
    f.write(json.dumps(annot['openness']))

# write the ground truth values for agreaableness trait to a text file
with open('agreaableness.txt', 'w') as f:
    f.write(json.dumps(annot['agreeableness']))

# write the ground truth values for conscientiousness trait to a text file
with open('conscientiousness.txt', 'w') as f:
    f.write(json.dumps(annot['conscientiousness']))

# write the ground truth values for extraversion trait to a text file
with open('extraversion.txt', 'w') as f:
    f.write(json.dumps(annot['extraversion']))

# write the ground truth values for neuroticism trait to a text file
with open('neuroticism.txt', 'w') as f:
    f.write(json.dumps(annot['neuroticism']))
