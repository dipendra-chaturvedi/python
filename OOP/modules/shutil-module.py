import shutil
from pathlib import Path

project_folder = Path(__file__).parent

source = project_folder / "employee.db"
backup = project_folder / "backup" / "employee_backup.db"

backup.parent.mkdir(exist_ok=True)

shutil.copy2(source, backup)

print("Database Backup Created")


#copy()          # Copy file
#copy2()         # Copy with metadata
#copytree()      # Copy folder
#move()          # Move file/folder
#rmtree()        # Delete folder recursively
#make_archive()  # Create ZIP archive