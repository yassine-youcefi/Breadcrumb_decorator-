## Breadcrumb decorator for flask api

### importation :
```
from breadcrumb import breadcrumb

```

### Implementation :

- simple route:

```{ .python }
@ application.route('/my_route/')
@breadcrumb('my_route')
def my_route():

    # Do something
    return "something"
```

- route with variable:

```{ .python }
@ application.route('/my_route/my_slug')
@breadcrumb('my_route')
def my_route(my_slug):
    slug = my_slug

    @breadcrumb(my_slug)
    def call():
        return "Done"

    # for breadcrumb list

    call()

    # Do something
    return "something"
```
