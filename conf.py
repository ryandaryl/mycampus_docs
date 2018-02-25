# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from datetime import datetime

from recommonmark.parser import CommonMarkParser

print('Hello World')

extensions = []
templates_path = ['/home/docs/checkouts/readthedocs.org/readthedocs/templates/sphinx', 'templates', '_templates', '.templates']
source_suffix = ['.rst', '.md']		
source_parsers = {		
            '.md': CommonMarkParser,		
        }
master_doc = 'index'
project = u'mycampus_docs'
copyright = str(datetime.now().year)
version = 'latest'
release = 'latest'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
htmlhelp_basename = 'mycampus-docs'
html_theme = 'sphinx_rtd_theme'
file_insertion_enabled = False
latex_documents = [
  ('index', 'mycampus-docs.tex', u'mycampus_docs Documentation',
   u'', 'manual'),
]




###########################################################################
#          auto-created readthedocs.org specific configuration            #
###########################################################################


#
# The following code was added during an automated build on readthedocs.org
# It is auto created and injected for every build. The result is based on the
# conf.py.tmpl file found in the readthedocs.org codebase:
# https://github.com/rtfd/readthedocs.org/blob/master/readthedocs/doc_builder/templates/doc_builder/conf.py.tmpl
#


import sys
import os.path
from six import string_types

from sphinx import version_info

# Get suffix for proper linking to GitHub
# This is deprecated in Sphinx 1.3+,
# as each page can have its own suffix
if globals().get('source_suffix', False):
    if isinstance(source_suffix, string_types):
        SUFFIX = source_suffix
    else:
        SUFFIX = source_suffix[0]
else:
    SUFFIX = '.rst'

# Add RTD Static Path. Add to the end because it overwrites previous files.
if not 'html_static_path' in globals():
    html_static_path = []
if os.path.exists('_static'):
    html_static_path.append('_static')
html_static_path.append('/home/docs/checkouts/readthedocs.org/readthedocs/templates/sphinx/_static')

# Add RTD Theme only if they aren't overriding it already
using_rtd_theme = False
if 'html_theme' in globals():
    if html_theme in ['default']:
        # Allow people to bail with a hack of having an html_style
        if not 'html_style' in globals():
            import sphinx_rtd_theme
            html_theme = 'sphinx_rtd_theme'
            html_style = None
            html_theme_options = {}
            if 'html_theme_path' in globals():
                html_theme_path.append(sphinx_rtd_theme.get_html_theme_path())
            else:
                html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

            using_rtd_theme = True
else:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_style = None
    html_theme_options = {}
    if 'html_theme_path' in globals():
        html_theme_path.append(sphinx_rtd_theme.get_html_theme_path())
    else:
        html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    using_rtd_theme = True

if globals().get('websupport2_base_url', False):
    websupport2_base_url = 'https://readthedocs.org/websupport'
    if 'http' not in settings.MEDIA_URL:
        websupport2_static_url = 'https://media.readthedocs.org/static/'
    else:
        websupport2_static_url = 'https://media.readthedocs.org//static'


#Add project information to the template context.
context = {
    'using_theme': using_rtd_theme,
    'html_theme': html_theme,
    'current_version': "latest",
    'version_slug': "latest",
    'MEDIA_URL': "https://media.readthedocs.org/",
    'PRODUCTION_DOMAIN': "readthedocs.org",
    'versions': [
    ("latest", "/en/latest/"),
    ],
    'downloads': [ 
    ("pdf", "//readthedocs.org/projects/mycampus-docs/downloads/pdf/latest/"),
    ("htmlzip", "//readthedocs.org/projects/mycampus-docs/downloads/htmlzip/latest/"),
    ("epub", "//readthedocs.org/projects/mycampus-docs/downloads/epub/latest/"),
    ],
    'subprojects': [ 
    ],
    'slug': 'mycampus-docs',
    'name': u'mycampus_docs',
    'rtd_language': u'en',
    'programming_language': u'py',
    'canonical_url': 'http://mycampus-docs.readthedocs.io/en/latest/',
    'analytics_code': 'None',
    'single_version': False,
    'conf_py_path': '/./',
    'api_host': 'https://readthedocs.org',
    'github_user': 'ryandaryl',
    'github_repo': 'mycampus_docs',
    'github_version': 'master',
    'display_github': True,
    'bitbucket_user': 'None',
    'bitbucket_repo': 'None',
    'bitbucket_version': 'master',
    'display_bitbucket': False,
    'gitlab_user': 'None',
    'gitlab_repo': 'None',
    'gitlab_version': 'master',
    'display_gitlab': False,
    'READTHEDOCS': True,
    'using_theme': (html_theme == "default"),
    'new_theme': (html_theme == "sphinx_rtd_theme"),
    'source_suffix': SUFFIX,
    'user_analytics_code': '',
    'global_analytics_code': 'UA-17997319-1',
    
    'commit': 'fbe530ff',
    
}




if 'html_context' in globals():
    html_context.update(context)
else:
    html_context = context

# Add custom RTD extension
if 'extensions' in globals():
    extensions.append("readthedocs_ext.readthedocs")
else:
    extensions = ["readthedocs_ext.readthedocs"]

print(os.system('echo $PWD'))
print(os.system('ls'))
os.system('sphinx-apidoc -f -o . .')
