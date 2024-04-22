from medpy import metric
def calculate_metric_percase(pred, gt):
    dice = metric.binary.dc(pred, gt)
    hd = metric.binary.hd95(pred, gt)
    return dice, hd