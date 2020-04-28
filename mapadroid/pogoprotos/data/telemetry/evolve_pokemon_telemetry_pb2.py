# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/evolve_pokemon_telemetry.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.telemetry import pokemon_telemetry_pb2 as pogoprotos_dot_data_dot_telemetry_dot_pokemon__telemetry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/evolve_pokemon_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n8pogoprotos/data/telemetry/evolve_pokemon_telemetry.proto\x12\x19pogoprotos.data.telemetry\x1a\x31pogoprotos/data/telemetry/pokemon_telemetry.proto\"\x9c\x01\n\x16\x45volvePokemonTelemetry\x12<\n\x07pokemon\x18\x01 \x01(\x0b\x32+.pogoprotos.data.telemetry.PokemonTelemetry\x12\x44\n\x0f\x65volved_pokemon\x18\x02 \x01(\x0b\x32+.pogoprotos.data.telemetry.PokemonTelemetryb\x06proto3'
  ,
  dependencies=[pogoprotos_dot_data_dot_telemetry_dot_pokemon__telemetry__pb2.DESCRIPTOR,])




_EVOLVEPOKEMONTELEMETRY = _descriptor.Descriptor(
  name='EvolvePokemonTelemetry',
  full_name='pogoprotos.data.telemetry.EvolvePokemonTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon', full_name='pogoprotos.data.telemetry.EvolvePokemonTelemetry.pokemon', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='evolved_pokemon', full_name='pogoprotos.data.telemetry.EvolvePokemonTelemetry.evolved_pokemon', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=139,
  serialized_end=295,
)

_EVOLVEPOKEMONTELEMETRY.fields_by_name['pokemon'].message_type = pogoprotos_dot_data_dot_telemetry_dot_pokemon__telemetry__pb2._POKEMONTELEMETRY
_EVOLVEPOKEMONTELEMETRY.fields_by_name['evolved_pokemon'].message_type = pogoprotos_dot_data_dot_telemetry_dot_pokemon__telemetry__pb2._POKEMONTELEMETRY
DESCRIPTOR.message_types_by_name['EvolvePokemonTelemetry'] = _EVOLVEPOKEMONTELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EvolvePokemonTelemetry = _reflection.GeneratedProtocolMessageType('EvolvePokemonTelemetry', (_message.Message,), {
  'DESCRIPTOR' : _EVOLVEPOKEMONTELEMETRY,
  '__module__' : 'pogoprotos.data.telemetry.evolve_pokemon_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.EvolvePokemonTelemetry)
  })
_sym_db.RegisterMessage(EvolvePokemonTelemetry)


# @@protoc_insertion_point(module_scope)