import openpyxl


# class for reading excel
class ReadExcel:
    # reading excel file
    path = "/Users/vasanp/PycharmProjects/pythonProject/API_MainAssignment/testdata/testdata.xlsx"
    book = openpyxl.load_workbook(path)

    # module for return sheet name
    def read_excel(self):
        sheet = self.book['Sheet1']
        return sheet

    # module for saving excel file
    def save_excel(self):
        self.book.save(self.path)
