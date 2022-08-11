from sklearn.metrics import accuracy_score, confusion_matrix

prediction = [2, 2, 0, 1, 1, 1, 1, 1, 2, 2, 0, 2]
actual_results = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]

print(f'Accuracy = {(accuracy_score(actual_results, prediction))*100:.2f}%')
print(f'Confusion Matrix:\n{confusion_matrix(actual_results, prediction)}')

