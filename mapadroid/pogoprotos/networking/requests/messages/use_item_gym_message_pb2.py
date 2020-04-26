# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/use_item_gym_message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory.item import item_id_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/use_item_gym_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nBpogoprotos/networking/requests/messages/use_item_gym_message.proto\x12\'pogoprotos.networking.requests.messages\x1a\'pogoprotos/inventory/item/item_id.proto\"\x8a\x01\n\x11UseItemGymMessage\x12\x32\n\x07item_id\x18\x01 \x01(\x0e\x32!.pogoprotos.inventory.item.ItemId\x12\x0e\n\x06gym_id\x18\x02 \x01(\t\x12\x17\n\x0fplayer_latitude\x18\x03 \x01(\x01\x12\x18\n\x10player_longitude\x18\x04 \x01(\x01\x62\x06proto3'
  ,
  dependencies=[pogoprotos_dot_inventory_dot_item_dot_item__id__pb2.DESCRIPTOR,])




_USEITEMGYMMESSAGE = _descriptor.Descriptor(
  name='UseItemGymMessage',
  full_name='pogoprotos.networking.requests.messages.UseItemGymMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='pogoprotos.networking.requests.messages.UseItemGymMessage.item_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gym_id', full_name='pogoprotos.networking.requests.messages.UseItemGymMessage.gym_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_latitude', full_name='pogoprotos.networking.requests.messages.UseItemGymMessage.player_latitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_longitude', full_name='pogoprotos.networking.requests.messages.UseItemGymMessage.player_longitude', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=153,
  serialized_end=291,
)

_USEITEMGYMMESSAGE.fields_by_name['item_id'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__id__pb2._ITEMID
DESCRIPTOR.message_types_by_name['UseItemGymMessage'] = _USEITEMGYMMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UseItemGymMessage = _reflection.GeneratedProtocolMessageType('UseItemGymMessage', (_message.Message,), {
  'DESCRIPTOR' : _USEITEMGYMMESSAGE,
  '__module__' : 'pogoprotos.networking.requests.messages.use_item_gym_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.UseItemGymMessage)
  })
_sym_db.RegisterMessage(UseItemGymMessage)


# @@protoc_insertion_point(module_scope)