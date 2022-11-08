import pandas as pd

inputFilePath = "Self_Care_Project_DB - Resource_DB.csv"

database = pd.read_csv(inputFilePath)
database = database.fillna('')

output_json_str = "{"
for i in range(0,len(database)):

    entry_str = f'"{i}":'+str("{")
    entry_str+=f'"Resource_ID":"{database.loc[i][0]}",'
    entry_str+=f'"Domain_ID":"{database.loc[i][1]}",'
    entry_str+=f'"Domain":"{database.loc[i][2]}",'
    entry_str+=f'"Resource_Name":"{database.loc[i][3]}",'
    entry_str+=f'"Resource_Description":"{database.loc[i][4]}",'
    entry_str+=f'"Resource_type":"{database.loc[i][5]}",'
    entry_str+=f'"Resource_Redirect_URL":"{database.loc[i][6]}",'
    entry_str+=f'"Category":"{database.loc[i][7]}",'
    entry_str+=f'"Resource_icon":"{database.loc[i][8]}"'
    
    if i == len(database)-1:
        entry_str+= "}"
    else:
        entry_str+= "},"
    output_json_str+=entry_str

output_json_str += "}"
outputFile_path = str('Converted_Database.json')
print(outputFile_path)

with open(outputFile_path,"a+") as outputFile:
    outputFile.write(output_json_str)