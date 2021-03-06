"""
    sphinx.builders.htmlhelp
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Build HTML help support files.
    Parts adapted from Python's Doc/tools/prechm.py.

    :copyright: Copyright 2007-2019 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import warnings

from sphinxcontrib.htmlhelp import (
    chm_locales, chm_htmlescape, HTMLHelpBuilder, default_htmlhelp_basename
)

from sphinx.deprecation import RemovedInSphinx40Warning, deprecated_alias


if False:
    # For type annotation
    from typing import Any, Dict  # NOQA
    from sphinx.application import Sphinx  # NOQA


deprecated_alias('sphinx.builders.htmlhelp',
                 {
                     'chm_locales': chm_locales,
                     'chm_htmlescape': chm_htmlescape,
                     'HTMLHelpBuilder': HTMLHelpBuilder,
                     'default_htmlhelp_basename': default_htmlhelp_basename,
                 },
                 RemovedInSphinx40Warning)


def setup(app):
    # type: (Sphinx) -> Dict[str, Any]
    warnings.warn('sphinx.builders.htmlhelp has been moved to sphinxcontrib-htmlhelp.',
                  RemovedInSphinx40Warning)
    app.setup_extension('sphinxcontrib.htmlhelp')

    return {
        'version': 'builtin',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
