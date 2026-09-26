import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Read the CSV file
data = pd.read_csv("salary_data.csv")

# Step 2: Display the data
print("Dataset:")
print(data)

# Step 3: Separate X and Y
X = data[["YearsExperience"]]
y = data["Salary"]

# Step 4: Create Linear Regression model
model = LinearRegression()

# Step 5: Train the model
model.fit(X, y)

# Step 6: Predict salary
y_pred = model.predict(X)

# Step 7: Display results
print("\nSlope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("R² Score:", model.score(X, y))

# Step 8: Create graph
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, y_pred, color="red", label="Regression Line")

plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Years of Experience vs Salary")
plt.legend()

# Step 9: Show graph
plt.show()
