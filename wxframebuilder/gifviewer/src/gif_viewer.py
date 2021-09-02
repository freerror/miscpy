import os
import wx
import gif_viewer_fb

# inheret from frameMain from our fb generated code
class frameMainApp(gif_viewer_fb.frameMain):
    # constructor
    def __init__(self, parent):
        # app variables
        self.dir_path = None

        # parent constructor
        gif_viewer_fb.frameMain.__init__(self, parent)

    # events we are overriding
    def m_dirPicker2OnDirChanged(self, event):
        self.change_dir(event)

    def m_listBoxFilesOnListBox(self, event):
        self.play_gif(event)

    def buttonPlayOnButtonClick(self, event):
        self.mediaCtrlAnim.Play()

    # our own event handlers
    def change_dir(self, event):
        self.dir_path = event.GetPath()
        self.populate_list(self.dir_path)

    def populate_list(self, cur_path):
        self.listBoxFiles.Clear()
        for file in os.listdir(cur_path):
            if file.endswith('.gif'):
                self.listBoxFiles.Append(file)

    def play_gif(self, event):
        try:
            # create full path to file
            anim_file = os.path.join(self.dir_path,
                                     event.GetString())
            # animate
            self.animCtrl.LoadFile(anim_file)
            self.animCtrl.Play()
            self.animCtrl.SetSize(-1,-1)
            self.animCtrl.Centre()
        except Exception as exc:
            print(f"Computer says no: {exc}")
app = wx.App()
frame = frameMainApp(None)
frame.Show(True)
app.MainLoop()