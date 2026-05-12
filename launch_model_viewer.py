#!/usr/bin/env python3
# X-Seti - Model-Viewer launcher
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from apps.components.Model_Viewer.model_viewer import open_model_viewer
from PyQt6.QtWidgets import QApplication
if __name__ == '__main__':
    try:
        from PyQt6.QtGui import QSurfaceFormat
        f=QSurfaceFormat(); f.setProfile(QSurfaceFormat.OpenGLContextProfile.CompatibilityProfile)
        f.setVersion(2,1); QSurfaceFormat.setDefaultFormat(f)
    except Exception: pass
    app = QApplication(sys.argv)
    w = open_model_viewer()
    sys.exit(app.exec())
