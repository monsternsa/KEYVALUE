import sys
import argparse
import json

FILE_NAME="data_file.json"

#определяем аргументы командной строки
def createParser():
 parser = argparse.ArgumentParser()
 parser.add_argument('-k','--key')
 parser.add_argument('-v','--val')

 return parser

#пишем в файл струтктуру json
def saveData(p_dict_DataVal,p_key,p_val):

 #ищем ключ наш параметр
 if not p_key in p_dict_DataVal:
  #добавялем новый ключ
  newval=[]
  newval.append(p_val)
  p_dict_DataVal[p_key]={"val": newval}

 else:
  #добовляем значение
  curKey = p_dict_DataVal.get(p_key, None)
  curval=curKey["val"]
  curval.append(p_val)


 with open(FILE_NAME, "w") as write_file:
  json.dump(p_dict_DataVal, write_file)

def readData():
    data = {}
    try:
        with open(FILE_NAME, "r") as read_file:
            data = json.load(read_file)
    except Exception as e:
        print('Ошибка, чтения файла, словарь проницилизирован')

    return data

#ищем ключ в словаре
def findKey(key,jsonData):
  ret_key=None
  valueKey=jsonData[key]
  return valueKey

#выводим значение из словаря
def outputDataKey(list_key):
 #for item_val in list_key['val']:
 # print(item_val)
    print(list_key['val'])

if __name__ == '__main__':
 #определяем аргументы командной строки
 parser = createParser()
 namespace = parser.parse_args(sys.argv[1:])

 #отладка print(parser.parse_known_args())

 allData = readData()

 print("Считаны все данные из файла до манипуляций\n", allData)

 if namespace.val is None:
 # Val передан незаполен ожидаем key параметр для чтения
 # чтение данных

   try:
    x=findKey(namespace.key,allData)
    print('\nПередан ключ:', namespace.key,' запросим данные:')
    outputDataKey(x)

   except Exception as e:
    print('\nОшибка, не найден ожидаемый параметр. Передан параметр(ключ): ', namespace.key)

 elif namespace.key is not None:
   print('\n передан ключ: ',namespace.key,' новое значение val: ', namespace.val)
   #сохранение данных
   saveData(allData,namespace.key,namespace.val)
   print("\nСчитаны все данные из файла после манипуляций\n", readData())

 else:
   print("Не верные параметры (аргументы) командной строки")

