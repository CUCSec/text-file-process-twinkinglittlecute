import time
with open('log_files/201811123024.log',encoding='utf8') as f:
    count=0
    for line in f:
        student_id = line.split(',')[1]
        student_id =student_id.strip()
        if student_id[3:]=='201811123024':
            count+=1
    print(count)
time.sleep(60)
