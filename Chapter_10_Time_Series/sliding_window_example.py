from numpy.lib.stride_tricks import sliding_window_view

data = [7.226, 6.595, 6.524, 5.944, 6.075]
window_size = 2
X = sliding_window_view(data[:-1], window_size)  # the -1 leaves the last value for the y value
y = y_train = data[window_size:]

print(f'Original data = {data}')
print(f'X = {X}')
print(f'y = {y}')
