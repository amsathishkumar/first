import pandas as pds
# Reference : https://hackersandslackers.com/compare-rows-pandas-dataframes/
file =('D:\\satpython\\bb.xls') 
cols =  [0,2,3,4,5]
cols1 = [0,1,3,7,9]

newData = pds.read_excel(file)
sheet1 = pds.read_excel(file,  
                        sheet_name = 'US',  
                         usecols=cols,skiprows=[0]) 
  
sheet2 = pds.read_excel(file,  
                        sheet_name = 'Europe',  
                        usecols=cols,skiprows=[0]) 
  
sheet3 = pds.read_excel(file,  
                        sheet_name = 'MENA',  
                        usecols=cols,skiprows=[0]) 
sheet4 = pds.read_excel(file,  
                        sheet_name = 'Africa',  
                        usecols=cols,skiprows=[0]) 
sheet5 = pds.read_excel(file,  
                        sheet_name = 'APAC',  
                        usecols=cols,skiprows=[0])

newData = pds.concat([sheet1,sheet2,sheet3,sheet4,sheet5]) 
newData = newData.applymap(lambda x: x.strip() if isinstance(x, str) else x)
newData = newData.apply(lambda x: x.astype(str).str.upper())
newData.dropna()


file1 =('D:\\satpython\\file.csv') 
sysdata = pds.read_csv(file1,usecols=cols1)
sysdata = sysdata.applymap(lambda x: x.strip() if isinstance(x, str) else x)#Remove leading and trailing spaces
sysdata = sysdata.apply(lambda x: x.astype(str).str.upper())#convert to upper
sysdata.dropna() #remove empty row

missing = sysdata.merge(newData, indicator=True, how='outer')
 #left_only/right_only/both. 
diff_df = missing[missing['_merge'] != 'left_only']


diff_df.to_csv('D:\\satpython\\missing.csv')
sysdata.to_csv('D:\\satpython\\sysdata.csv')
newData.to_csv('D:\\satpython\\newData.csv')

# diff_df.to_html('D:\\satpython\\missing.html')

r =" "
for i, j in diff_df.iterrows(): 
    for k in diff_df.columns:
       r = r + str(j[k]);
    print(r)
    r=" "

