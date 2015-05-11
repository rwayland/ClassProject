import wx

class DialogQuestion(wx.Dialog):
    '''
        Name: DialogQuestion
        Description:  Dialogbox that displays a question and four possible answers
    '''
    def __init__(self,question,questionChoices):
        '''
            Name:__init__
            Description: Main constructor
            Ins:
                self - class variable
                question - string representing a question
                queestionChoices - list of string representing answer to a question
        '''

        #init parent
        wx.Dialog.__init__(self,None,wx.ID_ANY,'Question')

        #Main Sizer
        szMain = wx.BoxSizer(wx.VERTICAL)

        ques = wx.StaticText(self,-1,question)
        szMain.Add(ques)

        #Questions
        choices = []
        for question in questionChoices:
            choice = wx.RadioButton(self,-1,question)
            choices.append(choice)
            szMain.Add(choice)

        btnSubmit = wx.Button(self,wx.ID_OK,'Submit')
        szMain.Add(btnSubmit)

        self.SetSizerAndFit(szMain)
        self.choices = choices

    def getSelection(self):
        '''
            Name: getSelection
            Description:  Return the selection
            In: self - class varaible
        '''
        cnt = 0
        val = 0
        for choice in self.choices:
            if choice.GetValue():
                val = cnt
            cnt += 1

        return val
        
class FrameTest(wx.Frame):
    '''
    def __init__(self,mainFrame):
        '''
        '''
        wx.Frame.__init__(self,None)

        szMain = wx.BoxSizer()

        btnQuestion = wx.Button(self,-1,'Question')
        self.Bind(wx.EVT_BUTTON,self.question,btnQuestion)

        btnAdvance = wx.Button(self,-1,'Advance')
        self.Bind(wx.EVT_BUTTON,self.advancePlayer1,btnAdvance)

        btnCake = wx.Button(self,-1,'Cake')
        self.Bind(wx.EVT_BUTTON,self.awardCake,btnCake)

        szMain.Add(btnQuestion)
        szMain.Add(btnAdvance)
        szMain.Add(btnCake)

        self.mainFrame = mainFrame

        self.SetSizer(szMain)

    def question(self,event):
        ques = 'This is a question!'
        choices = ['A','B','C','D']

        dlg = DialogQuestion(ques,choices)

        if dlg.ShowModal() == wx.ID_OK:
            val = dlg.getSelection()
            print(val)

        dlg.Destroy()
        
def main():
    app = wx.PySimpleApp()

    frm = FrameTest(frmTrival)
    frm.Show()

    app.MainLoop()

if __name__ == '__main__':
    main()
