import logging
from pathlib import Path

project_folder = Path(__file__).parent

log_file = project_folder / "employee.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

employee_id = 101

logging.info(f"Employee {employee_id} logged in")
logging.warning(f"Employee {employee_id} entered wrong password once")
logging.error(f"Database connection failed")

#logging.basicConfig()
#logging.info()
#logging.warning()
#logging.error()
#logging.debug()
#logging.critical()