# Excel
# Author :      Nathan Krueger
# Created       11:45 AM 8/9/15
# Last Updated  0:00 PM 8/9/15
# Version       0.1

import xlrd
import xlwt

file = None
sheet = None
#inclusion = [True,True,True,True,True,True]
#index = 1

def file_setup(data, file_name: str, sheet_index: int)->None:
    '''sets up the files header row'''
    global file, sheet#, col_index
    file = xlwt.Workbook()
    sheet = file.add_sheet('Sheet1')
    sheet.write(0,0,'Word')
    sheet.write(0,1,'Rating.Mean')
    sheet.write(0,2,'Rating.SD')
    sheet.write(0,3,'SUBTL_WF')
    sheet.write(0,4,'Log_10(WF)')
    sheet.write(0,5,'SUBTL_CD')
    sheet.write(0,6,'Log_10(CD)')
    sheet.write(0,7,'Zeno.sfi')
    sheet.write(0,8,'Zeno.d')
    write_to_file(data)
    file.save(file_name)
    return

def write_to_file(data)->None:
    '''writes data to an excel file'''
    index = 1
    for word in data:
        sheet.write(index,0,word[0])
        sheet.write(index,1,word[3][1][3])
        sheet.write(index,2,word[3][1][4])
        sheet.write(index,3,word[3][3][4])
        sheet.write(index,4,word[3][3][5])
        sheet.write(index,5,word[3][3][6])
        sheet.write(index,6,word[3][3][7])
        sheet.write(index,7,word[3][4][0])
        sheet.write(index,8,word[3][4][1])
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
