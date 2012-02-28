project = u'Sepia -- Notes on the test lab for the Ceph project'
copyright = u'2012, New Dream Network'
version = 'dev'
release = 'dev'

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['**/.#*', '**/*~', 'virtualenv']
pygments_style = 'sphinx'

html_theme = 'sepia'
html_theme_path = ['_themes']
html_title = project
#html_logo = 'logo.jpg'
html_favicon = 'favicon.ico'
html_use_smartypants = True
html_show_sphinx = False
html_sidebars = {
    '**': ['smarttoc.html', 'searchbox.html'],
    }

extensions = [
    'sphinx.ext.graphviz',
    'sphinx.ext.todo',
    ]
todo_include_todos = True
graphviz_output_format = 'svg'
