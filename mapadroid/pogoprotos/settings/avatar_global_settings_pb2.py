# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/avatar_global_settings.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/avatar_global_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n0pogoprotos/settings/avatar_global_settings.proto\x12\x13pogoprotos.settings\"+\n\x14\x41vatarGlobalSettings\x12\x13\n\x0b\x65nable_pose\x18\x01 \x01(\x08\x62\x06proto3'
)




_AVATARGLOBALSETTINGS = _descriptor.Descriptor(
  name='AvatarGlobalSettings',
  full_name='pogoprotos.settings.AvatarGlobalSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable_pose', full_name='pogoprotos.settings.AvatarGlobalSettings.enable_pose', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=73,
  serialized_end=116,
)

DESCRIPTOR.message_types_by_name['AvatarGlobalSettings'] = _AVATARGLOBALSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AvatarGlobalSettings = _reflection.GeneratedProtocolMessageType('AvatarGlobalSettings', (_message.Message,), {
  'DESCRIPTOR' : _AVATARGLOBALSETTINGS,
  '__module__' : 'pogoprotos.settings.avatar_global_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.AvatarGlobalSettings)
  })
_sym_db.RegisterMessage(AvatarGlobalSettings)


# @@protoc_insertion_point(module_scope)