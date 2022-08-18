from cmath import pi
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QFileDialog
import pyqtgraph
from pyqtgraph import PlotWidget
from Final1 import Ui_MainWindow
import numpy as np
import scipy
from scipy import signal
import matplotlib.pyplot as plt
import csv
import pandas as pd
from collections import Counter
from csv import writer
import qdarkstyle

signal_name=[]
FrequencyList=[]
Amplitude=[]
Occurenes=[]
added_signals_list=[0]  
time=np.linspace(0,2*pi,1000)
MaximumFrequency=0
Frequency=1
Magnitude=1
PhaseShift=45
Signal=0
ExcelCounter=0
loaded=-1
value=''
samplingvalue=0
currenttimeonillustrator=[]
currentsignalonillustrator=[0]

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionHide_Reconstructed_Signal.triggered.connect(lambda:self.Hide_Reconstructed(0))
        self.ui.actionShow_Reconstructed_Signal.triggered.connect(lambda: self.Hide_Reconstructed(1))
        self.ui.menuBrowse.triggered.connect(self.load)
        self.ui.actionSave_File.triggered.connect(self.save)
        self.ui.Preview_pushButton.clicked.connect(self.signal_preview)
        self.ui.Add_pushButton.clicked.connect(self.Addedsignals)
        self.ui.Delete_pushButton.clicked.connect(self.delete_item)
        self.ui.ViewInPrimary_pushButton.clicked.connect(self.Preview_onprimary)
        self.ui.Illustrator_Frequency_Slider.valueChanged[int].connect(self.ChangeSamplingRate)
        self.ui.A_Text.returnPressed.connect(lambda: self.signal_preview)
        self.ui.F_Text.returnPressed.connect(lambda: self.signal_preview)
        self.ui.Theta_Text.returnPressed.connect(lambda: self.signal_preview)

    def Hide_Reconstructed(self, input):
        if input==0:
            self.ui.Reconstructed_View.hide()
            self.ui.Reconstructed_Label.hide()
        else:
            self.ui.Reconstructed_View.show()
            self.ui.Reconstructed_Label.show()   

    def delete_item(self):
        global signal_name,added_signals_list,time,Frequency,Magnitude,PhaseShift,Signal,value,samplingvalue,FrequencyList,currenttimeonillustrator,currentsignalonillustrator,MaximumFrequency 
        clicked=self.ui.Signal_List.currentRow()
        print(FrequencyList[clicked])
        FrequencyList.pop(clicked)
        self.Find_Max_Frequency()
        print(MaximumFrequency)
        self.ui.Signal_List.takeItem(clicked)
        added_signals_list.pop(clicked+1)
        self.ui.AddedSignal_View.clear()
        if len(added_signals_list)==1:
            print("nothing to show on delete signal")
            self.ui.AddedSignal_View.clear()
        else:
            self.ui.AddedSignal_View.plot(time, np.round(sum(added_signals_list),2))


    def signal_preview(self):
        global signal_name,added_signals_list, time,Frequency,Magnitude,PhaseShift,Signal,value,samplingvalue,FrequencyList,currenttimeonillustrator,currentsignalonillustrator
        self.ui.Composed_View.clear()
        Magnitude = float(self.ui.A_Text.text())
        Frequency = float(self.ui.F_Text.text()) 
        PhaseShift = float(self.ui.Theta_Text.text())
        PhaseShift=np.round((PhaseShift*pi/180),4)

        # if self.ui.Sine_radioButton.isChecked():
        Signal = Magnitude* np.sin(2 * pi * Frequency * time + PhaseShift) 
        # elif self.ui.Cosine_radioButton.isChecked():
        #     Signal = Magnitude * np.cos(2 * pi * Frequency * time + PhaseShift)
  
        self.ui.Composed_View.plot(time, np.round(Signal,2)) 
        self.ui.Composed_View.show()

    def Addedsignals(self):
        global signal_name,added_signals_list, time,Frequency,Magnitude,PhaseShift,Signal,value,samplingvalue,FrequencyList,currenttimeonillustrator,currentsignalonillustrator
        self.ui.AddedSignal_View.clear()
        added_signals_list.append(Signal)
        if len(added_signals_list)==1:
            print("nothing to show on added signal")
            self.ui.AddedSignal_View.clear()
        else:
            self.ui.AddedSignal_View.plot(time, np.round(sum(added_signals_list),2))  
            self.ui.AddedSignal_View.show()
     

        FrequencyList.append(Frequency)
        # if self.ui.Sine_radioButton.isChecked():
        value=str(Magnitude)+'sin(2*pi*'+str(Frequency)+'*'+'t'+'+'+str(PhaseShift)+')'
        # elif self.ui.Cosine_radioButton.isChecked():
        #    value=str(Magnitude)+'cos(2*pi*'+str(Frequency)+'*'+'t'+'+'+str(PhaseShift)+')'

        signal_name.append(value) 
        self.ui.Signal_List.addItem(value) 

    def Preview_onprimary(self):
        global signal_name,added_signals_list, time,Frequency,Magnitude,PhaseShift,Signal,value,samplingvalue,FrequencyList,currenttimeonillustrator,currentsignalonillustrator,loaded
        loaded=0
        currenttimeonillustrator=time
        currentsignalonillustrator=added_signals_list
        if len(added_signals_list)==1:
            print("nothing to show on illustrator")
            self.ui.Illustrator_View.clear() 
        else:
            self.ui.Illustrator_View.clear()
            print(1,len(np.round(sum(currentsignalonillustrator),2)))    
            self.ui.Illustrator_View.plot(currenttimeonillustrator, np.round(sum(currentsignalonillustrator),2))

        self.Find_Max_Frequency()

   




    def sample(self, originalSignal, sampling_freq, analog_time):
        time_interval = analog_time[-1]
        nsamples = int(np.floor(sampling_freq * time_interval))
        if nsamples > 0:
            sampling_time = np.arange(0, time_interval, 1/sampling_freq)
            sampling_values = [ originalSignal[ np.searchsorted(analog_time, t)] for t in sampling_time ]
            return (sampling_time, sampling_values)
        return ([], [])     
            
                 
    def save(self):
        global ExcelCounter,added_signals_list,MaximumFrequency,time
        ExcelCounter = ExcelCounter+ 1
        self.Find_Max_Frequency()
        SavedSignal = np.asarray([ np.round(time,2), np.round(sum(added_signals_list),2)])
        np.savetxt('Generated Signal'+str(ExcelCounter)+'.csv', SavedSignal.T,header="Time,Signal,fm", delimiter=",",fmt=['%f' , '%f'])
        
        with open('Generated Signal'+str(ExcelCounter)+'.csv', 'a') as f_object:
             writer_object = writer(f_object)

        list=[MaximumFrequency,0]
        writer_object.writerow(list)
        print("in Save maximum freq= ",MaximumFrequency)
        f_object.close()

    def Browse(self):
        fname=QFileDialog.getOpenFileName(self, "Open file", "D:" )
        data = np.loadtxt(fname)
        xdata = data[:, 0]
        ydata = data[:, 1]
        self.ui.Illustrator_View.clear()    
        self.ui.Illustrator_View.plot(xdata, ydata)  

    def load(self):
        print("aloooooooooo")
        global currenttimeonillustrator,currentsignalonillustrator,MaximumFrequency,loaded
        loaded=1
        self.path = QFileDialog.getOpenFileName(self, 'Open a file', '') #open browse window
        if self.path != ('', ''):
            self.data = self.path[0]
            print("File path: " + self.data)
    
        self.col= pd.read_csv(self.data) #read columns from file
        self.signal_array1=self.col.iloc[:,1:2].values
        self.time_array1=self.col.iloc[:,0:1].values
        MaximumFrequency1=self.time_array1[len(self.time_array1)-1]
        self.signal_array=np.delete(self.signal_array1,len(self.signal_array1)-1)
        self.time_array=np.delete(self.time_array1,len(self.time_array1)-1)
        MaximumFrequency=MaximumFrequency1[0]
        print("in load maximum freq= ",MaximumFrequency)
        currentsignalonillustrator = self.signal_array.reshape(-1)
        currenttimeonillustrator = self.time_array.reshape(-1)
        self.ui.Illustrator_View.clear()
        self.ui.Signal_List.clear()
        self.ui.AddedSignal_View.clear()
        self.ui.Illustrator_View.plot(currenttimeonillustrator, currentsignalonillustrator)
        self.ui.Illustrator_View.show()

    def ChangeSamplingRate(self):
        global signal_name,added_signals_list, time,Frequency,Magnitude,PhaseShift,Signal,value,samplingvalue,FrequencyList,currenttimeonillustrator,currentsignalonillustrator,MaximumFrequency,loaded
        if loaded==0:
            self.Find_Max_Frequency
            print("elmaximum from compose=",MaximumFrequency)
            samplingvalue=MaximumFrequency*round(self.ui.Illustrator_Frequency_Slider.value()/33,2)
            print(2,len(currentsignalonillustrator),samplingvalue,len(currenttimeonillustrator))
            sampledTime, sampledSignal = self.sample(np.round(sum(currentsignalonillustrator),2), 2*samplingvalue, currenttimeonillustrator)
            self.ui.Illustrator_View.clear()
            self.ui.Reconstructed_View.clear()
            self.ui.Illustrator_View.plot(currenttimeonillustrator, np.round(sum(currentsignalonillustrator),2))
            self.ui.Illustrator_View.plot(sampledTime,sampledSignal,pen=None ,symbol="o", symbolsize=2, symbolBrush=('b'))
            resampledSignal,resampledTime = signal.resample(sampledSignal, len(np.round(sum(currentsignalonillustrator),2)), sampledTime)
            self.ui.Illustrator_View.plot(resampledTime,resampledSignal,pen='r')
            self.ui.Reconstructed_View.plot(resampledTime,resampledSignal)
        elif loaded==1:  ##this means the fn is loaded as Csv
            print("elmaximum from excel=",MaximumFrequency)
            samplingvalue=MaximumFrequency*round(self.ui.Illustrator_Frequency_Slider.value()/33,2)
            print(2,len(currentsignalonillustrator),samplingvalue,len(currenttimeonillustrator))
            sampledTime, sampledSignal = self.sample(currentsignalonillustrator, 2*samplingvalue, currenttimeonillustrator)
            self.ui.Illustrator_View.clear()
            self.ui.Reconstructed_View.clear()
            self.ui.Illustrator_View.plot(currenttimeonillustrator, currentsignalonillustrator)
            self.ui.Illustrator_View.plot(sampledTime,sampledSignal,pen=None ,symbol="o", symbolsize=2, symbolBrush=('b'))
            resampledSignal,resampledTime = signal.resample(sampledSignal, len(currentsignalonillustrator), sampledTime)
            self.ui.Illustrator_View.plot(resampledTime,resampledSignal,pen='r')
            self.ui.Reconstructed_View.plot(resampledTime,resampledSignal)  

    def Find_Max_Frequency(self):
        global MaximumFrequency, FrequencyList
        if FrequencyList:
            MaximumFrequency=max(FrequencyList)
            print(MaximumFrequency)
        else:
            MaximumFrequency=0        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
