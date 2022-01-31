import pandas as pd
file = pd.read_csv('Highest Holywood Grossing Movies.csv')
print(file.columns)
file = file.drop(columns=["Movie Info", 'Unnamed: 0'])
print(file.head())
# Slicing a dataframe
# Sort first
studio = file.set_index(["Distributor", "Title"]).sort_index()
warner = studio.loc[["Warner Bros."]]
print(warner.head())
warner_sales = warner.loc[:, "Domestic Sales":"World Sales"]
print(warner_sales.head())
# SLicing/subsetting dates
file["year"] = file["Release Date"].str.contains("2013")
thirteen = file[file["year"] == True]
print(thirteen)
thirteen = thirteen.set_index("Title").sort_index
high_gross_13 = thirteen.sort_values("World Sales", ascending=False)
high_gross_13 = high_gross_13[:,"Domestic Sales":"World Sales"]
print(high_gross_13.head())
studiopivot = file.pivot_table("World Sales", index="Distibutor", columns="World sales")
print(studiopivot)


