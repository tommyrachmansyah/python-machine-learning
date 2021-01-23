from modelling.classification.routes import classification_route

app_routes = [
    classification_route
]

all_routes = []
for route in app_routes:
    all_routes.extend(route)