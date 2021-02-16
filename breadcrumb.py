import functools
import collections

import flask

BreadCrumb = collections.namedtuple('BreadCrumb', ['path', 'title'])


def breadcrumb(view_title):
    def decorator(f):
        @functools.wraps(f)
        def decorated_function(*args, **kwargs):
            # Put title into flask.g so views have access and
            # don't need to repeat it
            flask.g.title = view_title

            # Also put previous breadcrumbs there, ready for view to use
            session_crumbs = flask.session.setdefault('crumbs', [])

            # Now add the request path and title for that view
            # to the list of crumbs we store in the session.
            flask.session.modified = True

            item = (flask.request.path, view_title)
            try:
                if item in session_crumbs:
                    index = session_crumbs.index(item)

                    session_crumbs = session_crumbs[:index+1]

                else:
                    session_crumbs.append(item)
                    # print("seesion crud ---", session_crumbs)

            except:
                pass

            if len(session_crumbs) > 4:
                if session_crumbs[0] == ("/", "Home"):
                    session_crumbs.pop(1)
                else:
                    session_crumbs.pop(0)

            flask.g.breadcrumbs = []
            for path, title in session_crumbs:
                flask.g.breadcrumbs.append(BreadCrumb(path, title))

            # Call the view
            rv = f(*args, **kwargs)

            # Only keep most recent crumbs (number should be configurable)

            return rv
        return decorated_function
    return decorator

