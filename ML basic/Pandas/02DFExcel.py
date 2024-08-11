import pandas

file = pandas.ExcelFile("courses.xlsx")
df = file.parse("Sheet1")
print(df)
