import os
import tornado.ioloop
import tornado.template as template
import tornado.web
from modules.get_systems_from_cobbler import CobblerSystemsData


class Application(tornado.web.Application):
    def __init__(self):
        settings = {
            "debug": True,
            "static_path": os.path.join(os.path.dirname(__file__), "stylesheets/css/"),
        }
        handlers = [
            (r'/cobbler_systems/', CobblerSystemsPage),
            (r'/(main\.css)', tornado.web.StaticFileHandler, dict(path=settings['static_path'])),

        ]
        tornado.web.Application.__init__(self, handlers, **settings)


class CobblerSystemsPage(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.set_header("Content-Type", "text/html")
        self.write(self.build_page())

    def build_page(self):
        loader = template.Loader("web_templates/")
        cobbler_systems_page = loader.load("cobbler_systems.html").generate(systems=self.get_cobbler_systems_data())
        return cobbler_systems_page

    @staticmethod
    def get_cobbler_systems_data():
        systems_dict = {}
        fetcher = CobblerSystemsData()
        systems_data = fetcher.get_all_systems_data()
        for item in systems_data:
            system_name = item.get('hostname')
            systems_dict[system_name] = item
        return systems_dict


def make_app():
    return Application()


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
