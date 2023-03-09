curl  http://192.168.43.97:8080/main-api/customers/  -H  "Accept: application/json" -X GET -u "admin:bonjour5gi"
curl  http://localhost:8080/main-api/customers/  -H  "Accept: application/json" -X POST -u "admin:bonjour5gi" --data "email=borel@gmail.com&username=borel&password=123456"
curl  http://localhost:8080/main-api/customers/28add55f-4aed-4357-8b71-cbe4136f1fe7/  -H  "Accept: application/json" -X PUT -u "admin:bonjour5gi" --data "email=borel2@gmail.com&username=borel&password=123456"
curl  http://localhost:8080/main-api/customers/28add55f-4aed-4357-8b71-cbe4136f1fe7/  -H  "Accept: application/json" -X DELETE -u "admin:bonjour5gi"
curl  http://192.168.43.97:8080/main-api/login/  -H  "Accept: application/json" -X POST  --data "email=borel@gmail.com&password=123456"
curl  http://192.168.43.97:8080/main-api/customers/?username=Borel -X GET  -H  "Accept: application/json" -u "admin:bonjour5gi"

