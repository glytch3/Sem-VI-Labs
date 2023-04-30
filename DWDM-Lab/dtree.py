import pandas as pd
import numpy as np

data = pd.DataFrame({
    'Age': ['<=30', '<=30', '31-40', '>40', '>40', '>40', '31-40', '<=30', '<=30', '>40', '<=30', '31-40', '31-40', '>40'],
    'Income': ['High', 'High', 'High', 'Medium', 'Low', 'Low', 'Low', 'Medium', 'Low', 'Medium', 'Medium', 'Medium', 'High', 'Medium'],
    'Marital Status': ['Single', 'Married', 'Single', 'Single', 'Single', 'Married', 'Married', 'Single', 'Married', 'Married', 'Married', 'Single', 'Married', 'Single'],
    'Credit Rating': ['Fair', 'Excellent', 'Fair', 'Fair', 'Fair', 'Excellent', 'Excellent', 'Fair', 'Fair', 'Fair', 'Excellent', 'Excellent', 'Fair', 'Excellent'],
    'Buys Computer': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
})

def entropy(target):
    classes, counts = np.unique(target, return_counts=True)
    probs = counts / len(target)
    return -np.sum(probs * np.log2(probs))

def information_gain(data, feature, target):
    feature_values, feature_counts = np.unique(data[feature], return_counts=True)
    feature_probs = feature_counts / len(data[feature])
    target_entropy = entropy(target)
    weighted_entropies = []
    for value in feature_values:
        value_data = data[data[feature] == value]
        value_target = target[data[feature] == value]
        value_entropy = entropy(value_target)
        weighted_entropies.append(feature_probs[np.where(feature_values == value)[0][0]] * value_entropy)
    return target_entropy - np.sum(weighted_entropies)

def id3(data, target, features):
    # Base case: all data points have the same target value
    if len(np.unique(target)) == 1:
        return target.iloc[0]
    # Base case: there are no more features to split on
    if len(features) == 0:
        return target.value_counts().idxmax()
    # Choose the feature with the highest information gain
    information_gains = [information_gain(data, feature, target) for feature in features]
    best_feature_index = np.argmax(information_gains)
    best_feature = features[best_feature_index]
    # Build the subtree recursively
    tree = {best_feature: {}}
    features = [f for f in features if f != best_feature]
    for value in np.unique(data[best_feature]):
        value_data = data[data[best_feature] == value]
        value_target = target[data[best_feature] == value]
        subtree = id3(value_data, value_target, features)
        tree[best_feature][value] = subtree
    return tree

target = data['Buys Computer']
features = ['Age', 'Income', 'Marital Status', 'Credit Rating' ]
tree = id3(data, target, features)
print(tree)

