# -*- coding: utf-8 -*-
#
#     cvsscalc - a PyQt-based CVSS v3 calculator
#     Copyright (C) 2017 Mathieu "mattoufoutu" Deous
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from decimal import Decimal
from enum import Enum


class Metric(Decimal, Enum):
    pass


class AttackVector(Metric):
    NOT_DEFINED = Decimal(1.)
    NETWORK = Decimal(0.85)
    ADJACENT = Decimal(0.62)
    LOCAL = Decimal(0.55)
    PHYSICAL = Decimal(0.2)


class AttackComplexity(Metric):
    NOT_DEFINED = Decimal(1.)
    LOW = Decimal(0.77)
    HIGH = Decimal(0.44)


class PrivilegeRequired(Metric):
    NONE = Decimal(0.85)
    LOW = Decimal(0.62)
    HIGH = Decimal(0.27)


class PrivilegeRequiredModified(Metric):
    NOT_DEFINED = Decimal(1.)
    NONE = Decimal(0.85)
    LOW = Decimal(0.68)
    HIGH = Decimal(0.5)


class UserInteraction(Metric):
    NOT_DEFINED = Decimal(1.)
    NONE = Decimal(0.85)
    REQUIRED = Decimal(0.62)


class Scope(Metric):
    NOT_DEFINED = Decimal(1.)
    CHANGED = Decimal(7.52)
    UNCHANGED = Decimal(6.42)


class CIA(Metric):
    NOT_DEFINED = Decimal(1.)
    NONE = Decimal(0.)
    LOW = Decimal(0.22)
    HIGH = Decimal(0.56)


class ExploitCodeMaturity(Metric):
    NOT_DEFINED = Decimal(1.)
    HIGH = Decimal(1.)
    FUNCTIONAL = Decimal(0.97)
    PROOF_OF_CONCEPT = Decimal(0.94)
    UNPROVEN = Decimal(0.91)


class RemediationLevel(Metric):
    NOT_DEFINED = Decimal(1.)
    UNAVAILABLE = Decimal(1.)
    WORKAROUND = Decimal(0.97)
    TEMPORARY_FIX = Decimal(0.96)
    OFFICIAL_FIX = Decimal(0.95)


class ReportConfidence(Metric):
    NOT_DEFINED = Decimal(1.)
    CONFIRMED = Decimal(1.)
    REASONABLE = Decimal(0.96)
    UNKNOWN = Decimal(0.92)


class CIARequirements(Metric):
    NOT_DEFINED = Decimal(1.)
    HIGH = Decimal(1.5)
    MEDIUM = Decimal(1.)
    LOW = Decimal(0.5)
