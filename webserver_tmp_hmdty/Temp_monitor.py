import picoweb
from time import sleep
from machine import Pin
from dht import DHT22
import network
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
  print('connecting to network...')
  sta_if.active(True)
  sta_if.connect('DangerVirus', 'abivarsh@2016')
  while not sta_if.isconnected():
    pass
print('network config:', sta_if.ifconfig())
ipadd=sta_if.ifconfig()
app = picoweb.WebApp(__name__)
hw_sensor=DHT22(Pin(13,Pin.IN,Pin.PULL_UP))
  
@app.route("/temp")
def html(req, resp):
    hw_sensor.measure()
    t = hw_sensor.temperature()
    h = hw_sensor.humidity()
    sensor={"tmpr":t,"hmdty":h}
    msg = (b'{0:3.1f} {1:3.1f}'.format(t,h))
    print(msg)
    yield from picoweb.start_response(resp, content_type = "text/html")
    yield from app.render_template(resp, "sensor.tpl", (sensor,))
app.run(debug=True, host =ipadd[0])
