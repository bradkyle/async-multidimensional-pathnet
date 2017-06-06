import random

import tensorflow as tf

#======================================================================================================================>
# Pathnet Class
#======================================================================================================================>

class PathNet():
    def __init__(self,scope):

        #todo make multi dimensional
        self.paths = [[None]*2]*2
        self.control_fixed = random.sample(self.paths, 1)[0]


        with tf.variable(scope):
            print()

    def return_all_paths(self):
        paths = [path.return_path() for path in self.paths]
        return paths

    #returns a random sample of two paths from the pathnet
    def sample(self):
        return random.sample(self.paths, 2)

    #returns randomly selected
    def return_control(self):
        return self.control_fixed

    def return_control_path(self):
        return self.control_fixed.return_path()

# ======================================================================================================================>
# Path
# ======================================================================================================================>

class Path():
    def __init__(self):
