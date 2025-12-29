---
name: data-ai-machine-learning
description: Master Data Science, AI Engineering, Machine Learning, MLOps, Prompt Engineering, and AI systems. Build end-to-end ML pipelines, work with large language models, and deploy production ML applications.
sasmp_version: "1.3.0"
bonded_agent: 01-frontend-ui-design
bond_type: PRIMARY_BOND
---

# Data, AI & Machine Learning

## Quick Start

### Machine Learning Fundamentals
```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load and prepare data
X, y = load_data()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

### Supervised Learning - Classification
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.3f}")
print(f"Precision: {precision_score(y_test, y_pred):.3f}")
print(f"Recall: {recall_score(y_test, y_pred):.3f}")
```

### Deep Learning with PyTorch
```python
import torch
import torch.nn as nn
from torch.optim import Adam

# Define model
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super().__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Train
model = NeuralNet(784, 128, 10)
optimizer = Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()

for epoch in range(10):
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

### NLP with Transformers
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load pre-trained model
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")

# Tokenize text
text = "This movie is fantastic!"
inputs = tokenizer(text, return_tensors="pt")

# Get predictions
outputs = model(**inputs)
logits = outputs.logits
```

### Prompt Engineering
```python
import openai

# System prompt defines behavior
system_prompt = """You are an expert data scientist.
Provide clear, technical explanations with code examples."""

# Few-shot learning
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "Explain logistic regression"},
    {"role": "assistant", "content": "Logistic regression is..."},
    {"role": "user", "content": "How do I implement it in Python?"},
]

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=messages,
    temperature=0.7,
    max_tokens=500
)
```

### MLOps Pipeline
```python
# Model versioning with MLflow
import mlflow

mlflow.set_experiment("customer_churn")

with mlflow.start_run():
    model = train_model(X_train, y_train)
    accuracy = evaluate_model(model, X_test, y_test)

    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "model")
```

## Learning Paths

### Machine Learning (roadmap.sh/machine-learning)
1. **Fundamentals**
   - Supervised vs unsupervised
   - Training/validation/test split
   - Overfitting and regularization
   - Cross-validation

2. **Algorithms**
   - Linear regression
   - Logistic regression
   - Decision trees
   - Random forests
   - SVM
   - K-means clustering

3. **Evaluation**
   - Confusion matrix
   - ROC curves
   - F1 score
   - Precision/Recall

### Deep Learning
```python
# CNN for image classification
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32)
```

### AI Engineer (roadmap.sh/ai-engineer)
- LLM applications
- Prompt engineering
- RAG (Retrieval-Augmented Generation)
- Fine-tuning models
- Building AI agents

### Data Science (roadmap.sh/ai-data-scientist)
- Statistical analysis
- Data visualization
- Hypothesis testing
- Exploratory data analysis
- Business metrics

### MLOps (roadmap.sh/mlops)
```yaml
# Model deployment with Docker
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY model.pkl .
COPY app.py .
CMD ["python", "app.py"]
```

**MLOps Components:**
- Model versioning
- Experiment tracking
- Model registry
- Continuous training
- Model monitoring
- A/B testing

### Data Science Stack

| Tool | Purpose | Language |
|------|---------|----------|
| Pandas | Data manipulation | Python |
| NumPy | Numerical computing | Python |
| Scikit-learn | ML algorithms | Python |
| TensorFlow | Deep learning | Python |
| PyTorch | Deep learning | Python |
| Hugging Face | NLP/LLMs | Python |
| Matplotlib/Seaborn | Visualization | Python |
| Plotly | Interactive viz | Python |

### Data Analyst (roadmap.sh/data-analyst)
- SQL for querying
- Data visualization
- Statistical analysis
- Business intelligence
- Tableau/Power BI

### BI Analyst (roadmap.sh/bi-analyst)
- Data warehousing
- ETL processes
- Dashboard creation
- KPI tracking
- Data storytelling

### Data Engineer (roadmap.sh/data-engineer)
- ETL/ELT pipelines
- Data warehouses
- Big data technologies
- Stream processing
- Data quality

## Specialized Topics

### Prompt Engineering (roadmap.sh/prompt-engineering)
```python
# Chain-of-thought prompting
prompt = """Think step by step:
1. First, identify the problem
2. Then, consider the constraints
3. Finally, propose a solution

Problem: How to improve model accuracy?
"""

# Temperature affects randomness (0-2)
# 0 = deterministic, 2 = very creative
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.5
)
```

### AI Red Teaming (roadmap.sh/ai-red-teaming)
- Adversarial testing
- Jailbreak attempts
- Bias detection
- Safety evaluation
- Vulnerability assessment

### AI Agents (roadmap.sh/ai-agents)
```python
# ReAct framework
def agent_loop(state, tools):
    while not done:
        thought = model.think(state)
        action = model.decide_action(thought, tools)
        observation = execute_action(action)
        state = update_state(state, action, observation)
    return state.result
```

## Best Practices Checklist

- [ ] Clean, labeled data
- [ ] Train/validation/test split
- [ ] Cross-validation
- [ ] Feature scaling
- [ ] Handle class imbalance
- [ ] Monitor for data drift
- [ ] Version control models
- [ ] Document experiments
- [ ] Track hyperparameters
- [ ] Evaluate on test set (once!)
- [ ] Consider fairness & bias
- [ ] Create model cards
- [ ] Monitor in production

## Resources

- [Kaggle](https://kaggle.com) - Datasets and competitions
- [Papers with Code](https://paperswithcode.com) - Research + code
- [Fast.ai](https://fast.ai) - Practical deep learning
- [DeepLearning.AI](https://deeplearning.ai) - Andrew Ng courses
