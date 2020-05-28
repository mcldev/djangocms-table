import json

class TableCell:
    def __init__(self, *args, **kwargs):
        if args:
            self.value = args[0]
        if 'value' in kwargs:
            self.cells = kwargs['cells']
        if 'is_header_row' in kwargs:
            self.is_header_row = kwargs['is_header_row']
        if 'is_footer_row' in kwargs:
            self.is_footer_row = kwargs['is_footer_row']
        if 'classes' in kwargs:
            self.classes = kwargs['classes']


    value = ''
    is_merged = False
    is_header_cell = False
    style = ''
    merge_span = ''
    classes = ''

class TableRow:

    def __init__(self, *args, **kwargs):
        if 'cells' in kwargs:
            self.cells = kwargs['cells']
        if 'is_header_row' in kwargs:
            self.is_header_row = kwargs['is_header_row']
        if 'is_footer_row' in kwargs:
            self.is_footer_row = kwargs['is_footer_row']
        if 'classes' in kwargs:
            self.classes = kwargs['classes']

    # Cells in each row
    cells=[]

    #Is header or footer row
    is_header_row = False
    is_footer_row = False
    open_row_headers = True
    close_row_headers = True

    #Row classes - header footer etc.
    classes = ''


class TableView:

    #Jagged Array of cells
    rows = []
    classes = ''
    error_message = ''

    # Settings
    mergeCells = None
    alignment = None

    max_rows = None
    max_cols = None

    def __init__(self, table_instance):
        self.table_instance = table_instance
        self.classes = self.table_instance.table_classes
        self.get_rows_from_instance()


    def set_max_row_col(self):
        # exit if nothing returned
        if self.rows:
            self.max_rows = len(self.rows)
            # For each row/col/cell
            self.max_cols = max(len(row.cells) for row in self.rows)

    def get_rows_from_instance(self):

        # Get Cell values
        self.get_cell_values()

        # exit if nothing returned
        if self.rows:

            self.set_max_row_col()

            curr_row_type = None
            prev_row_type = None

            # For each row/col/cell
            for row_idx, row in enumerate(self.rows):
                # Header / Footer Row Classes
                if row_idx < self.table_instance.header_rows_top:
                    row.classes = self.table_instance.header_row_classes
                    row.is_header_row = True
                elif row_idx >= self.num_rows() - self.table_instance.footer_rows:
                    row.classes = self.table_instance.footer_row_classes
                    row.is_footer_row = True
                else:
                    row.classes = self.table_instance.body_row_classes


                #Set Flag whether to use Row Headers - thead, tfooter, tbody
                curr_row_type = 'header' if row.is_header_row else 'footer' if row.is_footer_row else 'body'
                row.open_row_headers = not curr_row_type == prev_row_type
                if row_idx > 0:
                    self.rows[row_idx - 1].close_row_headers =  not curr_row_type == prev_row_type
                prev_row_type = curr_row_type


                # Header / Footer Cell Classes
                for col_idx, cell in enumerate(row.cells):
                    if row_idx < self.table_instance.header_rows_top or col_idx < self.table_instance.header_rows_left:
                        cell.classes = self.table_instance.header_cell_classes
                        cell.is_header_cell = True
                    else:
                        cell.classes = self.table_instance.cell_classes

        #Load Settings from table_settings
        self.get_settings()

        # Merged Cells
        if self.mergeCells:
            for merge in self.mergeCells:
                start_row = merge['row']
                start_col = merge['col']
                row_span =  merge['rowspan']
                col_span = merge['colspan']
                # TODO - Review this as HandsonTable are about to release fix for merge cells info
                # https://github.com/handsontable/handsontable/issues/3473
                merged_rows = range(start_row, min(self.max_rows, start_row + row_span))
                merged_cols = range(start_col, min(self.max_cols, start_col + col_span))
                for r in merged_rows:
                    for c in merged_cols:
                        self.rows[r].cells[c].is_merged = True

                self.rows[start_row].cells[start_col].is_merged = False
                self.rows[start_row].cells[start_col].merge_span = " colspan={} rowspan={} ".format(col_span, row_span)

        if self.alignment:
            for cls in self.alignment:
                # text-align: left center right justify
                # vertical-align: top middle bottom
                align_style = str(cls['className']).replace("htLeft", "text-align: left; ")\
                                                    .replace("htCenter", "text-align: center; ") \
                                                    .replace("htRight", "text-align: right; ")\
                                                    .replace("htJustify", "text-align: justify; ") \
                                                    .replace("htTop", "vertical-align: top; ") \
                                                    .replace("htMiddle", "vertical-align: middle; ") \
                                                    .replace("htBottom", "vertical-align: bottom; ")
                self.rows[cls['row']].cells[cls['col']].style = "style='%s'" % align_style


    def get_cell_values(self):
        try:
            data = json.loads(self.table_instance.table_data)
            if data:
                # Get all cell Values
                self.rows = [TableRow(cells=[TableCell(val) for val in row]) for row in data]

        except Exception as err:
            self.error_message = str(err)

    def num_rows(self):
        return len(self.rows)


    def get_settings(self):
        try:
            settings = json.loads(self.table_instance.table_settings)
            if settings:
                self.mergeCells = settings['mergeCells']
                self.alignment = settings['alignment']
        except Exception as err:
            self.error_message = str(err)

