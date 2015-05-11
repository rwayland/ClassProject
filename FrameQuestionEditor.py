import wx

class FrameQuestionEditor(wx.Frame):
    '''
        Name: FrameQuestionEditor
        Description:  This class build a GUI for a question editor
    '''
    def __init__(self,parent,title):
        '''
            Name: __init__
            Description: Main class constructor
            In: self - class variable
            parent: parent to this frame
            title: title for the frame
        '''
        wx.Frame.__init__(self,parent,-1,title)

        szMain = wx.BoxSizer(wx.VERTICAL)

        #Category Dropdown
        szCatDrop = wx.BoxSizer(wx.HORIZONTAL)

        catDropDown = wx.ComboBox(self)
        btnLoadCat = wx.Button(self,-1,'Load Category')
        self.Bind(wx.EVT_BUTTON,self.OnLoadCategory,btnLoadCat)
        szCatDrop.Add(catDropDown)
        szCatDrop.Add(btnLoadCat)

        #Question Dropdown
        szQuesDrop = wx.BoxSizer(wx.HORIZONTAL)

        quesDropDown = wx.ComboBox(self)
        btnLoadQues = wx.Button(self,-1,'Load Question')
        self.Bind(wx.EVT_BUTTON,self.OnLoadQuestion,btnLoadQues)
        szQuesDrop.Add(quesDropDown)
        szQuesDrop.Add(btnLoadQues)

        #Question Body
        szBody = wx.BoxSizer(wx.HORIZONTAL)
        lblQues = wx.StaticText(self,-1,'Body')
        tbQues = wx.TextCtrl(self)
        szBody.Add(lblQues)
        szBody.Add(tbQues,1,wx.EXPAND)

        #Answers 1-4
        szAns = wx.BoxSizer(wx.HORIZONTAL)
        lblAns = wx.StaticText(self,-1,'Correct Answer')
        tbAns = wx.TextCtrl(self)
        szAns.Add(lblAns)
        szAns.Add(tbAns,1,wx.EXPAND)

        szAns2 = wx.BoxSizer(wx.HORIZONTAL)
        lblAns2 = wx.StaticText(self,-1,'Choice 1')
        tbAns2 = wx.TextCtrl(self)
        szAns2.Add(lblAns2)
        szAns2.Add(tbAns2,1,wx.EXPAND)

        szAns3 = wx.BoxSizer(wx.HORIZONTAL)
        lblAns3 = wx.StaticText(self,-1,'Choice 2')
        tbAns3 = wx.TextCtrl(self)
        szAns3.Add(lblAns3)
        szAns3.Add(tbAns3,1,wx.EXPAND)

        szAns4 = wx.BoxSizer(wx.HORIZONTAL)
        lblAns4 = wx.StaticText(self,-1,'Choice 3')
        tbAns4 = wx.TextCtrl(self)
        szAns4.Add(lblAns4)
        szAns4.Add(tbAns4,1,wx.EXPAND)

        #Add to main
        szMain.Add(szCatDrop)
        szMain.Add(szQuesDrop)
        szMain.Add(szBody,0,wx.EXPAND)
        szMain.Add(szAns,0,wx.EXPAND)
        szMain.Add(szAns2,0,wx.EXPAND)
        szMain.Add(szAns3,0,wx.EXPAND)
        szMain.Add(szAns4,0,wx.EXPAND)

        self.SetSizerAndFit(szMain)

        self.cbQuestion = quesDropDown
        self.cbCat = catDropDown
        self.question = tbQues
        self.answers = [tbAns,tbAns2,tbAns3,tbAns4]

    def loadQuestionDictionary(self,dicQuestion):
        '''
            Name: loadQuestionDictionary
            Description: Loads the question dictionary
            In: self - class variable
            dicQuestion - dictionary containing each dictionary of questions
        '''
        self.questionDict = dicQuestion

        cats = dicQuestion.keys()
##        ques = dicQuestion[cats[0]].keys()
        cats.sort()
        self.cbCat.SetItems(cats)
        self.cbCat.Select(0)
        self.loadCategory(cats[0])

        self.loadQuestion(self.curQues)

    def loadCategory(self,category):
        '''
            Name: loadCategory
            Description: loads the selected category
            In: self - class variable
                category - key in the category dictionary
        '''
        ques = self.questionDict[category]
        qs = ques.keys()
        qs.sort()
        self.cbQuestion.SetItems(qs)
        self.cbQuestion.Select(0)
        self.curCategory = category
        self.curQues = qs[0]

    def loadQuestion(self,question):
        '''
            Name: loadQuestion
            Description: load a question into the display
            In: self - class variable
                question - key in the question dictionary
        '''
        ques = self.questionDict[self.curCategory]
        newQues = ques[question]

        self.question.SetLabel(newQues[0])
        self.answers[0].SetLabel(newQues[1])
        self.answers[1].SetLabel(newQues[2])
        self.answers[2].SetLabel(newQues[3])
        self.answers[3].SetLabel(newQues[4])

        self.curQues = question

    def OnLoadCategory(self,event):
        '''
            Name: OnLoadCategory
            Description: event handler for load category button
            In: self - class variable
                event - event structure
        '''
        cati = self.cbCat.GetSelection()
        cat = self.cbCat.GetString(cati)
        self.loadCategory(cat)
        self.loadQuestion(self.curQues)

    def OnLoadQuestion(self,event):
        '''
            Name: OnLoadQuestion
            Description: Event handler for the load question button
            In: self - variable
                event - event structure
        '''
        seli = self.cbQuestion.GetSelection()
        sel = self.cbQuestion.GetString(seli)
        self.loadQuestion(sel)

def main():
    app = wx.PySimpleApp()

    frmQues = FrameQuestionEditor(None,'Question Editor')
    testQuestion(frmQues)
    frmQues.Show()

    app.MainLoop()

if __name__ == '__main__':
    main()
