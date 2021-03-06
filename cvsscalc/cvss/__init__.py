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
from decimal import ROUND_UP
from .metrics import *

CRIT_COLORS = {
    'none': ('#ffffff', '#000000'),
    'low': ('#ffff00', '#000000'),
    'medium': ('#ffa500', '#000000'),
    'high': ('#ff0000', '#000000'),
    'critical': ('#8b0000', '#ffffff')
}


def criticity(score: Decimal):
    if Decimal(0.1) <= score <= Decimal(3.9):
        return 'low', CRIT_COLORS['low']
    elif Decimal(4.) <= score <= Decimal(6.9):
        return 'medium', CRIT_COLORS['medium']
    elif Decimal(7.) <= score <= Decimal(8.9):
        return 'high', CRIT_COLORS['high']
    elif Decimal(9.) <= score <= Decimal(10.):
        return 'critical', CRIT_COLORS['critical']
    else:  # score == 0
        return 'none', CRIT_COLORS['none']


def roundup(d: Decimal):
    return d.quantize(Decimal('1.0'), rounding=ROUND_UP)


def base_score(iss: Decimal, ess: Decimal, scope: Scope):
    if iss <= Decimal(0.):
        return Decimal(0.)
    if scope == Scope.UNCHANGED:
        return roundup(min(iss + ess, Decimal(10.)))
    return roundup(min(Decimal(1.08) * (iss + ess), Decimal(10.)))


def impact_subscore(scope: Scope, c: CIA, i: CIA, a: CIA):
    one = Decimal(1.)
    isc_base = one - ((one - c) * (one - i) * (one - a))
    if scope == Scope.UNCHANGED:
        return scope * isc_base
    return scope * (isc_base - Decimal(0.029)) - \
        Decimal(3.25) * ((isc_base - Decimal(0.02)) ** Decimal(15))


def exploitability_subscore(av: AttackVector, ac: AttackComplexity,
                            pr: PrivilegeRequired, ui: UserInteraction):
    return Decimal(8.22) * av * ac * pr * ui


def temporal_score(bs: Decimal, e: ExploitCodeMaturity,
                   rl: RemediationLevel, rc: ReportConfidence):
    return roundup(bs * e * rl * rc)


def environmental_score(scope: Scope, miss: Decimal, mess: Decimal,
                        e: ExploitCodeMaturity, rl: RemediationLevel,
                        rc: ReportConfidence):
    if miss <= Decimal(0.):
        return Decimal(0.)
    if scope == Scope.UNCHANGED:
        ie = roundup(min((miss + mess), Decimal(10.)))
        return roundup(ie * e * rl * rc)
    ie = roundup(min(Decimal(1.08) * (miss + mess), Decimal(10.)))
    return roundup(ie * e * rl * rc)


def modified_impact_subscore(scope: Scope, mc: CIA, mi: CIA, ma: CIA,
                             cr: CIARequirements, ir: CIARequirements,
                             ar: CIARequirements):
    one = Decimal(1.)
    isc_mod = min(
        one - (one - mc * cr) * (one - mi * ir) * (one - ma * ar),
        Decimal(0.915)
    )
    if scope == Scope.UNCHANGED:
        return scope * isc_mod
    return scope * (isc_mod - Decimal(0.029)) - Decimal(3.25) * \
                                                ((isc_mod - Decimal(0.2)) ** Decimal(15))


def modified_exploitability_subscore(mav: AttackVector, mac: AttackComplexity,
                                     mpr: PrivilegeRequiredModified,
                                     mui: UserInteraction):
    return Decimal(8.22) * mav * mac * mpr * mui
