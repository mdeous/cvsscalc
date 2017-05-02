#!/bin/env python
# -*- coding : utf-8 -*-
import sys

from PyQt5.QtWidgets import *

from cvss import *
from mainwindow import Ui_MainWindow


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
        self.CR = CIARequirements(CIARequirements.NOT_DEFINED)
        self.IR = CIARequirements(CIARequirements.NOT_DEFINED)
        self.AR = CIARequirements(CIARequirements.NOT_DEFINED)
        self.MAV = AttackVector(AttackVector.NOT_DEFINED)
        self.MAC = AttackComplexity(AttackComplexity.NOT_DEFINED)
        self.MPR = PrivilegeRequiredModified(PrivilegeRequiredModified.NOT_DEFINED)
        self.MUI = UserInteraction(UserInteraction.NOT_DEFINED)
        self.MS = Scope(Scope.NOT_DEFINED)
        self.MC = CIA(CIA.NONE)
        self.MI = CIA(CIA.NONE)
        self.MA = CIA(CIA.NONE)
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

    def _update_bs(self):
        if self.base_score is not None:
            txt = """
                <html><body><p align="center"><span style=" font-weight:600;">
                {:s}
                </span></p></body></html>""".format(str(self.base_score))
            self.baseScoreLabel.setText(txt)

    def _update_ts(self):
        if self.temporal_score is not None:
            txt = """
                <html><body><p align="center"><span style=" font-weight:600;">
                {:s}
                </span></p></body></html>""".format(str(self.temporal_score))
            self.temporalScoreLabel.setText(txt)

    def _update_es(self):
        if self.environmental_score is not None:
            txt = """
                <html><body><p align="center"><span style=" font-weight:600;">
                {:s}
                </span></p></body></html>""".format(str(self.environmental_score))
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
        if self.S is None:
            return None
        miss = modified_impact_subscore(
            self.S, self.MC, self.MI, self.MA, self.CR, self.IR, self.AR
        )
        mess = modified_exploitability_subscore(self.MAV, self.MAC, self.MPR, self.MUI)
        return environmental_score(self.S, miss, mess, self.E, self.RL, self.RC)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = CVSSCalc()
    calc.show()
    sys.exit(app.exec_())
