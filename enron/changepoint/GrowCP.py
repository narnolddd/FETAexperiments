import warnings
warnings.filterwarnings("ignore")
import os
import re

root = "experiments/enron"
tmpm_file = root+"EnronMeasure.tmp"

with open(root+"EnronMeasure.json",'r') as f:
    likedata = f.read()
    f.close()

for i in range(10):
    if i > 1:
        os.system("java -jar feta3-1.0.0.jar "+root+"changepoint/EnronCopyCP.json")
    tmp = re.sub("NUM",str(i),likedata)
    with open(tmpm_file,'w') as f:
        f.write(tmp)
        f.close()
    os.system("java -jar feta3-1.0.0.jar "+tmpm_file)

