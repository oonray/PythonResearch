import epicCSV as CSV

data = CSV.read_csv_data("etterspørsel.csv")
index = CSV.get_index(data,";")

print(index)
