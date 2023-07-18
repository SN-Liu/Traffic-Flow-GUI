import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QFileDialog,QWidget
from build_page import Ui_Form
from PyQt5.uic import loadUi
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QComboBox
import traffic_flow
import os
from PyQt5.QtGui import QScreen,QGuiApplication

class gui_main(QMainWindow):

    def __init__(self):
        super().__init__()
        loadUi('gui.ui',self)
        
        
        #读取testrun信息
        self.file_path = ''
        self.lane_length_all = -1
        self.lane_number = -1
        self.road_type = ''
        self.speed_limit = -1
        #设置交通目标占比
        self.Traffic_object_P = {
            'Car':0.55,         #小客车
            'Van':0.2,          #小货车
            'Truck':0.25        #大货车&大客车
        }
        #设置交通流参数
        self.range_start1 = -1
        self.range_end1 = -1
        self.traffic_flow_density1 = -1
        self.traffic_flow_state1 = ''
        self.traffic_flow_number1 = -1
        self.traffic_flow_character1 = 'Aggressive'
        self.traffic_flow_velocity1 = -1
        #是否为混合流
        self.is_mixed = False
        #设置混合流参数
        self.range_start2 = -1
        self.range_end2 = -1
        self.traffic_flow_density2 = -1
        self.traffic_flow_state2 = ''
        self.traffic_flow_number2 = -1
        self.traffic_flow_character2 = ''
        self.traffic_flow_velocity2 = -1
        

        #读取Testrun
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.file_dialog_opened = False
        #小客车占比
        self.lineEdit_6.editingFinished.connect(self.read_input_value)
        #小货车占比
        self.lineEdit_7.editingFinished.connect(self.read_input_value)
        #大货车占比
        self.lineEdit_8.editingFinished.connect(self.read_input_value)
        #交通流起点
        self.lineEdit_9.editingFinished.connect(self.read_input_value)
        #混合流起点
        self.lineEdit_16.editingFinished.connect(self.read_input_value)
        #交通流终点
        self.lineEdit_10.editingFinished.connect(self.read_input_value)
        #混合流终点
        self.lineEdit_17.editingFinished.connect(self.read_input_value)
        #交通流密度
        self.lineEdit_11.editingFinished.connect(self.read_input_value)
        #混合流密度
        self.lineEdit_15.editingFinished.connect(self.read_input_value)
        #交通流性格
        self.comboBox.currentIndexChanged.connect(self.read_traffic_character)
        #混合流性格
        self.comboBox_2.currentIndexChanged.connect(self.read_traffic_character)
        #交通流速度
        self.lineEdit_14.editingFinished.connect(self.read_input_value)
        #混合流速度
        self.lineEdit_18.editingFinished.connect(self.read_input_value)
        #是否为混合流
        self.checkBox.stateChanged.connect(self.mixed_traffic_flow)
        #生成交通流
        self.pushButton_2.clicked.connect(self.generate_traffic_flow)
            

    def on_pushButton_clicked(self):
        if not self.file_dialog_opened:
            self.file_dialog_opened = True
            file_path, _ = QFileDialog.getOpenFileName(self,'选择文件')
            self.file_path = file_path
            if file_path:
                self.process_selected_file(file_path)

    def process_selected_file(self,file_path):
        self.lineEdit.setText(file_path)
        with open(file_path,'r') as file:
            lines = file.readlines()
            
            for line in lines:
                if line.startswith('Road.RoadNetworkLength'):
                    key, value = line.split('=')
                    self.lane_length_all = float(value.strip())
                    self.lineEdit_2.setText(str(self.lane_length_all) + 'm')

                if line.startswith('Road.nRoutes'):
                    key, value = line.split('=')
                    self.lane_number = int(value.strip())
                    self.lineEdit_3.setText(str(self.lane_number))

                if line.startswith('Road.Link.0.RST'):
                    key,value = line.split('=')
                    self.road_type = value.strip()
                    self.lineEdit_4.setText(self.road_type)

                if line.startswith('Road.RST'):
                    key,value = line.split('=')
                    RST = value.split()
                    
            if self.road_type == 'Urban':
                self.speed_limit = RST[0]
            elif self.road_type == 'Countryroad':
                self.speed_limit = RST[1]
            elif self.road_type == 'Motorway':
                self.speed_limit = RST[2]
            elif self.road_type == 'Roundabout':
                self.speed_limit = RST[3]
            elif self.road_type == 'Ramp':
                self.speed_limit = RST[4]
            elif self.road_type == 'Dirttrack':
                self.speed_limit = RST[5]
            self.lineEdit_5.setText(str(self.speed_limit)+'km/h')
    
    def read_input_value(self):
        line_edit = self.sender()
        if isinstance(line_edit,QObject):
            if line_edit.objectName() == 'lineEdit_6':
                self.Traffic_object_P['Car'] = float(line_edit.property('text'))
            elif line_edit.objectName() == 'lineEdit_7':
                self.Traffic_object_P['Van'] = float(line_edit.property('text'))
            elif line_edit.objectName() == 'lineEdit_8':
                self.Traffic_object_P['Truck'] = float(line_edit.property('text'))

            elif line_edit.objectName() == 'lineEdit_9':
                self.range_start1 = float(line_edit.property('text'))
            elif line_edit.objectName() == 'lineEdit_10':
                self.range_end1 = float(line_edit.property('text'))

            elif line_edit.objectName() == 'lineEdit_11':
                self.traffic_flow_density1 = int(line_edit.property('text'))
                self.traffic_flow_number1 = round(self.traffic_flow_density1 * ((self.range_end1 - self.range_start1)/1000))

                density1 = (self.traffic_flow_number1 * 1609) /((self.range_end1 - self.range_start1) * self.lane_number)
                if density1 < 12:
                    self.traffic_flow_state1 = 'free'
                    self.traffic_flow_velocity1 = 95
                elif density1 > 12 and density1 < 30:
                    self.traffic_flow_state1 = 'stable'
                    self.traffic_flow_velocity1 = 67
                elif density1 > 30 :
                    self.traffic_flow_state1 = 'unstable'
                    self.traffic_flow_velocity1 = 20

                self.lineEdit_12.setText(self.traffic_flow_state1)
                self.lineEdit_13.setText(str(self.traffic_flow_number1))
                self.lineEdit_14.setText(str(self.traffic_flow_velocity1))

            elif line_edit.objectName() == 'lineEdit_14':
                self.traffic_flow_velocity1 = float(line_edit.property('text'))

            #混合流参数
            elif line_edit.objectName() == 'lineEdit_16':
                self.range_start2 = float(line_edit.property('text'))
            elif line_edit.objectName() == 'lineEdit_17':
                self.range_end2 = float(line_edit.property('text'))
            
            elif line_edit.objectName() == 'lineEdit_15':
                self.traffic_flow_density2 = int(line_edit.property('text'))
                self.traffic_flow_number2 = round(self.traffic_flow_density2 * ((self.range_end2 - self.range_start2)/1000))

                density2 = (self.traffic_flow_number2 * 1609) /((self.range_end2 - self.range_start2) * self.lane_number)
                if density2 < 12:
                    self.traffic_flow_state2 = 'free'
                    self.traffic_flow_velocity2 = 95
                elif density2 > 12 and density2 < 30:
                    self.traffic_flow_state2 = 'stable'
                    self.traffic_flow_velocity2 = 67
                elif density2 > 30 :
                    self.traffic_flow_state2 = 'unstable'
                    self.traffic_flow_velocity2 = 20

                self.lineEdit_19.setText(self.traffic_flow_state2)
                self.lineEdit_20.setText(str(self.traffic_flow_number2))
                self.lineEdit_18.setText(str(self.traffic_flow_velocity2))

            elif line_edit.objectName() == 'lineEdit_18':
                self.traffic_flow_velocity2 = float(line_edit.property('text'))

    def read_traffic_character(self):
        combobox = self.sender()
        if isinstance(combobox,QComboBox):
            if combobox.objectName()  == 'comboBox':
                self.traffic_flow_character1 = combobox.currentText()
            elif combobox.objectName() == 'comboBox_2':
                self.traffic_flow_character2 = combobox.currentText()
    
    def mixed_traffic_flow(self):
        self.is_mixed = self.checkBox.isChecked()

    def generate_traffic_flow(self):
        new_path = os.path.join(os.path.dirname(self.file_path),r'NewTestRun')
        new_path = new_path.replace('\\','/')
        self.lineEdit_21.setText(new_path)

        #不是混合流
        if self.is_mixed == False:
            traffic_flow.traffic_generate('traffic1.txt',self.lane_number,self.Traffic_object_P,self.range_start1,self.range_end1,self.traffic_flow_density1,self.traffic_flow_character1,self.traffic_flow_velocity1)
            traffic_flow.traffic_mixed('traffic1.txt','traffic2.txt',self.traffic_flow_number1,self.traffic_flow_number2)
            traffic_flow.traffic_write(self.file_path,new_path)

        #是混合流
        elif self.is_mixed == True:
            traffic_flow.traffic_generate('traffic1.txt',self.lane_number,self.Traffic_object_P,self.range_start1,self.range_end1,self.traffic_flow_density1,self.traffic_flow_character1,self.traffic_flow_velocity1)
            traffic_flow.traffic_generate('traffic2.txt',self.lane_number,self.Traffic_object_P,self.range_start2,self.range_end2,self.traffic_flow_density2,self.traffic_flow_character2,self.traffic_flow_velocity2)
            traffic_flow.traffic_mixed('traffic1.txt','traffic2.txt',self.traffic_flow_number1,self.traffic_flow_number2)
            traffic_flow.traffic_write(self.file_path,new_path)

        


if __name__ == '__main__':
    app = QApplication([])
    
    traffic_flow_gui = gui_main()

    traffic_flow_gui.resize(800,1000)

    screen = QGuiApplication.primaryScreen()

    screen_geometry = screen.geometry()

    x = (screen_geometry.width() - traffic_flow_gui.width()) // 2 
    y = (screen_geometry.width() - traffic_flow_gui.width()) // 2

    traffic_flow_gui.move(x,y)

    traffic_flow_gui.show()

    sys.exit(app.exec_())