import pandas as pd

def read_csv(path):
    path = 'F:/zhaobiao/'+path
    df = pd.read_csv(path,encoding = 'gbk')
    return df

def df_clean(df,name,keyword):
    df_data_1 = df.loc[df[name].str.contains(keyword)]
    return df_data_1

if __name__ == '__main__':
    Name = 'caigou'
    path = Name+'/'+Name+'/recruit.csv'
    df = read_csv(path)
    keyword = "中国"
    name = '公告名称'
    df = df_clean(df,name,keyword)
    print(df)
    df.to_csv(Name+'.csv',index=False)

    Name = 'chengezhao'
    path = Name + '/' + Name + '/recruit.csv'
    df = read_csv(path)
    keyword = "中国"
    name = '项目标题'
    df = df_clean(df, name, keyword)
    print(df)
    df.to_csv(Name + '.csv',index=False)

    Name = 'ebidding'
    path = Name + '/' + Name + '/recruit.csv'
    df = read_csv(path)
    keyword = "中国"
    name = '项目标题'
    df = df_clean(df, name, keyword)
    print(df)
    df.to_csv(Name + '.csv', index=False)

    Name = 'ggzy'
    path = Name + '/' + Name + '/recruit.csv'
    df = read_csv(path)
    keyword = "中国"
    name = '公告标题'
    df = df_clean(df, name, keyword)
    print(df)
    df.to_csv(Name + '.csv', index=False)

    Name = 'gzqunsheng'
    path = Name + '/' + Name + '/recruit.csv'
    df = read_csv(path)
    keyword = "中国"
    name = '招标项目'
    df = df_clean(df, name, keyword)
    print(df)
    df.to_csv(Name + '.csv', index=False)

    Name = 'gztpc'
    path = Name + '/' + Name + '/recruit.csv'
    df = read_csv(path)
    keyword = "中国"
    name = '公告标题'
    df = df_clean(df, name, keyword)
    print(df)
    df.to_csv(Name + '.csv', index=False)

    Name = 'zztender'
    path = Name + '/' + Name + '/recruit.csv'
    df = read_csv(path)
    keyword = "中国"
    name = '项目名称'
    df = df_clean(df, name, keyword)
    print(df)
    df.to_csv(Name + '.csv', index=False)

