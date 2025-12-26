import pandas as pd 
dict = {"name": ["Dorj", "Bat", "Byamba", "Bold", "Anar"],
         "gender":["M", "M", "F", "F", "M"],
         "salary":[100, 200, 100, 340, 500],
         "bd":["2000-12-11", "2001-12-15", "1976-5-3", "1992-2-12", "1999-9-9"]
         
          }
df = pd.DataFrame(dict)
print(df)