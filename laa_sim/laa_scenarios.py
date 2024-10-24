import numpy as np


def get_simple_5_percent_increase_laa(end):
    laa_start_times_sec = np.array([[0, 30],
                                    [0, 30],
                                    [0, 30]])
    laa_end_times_sec = np.array([[30, end],
                                  [30, end],
                                  [30, end]])
    laa_attack_strengths_pu = np.array([[0, 0.05],
                                        [0, 0.05],
                                        [0, 0.05]])
    return laa_start_times_sec, laa_end_times_sec, laa_attack_strengths_pu


def get_simple_10_percent_increase_laa(end):
    laa_start_times_sec = np.array([[0, 30],
                                    [0, 30],
                                    [0, 30]])
    laa_end_times_sec = np.array([[30, end],
                                  [30, end],
                                  [30, end]])
    laa_attack_strengths_pu = np.array([[0, 0.1],
                                        [0, 0.1],
                                        [0, 0.1]])
    return laa_start_times_sec, laa_end_times_sec, laa_attack_strengths_pu


def get_simple_20_percent_increase_laa(end):
    laa_start_times_sec = np.array([[0, 30],
                                    [0, 30],
                                    [0, 30]])
    laa_end_times_sec = np.array([[30, end],
                                  [30, end],
                                  [30, end]])
    laa_attack_strengths_pu = np.array([[0, 0.2],
                                        [0, 0.2],
                                        [0, 0.2]])
    return laa_start_times_sec, laa_end_times_sec, laa_attack_strengths_pu


def get_simple_50_percent_increase_laa(end):
    laa_start_times_sec = np.array([[0, 30],
                                    [0, 30],
                                    [0, 30]])
    laa_end_times_sec = np.array([[30, end],
                                  [30, end],
                                  [30, end]])
    laa_attack_strengths_pu = np.array([[0, 0.5, 0],
                                        [0, 0.5, 0],
                                        [0, 0.5, 0]])
    return laa_start_times_sec, laa_end_times_sec, laa_attack_strengths_pu


def get_multistep_5_then_10_then_15_percent_increase_laa(end):
    laa_start_times_sec = np.array([[0, 30],
                                    [0, 60],
                                    [0, 90]])
    laa_end_times_sec = np.array([[30, end],
                                  [60, end],
                                  [90, end]])
    laa_attack_strengths_pu = np.array([[0, 0.15],
                                        [0, 0.15],
                                        [0, 0.15]])
    return laa_start_times_sec, laa_end_times_sec, laa_attack_strengths_pu