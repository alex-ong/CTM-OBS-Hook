import os
#run "pip install pyexcel-ods" first
from pyexcel_ods import get_data
FILE = 'restream-export.ods'

#this function writes a value to a file.
def ExportData(filename, value):
    with open(filename, 'w') as f:
        f.write(value)
    
def ExportRow(folderName, r):
    os.makedirs(folderName)
    
    ExportData(folderName+'match_name.txt', 
                r[0] + r[1] + 'Match: ' + r[2])
    #player 1
    ExportData(folderName+'player1_name.txt',
                r[3])
    
    ExportData(folderName+'player1_seed.txt',
                r[4])
                
    ExportData(folderName+'player1_pronoun.txt',
                r[5])
                
    ExportData(folderName+'player1_style.txt',
                r[6])
    
    #player 2
    ExportData(folderName+'player2_name.txt',
                r[8])
    
    ExportData(folderName+'player2_seed.txt',
                r[9])
                
    ExportData(folderName+'player2_pronoun.txt',
                r[10])
                
    ExportData(folderName+'player2_style.txt',
                r[11])
                
if __name__ == '__main__':
    data = get_data(FILE)

    sheet = data['Now']

    first_row = sheet[0]
    r = sheet[1] #second_row
    print(first_row)

    # lets export some stuff

    # make sure our export directory exists.
    ExportRow('export/0/', sheet[1]) #second row

