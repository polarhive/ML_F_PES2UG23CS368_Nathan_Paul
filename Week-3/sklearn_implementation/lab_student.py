import numpy as np
from collections import Counter

def get_entropy_of_dataset(data: np.ndarray) -> float:
    """
    Calculate the entropy of the entire dataset using the target variable (last column).
    
    Args:
        data (np.ndarray): Dataset where the last column is the target variable
    
    Returns:
        float: Entropy value calculated using the formula: 
               Entropy = -Σ(p_i * log2(p_i)) where p_i is the probability of class i
    
    Example:
        data = np.array([[1, 0, 'yes'],
                        [1, 1, 'no'],
                        [0, 0, 'yes']])
        entropy = get_entropy_of_dataset(data)
        # Should return entropy based on target column ['yes', 'no', 'yes']
    """
    # TODO: Implement entropy calculation
    # Hint: Use np.unique() to get unique classes and their counts
    # Hint: Handle the case when probability is 0 to avoid log2(0)

    if data is None or len(data) == 0: return 0.0
    target = data[:, -1]
    counts = np.unique(target, return_counts=True)

    total = counts.sum()
    if total == 0: return 0.0

    probs = counts.astype(np.float64) / float(total)
    non_zero = probs > 0
    entropy = -np.sum(probs[non_zero] * np.log2(probs[non_zero]))
    return float(entropy)


def get_avg_info_of_attribute(data: np.ndarray, attribute: int) -> float:
    """
    Calculate the average information (weighted entropy) of a specific attribute.
    
    Args:
        data (np.ndarray): Dataset where the last column is the target variable
        attribute (int): Index of the attribute column to calculate average information for
    
    Returns:
        float: Average information calculated using the formula:
               Avg_Info = Σ((|S_v|/|S|) * Entropy(S_v)) 
               where S_v is subset of data with attribute value v
    
    Example:
        data = np.array([[1, 0, 'yes'],
                        [1, 1, 'no'],
                        [0, 0, 'yes']])
        avg_info = get_avg_info_of_attribute(data, 0)  # For attribute at index 0
        # Should return weighted average entropy for attribute splits
    """
    # TODO: Implement average information calculation
    # Hint: For each unique value in the attribute column:
    #   1. Create a subset of data with that value
    #   2. Calculate the entropy of that subset
    #   3. Weight it by the proportion of samples with that value
    #   4. Sum all weighted entropies

    if data is None or len(data) == 0: 
        return 0.0

    n_samples = data.shape[0]
    values, counts = np.unique(data[:, attribute], return_counts=True)

    avg_info = 0.0
    for v, cnt in zip(values, counts):
        mask = data[:, attribute] == v
        subset = data[mask]
        weight = cnt / n_samples
        # Calculate entropy for the subset
        subset_entropy = get_entropy_of_dataset(subset)
        # Add weighted entropy to avg_info
        avg_info += weight * subset_entropy

    # Return the average information (weighted entropy)
    return float(avg_info)


def get_information_gain(data: np.ndarray, attribute: int) -> float:
    """
    Calculate the Information Gain for a specific attribute.
    
    Args:
        data (np.ndarray): Dataset where the last column is the target variable
        attribute (int): Index of the attribute column to calculate information gain for
    
    Returns:
        float: Information gain calculated using the formula:
               Information_Gain = Entropy(S) - Avg_Info(attribute)
               Rounded to 4 decimal places
    
    Example:
        data = np.array([[1, 0, 'yes'],
                        [1, 1, 'no'],
                        [0, 0, 'yes']])
        gain = get_information_gain(data, 0)  # For attribute at index 0
        # Should return the information gain for splitting on attribute 0
    """
    # TODO: Implement information gain calculation
    # Hint: Information Gain = Dataset Entropy - Average Information of Attribute
    # Hint: Use the functions you implemented above
    # Hint: Round the result to 4 decimal places

    if data is None or len(data) == 0: return 0.0

    dataset_entropy = get_entropy_of_dataset(data)
    avg_info = get_avg_info_of_attribute(data, attribute)
    gain = dataset_entropy - avg_info
    return round(float(gain), 4)

def get_selected_attribute(data: np.ndarray) -> tuple:
    """
    Select the best attribute based on highest information gain.
    
    Args:
        data (np.ndarray): Dataset where the last column is the target variable
    
    Returns:
        tuple: A tuple containing:
            - dict: Dictionary mapping attribute indices to their information gains
            - int: Index of the attribute with the highest information gain
    
    Example:
        data = np.array([[1, 0, 2, 'yes'],
                        [1, 1, 1, 'no'],
                        [0, 0, 2, 'yes']])
        result = get_selected_attribute(data)
        # Should return something like: ({0: 0.123, 1: 0.456, 2: 0.789}, 2)
        # where 2 is the index of the attribute with highest gain
    """
    # TODO: Implement attribute selection
    # Hint: Calculate information gain for all attributes (except target variable)
    # Hint: Store gains in a dictionary with attribute index as key
    # Hint: Find the attribute with maximum gain using max() with key parameter
    # Hint: Return tuple (gain_dictionary, selected_attribute_index)

    if data is None or len(data) == 0:
        return ({}, -1)

    n_cols = data.shape[1]
    # Exclude the last column (target)
    gains = {}
    for attr in range(n_cols - 1):
        gains[attr] = get_information_gain(data, attr)

    if not gains:
        return (gains, -1)

    selected_attr = max(gains, key=lambda k: gains[k])
    return (gains, selected_attr)
