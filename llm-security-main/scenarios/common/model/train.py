import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sentence_transformers import SentenceTransformer
import joblib

DATA_DIR = "data"
MODEL_DIR = "llm-security-main/scenarios/common/model"
TRAIN_DATA_PATH = os.path.join(DATA_DIR, "train_dataset.csv")
TEST_DATA_PATH = os.path.join(DATA_DIR, "test_dataset.csv")
LOGISTIC_MODEL_PATH = os.path.join(MODEL_DIR, "logistic_regression_model.pkl")
SENTENCE_TRANSFORMER_PATH = os.path.join(MODEL_DIR, "sentence_transformer_model")

# creates the directory if it doesn't exist
os.makedirs(MODEL_DIR, exist_ok=True)

# loads the datasets
train_data = pd.read_csv(TRAIN_DATA_PATH)
test_data = pd.read_csv(TEST_DATA_PATH)

# here we extract inputs and labels
X_train = train_data['Input']
y_train = train_data['Label']
X_test = test_data['Input']
y_test = test_data['Label']

# initializing the sentence transformer
print("Loading Sentence Transformer model...")
sentence_transformer_model = SentenceTransformer('all-mpnet-base-v2')

# converting text content to embeddings for train and test datasets
print("Encoding training data...")
X_train_embeddings = sentence_transformer_model.encode(X_train.tolist(), convert_to_tensor=False)
print("Encoding test data...")
X_test_embeddings = sentence_transformer_model.encode(X_test.tolist(), convert_to_tensor=False)

# here we train the logistic regression model based on the train dataset
print("Training Logistic Regression model...")
classifier = LogisticRegression(max_iter=1000, random_state=42)
classifier.fit(X_train_embeddings, y_train)

# evaluation results
print("Evaluating model on training data...")
y_train_pred = classifier.predict(X_train_embeddings)
train_report = classification_report(y_train, y_train_pred)
print("Evaluating model on test data...")
y_test_pred = classifier.predict(X_test_embeddings)
test_report = classification_report(y_test, y_test_pred)

print("Saving models...")
joblib.dump(classifier, LOGISTIC_MODEL_PATH)
sentence_transformer_model.save(SENTENCE_TRANSFORMER_PATH)

print("\nTraining Performance:")
print(train_report)
print("\nTest Performance:")
print(test_report)