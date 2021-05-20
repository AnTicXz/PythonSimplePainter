#Sources: 
#https://stackoverflow.com/questions/41688668/how-to-return-mouse-coordinates-in-realtime
#https://stackoverflow.com/questions/52517516/pyqt5-fixed-window-size
#https://www.geeksforgeeks.org/python-how-to-save-canvas-in-pyqt5/


#Bevan E

from PyQt5.QtWidgets import QMainWindow,QFileDialog, QApplication, QPushButton, QLabel, QGridLayout, QAction, QInputDialog
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QColor
from PyQt5.QtCore import Qt, QPoint
import sys

global R,B,G,R_pen,G_pen,B_pen


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1400, 1000)
        self.setMouseTracking(True)
        
       
        R = 0
        G = 200
        B = 200
        
        R_pen = 200
        G_pen = 0
        B_pen = 0
        
        menuBar = self.menuBar()
        Menu = menuBar.addMenu("Background Color")
        
        ColorMenu = menuBar.addMenu("Brush Color")
        
        Color2Menu = menuBar.addMenu("Brush Size")
        
        SaveOrClear = menuBar.addMenu("Save or clear")
        
        action = QAction("Edit BackGround color", self)
        action.triggered.connect(self.editcolor)
        
        action2 = QAction("Edit brush Color", self)
        action2.triggered.connect(self.editbrushcolor)
        
        action3 = QAction("Edit brush size", self)
        action3.triggered.connect(self.brushsize)
        
        ActionBackRed = QAction("Red",self)
        ActionBackRed.triggered.connect(self.back_red)
        
        ActionBackyellow = QAction("yellow",self)
        ActionBackyellow.triggered.connect(self.back_yellow)
        
        ActionBackblue = QAction("blue",self)
        ActionBackblue.triggered.connect(self.back_blue)
        
        ActionBackgreen = QAction("green",self)
        ActionBackgreen.triggered.connect(self.back_green)
        
        ActionBackblack = QAction("black",self)
        ActionBackblack.triggered.connect(self.back_black)
        
        #saving and clearing
        ActionSave = QAction("Save Canvas",self)
        ActionSave.triggered.connect(self.Save)
        
        Clear = QAction("Clear Canvas",self)
        Clear.triggered.connect(self.Clear)
        
       #brushes
        ActionBrushRed = QAction("Red", self)
        ActionBrushRed.triggered.connect(self.Brush_red)
        
        ActionBrushyellow = QAction("yellow", self)
        ActionBrushyellow.triggered.connect(self.Brush_yellow)
        
        ActionBrushblue = QAction("blue", self)
        ActionBrushblue.triggered.connect(self.Brush_blue)
        
        ActionBrushgreen = QAction("green", self)
        ActionBrushgreen.triggered.connect(self.Brush_green)
        
        ActionBrushblack = QAction("black", self)
        ActionBrushblack.triggered.connect(self.Brush_black)
        
        
       
        
       #background
        #Menu.addAction("Will update on next click")
        Menu.addAction(action)
        Menu.addAction(ActionBackRed)
        Menu.addAction(ActionBackyellow)
        Menu.addAction(ActionBackblue)
        Menu.addAction(ActionBackblack)
        Menu.addAction(ActionBackgreen)
        
        
        ColorMenu.addAction(action2)
        #Brushes
        ColorMenu.addAction(ActionBrushRed)
        ColorMenu.addAction(ActionBrushyellow)
        ColorMenu.addAction(ActionBrushblue)
        ColorMenu.addAction(ActionBrushgreen)
        ColorMenu.addAction(ActionBrushblack)
        
        Color2Menu.addAction(action3)
        Menu.addAction(ActionBackRed)
        
        #saving and clearing
        SaveOrClear.addAction(ActionSave)
        SaveOrClear.addAction(Clear)
        
       

        title = "CS272 Painter"
        top = 400
        left = 400
        width = 800
        height = 600


        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QIcon("paint.png"))
        
          
        """
        fill_color = {
            1: Qt.red,
            #2: Qt.orange,
            3: Qt.yellow,
            4: Qt.blue,
            5: Qt.green,
            6: Qt.black,
            #7: Qt.purple,
            #8: Qt.pink,
            }
        """
        
        
       
       
        
        fill_color = QColor(R,G,B)
        
        Pen_color = QColor(R_pen,G_pen,B_pen)
        
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(fill_color)
        
       
        self.drawing = False
        self.brushSize = 4
        self.brushColor = Pen_color
        self.lastPoint = QPoint()
        
    def Brush_red(self):
        self.brushColor = Qt.red
    def Brush_yellow(self):
        self.brushColor = Qt.yellow
    def Brush_blue(self):
        self.brushColor = Qt.blue
    def Brush_green(self):
        self.brushColor = Qt.green
    def Brush_black(self):
        self.brushColor = Qt.black
        
        
    def back_red(self):
        self.image.fill(Qt.red) 
        self.update()
    def back_yellow(self):
        self.image.fill(Qt.yellow) 
        self.update()
    def back_blue(self):
        self.image.fill(Qt.blue) 
        self.update()
    def back_green(self):
        self.image.fill(Qt.green) 
        self.update()
    def back_black(self):
        self.image.fill(Qt.black) 
        self.update()
        
    def brushsize(self):
            x = QInputDialog.getText(self,"Brush size","size")
            print(x)
            self.brushSize = int(x[0])
    

    def editcolor(self):
            title = "Edit Background color"
            
            R= QInputDialog.getText(self,title,"Red")
            #print(R[0])
            G = QInputDialog.getText(self,title,"Green")
            B = QInputDialog.getText(self,title,"Blue")
            color = QColor(int(R[0]),int(G[0]),int(B[0]))
            self.image.fill(color)
   
    def editbrushcolor(self):
            title = "Edit Brush color"
            
            R_pen = QInputDialog.getText(self,title,"Red")
            #print(R[0])
            G_pen = QInputDialog.getText(self,title,"Green")
            B_pen = QInputDialog.getText(self,title,"Blue")
            Pen_color = QColor(int(R_pen[0]),int(G_pen[0]),int(B_pen[0]))
            self.brushColor = Pen_color
            
            
            
    file = open("Cords.txt", "w")
    file.close()       

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()
            
            file = open("Cords.txt", "a")
            
            X = str(self.lastPoint)
            First = X.split("(")
            Second = First[1].split(")")
            file.write(Second[0])
            file.write("\n")
            
            
            

    def mouseMoveEvent(self, event):
        if(event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize)) # Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()
            
            file = open("Cords.txt", "a")
            
            X = str(self.lastPoint)
            First = X.split("(")
            Second = First[1].split(")")
            file.write(Second[0])
            file.write("\n")
            


    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False
            
            file = open("Cords.txt", "a")
            file.close()



    def paintEvent(self, event):
        canvasPainter  = QPainter(self)
        canvasPainter.begin(self)
        canvasPainter.drawImage(self.rect(),self.image)
        canvasPainter.end()

    def Save(self):
        #Sorced from: https://www.geeksforgeeks.org/python-how-to-save-canvas-in-pyqt5/
        
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", 
                         "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        if filePath == "": 
            return
        
        self.image.save(filePath)
        
    
    def Clear(self):
        self.image.fill(Qt.white)
        self.update()
           
            
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()