# Excel
# Author :      Nathan Krueger
# Created       11:45 AM 8/9/15
# Last Updated  2:50 PM 8/18/15
# Version       2.5

from openpyxl import *

file = None
sheet = None

def file_setup(data, file_name: str, sheet_name = '', sheet_index = 0)->None:
    '''sets up the files header row'''
    global file, sheet
    try: #file exists, add a new sheet
        file = load_workbook(file_name)
        sheet = file.create_sheet(title = sheet_name)
    except: #file does not exist, rename first sheet
        file = Workbook()
        sheet = file.active
        sheet.title = sheet_name
    if len(data[0]) == 11:
        polys_mindep_setup(data)
    else:
        excel_based_setup(data)
    file.save(file_name)
    return

def polys_mindep_setup(data)->None:
    '''sets up a polys data spreadsheet'''
    sheet.cell(row = 1, column = 1).value = 'Word'
    sheet.cell(row = 1, column = 2).value = 'polys.noun'
    sheet.cell(row = 1, column = 3).value = 'polys.adj'
    sheet.cell(row = 1, column = 4).value = 'polys.sat_adj'
    sheet.cell(row = 1, column = 5).value = 'polys.adv'
    sheet.cell(row = 1, column = 6).value = 'polys.verb'
    sheet.cell(row = 1, column = 7).value = 'mindep.noun'
    sheet.cell(row = 1, column = 8).value = 'mindep.adj'
    sheet.cell(row = 1, column = 9).value = 'mindep.sat_adj'
    sheet.cell(row = 1, column = 10).value = 'mindep.adv'
    sheet.cell(row = 1, column = 11).value = 'mindep.verb'
    write_polys_mindep(data)
    return

def excel_based_setup(data)->None:
    '''sets up a spreadsheet based on excel data'''
    sheet.cell(row = 1, column = 1).value = 'Word'
    sheet.cell(row = 1, column = 2).value = 'Rating.Mean'
    sheet.cell(row = 1, column = 3).value = 'Rating.SD'
    sheet.cell(row = 1, column = 4).value = 'SUBTL_WF'
    sheet.cell(row = 1, column = 5).value = 'Log_10(WF)'
    sheet.cell(row = 1, column = 6).value = 'SUBTL_CD'
    sheet.cell(row = 1, column = 7).value = 'Log_10(CD)'
    sheet.cell(row = 1, column = 8).value = 'Zeno.sfi'
    sheet.cell(row = 1, column = 9).value = 'Zeno.d'
    write_excel(data)
    return

def write_excel(data)->None:
    '''writes excel data to an excel file'''
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
        index += 1
    return

def write_polys_mindep(data)->None:
    '''writes polysemy data to the file'''
    index = 2
    for word in data:
        sheet.cell(row = index, column = 1).value = word[0]
        sheet.cell(row = index, column = 2).value = word[1]
        sheet.cell(row = index, column = 3).value = word[2]
        sheet.cell(row = index, column = 4).value = word[3]
        sheet.cell(row = index, column = 5).value = word[4]
        sheet.cell(row = index, column = 6).value = word[5]
        sheet.cell(row = index, column = 7).value = word[6]
        sheet.cell(row = index, column = 8).value = word[7]
        sheet.cell(row = index, column = 9).value = word[8]
        sheet.cell(row = index, column = 10).value = word[9]
        sheet.cell(row = index, column = 11).value = word[10]
        index += 1
    return
