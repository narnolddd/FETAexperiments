# Configuration for Scientific Reports Paper: Citation Dataset

## Parameter fitting for number of changepoints

| Parameter | Value |
| --- | --- |
| Start | 747411840 |
| End | 1015956000 |

```bash
python3 experiments/citations/changepoint/numberChangepoints.py
```

## Extraction of operation model

```bash
java -jar feta3-1.0.0.jar experiments/citations/Citations_ParseOperations.json
```