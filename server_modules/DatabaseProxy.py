import tables
from tables import app_tables
import anvil.server


@anvil.server.callable
def get_employees():
  return app_tables.employees.search()
