# -*- coding: UTF-8 -*-
import serial
import glob, json
import collections
import datetime
import time
import numpy as np
from datetime import datetime

_ser1 = serial.Serial('/dev/ttyACM0', baudrate=115200, timeout=0.01)   


fi_num = datetime.now().strftime("%H_%M_%S")
cnt = 0
data_ls = []
data_dic = {}
while True:
    rx_1 = _ser1.readline()
    
    try:
        ti = datetime.now().strftime("%H:%M:%S.%f")
        # print('rx_1: ', rx_1)
        if(len(rx_1) >= 5 and rx_1[0:2] == 'mc'):
            data = rx_1.split(' ')
            print('---Time---: ', ti)
            print('data: ', data)
            d0, d1, d2, d3 = int(data[2], 16), int(data[3], 16), int(data[4], 16), int(data[5], 16)
            dis = [d0, d1, d2, d3]
            
            print('dis: ', dis)
            cnt+=1
            print(cnt)
            data_dic[cnt] = {'time': ti, 'dis': dis}
            #data_ls.append({'time': ti, 'dis': dis})
            if cnt == 300:
                time.sleep(.5)
                # with open('UWB_dis_' + fi_num + '.txt', 'a') as fout:    
                #     json.dump(data_dic, fout)
                #     print('Write!!!!')
                #     break
            #with open('UWB_dis_' + fi_num + '.txt', 'a') as fout:    
                #json.dump({'time': ti, 'dis': dis}, fout)
                #print('Write!!!!')
        
        else:
            # print('Wrong Data!')
            continue
         
            
    except ValueError:
        print('ValueError')
        
    
    except IndexError:
        print('IndexError')
    
    except KeyboardInterrupt:
        time.sleep(.5)
        with open('UWB_dis_' + fi_num + '.txt', 'a') as fout:    
            json.dump({'data_ls', data_ls}, fout)
            print('Write!!!!')
        time.sleep(.5)
        
