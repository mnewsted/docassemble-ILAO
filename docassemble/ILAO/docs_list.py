from docassemble.base.util import log, action_button_html, zip_file

def docs_list( doc_objects=[] ):
  '''Creates a Mako table with 'Download' and 'View' buttons for
    each doc given. How to use:
    
    ${ docs_list([ {label: 'First Document', doc: final_form}, {label: 'Cover page', doc: cover_page} ]) }
    
    @param docs_objects {list} A list of objects, each containing a `label` and `doc`.
    @param docs_objects[n] {object} The object containing the data for a row in the table.
    @param docs_objects[n].label {string} The name that will be listed for the document.
    @param docs_objects[n].doc {DAFileCollection} The document with which the user will interact.
  '''
  if not doc_objects:
    log( '`docs_list() did not get any documents. Please pass some in! Use: `${ docs_list([ {label: "Document", doc: final_form}, {label: "Cover page", doc: cover_page} ]) }' )
    return None
  
  # Header rows have to exist in order for the markdown to recognize it as a table. Hide it with css.
  header_hider = '<div class="ilao_header_hider" aria-hidden="true"></div>\n\n'
  rows = docs_list_top( 3 )
  docs_in_zip = []
  for doc_obj in doc_objects:
    rows += '\n' + docs_list_row( doc_obj["label"], doc_obj["doc"] )
    docs_in_zip.append(doc_obj["doc"])
  docs_zip_url = zip_file( docs_in_zip, filename="Easy Form files.zip").url_for(attachment=True)
  rows += '\n' + '**Get all your forms in a {.zip file :question-circle:}** | | ' + action_button_html( docs_zip_url, new_window=False, color="primary", label=":file-archive: Download" ) 
  return header_hider + rows

def docs_list_top( num_columns ):
  '''The top two rows are needed for markdown to recognize the
    following lines as a table.
    
    It also determines the alignment of the text in each column.
    At the moment, the left column is left aligned and all other
    columns are right aligned.
  '''
  right_headers = [' &nbsp; |'] * (num_columns - 2)
  header_row = '&nbsp; |' + ''.join( right_headers ) + ' &nbsp;\n'
  
  right_aligners = ['|-:'] * (num_columns - 1)
  algner_row = ':-' + ''.join( right_aligners )
  
  return header_row + algner_row

def docs_list_row( row_label='Document', doc=False ):
  '''Return a markdown string that can be used for a row in a table
     using the `row_label` in the very left column and adding
     the buttons in the right-hand columns.
  '''
  if doc is False:
    log( "No document was given to `docs_list_row()`. Use: `docs_list_row( 'First Document', doc1 )`" )
    return None
  
  # List of buttons on the right side
  # Data structure for a possible future development
  buttons = [
    action_button_html( doc.pdf.url_for(inline=True), new_window="True", color="success", label='<i class="far fa-eye"></i> View' ),
    action_button_html( doc.pdf.url_for(attachment=True), new_window=False, color="primary", label=":download: Download" )
  ]
  
  # Start with the row label then add all the buttons
  row_str = '<span class="ilao_doc_title">:file:&nbsp;&nbsp;' + row_label + '</span>'
  for button in buttons:
    row_str += ' | ' + button

  return row_str

def download_button( doc, label='Download :file-download:' ):
  '''The markdown string for a button that will download the
  given document in the same window.'''
  url = doc.pdf.url_for(attachment=True)
  return action_button_html( url, label=label, new_window=False, color="primary" )
  
  
def view_button( doc, label='View <i class="far fa-eye"></i>' ):
  '''The markdown string for a button that will show the
  given document in a new window.'''
  url = doc.pdf.url_for(inline=True)
  return action_button_html( url, label=label, new_window=True, color="primary" )
  
 
def docs_list_css():
  '''CSS styles for a markdown table that lists a
    set of documents and lets the user interact with them. '''
  
  return '''
  <style>
    .ilao_header_hider { display: none; } 
    .ilao_header_hider ~ div thead { display: none; }
    /*.table-striped tbody tr:nth-of-type(odd) { background-color: unset; } */
    td.text-right, th.text-right { width: 7em; }
    .table td, .table th  {
      padding: .4em;
      /* padding-bottom: .5em; */
      /* border-top: unset; */
      vertical-align: middle;
    }
    
    .ilao_doc_title{ font-weight: bold; }
    
    .table .btn-darevisit { margin-bottom: 0; }
    /*.table-striped tbody { background-color: rgb( 220, 220, 220 ); }*/  
  </style>
  '''