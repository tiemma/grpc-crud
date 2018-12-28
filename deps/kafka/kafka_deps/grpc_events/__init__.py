from uuid import uuid1

from proto.Event_pb2 import Event, EventResponse

from proto.Event_pb2_grpc import CreateEventServiceServicer

class CreateEvent(CreateEventServiceServicer):
    """

    """

    logger = Logger.get_logger(__name__)

    def CreateEvent(self, request, context):
        """

        :param request:
        :param context:
        """
        self.logger.debug('Creating response body to be used in publishing events with request %r and context %r', request, context)
        return Event(id=str(uuid1()),
                     event_type=request.event_type,
                     event_body=request.data)


