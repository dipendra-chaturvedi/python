from pathlib import Path

project_folder = Path(__file__).parent

invoice_folder = project_folder / "invoices"

invoice_folder.mkdir(exist_ok=True)

invoice_file = invoice_folder / "INV-1001.txt"

invoice_file.write_text(
"""Invoice No : INV-1001
Customer   : Dipendra
Amount     : 25000
""",
encoding="utf-8"
)

print(invoice_file)


#Path()
#exists()
#mkdir()
#iterdir()
#rename()
#unlink()
#read_text()
#write_text()
#parent
#name
#suffix
#stem