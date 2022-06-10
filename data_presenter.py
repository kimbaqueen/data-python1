# 2
open_cupcake_file = open("CupcakeInvoices.csv")

# 3
# for row in open_cupcake_file:
#     print(row)

# 4
# for row in open_cupcake_file:
#     flavors = row.split(",")
#     print(flavors[2])

# 5
# for row in open_cupcake_file:
#     values = row.split(",")
#     total = int(values[3]) * float(values[4])
#     print(total)

# 6
grand_total = 0
for row in open_cupcake_file:
    values = row.split(",")
    grand_total = grand_total + (int(values[3]))*float(values[4])
print(grand_total)

# 7
open_cupcake_file.close()
