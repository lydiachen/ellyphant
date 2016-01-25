import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write('Hello, World!')

class Page2(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write('See you later, World!')

app = webapp2.WSGIApplication([
	('/', MainPage),('/page2', Page2)
], debug=True)
