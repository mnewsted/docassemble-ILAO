import pandas
from docassemble.base.util import path_and_mimetype

__all__ = ['get_easy_forms_names', 'easy_forms_info']

easy_forms_info_by_name = {}
easy_forms_names = []


def read_data(filename):
    the_xlsx_file, mimetype = path_and_mimetype(filename)  # pylint: disable=unused-variable
    df = pandas.read_excel(the_xlsx_file)
    for indexno in df.index:
        if not df['name'][indexno]:
            continue
        easy_forms_names.append(df['name'][indexno])
        easy_forms_info_by_name[df['name'][indexno]] = {"url": df['url'][indexno]}


def get_easy_forms_names():
    return easy_forms_names


def easy_forms_info(easy_forms):
    if easy_forms not in easy_forms_info_by_name:
        raise Exception("Reference to invalid Easy Form " + easy_forms)
    return easy_forms_info_by_name[easy_forms]

read_data('docassemble.ILAO:data/sources/ilao_docassemble_easy_forms.xlsx')
