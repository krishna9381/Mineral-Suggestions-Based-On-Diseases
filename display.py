from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QFileDialog
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5 import uic, QtCore
import sys
import tensorflow as tf
import cv2
import colorama
from colorama import Fore
import urllib.parse



def is_diseased(name):

	if name == "Black_rot":
		return  "---------GRAPE--BLACK ROT---------\n\nGRAPE BLACK ROT is a fungal disease caused by an ascomycetous fungus \n\nSYMPTOMS : \nSmall, brown circular lesions on leaves, mummies on fruits \n\nDANGER : YES"

	elif name=="Esca_(Black_Measles)":

		return  "---------GRAPE--ESCA_(BLACK_MEASLES)---------\n\nESCA is a grape disease of mature grapevines. It is a type of grapevine trunk disease. sometimes called Apoplexy (severe infections)\n\nSYMPTOMS :\n1.Purple/Black blemishes found on the fruit\n2.Characterized by a ‘tiger stripe’ pattern on leaves \n3.Chlorosis (in white grapes), or reddening (in black grapes) followed by necrosis,\n\nDANGER  : YES"

	elif name=="Leaf_blight_(Isariopsis_Leaf_Spot)":
		return  "---------GRAPE--LEAF_BLIGHT---------\n\nLEAF BLIGHT also called as ISARIOPSIS LEAF SPOT \n\nSYMPTOMS :\nProduces dark brown patches on the surface of grape leaves. yellow-green disease spots\n\nDANGER : MODERATE"
	elif  name=="Healthy":
		return  "---------GRAPE--HEALTHY---------\n\n---------BINGO!---------\n\nEverything is fine You will have A Great Yield "


def mineral_deficiency(name):
    if name == "Black_rot":
        return  "\n\n---------BLACK ROT---------\n\nMINERAL_DEFICIENCY :\nCalcium, Manganese, Iron ,Born,Nitrogen\n\nCAUSAL AGENTS :\nDrought conditions or low Calcium mineral content \n\nTREATMENT : \nWatering or calcium-rich fertilizers"
    elif name == "Esca_(Black_Measles)":
        return  "\n\n---------ESCA_(BLACK_MEASLES)---------\n\nMINERAL_DEFICIENCY :\nNitogen,Phosporus,Magnesium\n\nTREATMENT : \nTill date there is no effective method to control this disease.\nRemove the infected berries, leaves and trunk and destroy them.\nProtect the prune wounds to minimize fungal infection using wound sealant (5% boric acid in acrylic paint) or essential oil or suitable fungicides. "

    elif name == "Leaf_blight_(Isariopsis_Leaf_Spot)":
        return "\n\n---------LEAF_BLIGHT---------\n\nMINERAL_DEFICIENCY :\nPotassium ,Boron ,Zinc,Nitrogen,Magnesium,Sulpur \n\nTREATMENT :\nProvide proper aeration keep soil clean.Throw the dead and diseased leaves.\nReduce overcrowding of your plants Pruning of plants"

    elif name == "Healthy":
        return "\n\n--------- HEALTHY_LEAVES---------" 
def linkf1(name):
    if name == "Black_rot":
        s=urllib.parse.quote('en.wikipedia.org/wiki/Black_rot_(grape_disease)')
        return  "\n\nLINK TO REFER\n"+'------------------'+"\n-->https://"+s
    elif name == "Esca_(Black_Measles)":
        s=urllib.parse.quote('grapes.extension.org/grapevine-measles/')
        return  "\n\nLINK TO REFER\n"+'------------------'+"\n-->https://"+s
    elif name == "Leaf_blight_(Isariopsis_Leaf_Spot)":
        s=urllib.parse.quote('vikaspedia.in/agriculture/crop-production/integrated-pest-managment/ipm-for-fruit-crops/ipm-strategies-for-grapes/grapes-diseases-and-symptoms')
        return  "\n\nLINK TO REFER\n"+'------------------'+"\n-->https://"+s
    elif name == "Healthy":
        s = urllib.parse.quote('drhealthbenefits.com/herbal/leaves/health-benefits-of-grape-leaves')
        return  "\n\nLINK TO REFER\n"+'------------------'+"\n-->https://"+s
def linkf2(name):
    s=urllib.parse.quote('www.homedepot.com/c/ah/how-to-grow-grapes/9ba683603be9fa5395fab901cdee46ea')
    return '\n\nFEW TIPS FOR GROWTH\n-----------------------------\n-->https://'+s
def linkf3(name):
    return ''
def linkf4(name):
    return ''
def finalans():
    s=urllib.parse.quote('vikaspedia.in/agriculture/crop-production/integrated-pest-managment/ipm-for-fruit-crops/ipm-strategies-for-grapes/grapes-diseases-and-symptoms')
    return '\n\nCOMMON LINK FOR ALL OTHER GRAPE DISEASES\n'+"----------------------------------------------------------"+'\n-->https://'+s
def res():
    s=urllib.parse.quote('www.agr.gc.ca/eng/agriculture-and-the-environment/agricultural-pest-management/agricultural-pest-management-resources/identification-guide-to-the-major-diseases-of-grapes/?id=1544449361476')

    return "\n\nIF OTHER MAJOR DISEASES GO WITH THIS LINK\n"+"----------------------------------------------------------"+"\n-->https://"+s


def gotoHome():
    window.setCurrentWidget(home)


def gotoDisplay():
    img = QPixmap(preprocessing.file[0])
    display.image.setPixmap(img)
    display.image.setScaledContents(True)
    window.setCurrentWidget(display)

def gotoPreprocessing():
    window.setCurrentWidget(preprocessing)


class Home(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Home.ui',self)
        self.Start.clicked.connect(gotoPreprocessing)
        img = QPixmap('background.jpeg')
        self.bg.setPixmap(img)
        self.bg.setScaledContents(True)


class Preprocessing(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Preprocessing.ui',self)
        self.Home.setIcon(QIcon('Icons/Home.png'))
        self.Home.setIconSize(QtCore.QSize(28, 28))
        self.preprocessing.clicked.connect(gotoDisplay)
        self.Input.clicked.connect(self.browsefiles)
        self.Home.clicked.connect(gotoHome)
        img = QPixmap('background.jpeg')
        self.bg.setPixmap(img)
        self.bg.setScaledContents(True)
        self.gotresult = ''
        self.gotmindef = ''
        self.link1 = ''
        self.link2=''
        self.link3=''
        self.link4=''
        self.final = ' '
        self.res=''

    def browsefiles(self):
        self.file = QFileDialog.getOpenFileName(self,'openfile','E:/Projects/vamshi')
        img = cv2.imread(self.file[0])
        img = cv2.resize(img,(256,256))
        img = img.reshape(-1, 256, 256, 3)
        predict_class = new_model.predict_classes(img)
        categories = ["Black_rot", "Esca_(Black_Measles)", "Healthy", "Leaf_blight_(Isariopsis_Leaf_Spot)"]
        name = categories[predict_class[0]]
        self.gotresult = is_diseased(name)
        self.gotmindef = mineral_deficiency(name)
        self.link1 = linkf1(name)
        self.link2 = linkf2(name)
        self.link3= linkf3(name)
        self.link4= linkf4(name)
        self.final=finalans()
        self.res=res()



class Display(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Display.ui',self)
        self.Home.setIcon(QIcon('Icons/Home.png'))
        self.Home.setIconSize(QtCore.QSize(28, 28))
        self.Back.setIcon(QIcon('Icons/Back.png'))
        self.Back.setIconSize(QtCore.QSize(28, 28))
        self.Home.clicked.connect(gotoHome)
        self.Back.clicked.connect(self.gotoBack)
        self.analyse.clicked.connect(self.gotoAnalyse)
        img = QPixmap('background.jpeg')
        self.bg.setPixmap(img)
        self.bg.setScaledContents(True)

    def gotoAnalyse(self):
        Dia = preprocessing.gotresult
        mindef = preprocessing.gotmindef
        link1 = preprocessing.link1
        link2=preprocessing.link2
        link3=preprocessing.link3
        link4=preprocessing.link4
        final=preprocessing.final
        res=preprocessing.res
        disease.result.setText(Dia + mindef + '\n' + link1+link2+link3+link4+final+res)
        window.setCurrentWidget(disease)

    def gotoBack(self):
        window.setCurrentWidget(preprocessing)


class Disease(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('disease.ui',self)
        self.Home.setIcon(QIcon('Icons/Home.png'))
        self.Home.setIconSize(QtCore.QSize(28, 28))
        self.Back.setIcon(QIcon('Icons/Back.png'))
        self.Back.setIconSize(QtCore.QSize(28, 28))
        self.Home.clicked.connect(gotoHome)
        self.Back.clicked.connect(self.gotoBack)
        img = QPixmap('background.jpeg')
        self.bg.setPixmap(img)
        self.bg.setScaledContents(True)

    def gotoBack(self):
        window.setCurrentWidget(display)


new_model = tf.keras.models.load_model("leaf_disease_coloured.h5")
app = QApplication([])
window = QStackedWidget()
home = Home()
preprocessing = Preprocessing()
display = Display()
disease = Disease()
window.addWidget(home)
window.addWidget(preprocessing)
window.addWidget(display)
window.addWidget(disease)
window.setFixedWidth(1000)
window.setFixedHeight(600)
window.show()
sys.exit(app.exec())