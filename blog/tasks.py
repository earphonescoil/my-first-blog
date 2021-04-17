import sys
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.mail import send_mail #040421


def send_myemail():
	print("----ORI---")
	#040421
	#send an email 
	#notice the ‘’ that may be needed to re-enter
	#later I will change the “to email”
	send_mail(
	'תזכורת מאפליקציית תקציב סופרמרקט והשלמות', # subject
	',שלום משפחת מטלון\nאנא עדכנו הוצאות באפליקציה\nhttp://earphonescoil1.pythonanywhere.com\nתודה מצוות הפיתוח', # message
	'fswd2021@gmail.com', # from email
	['ori.matalon@gmail.com', 'Liron.Branch@hot.net.il', 'amiros111111@gmail.com'], # to email
	fail_silently = False,
	)