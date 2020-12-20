import numpy as np

from keras.models import load_model
# # 载入数据
from model import *
from data import *
# (x_train,y_train),(x_test,y_test) = mnist.load_data()
# # (60000,28,28)
# print('x_shape:',x_train.shape)
# # (60000)
# print('y_shape:',y_train.shape)
# # (60000,28,28)->(60000,784)
# x_train = x_train.reshape(x_train.shape[0],-1)/255.0
# x_test = x_test.reshape(x_test.shape[0],-1)/255.0
# # 换one hot格式
# y_train = np_utils.to_categorical(y_train,num_classes=10)
# y_test = np_utils.to_categorical(y_test,num_classes=10)
def getFileName(path):
    filelist = []
    ''' 获取指定目录下的所有指定后缀的文件名 '''
    f_list = os.listdir(path)
    # print f_list
    for i in f_list:
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(i)[1] == '.jpg':
            print(i)
            filelist.append(i)
    return filelist
path='noguass/'
filelisttt = getFileName(path)
# 载入模型
model = load_model('unet_membrane_3.hdf5')
testGene = testGenerator(path)

results = model.predict_generator(testGene,len(filelisttt),verbose=1)
saveResult(path,results)
# # 评估模型
# loss,accuracy = model.evaluate(x_test,y_test)
#
# print('\ntest loss',loss)
# print('accuracy',accuracy)
#
# # 训练模型
# model.fit(x_train,y_train,batch_size=64,epochs=2)
#
# # 评估模型
# loss,accuracy = model.evaluate(x_test,y_test)
#
# print('\ntest loss',loss)
# print('accuracy',accuracy)
#
# # 保存参数，载入参数
# model.save_weights('my_model_weights.h5')
# model.load_weights('my_model_weights.h5')
# # 保存网络结构，载入网络结构
# from keras.models import model_from_json
# json_string = model.to_json()
# model = model_from_json(json_string)
#
# print(json_string)
