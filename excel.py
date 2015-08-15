# Excel
# Author :      Nathan Krueger
# Created       11:45 AM 8/9/15
# Last Updated  12:10 PM 8/15/15
# Version       2.0

from openpyxl import *

file = None
sheet = None
#inclusion = [True,True,True,True,True,True]
#index = 1

#def file_exists(file_name, sheet_name)->bool:
    #'''attempts to open a file and sheet and returns True/False if it suceeds/fails'''
    #try:
        #file = load_workbook(file_name)
        #sheet = file.get_sheet_by_name(sheet_name)
        #file.save(file_name)
    #except:
        #return False
    #return True

def file_setup(data, file_name: str, sheet_name = '', sheet_index = 0)->None:
    '''sets up the files header row'''
    global file, sheet#, col_index
    #file = xlwt.Workbook()
    #sheet = file.add_sheet('Sheet{}'.format(sheet_index))
    try:
        file = load_workbook(file_name)
        sheet = file.create_sheet(title = sheet_name)
    except:
        #try:
            file = Workbook()
            sheet = file.active
            sheet.title = sheet_name
        #except:
            #print("Something went wrong...")
    sheet.cell(row = 1, column = 1).value = 'Word'
    sheet.cell(row = 1, column = 2).value = 'Rating.Mean'
    sheet.cell(row = 1, column = 3).value = 'Rating.SD'
    sheet.cell(row = 1, column = 4).value = 'SUBTL_WF'
    sheet.cell(row = 1, column = 5).value = 'Log_10(WF)'
    sheet.cell(row = 1, column = 6).value = 'SUBTL_CD'
    sheet.cell(row = 1, column = 7).value = 'Log_10(CD)'
    sheet.cell(row = 1, column = 8).value = 'Zeno.sfi'
    sheet.cell(row = 1, column = 9).value = 'Zeno.d'
    #sheet.write(0,0,'Word')
    #sheet.write(0,1,'Rating.Mean')
    #sheet.write(0,2,'Rating.SD')
    #sheet.write(0,3,'SUBTL_WF')
    #sheet.write(0,4,'Log_10(WF)')
    #sheet.write(0,5,'SUBTL_CD')
    #sheet.write(0,6,'Log_10(CD)')
    #sheet.write(0,7,'Zeno.sfi')
    #sheet.write(0,8,'Zeno.d')
    write_to_file(data)
    file.save(file_name)
    return

def write_to_file(data)->None:
    '''writes data to an excel file'''
    index = 2
    for word in data:
        sheet.cell(row = index, column = 1).value = word[0]
        sheet.cell(row = index, column = 2).value = word[3][1][3]
        sheet.cell(row = index, column = 3).value = word[3][1][4]
        sheet.cell(row = index, column = 4).value = word[3][3][4]
        sheet.cell(row = index, column = 5).value = word[3][3][5]
        sheet.cell(row = index, column = 6).value = word[3][3][6]
        sheet.cell(row = index, column = 7).value = word[3][3][7]
        sheet.cell(row = index, column = 8).value = word[3][4][0]
        sheet.cell(row = index, column = 9).value = word[3][4][1]
        #sheet.write(index,0,word[0])
        #sheet.write(index,1,word[3][1][3])
        #sheet.write(index,2,word[3][1][4])
        #sheet.write(index,3,word[3][3][4])
        #sheet.write(index,4,word[3][3][5])
        #sheet.write(index,5,word[3][3][6])
        #sheet.write(index,6,word[3][3][7])
        #sheet.write(index,7,word[3][4][0])
        #sheet.write(index,8,word[3][4][1])
        index += 1
    return

def write_nltk(data, sheet)->None:
    '''writes nltk data to the file'''
    return

def write_wordnet(data, sheet)->None:
    '''writes wordnet data to the file'''
    return

def write_excel_data(data, sheet)->None:
    '''writes excel data to the file'''
    return

def write_polys(data, sheet)->None:
    '''writes polysemy data to the file'''
    return

def write_mindep(data, sheet)->None:
    '''writes mindep data to the file'''
    return

def write_dtree(data, sheet)->None:
    '''writes dtree data to the file'''
    return
