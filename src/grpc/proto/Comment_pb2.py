# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Comment.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import src.grpc.proto.Helpers_pb2 as Helpers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Comment.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rComment.proto\x1a\rHelpers.proto\"A\n\x07\x43omment\x12\x15\n\x06userId\x18\x01 \x01(\x0b\x32\x05.UUID\x12\x0e\n\x06header\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\"\x7f\n\x0f\x43ommentResponse\x12\x11\n\x02id\x18\x01 \x01(\x0b\x32\x05.UUID\x12\x19\n\x07\x63omment\x18\x02 \x01(\x0b\x32\x08.Comment\x12\x1e\n\ncreated_at\x18\x03 \x01(\x0b\x32\n.Timestamp\x12\x1e\n\nupdated_at\x18\x04 \x01(\x0b\x32\n.Timestamp2<\n\rCreateComment\x12+\n\rCreateComment\x12\x08.Comment\x1a\x10.CommentResponseb\x06proto3')
  ,
  dependencies=[Helpers__pb2.DESCRIPTOR,])




_COMMENT = _descriptor.Descriptor(
  name='Comment',
  full_name='Comment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='Comment.userId', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='header', full_name='Comment.header', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='Comment.content', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=97,
)


_COMMENTRESPONSE = _descriptor.Descriptor(
  name='CommentResponse',
  full_name='CommentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='CommentResponse.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comment', full_name='CommentResponse.comment', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='CommentResponse.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='CommentResponse.updated_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=226,
)

_COMMENT.fields_by_name['userId'].message_type = Helpers__pb2._UUID
_COMMENTRESPONSE.fields_by_name['id'].message_type = Helpers__pb2._UUID
_COMMENTRESPONSE.fields_by_name['comment'].message_type = _COMMENT
_COMMENTRESPONSE.fields_by_name['created_at'].message_type = Helpers__pb2._TIMESTAMP
_COMMENTRESPONSE.fields_by_name['updated_at'].message_type = Helpers__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Comment'] = _COMMENT
DESCRIPTOR.message_types_by_name['CommentResponse'] = _COMMENTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Comment = _reflection.GeneratedProtocolMessageType('Comment', (_message.Message,), dict(
  DESCRIPTOR = _COMMENT,
  __module__ = 'Comment_pb2'
  # @@protoc_insertion_point(class_scope:Comment)
  ))
_sym_db.RegisterMessage(Comment)

CommentResponse = _reflection.GeneratedProtocolMessageType('CommentResponse', (_message.Message,), dict(
  DESCRIPTOR = _COMMENTRESPONSE,
  __module__ = 'Comment_pb2'
  # @@protoc_insertion_point(class_scope:CommentResponse)
  ))
_sym_db.RegisterMessage(CommentResponse)



_CREATECOMMENT = _descriptor.ServiceDescriptor(
  name='CreateComment',
  full_name='CreateComment',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=228,
  serialized_end=288,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateComment',
    full_name='CreateComment.CreateComment',
    index=0,
    containing_service=None,
    input_type=_COMMENT,
    output_type=_COMMENTRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CREATECOMMENT)

DESCRIPTOR.services_by_name['CreateComment'] = _CREATECOMMENT

# @@protoc_insertion_point(module_scope)
