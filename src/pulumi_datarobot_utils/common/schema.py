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
from __future__ import annotations

from enum import Enum

from pydantic import BaseModel


class ResourceBundleSize(str, Enum):
    XXS = "cpu.nano"
    XS = "cpu.micro"
    S = "cpu.small"
    M = "cpu.medium"
    L = "cpu.large"
    XL = "cpu.xlarge"
    XXL = "cpu.2xlarge"
    XXXL = "cpu.3xlarge"
    XXXXL = "cpu.4xlarge"


class CredentialArgs(BaseModel):
    resource_name: str
    name: str | None = None


class DatasetArgs(BaseModel):
    resource_name: str
    name: str | None = None
    file_path: str

