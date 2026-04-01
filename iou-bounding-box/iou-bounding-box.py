def iou(box_a, box_b):
    area_box_a = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
    area_box_b = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])
    x1 = max(box_a[0], box_b[0])
    y1 = max(box_a[1], box_b[1])
    x2 = min(box_a[2], box_b[2])
    y2 = min(box_a[3], box_b[3])
    
    intersection = max(0, x2 - x1) * max(0, y2 - y1)  
    union = (area_box_a + area_box_b) - intersection
    return intersection / union
    pass

box_a = [0, 0, 4, 4] 
box_b = [2, 2, 6, 6]
iou(box_a, box_b)
box_a = [0, 0, 2, 2] 
box_b = [3, 3, 5, 5]
iou(box_a, box_b)