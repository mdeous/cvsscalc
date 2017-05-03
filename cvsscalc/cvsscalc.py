#!/bin/env python
# -*- coding : utf-8 -*-
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

import sys

from PyQt5.QtWidgets import *

from cvss import *
from mainwindow import Ui_MainWindow

SCORE_TEMPLATE = """
<html><body><p align="right"><span style="{style} font-weight:600;">
&nbsp;{score} ({criticity})&nbsp;</span></p></body></html>"""


class CVSSCalc(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(CVSSCalc, self).__init__()
        self.setupUi(self)

        # Base score metrics
        self.AV = None
        self.AC = None
        self.PR = None
        self.UI = None
        self.S = None
        self.C = None
        self.I = None
        self.A = None
        self.base_score = self.get_base_score()

        # Temporal score metrics
        self.E = ExploitCodeMaturity(ExploitCodeMaturity.NOT_DEFINED)
        self.RL = RemediationLevel(RemediationLevel.NOT_DEFINED)
        self.RC = ReportConfidence(ReportConfidence.NOT_DEFINED)
        self.temporal_score = self.get_temporal_score()

        # Environmental score metrics
        self.CR = None
        self.IR = None
        self.AR = None
        self.MAV = AttackVector(AttackVector.NOT_DEFINED)
        self.MAC = AttackComplexity(AttackComplexity.NOT_DEFINED)
        self.MPR = PrivilegeRequiredModified(PrivilegeRequiredModified.NOT_DEFINED)
        self.MUI = UserInteraction(UserInteraction.NOT_DEFINED)
        self.MS = Scope(Scope.NOT_DEFINED)
        self.MC = CIA(CIA.NOT_DEFINED)
        self.MI = CIA(CIA.NOT_DEFINED)
        self.MA = CIA(CIA.NOT_DEFINED)
        self.environmental_score = self.get_environmental_score()

        # Base score buttons event handlers
        self.avnPushButton.clicked.connect(
            lambda: self.update_score('AV', AttackVector(AttackVector.NETWORK)))
        self.avaPushButton.clicked.connect(
            lambda: self.update_score('AV', AttackVector(AttackVector.ADJACENT)))
        self.avlPushButton.clicked.connect(
            lambda: self.update_score('AV', AttackVector(AttackVector.LOCAL)))
        self.avpPushButton.clicked.connect(
            lambda: self.update_score('AV', AttackVector(AttackVector.PHYSICAL)))

        self.aclPushButton.clicked.connect(
            lambda: self.update_score('AC', AttackComplexity(AttackComplexity.LOW)))
        self.achPushButton.clicked.connect(
            lambda: self.update_score('AC', AttackComplexity(AttackComplexity.HIGH)))

        self.prnPushButton.clicked.connect(
            lambda: self.update_score('PR', PrivilegeRequired(PrivilegeRequired.NONE)))
        self.prlPutton.clicked.connect(
            lambda: self.update_score('PR', PrivilegeRequired(PrivilegeRequired.LOW)))
        self.prhPushButton.clicked.connect(
            lambda: self.update_score('PR', PrivilegeRequired(PrivilegeRequired.HIGH)))

        self.uinPushButton.clicked.connect(
            lambda: self.update_score('UI', UserInteraction(UserInteraction.NONE)))
        self.uirPushButton.clicked.connect(
            lambda: self.update_score('UI', UserInteraction(UserInteraction.REQUIRED)))

        self.suPushButton.clicked.connect(
            lambda: self.update_score('S', Scope(Scope.UNCHANGED)))
        self.scPushButton.clicked.connect(
            lambda: self.update_score('S', Scope(Scope.CHANGED)))

        self.cnPushButton.clicked.connect(
            lambda: self.update_score('C', CIA(CIA.NONE)))
        self.clPushButton.clicked.connect(
            lambda: self.update_score('C', CIA(CIA.LOW)))
        self.chPushButton.clicked.connect(
            lambda: self.update_score('C', CIA(CIA.HIGH)))

        self.inPushButton.clicked.connect(
            lambda: self.update_score('I', CIA(CIA.NONE)))
        self.ilPushButton.clicked.connect(
            lambda: self.update_score('I', CIA(CIA.LOW)))
        self.ihPushButton.clicked.connect(
            lambda: self.update_score('I', CIA(CIA.HIGH)))

        self.anPushButton.clicked.connect(
            lambda: self.update_score('A', CIA(CIA.NONE)))
        self.alPushButton.clicked.connect(
            lambda: self.update_score('A', CIA(CIA.LOW)))
        self.ahPushButton.clicked.connect(
            lambda: self.update_score('A', CIA(CIA.HIGH)))

        # Temporal score buttons event handlers
        self.exPushButton.clicked.connect(
            lambda: self.update_score(
                'E', ExploitCodeMaturity(ExploitCodeMaturity.NOT_DEFINED)))
        self.euPushButton.clicked.connect(
            lambda: self.update_score(
                'E', ExploitCodeMaturity(ExploitCodeMaturity.UNPROVEN)))
        self.epPushButton.clicked.connect(
            lambda: self.update_score(
                'E', ExploitCodeMaturity(ExploitCodeMaturity.PROOF_OF_CONCEPT)))
        self.efPushButton.clicked.connect(
            lambda: self.update_score(
                'E', ExploitCodeMaturity(ExploitCodeMaturity.FUNCTIONAL)))
        self.ehPushButton.clicked.connect(
            lambda: self.update_score(
                'E', ExploitCodeMaturity(ExploitCodeMaturity.HIGH)))

        self.rlxPushButton.clicked.connect(
            lambda: self.update_score(
                'RL', RemediationLevel(RemediationLevel.NOT_DEFINED)))
        self.rloPushButton.clicked.connect(
            lambda: self.update_score(
                'RL', RemediationLevel(RemediationLevel.OFFICIAL_FIX)))
        self.rltPushButton.clicked.connect(
            lambda: self.update_score(
                'RL', RemediationLevel(RemediationLevel.TEMPORARY_FIX)))
        self.rlwPushButton.clicked.connect(
            lambda: self.update_score(
                'RL', RemediationLevel(RemediationLevel.WORKAROUND)))
        self.rluPushButton.clicked.connect(
            lambda: self.update_score(
                'RL', RemediationLevel(RemediationLevel.UNAVAILABLE)))
        self.rcxPushButton.clicked.connect(
            lambda: self.update_score(
                'RC', ReportConfidence(ReportConfidence.NOT_DEFINED)))
        self.rcuPushButton.clicked.connect(
            lambda: self.update_score(
                'RC', ReportConfidence(ReportConfidence.UNKNOWN)))
        self.rcrPushButton.clicked.connect(
            lambda: self.update_score(
                'RC', ReportConfidence(ReportConfidence.REASONABLE)))
        self.rccPushButton.clicked.connect(
            lambda: self.update_score(
                'RC', ReportConfidence(ReportConfidence.CONFIRMED)))

        # Environmental score buttons event handlers
        self.crxPushButton.clicked.connect(
            lambda: self.update_score('CR', CIARequirements(CIARequirements.NOT_DEFINED)))
        self.crlPushButton.clicked.connect(
            lambda: self.update_score('CR', CIARequirements(CIARequirements.LOW)))
        self.crmPushButton.clicked.connect(
            lambda: self.update_score('CR', CIARequirements(CIARequirements.MEDIUM)))
        self.crhPushButton.clicked.connect(
            lambda: self.update_score('CR', CIARequirements(CIARequirements.HIGH)))

        self.irxPushButton.clicked.connect(
            lambda: self.update_score('IR', CIARequirements(CIARequirements.NOT_DEFINED)))
        self.irlPushButton.clicked.connect(
            lambda: self.update_score('IR', CIARequirements(CIARequirements.LOW)))
        self.irmPushButton.clicked.connect(
            lambda: self.update_score('IR', CIARequirements(CIARequirements.MEDIUM)))
        self.irhPushButton.clicked.connect(
            lambda: self.update_score('IR', CIARequirements(CIARequirements.HIGH)))

        self.arxPushButton.clicked.connect(
            lambda: self.update_score('AR', CIARequirements(CIARequirements.NOT_DEFINED)))
        self.arlPushButton.clicked.connect(
            lambda: self.update_score('AR', CIARequirements(CIARequirements.LOW)))
        self.armPushButton.clicked.connect(
            lambda: self.update_score('AR', CIARequirements(CIARequirements.MEDIUM)))
        self.arhPushButton.clicked.connect(
            lambda: self.update_score('AR', CIARequirements(CIARequirements.HIGH)))

        self.mavxPushButton.clicked.connect(
            lambda: self.update_score('MAV', AttackVector(AttackVector.NOT_DEFINED)))
        self.mavnPushButton.clicked.connect(
            lambda: self.update_score('MAV', AttackVector(AttackVector.NETWORK)))
        self.mavaPushButton.clicked.connect(
            lambda: self.update_score('MAV', AttackVector(AttackVector.ADJACENT)))
        self.mavlPushButton.clicked.connect(
            lambda: self.update_score('MAV', AttackVector(AttackVector.LOCAL)))
        self.mavpPushButton.clicked.connect(
            lambda: self.update_score('MAV', AttackVector(AttackVector.PHYSICAL)))

        self.macxPushButton.clicked.connect(
            lambda: self.update_score(
                'MAC', AttackComplexity(AttackComplexity.NOT_DEFINED)))
        self.maclPushButton.clicked.connect(
            lambda: self.update_score(
                'MAC', AttackComplexity(AttackComplexity.LOW)))
        self.machPushButton.clicked.connect(
            lambda: self.update_score(
                'MAC', AttackComplexity(AttackComplexity.HIGH)))

        self.mprxPushButton.clicked.connect(
            lambda: self.update_score(
                'MPR', PrivilegeRequiredModified(PrivilegeRequiredModified.NOT_DEFINED)))
        self.mprnPushButton.clicked.connect(
            lambda: self.update_score(
                'MPR', PrivilegeRequiredModified(PrivilegeRequiredModified.NONE)))
        self.mprlPushButton.clicked.connect(
            lambda: self.update_score(
                'MPR', PrivilegeRequiredModified(PrivilegeRequiredModified.LOW)))
        self.mprhPushButton.clicked.connect(
            lambda: self.update_score(
                'MPR', PrivilegeRequiredModified(PrivilegeRequiredModified.HIGH)))

        self.muixPushButton.clicked.connect(
            lambda: self.update_score(
                'MUI', UserInteraction(UserInteraction.NOT_DEFINED)))
        self.muinPushButton.clicked.connect(
            lambda: self.update_score(
                'MUI', UserInteraction(UserInteraction.NONE)))
        self.muirPushButton.clicked.connect(
            lambda: self.update_score(
                'MUI', UserInteraction(UserInteraction.REQUIRED)))

        self.msxPushButton.clicked.connect(
            lambda: self.update_score('MS', Scope.NOT_DEFINED))
        self.msuPushButton.clicked.connect(
            lambda: self.update_score('MS', Scope.UNCHANGED))
        self.mscPushButton.clicked.connect(
            lambda: self.update_score('MS', Scope.CHANGED))

        self.mcxPushButton.clicked.connect(
            lambda: self.update_score('MC', CIA(CIA.NOT_DEFINED)))
        self.mcnPushButton.clicked.connect(
            lambda: self.update_score('MC', CIA(CIA.NONE)))
        self.mclPushButton.clicked.connect(
            lambda: self.update_score('MC', CIA(CIA.LOW)))
        self.mchPushButton.clicked.connect(
            lambda: self.update_score('MC', CIA(CIA.HIGH)))

        self.mixPushButton.clicked.connect(
            lambda: self.update_score('MI', CIA(CIA.NOT_DEFINED)))
        self.minPushButton.clicked.connect(
            lambda: self.update_score('MI', CIA(CIA.NONE)))
        self.milPushButton.clicked.connect(
            lambda: self.update_score('MI', CIA(CIA.LOW)))
        self.mihPushButton.clicked.connect(
            lambda: self.update_score('MI', CIA(CIA.HIGH)))

        self.maxPushButton.clicked.connect(
            lambda: self.update_score('MA', CIA(CIA.NOT_DEFINED)))
        self.manPushButton.clicked.connect(
            lambda: self.update_score('MA', CIA(CIA.NONE)))
        self.malPushButton.clicked.connect(
            lambda: self.update_score('MA', CIA(CIA.LOW)))
        self.mahPushButton.clicked.connect(
            lambda: self.update_score('MA', CIA(CIA.HIGH)))

    def _update_bs(self):
        if self.base_score is not None:
            crit, (bg, fg) = criticity(self.base_score)
            style = 'color: {}; background-color: {};'.format(fg, bg)
            txt = SCORE_TEMPLATE.format(
                score=str(self.base_score), criticity=crit, style=style
            )
            self.baseScoreLabel.setText(txt)

    def _update_ts(self):
        if self.temporal_score is not None:
            crit, (bg, fg) = criticity(self.temporal_score)
            style = 'color: {}; background-color: {};'.format(fg, bg)
            txt = SCORE_TEMPLATE.format(
                score=str(self.temporal_score), criticity=crit, style=style
            )
            self.temporalScoreLabel.setText(txt)

    def _update_es(self):
        if self.environmental_score is not None:
            crit, (bg, fg) = criticity(self.environmental_score)
            style = 'color: {}; background-color: {};'.format(fg, bg)
            txt = SCORE_TEMPLATE.format(
                score=str(self.environmental_score), criticity=crit, style=style
            )
            self.environmentalScoreLabel.setText(txt)

    def update_score(self, metric: str, value: Metric):
        setattr(self, metric, value)
        self.base_score = self.get_base_score()
        self._update_bs()
        self.temporal_score = self.get_temporal_score()
        self._update_ts()
        self.environmental_score = self.get_environmental_score()
        self._update_es()

    def get_base_score(self):
        if None in (self.S, self.C, self.I, self.A, self.AV, self.AC, self.PR, self.UI):
            return None
        iss = impact_subscore(self.S, self.C, self.I, self.A)
        ess = exploitability_subscore(self.AV, self.AC, self.PR, self.UI)
        return base_score(iss, ess, self.S)

    def get_temporal_score(self):
        if self.base_score is None:
            return None
        return temporal_score(self.base_score, self.E, self.RL, self.RC)

    def get_environmental_score(self):
        if None in (self.base_score, self.CR, self.IR, self.AR):
            return None
        mav = self.AV if self.MAV == AttackVector.NOT_DEFINED else self.MAV
        mac = self.AC if self.MAC == AttackComplexity.NOT_DEFINED else self.MAC
        mpr = self.PR if self.MPR == PrivilegeRequiredModified.NOT_DEFINED else self.MPR
        mui = self.UI if self.MUI == UserInteraction.NOT_DEFINED else self.MUI
        ms = self.S if self.MS == Scope.NOT_DEFINED else self.MS
        mc = self.C if self.MC == CIA.NOT_DEFINED else self.MC
        mi = self.I if self.MI == CIA.NOT_DEFINED else self.MI
        ma = self.A if self.MA == CIA.NOT_DEFINED else self.MA

        miss = modified_impact_subscore(
            ms, mc, mi, ma, self.CR, self.IR, self.AR
        )
        mess = modified_exploitability_subscore(mav, mac, mpr, mui)
        return environmental_score(ms, miss, mess, self.E, self.RL, self.RC)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = CVSSCalc()
    calc.show()
    sys.exit(app.exec_())
