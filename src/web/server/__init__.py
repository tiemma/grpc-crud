
from flask_restplus import Api

from server.user import USER_NS

api = Api(title="Stack Overflow Lite",
          description="""
          This is where the rest endpoints for the application is defined.
          Multiple namespaces have been placed here for ease of reach
          """,
          prefix="/api/v1",
          version="1.0")

api.add_namespace(USER_NS)