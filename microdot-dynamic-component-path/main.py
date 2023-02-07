from microdot_asyncio import Microdot, Response, send_file
from microdot_utemplate import render_template
from color_service import ReadColorsService
from rgb_led import RGBLEDModule

# Initialize MicroDot
app = Microdot()
Response.default_content_type = 'text/html'

# Read the colors
color_service = ReadColorsService()
led_colors = color_service.read_colors()

# Set the GPIO pins
rgb_led_module = RGBLEDModule([13 , 14, 15])

# root route
@app.route('/')
async def index(request):
    return render_template('index.html', colors=led_colors)

# toggle RGB Module color
@app.route('/toggle-led/<color>')
async def index(request, color):
    for led_color in led_colors:
        if color == led_color['name']:
            rgb_led_module.set_rgb_color(led_color['rgb'])
            break
    return {"status": "OK"}

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
    rgb_led_module.deinit_pwms()
    request.app.shutdown()
    return 'The server is shutting down...'


if __name__ == "__main__":
    try:
        app.run()
    except KeyboardInterrupt:
        rgb_led_module.deinit_pwms()
