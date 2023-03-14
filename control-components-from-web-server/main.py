from microdot_asyncio import Microdot, Response, send_file
from microdot_utemplate import render_template
from microdot_asyncio_websocket import with_websocket
from rgb_led import RGBLEDModule
import time
import ujson

# initialize RGB
pwm_pins = [14, 15, 16]
rgb_led = RGBLEDModule(pwm_pins)
# Set default color to 50% each for RGB
rgb_led.set_rgb_color({'blue': '50', 'red': '50', 'green': '50'})

# Initialize MicroDot
app = Microdot()
Response.default_content_type = 'text/html'

# root route
@app.route('/')
async def index(request):
    return render_template('index.html')

# initialize websocket
@app.route('/ws')
@with_websocket
async def read_sensor(request, ws):
    while True:
        data = await ws.receive()
        rgb_color = ujson.loads(data)
        rgb_led.set_rgb_color(rgb_color)
        await ws.send("OK")

# Static CSS/JSS
@app.route("/static/<path:path>")
def static(request, path):
    if ".." in path:
        # directory traversal is not allowed
        return "Not found", 404
    return send_file("static/" + path)


# shutdown
@app.get('/shutdown')
def shutdown(request):
    request.app.shutdown()
    return 'The server is shutting down...'


if __name__ == "__main__":
    try:
        app.run()
    except KeyboardInterrupt:
        rgb_led.deinit_pwms()
        pass
