# VD-08-API
Работа с API 

Игнорирование проверки сертификатов: Если вам нужно временно обойти проверку SSL 
(не рекомендуется для производственного использования), 
вы можете изменить ваш запрос следующим образом:

вставить в файл app.py

   response = requests.get('https://api.quotable.io/random', verify=False)
   
   вот это - verify=False
   
