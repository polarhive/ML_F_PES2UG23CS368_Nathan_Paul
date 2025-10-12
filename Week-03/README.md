# Comparative Analysis

## 1. Algorithm Performance

**a. Which dataset achieved the highest accuracy and why?**

The **Mushroom dataset** has the highest accuracy 100%, as many categorical features (such as odour, cap shape, and colour) have a direct correlation with the class (edible vs. poisonous). This leads to very effective and clear split rules in the ID3 tree.

**b. How does dataset size affect performance?**

As dataset size increases, decision trees generally become deeper and more complex. However, actual performance depends on whether the features are balanced and predictive. Larger datasets with strong features improve stability, while imbalanced / noisy data may reduce generalisation.

**c. What role does the number of features play?**

A larger number of features provides better split options and can increase predictive power, but can also raises tree complexity and the risk of overfitting.

---

## 2. Data Characteristics Impact

**a. How does class imbalance affect tree construction?**

In the **Nursery**, class imbalance caused the model to favour the majority classes while ignoring minority ones, leading to biased predictions and reduced recall for rare classes.

**b. Which types of features (binary vs. multi-valued) work better?**

**Multi-valued categorical features** worked better in these experiments, as they captured stronger decision signals in fewer splits compared to purely binary features.

---

## 3. Practical Applications

**a. For which real-world scenarios is each dataset type most relevant?**

- **Mushroom:** agriculture, and food safety (classifying edible vs. poisonous mushrooms).
- **Tic-Tac-Toe:** Game theory research and strategy learning (evaluating board states).
- **Nursery:** Admission, schooling decision support systems.
  
**b. What are the interpretability advantages for each domain?**

- **Mushroom:** Highly interpretable with simple, human-readable rules (odour).
- **Tic-Tac-Toe:** Less intuitive, as multiple splits are required to get win/loss conditions.
- **Nursery:** Complex but rule-based, making policy-style decisions easily explainable.

**c. How would you improve performance for each dataset?**

- **Mushroom:** Already achieves 100%, pruning can simplify the tree without losing performance.
- **Tic-Tac-Toe:** Use ensemble methods to improve generalization and reduce depth.
- **Nursery:** Apply ensemble methods and class imbalance handling to improve minority class performance.