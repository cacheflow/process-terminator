import psutil
import re
import hashlib
import pdb
import math
import os
import click
from Levenshtein import distance as lev

def hash_process_name(process_name):
  return hashlib.sha1(process_name.encode("utf-8")).hexdigest()


class RunningProcesses:

  def __init__(self): 
      self.cache = []

  def get(self): 
    for proc in psutil.process_iter(): 
      self.cache.insert(0, (proc.name().lower(), proc.pid))
    return self.cache 

class ProcessMatchFinder:

  def __init__(self):
    self.found_exact_match = False
    self.process_names = set()
    self.process_id = None 

  def find(self, process_to_find): 
    running_processes = RunningProcesses().get()
    current_process_name = ''
    current_process_id = None
    current_min = math.inf

    for running_process in running_processes: 
      current_process_name = running_process[0]
      current_process_id = running_process[1]
      search_str = r"\b" + process_to_find + r"\b"
      match_output = re.search(search_str, current_process_name)
      if match_output is not None:
        self.process_names.add(current_process_name.strip())


@click.command()
@click.argument('process_name')
def run(process_name = ''):
  if not process_name:
    print('No process name given')
    return None
  ProcessMatchFinder().find(process_name)

if __name__ == "__main__":
  run()

