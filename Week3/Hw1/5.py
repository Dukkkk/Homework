import pandas as pd
df1 = pd.read_csv('C:/git/Homework/Week3/Data/2501.csv')
df2 = pd.read_csv('C:/git/Homework/Week3/Data/2502.csv')
df3 = pd.read_csv('C:/git/Homework/Week3/Data/2503.csv')
df4 = pd.read_csv('C:/git/Homework/Week3/Data/2504.csv')
df5 = pd.read_csv('C:/git/Homework/Week3/Data/2505.csv')
df6 = pd.read_csv('C:/git/Homework/Week3/Data/2506.csv')
df = pd.concat([df1, df2, df3, df4, df5, df6], ignore_index=True)
col_names = {
    'title': 'TItle',
    'price_total': 'Үнэ',
    'date': 'Date',
    'time': 'Time',
    'ad_id': 'ID',
    'phone': 'Утасны дугаар',
    'room_num': 'Room',
    'location': 'Location',      
    'ad_text': 'text',
    'url': 'URL',
    'floor_type': 'Шал',
    'balcony_num': 'Balcony',
    'date_op': 'Ашиглалтанд орсон он',
    'garage': 'Garage',
    'window_type': 'Цонх',
    'floor_num': 'Давхар',
    'door_type': 'Хаалга',
    'size': 'Талбай',
    'floor_at': 'Хэдэн давхарт',
    'leasing': 'leasing',
    'window_num': 'Цонхны тоо',
    'progress_cons': 'Явц',
    'elevator': 'Лифт',
    'ad_page': 'ad_page',
    'ad_order': 'ad_order',
    'weekday': 'weekday',
    'hour': 'hour',
    'area': 'area',
    'price': 'price',
    'price_m2': 'price_m2',
    'district': 'district',
    'mylocation': 'mylocation',
    'code': 'Код:',
}
       
     
df.columns = df.columns.str.strip()
df.rename(columns=col_names, inplace=True)
df.duplicated(subset=['ID', 'Date', 'Time'])
df = df.drop_duplicates(subset=['ID', 'Date', 'Time'], keep='first')
df = 