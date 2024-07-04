#function for cell red color
def set_cell_color_red(sheet, row, column):
        cell_range = f'{column}{row}'
        sheet.format(cell_range, {'backgroundColor': {'red': 1.0}})

#function for cell green color
def set_cell_color_green(sheet, row, column):
    cell_range = f'{column}{row}'
    sheet.format(cell_range, {'backgroundColor': {'green': 1.0}})

#if scale name not found green all cells of that object
def color_cells_a_google_sheet(obj, sheet):
    cell_found = False
    for row_index, row in enumerate(sheet.get_all_values()[1:], start=2):
        if obj.name == row[1] and obj.description == row[2] and obj.score == row[3] and obj.label == row[4] and obj.score_description == row[5]:
            cell_range = f'B{row_index}:F{row_index}'
            sheet.format(cell_range, {'backgroundColor': {'red': 1.0}})
            cell_found = True
            break
    if not cell_found:
        print("Object not found in the sheet.")