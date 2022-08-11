from scipy.stats import entropy

print('''
The following calculations are based on the following data (found in sledding.csv):
snowing	temperature	wind	time	predictor(sledding)
yes	below_freezing	high	morning	yes
yes	freezing	high	morning	yes
yes	above_freezing	low	afternoon	yes
yes	below_freezing	low	afternoon	yes
yes	freezing	medium	morning	no
yes	below_freezing	low	afternoon	yes
no	freezing	medium	afternoon	yes
no	above_freezing	medium	morning	no
no	above_freezing	medium	morning	no
no	below_freezing	low	afternoon	yes
no	freezing	low	afternoon	no
no	above_freezing	high	afternoon	no''')

print('Part I - determining the root node following the ID3 technique:')

print(f'Entropy(snowing) = {entropy([5, 7], base=2):.2f}')
print(f'Entropy(snowing_yes) = {entropy([1, 5], base=2):.2f}')
print(f'Entropy(snowing_no) = {entropy([4, 2], base=2):.2f}')
print(f'Information Gain for snowing = {entropy([5, 7], base=2) - (6/12 * entropy([1, 5], base=2) + 6/12 * entropy([4, 2], base=2)):.3f}')
print()

print(f'Entropy(temperature) = {entropy([5, 7], base=2):.2f}')
print(f'Entropy(temperature_above_freezing) = {entropy([3, 1], base=2):.2f}')
print(f'Entropy(temperature_below_freezing) = {entropy([0, 4], base=2):.2f}')
print(f'Entropy(temperature_freezing) = {entropy([2, 2], base=2):.2f}')
print(f'Information Gain for temperature = {entropy([5, 7], base=2) - (4/12 * entropy([3, 1], base=2) + 4/12 * entropy([0, 4], base=2) + 4/12 * entropy([2, 2], base=2)):.3f}')
print()

print(f'Entropy(wind) = {entropy([5, 7], base=2):.2f}')
print(f'Entropy(wind_low) = {entropy([1, 4], base=2):.2f}')
print(f'Entropy(wind_medium) = {entropy([3, 1], base=2):.2f}')
print(f'Entropy(wind_high) = {entropy([1, 2], base=2):.2f}')
print(f'Information Gain for wind = {entropy([5, 7], base=2) - (5/12 * entropy([1, 4], base=2) + 4/12 * entropy([3, 1], base=2) + 3/12 * entropy([1, 2], base=2)):.3f}')
print()

print(f'Entropy(time) = {entropy([5, 7], base=2):.2f}')
print(f'Entropy(time_morning) = {entropy([3, 2], base=2):.2f}')
print(f'Entropy(time_afternoon) = {entropy([2, 5], base=2):.2f}')
print(f'Information Gain for time = {entropy([5, 7], base=2) - (5/12 * entropy([3, 2], base=2) + 7/12 * entropy([2, 5], base=2)):.3f}')
print()

print('temperature has the highest information gain, so that will be our root node.')
print()

print('Part II:')
print('Now there are three sets of data:')
print('''snowing	wind	time	predictor(sledding)
yes	low	afternoon	yes
no	medium	morning	no
no	medium	morning	no
no	high	afternoon	no''')
print()

print(f'Entropy(snowing) = {entropy([3, 1], base=2):.2f}')
print(f'Entropy(snowing_yes) = {entropy([0, 1], base=2):.2f}')
print(f'Entropy(snowing_no) = {entropy([3, 0], base=2):.2f}')
print(f'Information Gain for snowing = {entropy([3, 1], base=2) - (1/4 * entropy([0, 1], base=2) + 3/4 * entropy([3, 0], base=2)):.3f}')
print()

print(f'Entropy(wind) = {entropy([3, 1], base=2):.2f}')
print(f'Entropy(wind_low) = {entropy([0, 1], base=2):.2f}')
print(f'Entropy(wind_medium) = {entropy([2, 0], base=2):.2f}')
print(f'Entropy(wind_high) = {entropy([1, 0], base=2):.2f}')
print(f'Information Gain for wind = {entropy([3, 1], base=2) - (1/4 * entropy([0, 1], base=2) + 2/4 * entropy([2, 0], base=2) + 1/4 * entropy([1, 0], base=2)):.3f}')
print()

print(f'Entropy(time) = {entropy([3, 1], base=2):.2f}')
print(f'Entropy(time_morning) = {entropy([2, 0], base=2):.2f}')
print(f'Entropy(time_afternoon) = {entropy([1, 1], base=2):.2f}')
print(f'Information Gain for time = {entropy([3, 1], base=2) - (2/4 * entropy([2, 0], base=2) + 2/4 * entropy([1, 1], base=2)):.3f}')
print()

print('Now we consider the freezing attribute.')
print('''snowing	wind	time	predictor(sledding)
yes	high	morning	yes
yes	medium	morning	no
no	medium	afternoon	yes
no	low	afternoon	no''')
print()

print(f'Entropy(snowing) = {entropy([2, 2], base=2):.2f}')
print(f'Entropy(snowing_yes) = {entropy([2, 2], base=2):.2f}')
print(f'Entropy(snowing_no) = {entropy([2, 2], base=2):.2f}')
print(f'Information Gain for snowing = {entropy([2, 2], base=2) - (2/4 * entropy([2, 2], base=2) + 2/4 * entropy([2, 2], base=2)):.3f}')
print()

print(f'Entropy(wind) = {entropy([2, 2], base=2):.2f}')
print(f'Entropy(wind_low) = {entropy([1, 0], base=2):.2f}')
print(f'Entropy(wind_medium) = {entropy([1, 1], base=2):.2f}')
print(f'Entropy(wind_high) = {entropy([0, 1], base=2):.2f}')
print(f'Information Gain for wind = {entropy([2, 2], base=2) - (1/4 * entropy([1, 0], base=2) + 2/4 * entropy([1, 1], base=2) + 1/4 * entropy([0, 1], base=2)):.3f}')
print()

print(f'Entropy(time) = {entropy([2, 2], base=2):.2f}')
print(f'Entropy(time_morning) = {entropy([1, 1], base=2):.2f}')
print(f'Entropy(time_afternoon) = {entropy([1, 1], base=2):.2f}')
print(f'Information Gain for time = {entropy([2, 2], base=2) - (2/4 * entropy([1, 1], base=2) + 2/4 * entropy([1, 1], base=2)):.3f}')
print()

print('Considering the path of freezing temperature, medium wind, we have the following data:')
print('''snowing	time	predictor(sledding)
yes	morning	no
no	afternoon	yes''')
print()

print(f'Entropy(snowing) = {entropy([1, 1], base=2):.2f}')
print(f'Entropy(snowing_yes) = {entropy([1, 0], base=2):.2f}')
print(f'Entropy(snowing_no) = {entropy([0, 1], base=2):.2f}')
print(f'Information Gain for snowing = {entropy([1, 1], base=2) - (1/2 * entropy([1, 0], base=2) + 1/2 * entropy([0, 1], base=2)):.3f}')
print()

print(f'Entropy(time) = {entropy([1, 1], base=2):.2f}')
print(f'Entropy(time_morning) = {entropy([1, 0], base=2):.2f}')
print(f'Entropy(time_afternoon) = {entropy([0, 1], base=2):.2f}')
print(f'Information Gain for time = {entropy([1, 1], base=2) - (1/2 * entropy([1, 0], base=2) + 1/2 * entropy([0, 1], base=2)):.3f}')
print()

print('Now we consider the below_freezing attribute:')
print('''snowing	wind	time	predictor(sledding)
yes	high	morning	yes
yes	low	afternoon	yes
yes	low	afternoon	yes
no	low	afternoon	yes''')

print('All yes\'s, so it does not matter.')
