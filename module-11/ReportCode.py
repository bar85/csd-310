import mysql.connector

# Connect to the database
db_config = mysql.connector.connect(
    user="winery_user",
    password="popcorn",
    host="localhost",
    database="winery"
)

cursor = db_config.cursor()

# Query to get supply inventory data
print("Supplier Delivery Report:")
cursor.execute("SELECT Type, ExpectedDate, DeliveryDate FROM SupplyInventory")
supply_data = cursor.fetchall()
for Type, ExpectedDate, DeliveryDate in supply_data:
    delivery_gap = DeliveryDate - ExpectedDate
    if delivery_gap.days > 0:
        print(f"Item {Type}: Delivery gap exceeded ({delivery_gap.days} days)")

# Query to retrieve sales information
print("\nWine Distribution Report:")
cursor.execute("""
    SELECT p.Name, d.Name, dist.SalesQuantity
    FROM Distribution dist
    JOIN Products p ON dist.ProductID = p.ProductID
    JOIN Distributors d ON dist.DistributorID = d.DistributorID
""")
sales_data = cursor.fetchall()
for row in sales_data:
    product_name, distributor_name, sales_quantity = row
    print(f"Product: {product_name}, Distributor: {distributor_name}, Sales Quantity: {sales_quantity}")

# Query to get employee work hours
print("\nEmployee Work Hours Report:")
cursor.execute("SELECT Name, SUM(HoursWorked) FROM Employees GROUP BY Name")
employee_hours_data = cursor.fetchall()
for Name, total_hours in employee_hours_data:
    print(f"{Name}: Total work hours = {total_hours}")

db_config.close()

