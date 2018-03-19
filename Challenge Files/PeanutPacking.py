boxes = int(input())
while(boxes != 0):
    box_details = [(list(input().split())) for box in range(boxes)]
    peanuts = int(input())
    peanut_details = [(list(input().split())) for peanut in range(peanuts)]

    for peanut in range(len(peanut_details)):
        x = float(peanut_details[peanut][0])
        y = float(peanut_details[peanut][1])
        size = peanut_details[peanut][2]
        loc = "floor"

        for box in range(len(box_details)):
            box_x1 = float(box_details[box][0])
            box_x2 = float(box_details[box][2])
            box_y1 = float(box_details[box][1])
            box_y2 = float(box_details[box][3])
            box_size = box_details[box][4]

            if (box_x1 <= x <= box_x2) and (box_y1 <= y <= box_y2):
                if box_size == size:
                    loc = "correct"
                else:
                    loc = box_details[box][4]
        print(size, loc)



    print("\n")

    box_details.clear()
    peanut_details.clear()
    boxes = int(input())


