from anvil import *
import tables
from tables import app_tables
import anvil.server

class Form1(Form1Template):
  

  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
#    anvil.server.call('generate_denormalised')
    self.repeating_panel_employees.items = anvil.server.call('get_employees')

  def text_box_1_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.data_grid_employees.rows_per_page = int(self.text_box_1.text) + 1

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass
  
  
  def radio_button_1_clicked(self, **event_args):
    self.message1.text = 'Participant A chose ' + self.rb11.text + '.'
    """This method is called when this radio button is selected"""
   
   
    pass

  def radio_button_2_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    self.message1.text = 'Participant A chose ' + self.rb12.text + '.'
   
    pass
 
  
  def rb21_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
 
    self.message2.text = 'Participant B chose ' + self.rb21.text + '.'
    pass

  def rb22_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    self.message2.text = 'Participant B chose ' + self.rb22.text + '.'
    
    pass

  def button_click(self, **event_args):
    """This method is called when the button is clicked"""
  
    if (self.rb11.selected == True) and (self.rb21.selected == True):
      self.message3.text = 'Participant A: 3 (R), Participant B: 3 (R)'
    if (self.rb11.selected == True) and (self.rb22.selected == True):
      self.message3.text = 'Participant A: 0 (S), Participant B: 5 (T)'
    if (self.rb12.selected == True) and (self.rb21.selected == True):
      self.message3.text = 'Participant A: 5 (T), Participant B: 0 (S)'
    if (self.rb12.selected == True) and (self.rb22.selected == True):
      self.message3.text = 'Participant A: 1 (P), Participant B: 1 (P)'
    pass

  def message3_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    self.message3.bold = True
    self.message3.font_size = 18
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  
  







