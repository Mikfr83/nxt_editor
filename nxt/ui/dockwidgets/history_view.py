# Builtin
import logging

# External
from Qt import QtWidgets

# Internal
from dock_widget_base import DockWidgetBase

logger = logging.getLogger(__name__)


class HistoryView(DockWidgetBase):

    def __init__(self, parent=None):
        super(HistoryView, self).__init__(title='History View', parent=parent)
        self.undo_view = QtWidgets.QUndoView()
        self.setWidget(self.undo_view)

    def set_stage_model(self, model):
        super(HistoryView, self).set_stage_model(model)
        self.undo_view.setStack(model.undo_stack)
