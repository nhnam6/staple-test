from cmd.elasticsearch_cmd import register_commands as register_es_commands
from cmd.load_salary_survey_cmd import (
    register_commands as register_load_salary_commands,
)

import graphene
from flask import Flask
from graphql_server.flask import GraphQLView

from api.graph.queries.query import Query
from api.rest.healthcheck.routes import health as health_routes
from logger.logger import logger


def create_schema():
    return graphene.Schema(query=Query, mutation=None)


def create_app():
    """
    This function creates and configures a new Flask application instance.

    Returns:
        app: A Flask application instance.
    """
    app = Flask(__name__)
    # Register routes
    app.register_blueprint(health_routes)

    # Add logger
    app.logger.addHandler(logger)

    # Register commands
    register_es_commands(app)
    register_load_salary_commands(app)

    # Register GraphQL endpoint
    schema = create_schema()
    app.add_url_rule(
        "/graphql",
        view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True),
    )
    return app
