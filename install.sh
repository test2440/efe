#!/bin/bash

# تحديث الحزم
pkg update && pkg upgrade -y

# تثبيت المتطلبات
pkg install python -y
pkg install git -y

# استنساخ المستودع
git clone https://github.com/eeeterii/git-init.git
cd git-init

# تشغيل المشروع (حدد ملف التشغيل الصحيح)
python 'يسورس ايفا.py'

