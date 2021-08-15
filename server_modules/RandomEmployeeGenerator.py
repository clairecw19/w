"""
This is not part of the actual example app, it just generates fake data for the example to use.

generate_normalised() generates the data for the Grouping tutorial. 
generate_denormalised() generates the data for all other tutorials.
"""
import tables
from tables import app_tables
import anvil.server
import random
from datetime import datetime
from datetime import timedelta

TEAMS = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot']


@anvil.server.callable
def generate_normalised():
  """Generate separate Employees and Teams tables.
  
  NB: you'll need to set up the schema manually:
    - The 'teams' table needs a 'name' text column only.
    - The 'employees' table should have a link to the Teams table named 'team'.
  """
  app_tables.teams.delete_all_rows()
  for team in TEAMS:
    app_tables.teams.add_row(name=team)

  app_tables.employees.delete_all_rows()
  employees = anvil.http.request('https://randomuser.me/api/?results=60', json=True)['results']

  teams = [app_tables.teams.get(name=x) for x in TEAMS]

  for employee in employees:
    app_tables.employees.add_row(
      first_name=employee['name']['first'][0].upper() + employee['name']['first'][1:],
      last_name=employee['name']['last'][0].upper() + employee['name']['last'][1:],
      team=random.choice(teams),
      pay_grade=random.randint(0, 10),
    )
  

@anvil.server.callable
def generate_denormalised():
  """Generate some employees randomly.
  
  This assumes the 'teams' column is just a text column.
  """
  app_tables.employees.delete_all_rows()
  employees = anvil.http.request('https://randomuser.me/api/?results=60', json=True)['results']

  for employee in employees:
    app_tables.employees.add_row(
      first_name=employee['name']['first'][0].upper() + employee['name']['first'][1:],
      last_name=employee['name']['last'][0].upper() + employee['name']['last'][1:],
      team=random.choice(TEAMS),
      pay_grade=random.randint(0, 10),
    )
