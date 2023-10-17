{
  'variables': {
    'protocol_tool_path': '../../tools/inspector_protocol',
    'node_inspector_sources': [
      'src/inspector_agent.cc',
      'src/inspector_io.cc',
      'src/inspector_agent.h',
      'src/inspector_io.h',
      'src/inspector_profiler.h',
      'src/inspector_profiler.cc',
      'src/inspector_js_api.cc',
      'src/inspector_socket.cc',
      'src/inspector_socket.h',
      'src/inspector_socket_server.cc',
      'src/inspector_socket_server.h',
      'src/inspector/main_thread_interface.cc',
      'src/inspector/main_thread_interface.h',
      'src/inspector/node_string.cc',
      'src/inspector/node_string.h',
      'src/inspector/runtime_agent.cc',
      'src/inspector/runtime_agent.h',
      'src/inspector/tracing_agent.cc',
      'src/inspector/tracing_agent.h',
      'src/inspector/worker_agent.cc',
      'src/inspector/worker_agent.h',
      'src/inspector/worker_inspector.cc',
      'src/inspector/worker_inspector.h',
    ],
    'node_inspector_generated_sources': [
      '<(SHARED_INTERMEDIATE_DIR)/src/node/inspector/protocol/Forward.h',
      '<(SHARED_INTERMEDIATE_DIR)/src/node/inspector/protocol/Protocol.cpp',
      '<(SHARED_INTERMEDIATE_DIR)/src/node/inspector/protocol/Protocol.h',
      '<(SHARED_INTERMEDIATE_DIR)/src/node/inspector/protocol/NodeWorker.cpp',
      '<(SHARED_INTERMEDIATE_DIR)/src/node/inspector/protocol/NodeWorker.h',
      '<(SHARED_INTERMEDIATE_DIR)/src/node/inspector/protocol/NodeTracing.cpp',
      '<(SHARED_INTERMEDIATE_DIR)/src/node/inspector/protocol/NodeTracing.h',
      '<(SHARED_INTERMEDIATE_DIR)/src/node/inspector/protocol/NodeRuntime.cpp',
      '<(SHARED_INTERMEDIATE_DIR)/src/node/inspector/protocol/NodeRuntime.h',
    ],
    'node_protocol_files': [
      '<(protocol_tool_path)/lib/Allocator_h.template',
      '<(protocol_tool_path)/lib/Array_h.template',
      '<(protocol_tool_path)/lib/base_string_adapter_cc.template',
      '<(protocol_tool_path)/lib/base_string_adapter_h.template',
      '<(protocol_tool_path)/lib/DispatcherBase_cpp.template',
      '<(protocol_tool_path)/lib/DispatcherBase_h.template',
      '<(protocol_tool_path)/lib/encoding_cpp.template',
      '<(protocol_tool_path)/lib/encoding_h.template',
      '<(protocol_tool_path)/lib/ErrorSupport_cpp.template',
      '<(protocol_tool_path)/lib/ErrorSupport_h.template',
      '<(protocol_tool_path)/lib/Forward_h.template',
      '<(protocol_tool_path)/lib/FrontendChannel_h.template',
      '<(protocol_tool_path)/lib/Maybe_h.template',
      '<(protocol_tool_path)/lib/Object_cpp.template',
      '<(protocol_tool_path)/lib/Object_h.template',
      '<(protocol_tool_path)/lib/Parser_cpp.template',
      '<(protocol_tool_path)/lib/Parser_h.template',
      '<(protocol_tool_path)/lib/Protocol_cpp.template',
      '<(protocol_tool_path)/lib/ValueConversions_h.template',
      '<(protocol_tool_path)/lib/Values_cpp.template',
      '<(protocol_tool_path)/lib/Values_h.template',
      '<(protocol_tool_path)/templates/Exported_h.template',
      '<(protocol_tool_path)/templates/Imported_h.template',
      '<(protocol_tool_path)/templates/TypeBuilder_cpp.template',
      '<(protocol_tool_path)/templates/TypeBuilder_h.template',
    ]
  },
  'defines': [
    'HAVE_INSPECTOR=1',
  ],
  'sources': [
    '<@(node_inspector_sources)',
  ],
  'include_dirs': [
    '<(SHARED_INTERMEDIATE_DIR)/include', # for inspector
    '<(SHARED_INTERMEDIATE_DIR)',
    '<(SHARED_INTERMEDIATE_DIR)/src', # for inspector
  ],
  'actions': [
    {
      'action_name': 'convert_node_protocol_to_json',
      'inputs': [
        'node_protocol.pdl',
      ],
      'outputs': [
        '<(SHARED_INTERMEDIATE_DIR)/src/node_protocol.json',
      ],
      'action': [
        '<(python)',
        '../../v8/third_party/inspector_protocol/convert_protocol_to_json.py',
        '<@(_inputs)',
        '<@(_outputs)',
      ],
    },
    {
      'action_name': 'node_protocol_generated_sources',
      'inputs': [
        'node_protocol_config.json',
        '<(SHARED_INTERMEDIATE_DIR)/src/node_protocol.json',
        '<@(node_protocol_files)',
        '<(protocol_tool_path)/code_generator.py',
      ],
      'outputs': [
        '<@(node_inspector_generated_sources)',
      ],
      'process_outputs_as_sources': 1,
      'action': [
        '<(python)',
        'tools/inspector_protocol/code_generator.py',
        '--jinja_dir', '<@(protocol_tool_path)',
        '--output_base', '<(SHARED_INTERMEDIATE_DIR)/src/',
        '--config', 'src/inspector/node_protocol_config.json',
      ],
      'message': 'Generating node protocol sources from protocol json',
    },
    {
      'action_name': 'concatenate_protocols',
      'inputs': [
        #'../../../../v8/src/inspector/js_protocol.json',
        '<(SHARED_INTERMEDIATE_DIR)/src/node_protocol.json',
      ],
      'outputs': [
        '<(SHARED_INTERMEDIATE_DIR)/concatenated_protocol.json',
      ],
      'action': [
        '<(python)',
        '../../v8/third_party/inspector_protocol/concatenate_protocols.py',
        '<@(_inputs)',
        '<@(_outputs)',
      ],
    },
    {
      'action_name': 'v8_inspector_compress_protocol_json',
      'inputs': [
        '<(SHARED_INTERMEDIATE_DIR)/concatenated_protocol.json',
      ],
      'outputs': [
        '<(SHARED_INTERMEDIATE_DIR)/v8_inspector_protocol_json.h',
      ],
      'process_outputs_as_sources': 1,
      'action': [
        '<(python)',
        'tools/compress_json.py',
        '<@(_inputs)',
        '<@(_outputs)',
      ],
    },
  ],
}
