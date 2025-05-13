def period_numericki(self, dt, T):
    t, x, _, _ = self.euler_method(dt, T)

    prolazi_kroz_nulu = []
    for i in range(1, len(x)):
        if x[i-1] < 0 and x[i] >= 0:
            t_prijelaz = t[i-1] + dt * (-x[i-1]) / (x[i] - x[i-1])
            prolazi_kroz_nulu.append(t_prijelaz)
    if len(prolazi_kroz_nulu) < 2:
        return None
    