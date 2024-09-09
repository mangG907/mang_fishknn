from sklearn.neighbors import KNeighborsClassifier

home_path = os.path.expanduser('~')
file_path = '{home_path}/data/fish_pd/fish.csv'

def fish_pred(length:float, weight:float, fish_class:int):
    if fish_class == 0:
        fish_real_name = "도미"
    else:
        fish_real_name = "빙어"

# 파일이 없다면 파일을 만들자
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path), exist_ok = True)
        df=pd.DataFrame({'length':[length], 'weight':[weight], 'label':[fish_class]})
        df.to_csv(file_path, index=False)
        return
    # 파일이 있으나 5개 미만일 때 
    data = pd.read_csv(file_path)
    if len(data) < 5:
        df=pd.DataFrame({'length':[length], 'weight':[weight], 'label':[fish_class]})
        df=pd.concat([data, df], ignore_index=True) # 데이터프레임 합치기
        df.to_csv(file_path, index=False)
        return
    # 파일이 있을 때
    x = data.drop('label', axis = 1)
    y = data['label']

    knn = KNeighborsClassifier() # 모델 부르기
    knn.fit(x, y) # 모델 학습시키기
    prediction = knn.predict([[length,weight]]) # 예측값 저장

    if prediction == 0:
        fish_pred_name = "도미"
    else:
        fish_pred_name = "빙어"

    if prediction == fish_class: # 예측이 정답인 경우
        df=pd.DataFrame({'length':[length], 'weight':[weight], 'label':[fish_class]})
        df=pd.concat([data, df], ignore_index=True) # 데이터프레임 합치기               
        df.to_csv(file_path, index=False)                                                  return
    
    else:
        if len(data) < 50:
            df=pd.DataFrame({'length':[length], 'weight':[weight], 'label':[fish_class]})
            df=pd.concat([data, df], ignore_index=True) # 데이터프레임 합치기
            df.to_csv(file_path, index=False)
        return
    # 이 작품은 원준님의 작품입니다. 오해 금물 



