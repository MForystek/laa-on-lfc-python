class PIDController:
    def __init__(self, K, setpoint, time_step):
        self._Kp = K[0]
        self._Ki = K[1]
        self._Kd = K[2]
        self._setpoint = setpoint
        self._time_step = time_step
        self._prev_error = 0
        self._second_prev_error = 0


    def update(self, measured_value, prev_output):
        error = self._setpoint - measured_value
        proportional = error - self._prev_error
        integral = error * self._time_step
        derivative = (error - 2*self._prev_error + self._second_prev_error) / self._time_step
        self._second_prev_error = self._prev_error
        self._prev_error = error

        change_in_control_signal = self._Kp*proportional + self._Ki*integral + self._Kd*derivative
        return prev_output + change_in_control_signal