from sklearn.metrics import accuracy_score

prediction = [1, 1, 1]
actual_results = [1, 0, 1]

correct  = 0
for i in range(len(prediction)):
    if prediction[i] == actual_results[i]:
        correct  += 1

print(f'For loop accuracy = {(correct  / len(prediction))*100:.2f}%')

print(f'Sklearn accuracy = {(accuracy_score(actual_results, prediction))*100:.2f}%')
