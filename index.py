import psutil
import math

import os 
from Levenshtein import distance as lev


class RunningProcesses:

  def __init__(self): 
      self.cache = []

  def get(self): 
    for proc in psutil.process_iter(): 
      self.cache.insert(0, (proc.name().lower(), proc.pid))
    return self.cache 

running_processes = RunningProcesses().get()

class ProcessMatchFinder:

  def __init__(self): 
    self.process_name = ''
    self.process_id = None 

  def find(self, process_to_find): 
    running_processes = RunningProcesses().get()
    current_process_name = ''
    current_process_id = None
    current_min = math.inf 

    for running_process in running_processes: 
      current_process_name = running_process[0]
      current_process_id = running_process[1]
      lev_distance = lev(process_to_find, current_process_name)
      if current_min > lev_distance:
        current_min = lev_distance
        self.process_name = current_process_name
        self.process_id = current_process_id
    return (self.process_name, self.process_id)


