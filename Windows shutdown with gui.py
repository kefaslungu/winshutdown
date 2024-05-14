#import the Thread object from the threading module
from threading import Thread as t
#importing the os module and the wxpython package
import os, wx

class Frame(wx.Frame):

    def __init__(self):
        super().__init__(None, wx.ID_ANY, title = "Advance windows shutdown with gui")

        #call the showMenubar method here;
        self.showMenubar()

        pnl = wx.Panel(self)

        self.btnImplementor(pnl)    #call the btnImplementor method
        self.Show()    #makes the frame visible

    #a method that create a menubar 
    def showMenubar(self):
        menubar = wx.MenuBar()

        #the file menu item
        fileMenu = wx.Menu()
        file_quitItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        self.Bind(wx.EVT_MENU, self.on_quit, file_quitItem)    #binding the event to the file_quitItem)
        menubar.Append(fileMenu, '&File')

        advancedMenu = wx.Menu()
        first_option = advancedMenu.Append(wx.ID_ANY, 'Shutdown the computer. On the next boot, if Automatic Restart Sign-On is enabled, automatically sign in and lock last interactive user.')
        self.Bind(wx.EVT_MENU, self.on_one, first_option)
        second_option = advancedMenu.Append(wx.ID_ANY, 'Full shutdown and restart the computer. After the system is rebooted, if Automatic Restart Sign-On is enabled, automatically sign in and lock last interactive user. After sign in, restart any registered applications.')
        self.Bind(wx.EVT_MENU, self.on_two, second_option)
        third_option = advancedMenu.Append(wx.ID_ANY, 'Performs a shutdown of the computer and prepares it for fast startup.')
        self.Bind(wx.EVT_MENU, self.on_three, third_option)
        fourth_option = advancedMenu.Append(wx.ID_ANY, 'Cause the next boot to go to the firmware user interface if your system supports it.', 'a required Privilege  must be held by the client')
        self.Bind(wx.EVT_MENU, self.on_four, fourth_option)
        fifth_option = advancedMenu.Append(wx.ID_ANY, 'Go to the advanced boot options menu and restart the computer.')
        self.Bind(wx.EVT_MENU, self.on_two, fifth_option)
        menubar.Append(advancedMenu, '&Advanced')

        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        menubar.Append(helpMenu, '&Help')

        self.SetMenuBar(menubar)

    #a method that creates a button and binds it an event
    def createBtn(self, parent, label, handler):
        btn = wx.Button(parent, wx.ID_ANY, label)    #instantiating the button class
        #binds the button to an event
        btn.Bind(wx.EVT_BUTTON, handler)
        return btn

    #a method that implemetns the buttons on the panel
    def btnImplementor(self, parent):
        #a variable that holds nested tuple of required arguments of the createBtn method.
        tupleArgs = (('Shutdown', self.on_shutdown), ('restart', self.on_restart), ('Sign out', self.on_sign_out), ('Puts This PC to sleep', self.on_sleep), ('hibernate', self.on_hibernate), ('power off', self.on_power),('abort operation', self.on_abort),)
        #unpack the tupleArgs by iterating through
        for label, handler in tupleArgs:
            self.createBtn(parent, label, handler)

    #various event handlers 
    #event handler for closing the window
    def on_quit(self, e):
        self.Close()

    #an event for shutting down the pc
    def on_shutdown(self, e):
        t1 = t(target=os.system, args=("shutdown /s",))
        t1.start()

    def on_power(self, e):
        t1 = t(target=os.system, args=("shutdown /p",))
        t1.start()
        
    def on_abort(self, e):
        t1 = t(target=os.system, args=("shutdown /a",))
        t1.start()
        
    def on_restart(self, e):
        t1 = t(target=os.system, args=("shutdown /r",))
        t1.start()

    def on_sign_out(self, e):
        t1 = t(target=os.system, args=("shutdown /l",))
        t1.start()

    def on_sleep(self, e):
        t1 = t(target=os.system, args=("powercfg -h off",))
        t2 = t(target=os.system, args=("rundll32.exe powrprof.dll,SetSuspendState 0,1,0",))
        t3 = t(target=os.system, args=("powercfg -h on",))
        t1.start()
        t2.start()
        t3.start()

    def on_hibernate(self, e):
        t1 = t(target=os.system, args=("powercfg -h on",))
        t2 = t(target=os.system, args=("rundll32.exe powrprof.dll,SetSuspendState 0,1,0",))
        t3 = t(target=os.system, args=("powercfg -h off",))
        t1.start()
        t2.start()
        t3.start()

    def on_one(self, e):
        t1 = t(target=os.system, args=("shutdown /sg",))
        t1.start()

    def on_two(self, e):
        t1 = t(target=os.system, args=("shutdown /g",))
        t1.start()

    def on_three(self, e):
        t1 = t(target=os.system, args=("shutdown /s /hybrid",))
        t1.start()

    def on_four(self, e):
        t1 = t(target=os.system, args=("shutdown /s /fw",))
        t1.start()

    def on_five(self, e):
        t1 = t(target=os.system, args=("shutdown /r /o",))
        t1.start()

    def OnAbout(self, event):
        wx.MessageBox("this is a simple application, that helps you handle more advanced shutting down tasks, instead of typing long string of text on your windows terminal. It gives you lot of option to select from, please contact the developer for more info.",
        "About Advance windows shutdown with gui",
        wx.OK|wx.ICON_INFORMATION)

if(__name__ == '__main__'):
    app = wx.App()    #have to instantiates the App class
    frame = Frame()    #instantiate the Frame subclass above
    app.MainLoop()    #call the App's MainLoop method to handle waiting events
