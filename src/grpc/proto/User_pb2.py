# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: User.proto

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
  name='User.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nUser.proto\x1a\rHelpers.proto\"L\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x12\n\x08password\x18\x03 \x01(\tH\x00\x42\x13\n\x11optional_password\"\xbc\x01\n\x0cUserResponse\x12\x13\n\x04user\x18\x01 \x01(\x0b\x32\x05.User\x12\x1f\n\nuserStatus\x18\x02 \x01(\x0e\x32\x0b.UserStatus\x12\x15\n\x06userId\x18\x03 \x01(\x0b\x32\x05.UUID\x12\r\n\x05token\x18\x04 \x01(\t\x12\x1d\n\tcreatedAt\x18\x05 \x01(\x0b\x32\n.Timestamp\x12\x1d\n\tupdatedAt\x18\x06 \x01(\x0b\x32\n.Timestamp\x12\x12\n\nisVerified\x18\x07 \x01(\x08\x32\x37\n\x11\x43reateUserService\x12\"\n\nCreateUser\x12\x05.User\x1a\r.UserResponseb\x06proto3')
  ,
  dependencies=[Helpers__pb2.DESCRIPTOR,])




_USER = _descriptor.Descriptor(
  name='User',
  full_name='User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='User.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='User.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='User.password', index=2,
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
    _descriptor.OneofDescriptor(
      name='optional_password', full_name='User.optional_password',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=29,
  serialized_end=105,
)


_USERRESPONSE = _descriptor.Descriptor(
  name='UserResponse',
  full_name='UserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='UserResponse.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userStatus', full_name='UserResponse.userStatus', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userId', full_name='UserResponse.userId', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='UserResponse.token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createdAt', full_name='UserResponse.createdAt', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updatedAt', full_name='UserResponse.updatedAt', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isVerified', full_name='UserResponse.isVerified', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=108,
  serialized_end=296,
)

_USER.oneofs_by_name['optional_password'].fields.append(
  _USER.fields_by_name['password'])
_USER.fields_by_name['password'].containing_oneof = _USER.oneofs_by_name['optional_password']
_USERRESPONSE.fields_by_name['user'].message_type = _USER
_USERRESPONSE.fields_by_name['userStatus'].enum_type = Helpers__pb2._USERSTATUS
_USERRESPONSE.fields_by_name['userId'].message_type = Helpers__pb2._UUID
_USERRESPONSE.fields_by_name['createdAt'].message_type = Helpers__pb2._TIMESTAMP
_USERRESPONSE.fields_by_name['updatedAt'].message_type = Helpers__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['UserResponse'] = _USERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), dict(
  DESCRIPTOR = _USER,
  __module__ = 'User_pb2'
  # @@protoc_insertion_point(class_scope:User)
  ))
_sym_db.RegisterMessage(User)

UserResponse = _reflection.GeneratedProtocolMessageType('UserResponse', (_message.Message,), dict(
  DESCRIPTOR = _USERRESPONSE,
  __module__ = 'User_pb2'
  # @@protoc_insertion_point(class_scope:UserResponse)
  ))
_sym_db.RegisterMessage(UserResponse)



_CREATEUSERSERVICE = _descriptor.ServiceDescriptor(
  name='CreateUserService',
  full_name='CreateUserService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=298,
  serialized_end=353,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateUser',
    full_name='CreateUserService.CreateUser',
    index=0,
    containing_service=None,
    input_type=_USER,
    output_type=_USERRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CREATEUSERSERVICE)

DESCRIPTOR.services_by_name['CreateUserService'] = _CREATEUSERSERVICE

# @@protoc_insertion_point(module_scope)
