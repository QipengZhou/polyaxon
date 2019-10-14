#!/usr/bin/python
#
# Copyright 2019 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from v1 import auth_pb2 as v1_dot_auth__pb2
from v1 import base_pb2 as v1_dot_base__pb2
from v1 import code_ref_pb2 as v1_dot_code__ref__pb2
from v1 import project_pb2 as v1_dot_project__pb2
from v1 import run_pb2 as v1_dot_run__pb2
from v1 import versions_pb2 as v1_dot_versions__pb2


class RunServiceStub(object):
  """Service to manage runs
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListRuns = channel.unary_unary(
        '/v1.RunService/ListRuns',
        request_serializer=v1_dot_base__pb2.ProjectBodyRequest.SerializeToString,
        response_deserializer=v1_dot_run__pb2.ListRunsResponse.FromString,
        )
    self.ListBookmarkedRuns = channel.unary_unary(
        '/v1.RunService/ListBookmarkedRuns',
        request_serializer=v1_dot_base__pb2.OwnerBodyRequest.SerializeToString,
        response_deserializer=v1_dot_run__pb2.ListRunsResponse.FromString,
        )
    self.ListArchivedRuns = channel.unary_unary(
        '/v1.RunService/ListArchivedRuns',
        request_serializer=v1_dot_base__pb2.OwnerBodyRequest.SerializeToString,
        response_deserializer=v1_dot_run__pb2.ListRunsResponse.FromString,
        )
    self.CreateRun = channel.unary_unary(
        '/v1.RunService/CreateRun',
        request_serializer=v1_dot_run__pb2.RunBodyRequest.SerializeToString,
        response_deserializer=v1_dot_run__pb2.Run.FromString,
        )
    self.GetRun = channel.unary_unary(
        '/v1.RunService/GetRun',
        request_serializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.SerializeToString,
        response_deserializer=v1_dot_run__pb2.Run.FromString,
        )
    self.UpdateRun = channel.unary_unary(
        '/v1.RunService/UpdateRun',
        request_serializer=v1_dot_run__pb2.RunBodyRequest.SerializeToString,
        response_deserializer=v1_dot_run__pb2.Run.FromString,
        )
    self.PatchRun = channel.unary_unary(
        '/v1.RunService/PatchRun',
        request_serializer=v1_dot_run__pb2.RunBodyRequest.SerializeToString,
        response_deserializer=v1_dot_run__pb2.Run.FromString,
        )
    self.DeleteRun = channel.unary_unary(
        '/v1.RunService/DeleteRun',
        request_serializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.DeleteRuns = channel.unary_unary(
        '/v1.RunService/DeleteRuns',
        request_serializer=v1_dot_base__pb2.ProjectBodyRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.StopRun = channel.unary_unary(
        '/v1.RunService/StopRun',
        request_serializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.StopRuns = channel.unary_unary(
        '/v1.RunService/StopRuns',
        request_serializer=v1_dot_base__pb2.ProjectBodyRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.InvalidateRun = channel.unary_unary(
        '/v1.RunService/InvalidateRun',
        request_serializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.InvalidateRuns = channel.unary_unary(
        '/v1.RunService/InvalidateRuns',
        request_serializer=v1_dot_base__pb2.ProjectBodyRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.RestartRun = channel.unary_unary(
        '/v1.RunService/RestartRun',
        request_serializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.SerializeToString,
        response_deserializer=v1_dot_run__pb2.Run.FromString,
        )
    self.ResumeRun = channel.unary_unary(
        '/v1.RunService/ResumeRun',
        request_serializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.SerializeToString,
        response_deserializer=v1_dot_run__pb2.Run.FromString,
        )
    self.ArchiveRun = channel.unary_unary(
        '/v1.RunService/ArchiveRun',
        request_serializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.RestoreRun = channel.unary_unary(
        '/v1.RunService/RestoreRun',
        request_serializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.BookmarkRun = channel.unary_unary(
        '/v1.RunService/BookmarkRun',
        request_serializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.UnBookmarkRun = channel.unary_unary(
        '/v1.RunService/UnBookmarkRun',
        request_serializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.StartRunTensorboard = channel.unary_unary(
        '/v1.RunService/StartRunTensorboard',
        request_serializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.StopRunTensorboard = channel.unary_unary(
        '/v1.RunService/StopRunTensorboard',
        request_serializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetRunStatuses = channel.unary_unary(
        '/v1.RunService/GetRunStatuses',
        request_serializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.SerializeToString,
        response_deserializer=v1_dot_base__pb2.StatusResponse.FromString,
        )
    self.CreateRunStatus = channel.unary_unary(
        '/v1.RunService/CreateRunStatus',
        request_serializer=v1_dot_base__pb2.EntityStatusRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetRunCodeRefs = channel.unary_unary(
        '/v1.RunService/GetRunCodeRefs',
        request_serializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.SerializeToString,
        response_deserializer=v1_dot_code__ref__pb2.ListCodeRefResponse.FromString,
        )
    self.CreateRunCodeRef = channel.unary_unary(
        '/v1.RunService/CreateRunCodeRef',
        request_serializer=v1_dot_code__ref__pb2.CodeRefBodyRequest.SerializeToString,
        response_deserializer=v1_dot_code__ref__pb2.CodeReference.FromString,
        )


class RunServiceServicer(object):
  """Service to manage runs
  """

  def ListRuns(self, request, context):
    """List runs
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListBookmarkedRuns(self, request, context):
    """List bookmarked runs
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListArchivedRuns(self, request, context):
    """List archived runs
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateRun(self, request, context):
    """Create new run
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetRun(self, request, context):
    """Get run
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateRun(self, request, context):
    """Update run
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PatchRun(self, request, context):
    """Patch run
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteRun(self, request, context):
    """Delete run
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteRuns(self, request, context):
    """Delete runs
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StopRun(self, request, context):
    """Stop run
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StopRuns(self, request, context):
    """Stop runs
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InvalidateRun(self, request, context):
    """Stop run
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InvalidateRuns(self, request, context):
    """Invalidate runs
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RestartRun(self, request, context):
    """Restart run
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ResumeRun(self, request, context):
    """Resume run
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ArchiveRun(self, request, context):
    """Archive run
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RestoreRun(self, request, context):
    """Restore run
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BookmarkRun(self, request, context):
    """Bookmark run
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UnBookmarkRun(self, request, context):
    """UnBookmark run
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartRunTensorboard(self, request, context):
    """Start run tensorboard
    TODO: should be a tensorboard object
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StopRunTensorboard(self, request, context):
    """Stop run tensorboard
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetRunStatuses(self, request, context):
    """Get run status
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateRunStatus(self, request, context):
    """Create new run status
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetRunCodeRefs(self, request, context):
    """Get run code ref
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateRunCodeRef(self, request, context):
    """Get run code ref
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RunServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListRuns': grpc.unary_unary_rpc_method_handler(
          servicer.ListRuns,
          request_deserializer=v1_dot_base__pb2.ProjectBodyRequest.FromString,
          response_serializer=v1_dot_run__pb2.ListRunsResponse.SerializeToString,
      ),
      'ListBookmarkedRuns': grpc.unary_unary_rpc_method_handler(
          servicer.ListBookmarkedRuns,
          request_deserializer=v1_dot_base__pb2.OwnerBodyRequest.FromString,
          response_serializer=v1_dot_run__pb2.ListRunsResponse.SerializeToString,
      ),
      'ListArchivedRuns': grpc.unary_unary_rpc_method_handler(
          servicer.ListArchivedRuns,
          request_deserializer=v1_dot_base__pb2.OwnerBodyRequest.FromString,
          response_serializer=v1_dot_run__pb2.ListRunsResponse.SerializeToString,
      ),
      'CreateRun': grpc.unary_unary_rpc_method_handler(
          servicer.CreateRun,
          request_deserializer=v1_dot_run__pb2.RunBodyRequest.FromString,
          response_serializer=v1_dot_run__pb2.Run.SerializeToString,
      ),
      'GetRun': grpc.unary_unary_rpc_method_handler(
          servicer.GetRun,
          request_deserializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.FromString,
          response_serializer=v1_dot_run__pb2.Run.SerializeToString,
      ),
      'UpdateRun': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateRun,
          request_deserializer=v1_dot_run__pb2.RunBodyRequest.FromString,
          response_serializer=v1_dot_run__pb2.Run.SerializeToString,
      ),
      'PatchRun': grpc.unary_unary_rpc_method_handler(
          servicer.PatchRun,
          request_deserializer=v1_dot_run__pb2.RunBodyRequest.FromString,
          response_serializer=v1_dot_run__pb2.Run.SerializeToString,
      ),
      'DeleteRun': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteRun,
          request_deserializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'DeleteRuns': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteRuns,
          request_deserializer=v1_dot_base__pb2.ProjectBodyRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'StopRun': grpc.unary_unary_rpc_method_handler(
          servicer.StopRun,
          request_deserializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'StopRuns': grpc.unary_unary_rpc_method_handler(
          servicer.StopRuns,
          request_deserializer=v1_dot_base__pb2.ProjectBodyRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'InvalidateRun': grpc.unary_unary_rpc_method_handler(
          servicer.InvalidateRun,
          request_deserializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'InvalidateRuns': grpc.unary_unary_rpc_method_handler(
          servicer.InvalidateRuns,
          request_deserializer=v1_dot_base__pb2.ProjectBodyRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'RestartRun': grpc.unary_unary_rpc_method_handler(
          servicer.RestartRun,
          request_deserializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.FromString,
          response_serializer=v1_dot_run__pb2.Run.SerializeToString,
      ),
      'ResumeRun': grpc.unary_unary_rpc_method_handler(
          servicer.ResumeRun,
          request_deserializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.FromString,
          response_serializer=v1_dot_run__pb2.Run.SerializeToString,
      ),
      'ArchiveRun': grpc.unary_unary_rpc_method_handler(
          servicer.ArchiveRun,
          request_deserializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'RestoreRun': grpc.unary_unary_rpc_method_handler(
          servicer.RestoreRun,
          request_deserializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'BookmarkRun': grpc.unary_unary_rpc_method_handler(
          servicer.BookmarkRun,
          request_deserializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'UnBookmarkRun': grpc.unary_unary_rpc_method_handler(
          servicer.UnBookmarkRun,
          request_deserializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'StartRunTensorboard': grpc.unary_unary_rpc_method_handler(
          servicer.StartRunTensorboard,
          request_deserializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'StopRunTensorboard': grpc.unary_unary_rpc_method_handler(
          servicer.StopRunTensorboard,
          request_deserializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetRunStatuses': grpc.unary_unary_rpc_method_handler(
          servicer.GetRunStatuses,
          request_deserializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.FromString,
          response_serializer=v1_dot_base__pb2.StatusResponse.SerializeToString,
      ),
      'CreateRunStatus': grpc.unary_unary_rpc_method_handler(
          servicer.CreateRunStatus,
          request_deserializer=v1_dot_base__pb2.EntityStatusRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetRunCodeRefs': grpc.unary_unary_rpc_method_handler(
          servicer.GetRunCodeRefs,
          request_deserializer=v1_dot_base__pb2.OwnedEntityUUIdRequest.FromString,
          response_serializer=v1_dot_code__ref__pb2.ListCodeRefResponse.SerializeToString,
      ),
      'CreateRunCodeRef': grpc.unary_unary_rpc_method_handler(
          servicer.CreateRunCodeRef,
          request_deserializer=v1_dot_code__ref__pb2.CodeRefBodyRequest.FromString,
          response_serializer=v1_dot_code__ref__pb2.CodeReference.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'v1.RunService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class ProjectServiceStub(object):
  """Service to manage project
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListProjects = channel.unary_unary(
        '/v1.ProjectService/ListProjects',
        request_serializer=v1_dot_base__pb2.OwnerBodyRequest.SerializeToString,
        response_deserializer=v1_dot_project__pb2.ListProjectsResponse.FromString,
        )
    self.ListProjectNames = channel.unary_unary(
        '/v1.ProjectService/ListProjectNames',
        request_serializer=v1_dot_base__pb2.OwnerBodyRequest.SerializeToString,
        response_deserializer=v1_dot_project__pb2.ListProjectsResponse.FromString,
        )
    self.ListBookmarkedProjects = channel.unary_unary(
        '/v1.ProjectService/ListBookmarkedProjects',
        request_serializer=v1_dot_base__pb2.OwnerBodyRequest.SerializeToString,
        response_deserializer=v1_dot_project__pb2.ListProjectsResponse.FromString,
        )
    self.ListArchivedProjects = channel.unary_unary(
        '/v1.ProjectService/ListArchivedProjects',
        request_serializer=v1_dot_base__pb2.OwnerBodyRequest.SerializeToString,
        response_deserializer=v1_dot_project__pb2.ListProjectsResponse.FromString,
        )
    self.CreateProject = channel.unary_unary(
        '/v1.ProjectService/CreateProject',
        request_serializer=v1_dot_base__pb2.OwnerBodyRequest.SerializeToString,
        response_deserializer=v1_dot_project__pb2.Project.FromString,
        )
    self.GetProject = channel.unary_unary(
        '/v1.ProjectService/GetProject',
        request_serializer=v1_dot_base__pb2.ProjectBodyRequest.SerializeToString,
        response_deserializer=v1_dot_project__pb2.Project.FromString,
        )
    self.UpdateProject = channel.unary_unary(
        '/v1.ProjectService/UpdateProject',
        request_serializer=v1_dot_base__pb2.ProjectBodyRequest.SerializeToString,
        response_deserializer=v1_dot_project__pb2.Project.FromString,
        )
    self.PatchProject = channel.unary_unary(
        '/v1.ProjectService/PatchProject',
        request_serializer=v1_dot_base__pb2.ProjectBodyRequest.SerializeToString,
        response_deserializer=v1_dot_project__pb2.Project.FromString,
        )
    self.DeleteExperiment = channel.unary_unary(
        '/v1.ProjectService/DeleteExperiment',
        request_serializer=v1_dot_base__pb2.ProjectBodyRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ArchiveProject = channel.unary_unary(
        '/v1.ProjectService/ArchiveProject',
        request_serializer=v1_dot_base__pb2.ProjectBodyRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.RestoreExperiment = channel.unary_unary(
        '/v1.ProjectService/RestoreExperiment',
        request_serializer=v1_dot_base__pb2.ProjectBodyRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.BookmarkProject = channel.unary_unary(
        '/v1.ProjectService/BookmarkProject',
        request_serializer=v1_dot_base__pb2.ProjectBodyRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.UnBookmarkProject = channel.unary_unary(
        '/v1.ProjectService/UnBookmarkProject',
        request_serializer=v1_dot_base__pb2.ProjectBodyRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.EnableProjectCI = channel.unary_unary(
        '/v1.ProjectService/EnableProjectCI',
        request_serializer=v1_dot_base__pb2.ProjectBodyRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.DisableProjectCI = channel.unary_unary(
        '/v1.ProjectService/DisableProjectCI',
        request_serializer=v1_dot_base__pb2.ProjectBodyRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class ProjectServiceServicer(object):
  """Service to manage project
  """

  def ListProjects(self, request, context):
    """List projects
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListProjectNames(self, request, context):
    """List project namess
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListBookmarkedProjects(self, request, context):
    """List bookmarked projects
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListArchivedProjects(self, request, context):
    """List archived projects
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateProject(self, request, context):
    """Create new project
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetProject(self, request, context):
    """Get project
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateProject(self, request, context):
    """Update project
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PatchProject(self, request, context):
    """Patch project
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteExperiment(self, request, context):
    """Delete project
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ArchiveProject(self, request, context):
    """Archive project
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RestoreExperiment(self, request, context):
    """Restore project
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BookmarkProject(self, request, context):
    """Bookmark project
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UnBookmarkProject(self, request, context):
    """UnBookmark project
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EnableProjectCI(self, request, context):
    """Enable CI
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DisableProjectCI(self, request, context):
    """UnBookmark project
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ProjectServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListProjects': grpc.unary_unary_rpc_method_handler(
          servicer.ListProjects,
          request_deserializer=v1_dot_base__pb2.OwnerBodyRequest.FromString,
          response_serializer=v1_dot_project__pb2.ListProjectsResponse.SerializeToString,
      ),
      'ListProjectNames': grpc.unary_unary_rpc_method_handler(
          servicer.ListProjectNames,
          request_deserializer=v1_dot_base__pb2.OwnerBodyRequest.FromString,
          response_serializer=v1_dot_project__pb2.ListProjectsResponse.SerializeToString,
      ),
      'ListBookmarkedProjects': grpc.unary_unary_rpc_method_handler(
          servicer.ListBookmarkedProjects,
          request_deserializer=v1_dot_base__pb2.OwnerBodyRequest.FromString,
          response_serializer=v1_dot_project__pb2.ListProjectsResponse.SerializeToString,
      ),
      'ListArchivedProjects': grpc.unary_unary_rpc_method_handler(
          servicer.ListArchivedProjects,
          request_deserializer=v1_dot_base__pb2.OwnerBodyRequest.FromString,
          response_serializer=v1_dot_project__pb2.ListProjectsResponse.SerializeToString,
      ),
      'CreateProject': grpc.unary_unary_rpc_method_handler(
          servicer.CreateProject,
          request_deserializer=v1_dot_base__pb2.OwnerBodyRequest.FromString,
          response_serializer=v1_dot_project__pb2.Project.SerializeToString,
      ),
      'GetProject': grpc.unary_unary_rpc_method_handler(
          servicer.GetProject,
          request_deserializer=v1_dot_base__pb2.ProjectBodyRequest.FromString,
          response_serializer=v1_dot_project__pb2.Project.SerializeToString,
      ),
      'UpdateProject': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateProject,
          request_deserializer=v1_dot_base__pb2.ProjectBodyRequest.FromString,
          response_serializer=v1_dot_project__pb2.Project.SerializeToString,
      ),
      'PatchProject': grpc.unary_unary_rpc_method_handler(
          servicer.PatchProject,
          request_deserializer=v1_dot_base__pb2.ProjectBodyRequest.FromString,
          response_serializer=v1_dot_project__pb2.Project.SerializeToString,
      ),
      'DeleteExperiment': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteExperiment,
          request_deserializer=v1_dot_base__pb2.ProjectBodyRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ArchiveProject': grpc.unary_unary_rpc_method_handler(
          servicer.ArchiveProject,
          request_deserializer=v1_dot_base__pb2.ProjectBodyRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'RestoreExperiment': grpc.unary_unary_rpc_method_handler(
          servicer.RestoreExperiment,
          request_deserializer=v1_dot_base__pb2.ProjectBodyRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'BookmarkProject': grpc.unary_unary_rpc_method_handler(
          servicer.BookmarkProject,
          request_deserializer=v1_dot_base__pb2.ProjectBodyRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'UnBookmarkProject': grpc.unary_unary_rpc_method_handler(
          servicer.UnBookmarkProject,
          request_deserializer=v1_dot_base__pb2.ProjectBodyRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'EnableProjectCI': grpc.unary_unary_rpc_method_handler(
          servicer.EnableProjectCI,
          request_deserializer=v1_dot_base__pb2.ProjectBodyRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'DisableProjectCI': grpc.unary_unary_rpc_method_handler(
          servicer.DisableProjectCI,
          request_deserializer=v1_dot_base__pb2.ProjectBodyRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'v1.ProjectService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class AuthServiceStub(object):
  """Service to manage auth
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Login = channel.unary_unary(
        '/v1.AuthService/Login',
        request_serializer=v1_dot_auth__pb2.CredsBodyRequest.SerializeToString,
        response_deserializer=v1_dot_auth__pb2.Auth.FromString,
        )


class AuthServiceServicer(object):
  """Service to manage auth
  """

  def Login(self, request, context):
    """Login
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AuthServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Login': grpc.unary_unary_rpc_method_handler(
          servicer.Login,
          request_deserializer=v1_dot_auth__pb2.CredsBodyRequest.FromString,
          response_serializer=v1_dot_auth__pb2.Auth.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'v1.AuthService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class VersionsServiceStub(object):
  """Service to get versions
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetVersions = channel.unary_unary(
        '/v1.VersionsService/GetVersions',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=v1_dot_versions__pb2.Versions.FromString,
        )


class VersionsServiceServicer(object):
  """Service to get versions
  """

  def GetVersions(self, request, context):
    """Get versions
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_VersionsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetVersions': grpc.unary_unary_rpc_method_handler(
          servicer.GetVersions,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=v1_dot_versions__pb2.Versions.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'v1.VersionsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
