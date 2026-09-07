"""Accessible, inclusive user-feedback form.

Run this file and open http://localhost:8000 in a browser.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs


PAGE = """<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>User feedback</title>
	<style>
		:root { color-scheme: light dark; font-family: system-ui, sans-serif; }
		body { max-width: 42rem; margin: auto; padding: 1rem; line-height: 1.5; }
		label, legend { font-weight: 600; }
		input, textarea, select, button { box-sizing: border-box; width: 100%;
			margin: .35rem 0 1rem; padding: .65rem; font: inherit; }
		fieldset { border: 0; padding: 0; margin: 1rem 0; }
		fieldset label { display: block; font-weight: 400; }
		input[type=radio], input[type=checkbox] { width: auto; margin-right: .5rem; }
		button { cursor: pointer; font-weight: 700; }
		:focus-visible { outline: 3px solid #1769aa; outline-offset: 2px; }
		.hint { margin-top: -.75rem; font-size: .9rem; }
		.error { color: #b00020; }
	</style>
</head>
<body>
	<main>
		<h1>Share your feedback</h1>
		<p id="intro">Your feedback helps us improve. Fields marked with * are required.</p>
		<form method="post" action="/" aria-describedby="intro">
			<label for="name">Name (optional)</label>
			<input id="name" name="name" autocomplete="name">

			<label for="email">Email address (optional)</label>
			<input id="email" name="email" type="email" autocomplete="email"
						 aria-describedby="email-hint">
			<p id="email-hint" class="hint">Only provide this if you would like a reply.</p>

			<fieldset>
				<legend>How would you describe your experience? *</legend>
				<label><input type="radio" name="experience" value="positive" required> Positive</label>
				<label><input type="radio" name="experience" value="mixed"> Mixed</label>
				<label><input type="radio" name="experience" value="negative"> Negative</label>
				<label><input type="radio" name="experience" value="not-sure"> Not sure or prefer not to say</label>
			</fieldset>

			<label for="details">Tell us more (optional)</label>
			<textarea id="details" name="details" rows="6"></textarea>

			<fieldset>
				<legend>How did you use the service? (optional)</legend>
				<label><input type="checkbox" name="context" value="work"> For work or study</label>
				<label><input type="checkbox" name="context" value="personal"> For personal use</label>
				<label><input type="checkbox" name="context" value="other"> Another reason</label>
				<label><input type="checkbox" name="context" value="prefer-not"> Prefer not to say</label>
			</fieldset>

			<button type="submit">Send feedback</button>
		</form>
	</main>
</body>
</html>"""


class FeedbackHandler(BaseHTTPRequestHandler):
		def do_GET(self):
				self._send(PAGE)

		def do_POST(self):
				length = int(self.headers.get("Content-Length", 0))
				feedback = parse_qs(self.rfile.read(length).decode("utf-8"), keep_blank_values=True)
				if not feedback.get("experience", [""])[0]:
						self._send(PAGE.replace("<main>", '<main><p class="error" role="alert">Please choose an experience option.</p>'), 400)
						return
				# Demonstration only: avoid storing or exposing personal information.
				self._send("<main lang='en'><h1>Thank you</h1><p>Your feedback was received.</p><p><a href='/'>Send another response</a></p></main>")

		def _send(self, content, status=200):
				data = content.encode("utf-8")
				self.send_response(status)
				self.send_header("Content-Type", "text/html; charset=utf-8")
				self.send_header("Content-Length", str(len(data)))
				self.end_headers()
				self.wfile.write(data)


if __name__ == "__main__":
		print("Open http://localhost:8000")
		HTTPServer(("localhost", 8000), FeedbackHandler).serve_forever()
