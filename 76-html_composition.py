

class Tag(object):

	def __init__(self, name, contents):
		self.start_tag = "<{}>".format(name)
		self.end_tag = "</{}>".format(name)
		self.contents = contents

	def __str__(self):
		return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

	def display(self, file=None):
		print(self, file=file)


class DocType(Tag):

	def __init__(self):
		super().__init__("!DOCTYPE html", "")
		self.end_tag = ""  # DOCTYPE doesn't have an end tag;


class Head(Tag):

	def __init__(self, title=None):
		super().__init__("head", "")
		if title:
			self._title = Tag("title", title)
			self.contents = str(self._title)


class Body(Tag):

	def __init__(self):
		super().__init__("body", "")  # Body contents will be built separately;
		self._body_contents = []

	def add_tag(self, name, contents):
		new_tag = Tag(name, contents)
		self._body_contents.append(new_tag)

	def display(self, file=None):
		for tag in self._body_contents:
			self.contents += str(tag)
		super().display(file=file)


class HtmlDoc(object):

	def __init__(self, title=None):
		self._doc_type = DocType()
		self._head = Head(title)
		self._body = Body()

	def add_tag(self, name, contents):
		self._body.add_tag(name, contents)

	def display(self, file=None):
		self._doc_type.display(file=file)
		print("<html>", file=file)
		self._head.display(file=file)
		self._body.display(file=file)
		print("</html>", file=file)


if __name__ == "__main__":
	my_page = HtmlDoc("My Page")
	my_page.add_tag("h1", "Main Heading")
	my_page.add_tag("h2", "Sub-heading")
	my_page.add_tag("p", "This is a paragraph that will appear on the page.")
	with open("76-html_composition.html", "w") as html_doc:
		my_page.display(file=html_doc)
