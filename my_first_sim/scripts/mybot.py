class MyBot(object):

    motion = None
    sick = None
    pose = None
    _robot = None
    MAX_SPEED = 0.5
    LOW_SPEED = 0.25

    def __init__(self, simu):
        self.robot = simu.robot
        self.simu = simu

        self._last_n_steps = []

    @property
    def last_n_steps(self):
        return self._last_n_steps

    @last_n_steps.setter
    def last_n_steps(self, value):
        items_len = len(self._last_n_steps)

        if items_len > 10:
            start = items_len - 10
            self._last_n_steps = self._last_n_steps[start+1:]

        self._last_n_steps.append(value)

    @property
    def robot(self):
        return self._robot

    @robot.setter
    def robot(self, robot):
        self._robot = robot

        self.motion = robot.motion
        self.pose = robot.pose
        self.sick = robot.sick

    def get_rangelist(self):
        return self.sick.get().get('range_list', [])

    def wait(self):
        print('waiting...')
        self.simu.sleep(0.5)
        return self

    def turn_sharp(self):
        print('turning sharp...')
        v_w = {'v': 0, 'w': -4}
        self.motion.publish(v_w)

        return self

    def turn_right(self):
        print('turning right...')
        v_w = {'v': 0, 'w': 1}
        self.motion.publish(v_w)

        return self

    def turn_left(self):
        print('turning left...')
        v_w = {'v': 0, 'w': -1}
        self.motion.publish(v_w)

        return self

    def go_forward(self):
        print('going forward...')
        v_w = {"v": self.MAX_SPEED, "w": 0}
        self.motion.publish(v_w)

        return self

    def slow_down(self):
        print('slowing down...')
        v_w = {"v": self.LOW_SPEED, "w": 0}
        self.motion.publish(v_w)

        return self

    def stop(self):
        #print('stopping for a moment...')
        v_w = {'v': 0, 'w': 0}
        self.motion.publish(v_w)

        return self

    def turning(self, value):
        print('turning somewhere with value %s...' % value)
        v_w = {'v': 0, 'w': value}
        self.motion.publish(v_w)

        return self

    def move(self, v, w):
        #print('moving to somewhere with values (%s / %s)...' % (v, w))
        v_w = {'v': v, 'w': w}
        self.motion.publish(v_w)

        return self