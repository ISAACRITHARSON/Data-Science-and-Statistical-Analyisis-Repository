threerows = [pd.Series([55,55,55,'LPG',55,5,1,55,5,1155], index=df.columns )
,
pd.Series([65,65,65,'Petrol',65,6,0,65,6,1166], index=df.columns
) ,
pd.Series([75,75,75,'Diesel',75,7,1,75,7,1177], index=df.columns
) ]
modified = df.append(threerows)
modified.tail(5)
