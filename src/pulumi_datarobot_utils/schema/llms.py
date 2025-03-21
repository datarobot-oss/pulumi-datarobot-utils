# Copyright 2025 DataRobot, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import pulumi_datarobot as drp

from pulumi_datarobot_utils.schema.base import Field, Schema


class PlaygroundArgs(Schema):
    resource_name: str
    name: str | None = None


class LLMSettings(Schema):
    system_prompt: str
    max_completion_length: int = Field(le=512)


class LLMBlueprintArgs(Schema):
    resource_name: str
    description: str | None = None
    llm_id: str
    llm_settings: drp.LlmBlueprintLlmSettingsArgs | None = None
    name: str | None = None
    prompt_type: str | None = None
    vector_database_settings: drp.LlmBlueprintVectorDatabaseSettingsArgs | None = None