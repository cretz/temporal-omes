# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kitchen_sink.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from temporalio.api.common.v1 import message_pb2 as temporal_dot_api_dot_common_dot_v1_dot_message__pb2
from temporalio.api.failure.v1 import message_pb2 as temporal_dot_api_dot_failure_dot_v1_dot_message__pb2
from temporalio.api.enums.v1 import workflow_pb2 as temporal_dot_api_dot_enums_dot_v1_dot_workflow__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12kitchen_sink.proto\x12\x1atemporal.omes.kitchen_sink\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a$temporal/api/common/v1/message.proto\x1a%temporal/api/failure/v1/message.proto\x1a$temporal/api/enums/v1/workflow.proto\"\xe1\x01\n\tTestInput\x12\x41\n\x0eworkflow_input\x18\x01 \x01(\x0b\x32).temporal.omes.kitchen_sink.WorkflowInput\x12\x43\n\x0f\x63lient_sequence\x18\x02 \x01(\x0b\x32*.temporal.omes.kitchen_sink.ClientSequence\x12L\n\x11with_start_action\x18\x03 \x01(\x0b\x32\x31.temporal.omes.kitchen_sink.WithStartClientAction\"R\n\x0e\x43lientSequence\x12@\n\x0b\x61\x63tion_sets\x18\x01 \x03(\x0b\x32+.temporal.omes.kitchen_sink.ClientActionSet\"\xbf\x01\n\x0f\x43lientActionSet\x12\x39\n\x07\x61\x63tions\x18\x01 \x03(\x0b\x32(.temporal.omes.kitchen_sink.ClientAction\x12\x12\n\nconcurrent\x18\x02 \x01(\x08\x12.\n\x0bwait_at_end\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12-\n%wait_for_current_run_to_finish_at_end\x18\x04 \x01(\x08\"]\n\x15WithStartClientAction\x12\x39\n\tdo_signal\x18\x01 \x01(\x0b\x32$.temporal.omes.kitchen_sink.DoSignalH\x00\x42\t\n\x07variant\"\x8f\x02\n\x0c\x43lientAction\x12\x39\n\tdo_signal\x18\x01 \x01(\x0b\x32$.temporal.omes.kitchen_sink.DoSignalH\x00\x12\x37\n\x08\x64o_query\x18\x02 \x01(\x0b\x32#.temporal.omes.kitchen_sink.DoQueryH\x00\x12\x39\n\tdo_update\x18\x03 \x01(\x0b\x32$.temporal.omes.kitchen_sink.DoUpdateH\x00\x12\x45\n\x0enested_actions\x18\x04 \x01(\x0b\x32+.temporal.omes.kitchen_sink.ClientActionSetH\x00\x42\t\n\x07variant\"\xde\x02\n\x08\x44oSignal\x12Q\n\x11\x64o_signal_actions\x18\x01 \x01(\x0b\x32\x34.temporal.omes.kitchen_sink.DoSignal.DoSignalActionsH\x00\x12?\n\x06\x63ustom\x18\x02 \x01(\x0b\x32-.temporal.omes.kitchen_sink.HandlerInvocationH\x00\x12\x12\n\nwith_start\x18\x03 \x01(\x08\x1a\x9e\x01\n\x0f\x44oSignalActions\x12;\n\ndo_actions\x18\x01 \x01(\x0b\x32%.temporal.omes.kitchen_sink.ActionSetH\x00\x12\x43\n\x12\x64o_actions_in_main\x18\x02 \x01(\x0b\x32%.temporal.omes.kitchen_sink.ActionSetH\x00\x42\t\n\x07variantB\t\n\x07variant\"\xa9\x01\n\x07\x44oQuery\x12\x38\n\x0creport_state\x18\x01 \x01(\x0b\x32 .temporal.api.common.v1.PayloadsH\x00\x12?\n\x06\x63ustom\x18\x02 \x01(\x0b\x32-.temporal.omes.kitchen_sink.HandlerInvocationH\x00\x12\x18\n\x10\x66\x61ilure_expected\x18\n \x01(\x08\x42\t\n\x07variant\"\xb3\x01\n\x08\x44oUpdate\x12\x41\n\ndo_actions\x18\x01 \x01(\x0b\x32+.temporal.omes.kitchen_sink.DoActionsUpdateH\x00\x12?\n\x06\x63ustom\x18\x02 \x01(\x0b\x32-.temporal.omes.kitchen_sink.HandlerInvocationH\x00\x12\x18\n\x10\x66\x61ilure_expected\x18\n \x01(\x08\x42\t\n\x07variant\"\x86\x01\n\x0f\x44oActionsUpdate\x12;\n\ndo_actions\x18\x01 \x01(\x0b\x32%.temporal.omes.kitchen_sink.ActionSetH\x00\x12+\n\treject_me\x18\x02 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x42\t\n\x07variant\"P\n\x11HandlerInvocation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12-\n\x04\x61rgs\x18\x02 \x03(\x0b\x32\x1f.temporal.api.common.v1.Payload\"|\n\rWorkflowState\x12?\n\x03kvs\x18\x01 \x03(\x0b\x32\x32.temporal.omes.kitchen_sink.WorkflowState.KvsEntry\x1a*\n\x08KvsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"O\n\rWorkflowInput\x12>\n\x0finitial_actions\x18\x01 \x03(\x0b\x32%.temporal.omes.kitchen_sink.ActionSet\"T\n\tActionSet\x12\x33\n\x07\x61\x63tions\x18\x01 \x03(\x0b\x32\".temporal.omes.kitchen_sink.Action\x12\x12\n\nconcurrent\x18\x02 \x01(\x08\"\xac\x08\n\x06\x41\x63tion\x12\x38\n\x05timer\x18\x01 \x01(\x0b\x32\'.temporal.omes.kitchen_sink.TimerActionH\x00\x12J\n\rexec_activity\x18\x02 \x01(\x0b\x32\x31.temporal.omes.kitchen_sink.ExecuteActivityActionH\x00\x12U\n\x13\x65xec_child_workflow\x18\x03 \x01(\x0b\x32\x36.temporal.omes.kitchen_sink.ExecuteChildWorkflowActionH\x00\x12N\n\x14\x61wait_workflow_state\x18\x04 \x01(\x0b\x32..temporal.omes.kitchen_sink.AwaitWorkflowStateH\x00\x12\x43\n\x0bsend_signal\x18\x05 \x01(\x0b\x32,.temporal.omes.kitchen_sink.SendSignalActionH\x00\x12K\n\x0f\x63\x61ncel_workflow\x18\x06 \x01(\x0b\x32\x30.temporal.omes.kitchen_sink.CancelWorkflowActionH\x00\x12L\n\x10set_patch_marker\x18\x07 \x01(\x0b\x32\x30.temporal.omes.kitchen_sink.SetPatchMarkerActionH\x00\x12\\\n\x18upsert_search_attributes\x18\x08 \x01(\x0b\x32\x38.temporal.omes.kitchen_sink.UpsertSearchAttributesActionH\x00\x12\x43\n\x0bupsert_memo\x18\t \x01(\x0b\x32,.temporal.omes.kitchen_sink.UpsertMemoActionH\x00\x12G\n\x12set_workflow_state\x18\n \x01(\x0b\x32).temporal.omes.kitchen_sink.WorkflowStateH\x00\x12G\n\rreturn_result\x18\x0b \x01(\x0b\x32..temporal.omes.kitchen_sink.ReturnResultActionH\x00\x12\x45\n\x0creturn_error\x18\x0c \x01(\x0b\x32-.temporal.omes.kitchen_sink.ReturnErrorActionH\x00\x12J\n\x0f\x63ontinue_as_new\x18\r \x01(\x0b\x32/.temporal.omes.kitchen_sink.ContinueAsNewActionH\x00\x12\x42\n\x11nested_action_set\x18\x0e \x01(\x0b\x32%.temporal.omes.kitchen_sink.ActionSetH\x00\x42\t\n\x07variant\"\xa3\x02\n\x0f\x41waitableChoice\x12-\n\x0bwait_finish\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12)\n\x07\x61\x62\x61ndon\x18\x02 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12\x37\n\x15\x63\x61ncel_before_started\x18\x03 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12\x36\n\x14\x63\x61ncel_after_started\x18\x04 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12\x38\n\x16\x63\x61ncel_after_completed\x18\x05 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x42\x0b\n\tcondition\"j\n\x0bTimerAction\x12\x14\n\x0cmilliseconds\x18\x01 \x01(\x04\x12\x45\n\x10\x61waitable_choice\x18\x02 \x01(\x0b\x32+.temporal.omes.kitchen_sink.AwaitableChoice\"\xc0\t\n\x15\x45xecuteActivityAction\x12T\n\x07generic\x18\x01 \x01(\x0b\x32\x41.temporal.omes.kitchen_sink.ExecuteActivityAction.GenericActivityH\x00\x12*\n\x05\x64\x65lay\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationH\x00\x12&\n\x04noop\x18\x03 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12X\n\tresources\x18\x0e \x01(\x0b\x32\x43.temporal.omes.kitchen_sink.ExecuteActivityAction.ResourcesActivityH\x00\x12\x12\n\ntask_queue\x18\x04 \x01(\t\x12O\n\x07headers\x18\x05 \x03(\x0b\x32>.temporal.omes.kitchen_sink.ExecuteActivityAction.HeadersEntry\x12<\n\x19schedule_to_close_timeout\x18\x06 \x01(\x0b\x32\x19.google.protobuf.Duration\x12<\n\x19schedule_to_start_timeout\x18\x07 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x39\n\x16start_to_close_timeout\x18\x08 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x34\n\x11heartbeat_timeout\x18\t \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x39\n\x0cretry_policy\x18\n \x01(\x0b\x32#.temporal.api.common.v1.RetryPolicy\x12*\n\x08is_local\x18\x0b \x01(\x0b\x32\x16.google.protobuf.EmptyH\x01\x12\x43\n\x06remote\x18\x0c \x01(\x0b\x32\x31.temporal.omes.kitchen_sink.RemoteActivityOptionsH\x01\x12\x45\n\x10\x61waitable_choice\x18\r \x01(\x0b\x32+.temporal.omes.kitchen_sink.AwaitableChoice\x1aS\n\x0fGenericActivity\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x32\n\targuments\x18\x02 \x03(\x0b\x32\x1f.temporal.api.common.v1.Payload\x1a\x9a\x01\n\x11ResourcesActivity\x12*\n\x07run_for\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x19\n\x11\x62ytes_to_allocate\x18\x02 \x01(\x04\x12$\n\x1c\x63pu_yield_every_n_iterations\x18\x03 \x01(\r\x12\x18\n\x10\x63pu_yield_for_ms\x18\x04 \x01(\r\x1aO\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload:\x02\x38\x01\x42\x0f\n\ractivity_typeB\n\n\x08locality\"\xad\n\n\x1a\x45xecuteChildWorkflowAction\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\x13\n\x0bworkflow_id\x18\x03 \x01(\t\x12\x15\n\rworkflow_type\x18\x04 \x01(\t\x12\x12\n\ntask_queue\x18\x05 \x01(\t\x12.\n\x05input\x18\x06 \x03(\x0b\x32\x1f.temporal.api.common.v1.Payload\x12=\n\x1aworkflow_execution_timeout\x18\x07 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x37\n\x14workflow_run_timeout\x18\x08 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x38\n\x15workflow_task_timeout\x18\t \x01(\x0b\x32\x19.google.protobuf.Duration\x12J\n\x13parent_close_policy\x18\n \x01(\x0e\x32-.temporal.omes.kitchen_sink.ParentClosePolicy\x12N\n\x18workflow_id_reuse_policy\x18\x0c \x01(\x0e\x32,.temporal.api.enums.v1.WorkflowIdReusePolicy\x12\x39\n\x0cretry_policy\x18\r \x01(\x0b\x32#.temporal.api.common.v1.RetryPolicy\x12\x15\n\rcron_schedule\x18\x0e \x01(\t\x12T\n\x07headers\x18\x0f \x03(\x0b\x32\x43.temporal.omes.kitchen_sink.ExecuteChildWorkflowAction.HeadersEntry\x12N\n\x04memo\x18\x10 \x03(\x0b\x32@.temporal.omes.kitchen_sink.ExecuteChildWorkflowAction.MemoEntry\x12g\n\x11search_attributes\x18\x11 \x03(\x0b\x32L.temporal.omes.kitchen_sink.ExecuteChildWorkflowAction.SearchAttributesEntry\x12T\n\x11\x63\x61ncellation_type\x18\x12 \x01(\x0e\x32\x39.temporal.omes.kitchen_sink.ChildWorkflowCancellationType\x12G\n\x11versioning_intent\x18\x13 \x01(\x0e\x32,.temporal.omes.kitchen_sink.VersioningIntent\x12\x45\n\x10\x61waitable_choice\x18\x14 \x01(\x0b\x32+.temporal.omes.kitchen_sink.AwaitableChoice\x1aO\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload:\x02\x38\x01\x1aL\n\tMemoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload:\x02\x38\x01\x1aX\n\x15SearchAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload:\x02\x38\x01\"0\n\x12\x41waitWorkflowState\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xdf\x02\n\x10SendSignalAction\x12\x13\n\x0bworkflow_id\x18\x01 \x01(\t\x12\x0e\n\x06run_id\x18\x02 \x01(\t\x12\x13\n\x0bsignal_name\x18\x03 \x01(\t\x12-\n\x04\x61rgs\x18\x04 \x03(\x0b\x32\x1f.temporal.api.common.v1.Payload\x12J\n\x07headers\x18\x05 \x03(\x0b\x32\x39.temporal.omes.kitchen_sink.SendSignalAction.HeadersEntry\x12\x45\n\x10\x61waitable_choice\x18\x06 \x01(\x0b\x32+.temporal.omes.kitchen_sink.AwaitableChoice\x1aO\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload:\x02\x38\x01\";\n\x14\x43\x61ncelWorkflowAction\x12\x13\n\x0bworkflow_id\x18\x01 \x01(\t\x12\x0e\n\x06run_id\x18\x02 \x01(\t\"v\n\x14SetPatchMarkerAction\x12\x10\n\x08patch_id\x18\x01 \x01(\t\x12\x12\n\ndeprecated\x18\x02 \x01(\x08\x12\x38\n\x0cinner_action\x18\x03 \x01(\x0b\x32\".temporal.omes.kitchen_sink.Action\"\xe3\x01\n\x1cUpsertSearchAttributesAction\x12i\n\x11search_attributes\x18\x01 \x03(\x0b\x32N.temporal.omes.kitchen_sink.UpsertSearchAttributesAction.SearchAttributesEntry\x1aX\n\x15SearchAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload:\x02\x38\x01\"G\n\x10UpsertMemoAction\x12\x33\n\rupserted_memo\x18\x01 \x01(\x0b\x32\x1c.temporal.api.common.v1.Memo\"J\n\x12ReturnResultAction\x12\x34\n\x0breturn_this\x18\x01 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload\"F\n\x11ReturnErrorAction\x12\x31\n\x07\x66\x61ilure\x18\x01 \x01(\x0b\x32 .temporal.api.failure.v1.Failure\"\xde\x06\n\x13\x43ontinueAsNewAction\x12\x15\n\rworkflow_type\x18\x01 \x01(\t\x12\x12\n\ntask_queue\x18\x02 \x01(\t\x12\x32\n\targuments\x18\x03 \x03(\x0b\x32\x1f.temporal.api.common.v1.Payload\x12\x37\n\x14workflow_run_timeout\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x38\n\x15workflow_task_timeout\x18\x05 \x01(\x0b\x32\x19.google.protobuf.Duration\x12G\n\x04memo\x18\x06 \x03(\x0b\x32\x39.temporal.omes.kitchen_sink.ContinueAsNewAction.MemoEntry\x12M\n\x07headers\x18\x07 \x03(\x0b\x32<.temporal.omes.kitchen_sink.ContinueAsNewAction.HeadersEntry\x12`\n\x11search_attributes\x18\x08 \x03(\x0b\x32\x45.temporal.omes.kitchen_sink.ContinueAsNewAction.SearchAttributesEntry\x12\x39\n\x0cretry_policy\x18\t \x01(\x0b\x32#.temporal.api.common.v1.RetryPolicy\x12G\n\x11versioning_intent\x18\n \x01(\x0e\x32,.temporal.omes.kitchen_sink.VersioningIntent\x1aL\n\tMemoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload:\x02\x38\x01\x1aO\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload:\x02\x38\x01\x1aX\n\x15SearchAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload:\x02\x38\x01\"\xd1\x01\n\x15RemoteActivityOptions\x12O\n\x11\x63\x61ncellation_type\x18\x01 \x01(\x0e\x32\x34.temporal.omes.kitchen_sink.ActivityCancellationType\x12\x1e\n\x16\x64o_not_eagerly_execute\x18\x02 \x01(\x08\x12G\n\x11versioning_intent\x18\x03 \x01(\x0e\x32,.temporal.omes.kitchen_sink.VersioningIntent*\xa4\x01\n\x11ParentClosePolicy\x12#\n\x1fPARENT_CLOSE_POLICY_UNSPECIFIED\x10\x00\x12!\n\x1dPARENT_CLOSE_POLICY_TERMINATE\x10\x01\x12\x1f\n\x1bPARENT_CLOSE_POLICY_ABANDON\x10\x02\x12&\n\"PARENT_CLOSE_POLICY_REQUEST_CANCEL\x10\x03*@\n\x10VersioningIntent\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0e\n\nCOMPATIBLE\x10\x01\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x02*\xa2\x01\n\x1d\x43hildWorkflowCancellationType\x12\x14\n\x10\x43HILD_WF_ABANDON\x10\x00\x12\x17\n\x13\x43HILD_WF_TRY_CANCEL\x10\x01\x12(\n$CHILD_WF_WAIT_CANCELLATION_COMPLETED\x10\x02\x12(\n$CHILD_WF_WAIT_CANCELLATION_REQUESTED\x10\x03*X\n\x18\x41\x63tivityCancellationType\x12\x0e\n\nTRY_CANCEL\x10\x00\x12\x1f\n\x1bWAIT_CANCELLATION_COMPLETED\x10\x01\x12\x0b\n\x07\x41\x42\x41NDON\x10\x02\x42\x42\n\x10io.temporal.omesZ.github.com/temporalio/omes/loadgen/kitchensinkb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kitchen_sink_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020io.temporal.omesZ.github.com/temporalio/omes/loadgen/kitchensink'
  _globals['_WORKFLOWSTATE_KVSENTRY']._options = None
  _globals['_WORKFLOWSTATE_KVSENTRY']._serialized_options = b'8\001'
  _globals['_EXECUTEACTIVITYACTION_HEADERSENTRY']._options = None
  _globals['_EXECUTEACTIVITYACTION_HEADERSENTRY']._serialized_options = b'8\001'
  _globals['_EXECUTECHILDWORKFLOWACTION_HEADERSENTRY']._options = None
  _globals['_EXECUTECHILDWORKFLOWACTION_HEADERSENTRY']._serialized_options = b'8\001'
  _globals['_EXECUTECHILDWORKFLOWACTION_MEMOENTRY']._options = None
  _globals['_EXECUTECHILDWORKFLOWACTION_MEMOENTRY']._serialized_options = b'8\001'
  _globals['_EXECUTECHILDWORKFLOWACTION_SEARCHATTRIBUTESENTRY']._options = None
  _globals['_EXECUTECHILDWORKFLOWACTION_SEARCHATTRIBUTESENTRY']._serialized_options = b'8\001'
  _globals['_SENDSIGNALACTION_HEADERSENTRY']._options = None
  _globals['_SENDSIGNALACTION_HEADERSENTRY']._serialized_options = b'8\001'
  _globals['_UPSERTSEARCHATTRIBUTESACTION_SEARCHATTRIBUTESENTRY']._options = None
  _globals['_UPSERTSEARCHATTRIBUTESACTION_SEARCHATTRIBUTESENTRY']._serialized_options = b'8\001'
  _globals['_CONTINUEASNEWACTION_MEMOENTRY']._options = None
  _globals['_CONTINUEASNEWACTION_MEMOENTRY']._serialized_options = b'8\001'
  _globals['_CONTINUEASNEWACTION_HEADERSENTRY']._options = None
  _globals['_CONTINUEASNEWACTION_HEADERSENTRY']._serialized_options = b'8\001'
  _globals['_CONTINUEASNEWACTION_SEARCHATTRIBUTESENTRY']._options = None
  _globals['_CONTINUEASNEWACTION_SEARCHATTRIBUTESENTRY']._serialized_options = b'8\001'
  _globals['_PARENTCLOSEPOLICY']._serialized_start=8454
  _globals['_PARENTCLOSEPOLICY']._serialized_end=8618
  _globals['_VERSIONINGINTENT']._serialized_start=8620
  _globals['_VERSIONINGINTENT']._serialized_end=8684
  _globals['_CHILDWORKFLOWCANCELLATIONTYPE']._serialized_start=8687
  _globals['_CHILDWORKFLOWCANCELLATIONTYPE']._serialized_end=8849
  _globals['_ACTIVITYCANCELLATIONTYPE']._serialized_start=8851
  _globals['_ACTIVITYCANCELLATIONTYPE']._serialized_end=8939
  _globals['_TESTINPUT']._serialized_start=227
  _globals['_TESTINPUT']._serialized_end=452
  _globals['_CLIENTSEQUENCE']._serialized_start=454
  _globals['_CLIENTSEQUENCE']._serialized_end=536
  _globals['_CLIENTACTIONSET']._serialized_start=539
  _globals['_CLIENTACTIONSET']._serialized_end=730
  _globals['_WITHSTARTCLIENTACTION']._serialized_start=732
  _globals['_WITHSTARTCLIENTACTION']._serialized_end=825
  _globals['_CLIENTACTION']._serialized_start=828
  _globals['_CLIENTACTION']._serialized_end=1099
  _globals['_DOSIGNAL']._serialized_start=1102
  _globals['_DOSIGNAL']._serialized_end=1452
  _globals['_DOSIGNAL_DOSIGNALACTIONS']._serialized_start=1283
  _globals['_DOSIGNAL_DOSIGNALACTIONS']._serialized_end=1441
  _globals['_DOQUERY']._serialized_start=1455
  _globals['_DOQUERY']._serialized_end=1624
  _globals['_DOUPDATE']._serialized_start=1627
  _globals['_DOUPDATE']._serialized_end=1806
  _globals['_DOACTIONSUPDATE']._serialized_start=1809
  _globals['_DOACTIONSUPDATE']._serialized_end=1943
  _globals['_HANDLERINVOCATION']._serialized_start=1945
  _globals['_HANDLERINVOCATION']._serialized_end=2025
  _globals['_WORKFLOWSTATE']._serialized_start=2027
  _globals['_WORKFLOWSTATE']._serialized_end=2151
  _globals['_WORKFLOWSTATE_KVSENTRY']._serialized_start=2109
  _globals['_WORKFLOWSTATE_KVSENTRY']._serialized_end=2151
  _globals['_WORKFLOWINPUT']._serialized_start=2153
  _globals['_WORKFLOWINPUT']._serialized_end=2232
  _globals['_ACTIONSET']._serialized_start=2234
  _globals['_ACTIONSET']._serialized_end=2318
  _globals['_ACTION']._serialized_start=2321
  _globals['_ACTION']._serialized_end=3389
  _globals['_AWAITABLECHOICE']._serialized_start=3392
  _globals['_AWAITABLECHOICE']._serialized_end=3683
  _globals['_TIMERACTION']._serialized_start=3685
  _globals['_TIMERACTION']._serialized_end=3791
  _globals['_EXECUTEACTIVITYACTION']._serialized_start=3794
  _globals['_EXECUTEACTIVITYACTION']._serialized_end=5010
  _globals['_EXECUTEACTIVITYACTION_GENERICACTIVITY']._serialized_start=4660
  _globals['_EXECUTEACTIVITYACTION_GENERICACTIVITY']._serialized_end=4743
  _globals['_EXECUTEACTIVITYACTION_RESOURCESACTIVITY']._serialized_start=4746
  _globals['_EXECUTEACTIVITYACTION_RESOURCESACTIVITY']._serialized_end=4900
  _globals['_EXECUTEACTIVITYACTION_HEADERSENTRY']._serialized_start=4902
  _globals['_EXECUTEACTIVITYACTION_HEADERSENTRY']._serialized_end=4981
  _globals['_EXECUTECHILDWORKFLOWACTION']._serialized_start=5013
  _globals['_EXECUTECHILDWORKFLOWACTION']._serialized_end=6338
  _globals['_EXECUTECHILDWORKFLOWACTION_HEADERSENTRY']._serialized_start=4902
  _globals['_EXECUTECHILDWORKFLOWACTION_HEADERSENTRY']._serialized_end=4981
  _globals['_EXECUTECHILDWORKFLOWACTION_MEMOENTRY']._serialized_start=6172
  _globals['_EXECUTECHILDWORKFLOWACTION_MEMOENTRY']._serialized_end=6248
  _globals['_EXECUTECHILDWORKFLOWACTION_SEARCHATTRIBUTESENTRY']._serialized_start=6250
  _globals['_EXECUTECHILDWORKFLOWACTION_SEARCHATTRIBUTESENTRY']._serialized_end=6338
  _globals['_AWAITWORKFLOWSTATE']._serialized_start=6340
  _globals['_AWAITWORKFLOWSTATE']._serialized_end=6388
  _globals['_SENDSIGNALACTION']._serialized_start=6391
  _globals['_SENDSIGNALACTION']._serialized_end=6742
  _globals['_SENDSIGNALACTION_HEADERSENTRY']._serialized_start=4902
  _globals['_SENDSIGNALACTION_HEADERSENTRY']._serialized_end=4981
  _globals['_CANCELWORKFLOWACTION']._serialized_start=6744
  _globals['_CANCELWORKFLOWACTION']._serialized_end=6803
  _globals['_SETPATCHMARKERACTION']._serialized_start=6805
  _globals['_SETPATCHMARKERACTION']._serialized_end=6923
  _globals['_UPSERTSEARCHATTRIBUTESACTION']._serialized_start=6926
  _globals['_UPSERTSEARCHATTRIBUTESACTION']._serialized_end=7153
  _globals['_UPSERTSEARCHATTRIBUTESACTION_SEARCHATTRIBUTESENTRY']._serialized_start=6250
  _globals['_UPSERTSEARCHATTRIBUTESACTION_SEARCHATTRIBUTESENTRY']._serialized_end=6338
  _globals['_UPSERTMEMOACTION']._serialized_start=7155
  _globals['_UPSERTMEMOACTION']._serialized_end=7226
  _globals['_RETURNRESULTACTION']._serialized_start=7228
  _globals['_RETURNRESULTACTION']._serialized_end=7302
  _globals['_RETURNERRORACTION']._serialized_start=7304
  _globals['_RETURNERRORACTION']._serialized_end=7374
  _globals['_CONTINUEASNEWACTION']._serialized_start=7377
  _globals['_CONTINUEASNEWACTION']._serialized_end=8239
  _globals['_CONTINUEASNEWACTION_MEMOENTRY']._serialized_start=6172
  _globals['_CONTINUEASNEWACTION_MEMOENTRY']._serialized_end=6248
  _globals['_CONTINUEASNEWACTION_HEADERSENTRY']._serialized_start=4902
  _globals['_CONTINUEASNEWACTION_HEADERSENTRY']._serialized_end=4981
  _globals['_CONTINUEASNEWACTION_SEARCHATTRIBUTESENTRY']._serialized_start=6250
  _globals['_CONTINUEASNEWACTION_SEARCHATTRIBUTESENTRY']._serialized_end=6338
  _globals['_REMOTEACTIVITYOPTIONS']._serialized_start=8242
  _globals['_REMOTEACTIVITYOPTIONS']._serialized_end=8451
# @@protoc_insertion_point(module_scope)
