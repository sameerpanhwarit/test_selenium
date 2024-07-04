#function for cell red color
def set_cell_color_red(sheet, row, column):
        row = row+1
        cell_range = f'{column}{row}'
        sheet.format(cell_range, {'backgroundColor': {'red': 1.0}})

#function for cell green color
def set_cell_color_green(sheet, row, column):
    row = row+1
    cell_range = f'{column}{row}'
    sheet.format(cell_range, {'backgroundColor': {'green': 1.0}})

#if scale name not found green all cells of that object
def color_cells_a_google_sheet(obj, sheet):
    cell_found = False
    for row_index, row in enumerate(sheet.get_all_values()[1:], start=2):
        if obj.id == row[1] and obj.listName == row[2] and obj.item == row[3]:
            cell_range = f'B{row_index}:D{row_index}'
            sheet.format(cell_range, {'backgroundColor': {'red': 1.0}})
            cell_found = True
            break
    if not cell_found:
        print("Object not found in the sheet.")