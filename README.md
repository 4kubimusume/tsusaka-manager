# ここは
津坂杯管理システムです

## 使い方
管理ユーザーの作成
```
python manage.py createsuperuser
```

開発サーバー起動
```
python manage.py runserver
```
ブラウザで`http://127.0.0.1:8000/admin/`にアクセス

全テスト実行
```
python manage.py test
```
テストを指定して実行
```
python manage.py test <app_name>.<module_name>.<ClassName>.<method_name>
```
例
```
python manage.py test core.tests.ParticipantModelTest.test_create_participant
```