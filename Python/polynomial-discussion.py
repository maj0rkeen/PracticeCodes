# import numpy as np
# import matplotlib.pyplot as plt

# # Define x values (range from -10 to 10)
# x = np.linspace(-10, 10, 100)

# # Generate random coefficients for each polynomial degree
# np.random.seed(42)  # For reproducibility
# coefficients = {
#     1: np.random.uniform(-5, 5, 2),  # Degree 1 (Linear)
#     2: np.random.uniform(-5, 5, 3),  # Degree 2 (Quadratic)
#     3: np.random.uniform(-5, 5, 4),  # Degree 3 (Cubic)
#     4: np.random.uniform(-5, 5, 5),  # Degree 4 (Quartic)
#     5: np.random.uniform(-5, 5, 6),  # Degree 5 (Quintic)
# }

# # Create separate plots for each polynomial degree
# for degree, coeffs in coefficients.items():
#     y = np.polyval(coeffs, x)  # Compute y values

#     plt.figure(figsize=(6, 4))  # Create a new figure for each plot
#     plt.plot(x, y, label=f'Degree {deg ree}', color='b')

#     # Plot settings
#     plt.axhline(0, color='black', linewidth=0.5, linestyle="--")
#     plt.axvline(0, color='black', linewidth=0.5, linestyle="--")
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.title(f'Polynomial Regression (Degree {degree})')
#     plt.legend()
#     plt.grid(True)

#     plt.show()  # Show each plot separately
    
    
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# Day Number
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)

# Plant Growth
y = np.array([1, 2, 3, 5, 15, 34, 48, 70, 136, 185])

poly = PolynomialFeatures(degree = 8)
x_poly = poly.fit_transform(x)


# Create and fit the model
model = LinearRegression()
model.fit(x_poly, y)

# Predict values
y_pred = model.predict(x_poly)

# Calculate R² score
r2 = r2_score(y, y_pred)

# Print model details
print(f"Slope (coefficient): {model.coef_[0]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")
print(f"R² Score: {r2:.4f}")

# Plotting
plt.scatter(x, y, color='green', label='Actual Growth')
plt.plot(x, y_pred, color='blue', linestyle='--', label=f'Fitted Line (R² = {r2:.2f})')
plt.xlabel('Day Number')
plt.ylabel('Plant Growth')
plt.title('Regression - Plant Growth Over Time')
plt.legend()
plt.grid(True)
plt.show()
