import urllib.request, urllib.parse
import os.path


SUBM_FORM = "https://s3.amazonaws.com/drivendata-prod/data/66/public/submission_format.csv"
TRAIN_FEATURES = "https://s3.amazonaws.com/drivendata-prod/data/66/public/training_set_features.csv"
TRAIN_LABELS = "https://s3.amazonaws.com/drivendata-prod/data/66/public/training_set_labels.csv"
TEST_FEATURES = "https://s3.amazonaws.com/drivendata-prod/data/66/public/test_set_features.csv"

print("Downloading datasets...")

for url in [SUBM_FORM, TRAIN_FEATURES, TRAIN_LABELS, TEST_FEATURES]:
    urllib.request.urlretrieve(url, os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'raw', os.path.basename(url)))
