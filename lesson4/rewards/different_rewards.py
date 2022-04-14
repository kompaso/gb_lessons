def get_reward(salary):
    additional_reward = ((salary * 0.3) / 12 + 365) / 16
    return additional_reward


def get_month_reward(salary):
    additional_reward = ((salary * 0.3) / 12 + 365) / 16 * 31
    return additional_reward