import docassemble.base.util

def ilao_name_suffix(**kwargs):
    return ['Jr', 'Junior', 'Sr', 'Senior', 'II', 'III', 'IV', 'V', 'VI']
  
docassemble.base.util.update_language_function('*', 'name_suffix', ilao_name_suffix)