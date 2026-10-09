from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt 

car_data = pd.read_csv("car.csv")

m = car_data[["mileage"]]
v = car_data["vehicle_score"]

model = LinearRegression()

model.fit(m,v)

x = 9
y =   model.predict([[x]])
newt = model.predict(m)

plt.plot(m,v)
plt.plot(m,newt)
plt.scatter(x,y)
plt.show()