import csv
import optparse
from xlsxwriter.workbook import Workbook
import os
#blockchair_bitcoin_blocks_20240129.tsv

parser = optparse.OptionParser()
parser.add_option(
    "-i",
    "--in",
    dest="input",
    help="pass the file name of the tsv -i or --in parameter yourfilename")

(opt, arg) = parser.parse_args()

if opt.input is not None:

    try:
        xlsx_file = 'output.xlsx'

        workbook = Workbook(xlsx_file)
        worksheet = workbook.add_worksheet()

        read_tsv = csv.reader(open(opt.input, 'r', encoding='utf-8'), delimiter='\t')

        for row, data in enumerate(read_tsv):
            worksheet.write_row(row, 0, data)
        pth = os.getcwd()
        workbook.close()
        print("[✅] Success ! file saved at", pth,"/output.xlsx")
    except(FileNotFoundError):
        print("[❌] Something went wrong ,Consider checking your file name as you passed",opt.input,"But it seems that the file does not exists")

else:
  print('''
      ------------------------------------------------------------\n
      Please pass the input as a filename using -i or --in then your filename \n
      -------------------------------------------------------------
      
      \n -i hellomom.tsv \t or \t --in hellomom.tsv''')
