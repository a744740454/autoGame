nohup python main.py > output.log 2>&1 &


flask --app .\main.py db migrate -m "xxxx"
flask --app .\main.py db upgrade