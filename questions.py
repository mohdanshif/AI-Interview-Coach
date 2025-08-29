# Simple starter set. Extend freely.
QUESTIONS = [
{
'id': 1,
'topic': 'ML Basics',
'question': 'What is overfitting in machine learning, and how can you prevent it?',
'answer': (
'Overfitting happens when a model fits noise rather than signal, '
'leading to poor generalization. Mitigations include collecting more data, '
'stronger regularization (L1/L2), dropout, early stopping, data augmentation, '
'simpler architectures, and cross-validation for model selection.'
),
'keywords': ['generalization', 'regularization', 'cross-validation', 'dropout', 'early stopping']
},
{
'id': 2,
'topic': 'Supervised vs Unsupervised',
'question': 'Explain the difference between supervised and unsupervised learning with examples.',
'answer': (
'Supervised learning uses labeled data to learn a mapping (e.g., classification, regression). '
'Unsupervised learning finds structure in unlabeled data (e.g., clustering, dimensionality reduction). '
'Examples: supervised – spam detection, house price prediction; unsupervised    +– k-means clustering, PCA.'
),
'keywords': ['labeled', 'unlabeled', 'classification', 'clustering', 'PCA']
},
{
'id': 3,
'topic': 'Model Evaluation',
'question': 'What is precision, recall, and F1-score? When would you prefer recall over precision?',
'answer':(
'Precision is TP/(TP+FP), recall is TP/(TP+FN), and F1 is the harmonic mean of precision and recall. '
'Prefer recall when missing positives is costly (e.g., disease screening, fraud detection).'
),
'keywords': ['precision', 'recall', 'F1', 'false positives', 'false negatives']
}
]
