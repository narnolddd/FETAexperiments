import warnings
warnings.filterwarnings("ignore")
import os
import re

root = "experiments/citations/"
tmpm_file = root+"CitationsMeasure.tmp"

with open(root+"CitationsMeasure.json",'r') as f:
    likedata = f.read()
    f.close()

for i in range(10):
    os.system("java -jar feta3-1.0.0.jar "+root+"CitationsCopy.json")
    tmp = re.sub("NUM",str(i),likedata)
    with open(tmpm_file,'w') as f:
        f.write(tmp)
        f.close()
    os.system("java -jar feta3-1.0.0.jar "+tmpm_file)

