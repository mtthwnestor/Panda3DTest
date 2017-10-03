#! /usr/bin/env python3

from direct.showbase.ShowBase import ShowBase


class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # Load a model and render it.
        self.scene = self.loader.loadModel('models/environment')
        self.scene.reparentTo(self.render)

        # Set the model's position and scale.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)


if __name__ == '__main__':

    app = MyApp()
    app.run()
