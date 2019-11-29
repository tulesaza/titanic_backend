from collections import namedtuple
import numpy as np

ConfusionMatrix = namedtuple('conf_matrix', ['tp', 'tn', 'fn', 'fp'])


def calc_confusion_matrix(y_true, y_scores, threshold=0.5):
    tp = fp = tn = fn=0
    for true, scores in zip(y_true, y_scores):
        if scores > threshold:           #predicted positive class
            if true == 1:                #actual positive class
                tp += 1
            else:                        #actual negative
                fp += 1
        else:                            #predicted negative
            if true == 0:                #actual negative
                tn += 1
            else:                        #actual positive
                fn += 1
    return ConfusionMatrix(tp, tn, fn, fp)


def fpr(conf_matrix):
    return conf_matrix.fp / (conf_matrix.fp + conf_matrix.tn) if (conf_matrix.fp + conf_matrix.tn) != 0 else 0


def tpr(conf_matrix):
    return conf_matrix.tp / (conf_matrix.tp + conf_matrix.fn) if (conf_matrix.tp + conf_matrix.fn) != 0 else 0


def calculate_roc_curve(y_true, y_scores):
    # generate thresholds over score domain
    low = min(y_scores)
    high = max(y_scores)
    step = (abs(low) + abs(high)) / 1000
    thresholds = np.arange(low-step, high+step, step)
    results = {"thresholds": thresholds}
    # calculate confusion matrices for all thresholds
    confusion_matrices = []
    for threshold in thresholds:
        confusion_matrices.append(calc_confusion_matrix(y_true, y_scores, threshold))
    # apply functions to confusion matrices
    results["FPR"]=list(map(fpr, confusion_matrices))
    results["TPR"]=list(map(tpr, confusion_matrices))
    results["conf_matrices"] = confusion_matrices
    return results
