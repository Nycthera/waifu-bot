from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit([[0, 0], [1, 1]], [0, 1])
print(model.predict([[2, 2]]))  # Output: [2.]